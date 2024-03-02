interpolate
==============

.. py:function:: interpolate(values, source_gridspec, target_gridspec, matrix_version=None)

    Interpolate the ``values`` from the ``source_gridspec`` onto the ``target_gridspec``.

    :param values: the input values
    :type values: ndarray
    :param source_gridspec: the :ref:`gridspec <gridspec>` describing the grid that ``values`` are defined on
    :type source_gridspec: dict
    :param target_gridspec: the :ref:`gridspec <gridspec>` describing the target grid that ``values`` will be interpolated onto
    :type target_gridspec: dict
    :param matrix_version: the version of the pre-generated interpolation matrix to be used. None means the latest version will be used.
    :type matrix_version: str
    :return: the interpolated values
    :rtype: ndarray
    :raises ValueError: if a pre-generated interpolation matrix is not available

    The interpolation only works when a pre-generated interpolation matrix is available for the given ``source_gridspec`` - ``target_gridspec`` combination. In this case the interpolation matrix is automatically downloaded and stored in a local cache and when it is needed again the cached version is used.

    Once the matrix is available the interpolation is performed by multiplying the ``values`` vector with it.

.. note::

    Please see the :ref:`inventory <matrix_inventory>` for the list of available matrices.

Examples
--------

    - :ref:`/examples/interpolation.ipynb`
