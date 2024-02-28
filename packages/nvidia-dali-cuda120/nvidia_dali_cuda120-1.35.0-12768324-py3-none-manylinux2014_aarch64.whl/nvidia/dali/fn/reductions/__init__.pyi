# Copyright (c) 2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Union, Optional, overload
from typing import Any, List, Sequence

from nvidia.dali._typing import TensorLikeIn, TensorLikeArg

from nvidia.dali.data_node import DataNode

from nvidia.dali.types import DALIDataType, DALIImageType, DALIInterpType

@overload
def max(
    __input: Union[DataNode, TensorLikeIn],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Gets maximal input element along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def max(
    __input: List[DataNode],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, List[DataNode]]:
    """
    Gets maximal input element along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def mean(
    __input: Union[DataNode, TensorLikeIn],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dtype: Union[DALIDataType, None] = None,
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Gets mean of elements along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional
        Output data type. This type is used to accumulate the result.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def mean(
    __input: List[DataNode],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dtype: Union[DALIDataType, None] = None,
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, List[DataNode]]:
    """
    Gets mean of elements along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional
        Output data type. This type is used to accumulate the result.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def mean_square(
    __input: Union[DataNode, TensorLikeIn],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dtype: Union[DALIDataType, None] = None,
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Gets mean square of elements along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional
        Output data type. This type is used to accumulate the result.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def mean_square(
    __input: List[DataNode],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dtype: Union[DALIDataType, None] = None,
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, List[DataNode]]:
    """
    Gets mean square of elements along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional
        Output data type. This type is used to accumulate the result.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def min(
    __input: Union[DataNode, TensorLikeIn],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Gets minimal input element along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def min(
    __input: List[DataNode],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, List[DataNode]]:
    """
    Gets minimal input element along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def rms(
    __input: Union[DataNode, TensorLikeIn],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dtype: Union[DALIDataType, None] = None,
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Gets root mean square of elements along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional
        Output data type. This type is used to accumulate the result.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def rms(
    __input: List[DataNode],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dtype: Union[DALIDataType, None] = None,
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, List[DataNode]]:
    """
    Gets root mean square of elements along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional
        Output data type. This type is used to accumulate the result.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def std_dev(
    __data: Union[DataNode, TensorLikeIn],
    __mean: Union[DataNode, TensorLikeIn],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    ddof: Union[int, None] = 0,
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Gets standard deviation of elements along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__data` : TensorList
        Input to the operator.
    `__mean` : float or TensorList of float
        Mean value to use in the calculations.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `ddof` : int, optional, default = `0`
        Delta Degrees of Freedom. Adjusts the divisor used in calculations, which is `N - ddof`.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def std_dev(
    __data: Union[List[DataNode], DataNode, TensorLikeIn],
    __mean: Union[List[DataNode], DataNode, TensorLikeIn],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    ddof: Union[int, None] = 0,
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, List[DataNode]]:
    """
    Gets standard deviation of elements along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__data` : TensorList
        Input to the operator.
    `__mean` : float or TensorList of float
        Mean value to use in the calculations.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `ddof` : int, optional, default = `0`
        Delta Degrees of Freedom. Adjusts the divisor used in calculations, which is `N - ddof`.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def sum(
    __input: Union[DataNode, TensorLikeIn],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dtype: Union[DALIDataType, None] = None,
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Gets sum of elements along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional
        Output data type. This type is used to accumulate the result.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def sum(
    __input: List[DataNode],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dtype: Union[DALIDataType, None] = None,
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, List[DataNode]]:
    """
    Gets sum of elements along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional
        Output data type. This type is used to accumulate the result.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def variance(
    __data: Union[DataNode, TensorLikeIn],
    __mean: Union[DataNode, TensorLikeIn],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    ddof: Union[int, None] = 0,
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Gets variance of elements along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__data` : TensorList
        Input to the operator.
    `__mean` : float or TensorList of float
        Mean value to use in the calculations.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `ddof` : int, optional, default = `0`
        Delta Degrees of Freedom. Adjusts the divisor used in calculations, which is `N - ddof`.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def variance(
    __data: Union[List[DataNode], DataNode, TensorLikeIn],
    __mean: Union[List[DataNode], DataNode, TensorLikeIn],
    /,
    *,
    axes: Union[Sequence[int], int, None] = None,
    axis_names: Union[str, None] = None,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    ddof: Union[int, None] = 0,
    keep_dims: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, List[DataNode]]:
    """
    Gets variance of elements along provided axes.

    Supported backends
     * 'cpu'
     * 'gpu'


    Args
    ----
    `__data` : TensorList
        Input to the operator.
    `__mean` : float or TensorList of float
        Mean value to use in the calculations.


    Keyword args
    ------------
    `axes` : int or list of int, optional
        Axis or axes along which reduction is performed.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        Not providing any axis results in reduction of all elements.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Name(s) of the axis or axes along which the reduction is performed.

        The input layout is used to translate the axis names to axis indices, for example ``axis_names="HW"`` with input
        layout `"FHWC"` is equivalent to specifying ``axes=[1,2]``. This argument cannot be used together with ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `ddof` : int, optional, default = `0`
        Delta Degrees of Freedom. Adjusts the divisor used in calculations, which is `N - ddof`.
    `keep_dims` : bool, optional, default = `False`
        If True, maintains original input dimensions.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...
