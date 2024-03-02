# (C) Copyright 2023 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import json
import logging
import os
from contextlib import contextmanager

from scipy.sparse import load_npz

from earthkit.regrid.gridspec import GridSpec
from earthkit.regrid.utils import no_progress_bar
from earthkit.regrid.utils.download import download_and_cache

LOG = logging.getLogger(__name__)

_URL = "https://get.ecmwf.int/repository/earthkit/regrid/matrices"
_INDEX_FILENAME = "index.json"


class UrlAccessor:
    def __init__(self, url):
        self.url = url

    def index_path(self):
        # checking the out of date status does not work for this file,
        # so we have to force the download using Force=True
        try:
            url = os.path.join(self.url, _INDEX_FILENAME)
            path = download_and_cache(
                url,
                owner="url",
                verify=True,
                force=True,
                chunk_size=1024 * 1024,
                http_headers=None,
                update_if_out_of_date=True,
                progress_bar=no_progress_bar,
                maximum_retries=5,
                retry_after=10,
            )
        except Exception:
            LOG.error(f"Could not download index file={url}")
            raise

        return path

    def matrix_path(self, name):
        try:
            url = os.path.join(self.url, name)
            path = download_and_cache(
                url,
                owner="url",
                verify=True,
                force=None,
                chunk_size=1024 * 1024,
                http_headers=None,
                update_if_out_of_date=False,
                maximum_retries=5,
                retry_after=10,
            )
        except Exception:
            LOG.error(f"Could not download matrix file={url}")
            raise

        return path


class LocalAccessor:
    """Only used for test purposes"""

    def __init__(self, path):
        self.path = path

    def index_path(self):
        return os.path.join(self.path, _INDEX_FILENAME)

    def matrix_path(self, name):
        return os.path.join(self.path, name)


@contextmanager
def _use_local_index(path):
    """Context manager for testing only. Allow using local index
    file and matrices.
    """
    DB.clear_index()
    DB.accessor = LocalAccessor(path)
    try:
        yield None
    finally:
        DB.clear_index()
        DB.accessor = UrlAccessor(_URL)


class MatrixDb:
    def __init__(self):
        self._index = None
        self.accessor = UrlAccessor(_URL)

    @property
    def index(self):
        if self._index is None:
            self.load_index()
        return self._index

    def load_index(self):
        self._index = {}
        path = self.accessor.index_path()

        with open(path, "r") as f:
            index = json.load(f)
            for name, entry in index.items():
                # it is possible that the inventory is already updated with new
                # a gridspecs type, but a given earthkit-regrid version is not
                # yet supporting it. In this case loading the index should not crash.
                try:
                    in_gs = GridSpec.from_dict(entry["input"])
                    out_gs = GridSpec.from_dict(entry["output"])
                    entry["input"] = in_gs
                    entry["output"] = out_gs
                    # print(f"{in_gs=}")
                    # print(f"{out_gs=}")
                    self._index[name] = entry
                # when the inventory is already updated with new a gridspecs type
                # but the old code is not yet supporting it should not crash
                except Exception:
                    pass

    def clear_index(self):
        """For testing only"""
        self._index = None

    def find(self, gridspec_in, gridspec_out, matrix_version=None):
        entry = self.find_entry(gridspec_in, gridspec_out)

        if entry is not None:
            versions = entry["versions"]
            if matrix_version is not None:
                if matrix_version not in versions:
                    raise ValueError(f"Unsupported matrix_version={matrix_version}")
            else:
                matrix_version = sorted(versions)[0]

            z = self.load_matrix(entry["name"], matrix_version)
            return z, entry["output"]["shape"]
        return None, None

    def find_entry(self, gridspec_in, gridspec_out):
        gridspec_in = GridSpec.from_dict(gridspec_in)
        gridspec_out = GridSpec.from_dict(gridspec_out)

        if gridspec_in is None or gridspec_out is None:
            return None

        for _, entry in self.index.items():
            if gridspec_in == entry["input"] and gridspec_out == entry["output"]:
                return entry

        return None

    def load_matrix(self, name, version):
        name = f"{name}-{version}.npz"
        path = self.accessor.matrix_path(name)
        z = load_npz(path)
        return z


DB = MatrixDb()
