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
def random_mask_pixel(
    __input: Union[DataNode, TensorLikeIn],
    /,
    *,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    foreground: Union[DataNode, TensorLikeArg, int, None] = 0,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    threshold: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    value: Union[DataNode, TensorLikeArg, int, None] = None,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Selects random pixel coordinates in a mask, sampled from a uniform distribution.

    Based on run-time argument ``foreground``, it returns either only foreground pixels or any pixels.

    Pixels are classified as foreground either when their value exceeds a given ``threshold`` or when
    it's equal to a specific ``value``.


    Supported backends
     * 'cpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `foreground` : int or TensorList of int, optional, default = `0`
        If different than 0, the pixel position is sampled uniformly from all foreground pixels.

        If 0, the pixel position is sampled uniformly from all available pixels.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `threshold` : float or TensorList of float, optional, default = `0.0`
        All pixels with a value above this threshold are interpreted as foreground.

        This argument is mutually exclusive with ``value`` argument.
    `value` : int or TensorList of int, optional
        All pixels equal to this value are interpreted as foreground.

        This argument is mutually exclusive with ``threshold`` argument and is meant to be used only
        with integer inputs.

    """
    ...

@overload
def random_mask_pixel(
    __input: List[DataNode],
    /,
    *,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    foreground: Union[DataNode, TensorLikeArg, int, None] = 0,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    threshold: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    value: Union[DataNode, TensorLikeArg, int, None] = None,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, List[DataNode]]:
    """
    Selects random pixel coordinates in a mask, sampled from a uniform distribution.

    Based on run-time argument ``foreground``, it returns either only foreground pixels or any pixels.

    Pixels are classified as foreground either when their value exceeds a given ``threshold`` or when
    it's equal to a specific ``value``.


    Supported backends
     * 'cpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `foreground` : int or TensorList of int, optional, default = `0`
        If different than 0, the pixel position is sampled uniformly from all foreground pixels.

        If 0, the pixel position is sampled uniformly from all available pixels.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `threshold` : float or TensorList of float, optional, default = `0.0`
        All pixels with a value above this threshold are interpreted as foreground.

        This argument is mutually exclusive with ``value`` argument.
    `value` : int or TensorList of int, optional
        All pixels equal to this value are interpreted as foreground.

        This argument is mutually exclusive with ``threshold`` argument and is meant to be used only
        with integer inputs.

    """
    ...

@overload
def random_object_bbox(
    __input: Union[DataNode, TensorLikeIn],
    /,
    *,
    background: Union[DataNode, TensorLikeArg, int, None] = 0,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    cache_objects: Union[bool, None] = False,
    class_weights: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    classes: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
    foreground_prob: Union[DataNode, TensorLikeArg, float, None] = 1.0,
    format: Union[str, None] = "anchor_shape",
    ignore_class: Union[bool, None] = False,
    k_largest: Union[int, None] = None,
    output_class: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    threshold: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, Sequence[DataNode], None]:
    """
    Randomly selects an object from a mask and returns its bounding box.

    This operator takes a labeled segmentation map as its input. With probability ``foreground_prob``
    it randomly selects a label (uniformly or according to the distribution given as ``class_weights``),
    extracts connected blobs of pixels with the selected label and randomly selects one of the blobs.
    The blobs may be further filtered according to ``k_largest`` and ``threshold``.
    The output is a bounding box of the selected blob in one of the formats described in ``format``.

    With probability 1-foreground_prob, the entire area of the input is returned.

    Supported backends
     * 'cpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `background` : int or TensorList of int, optional, default = `0`
        Background label.

        If left unspecified, it's either 0 or any value not in ``classes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `cache_objects` : bool, optional, default = `False`
        Cache object bounding boxes to avoid the computational cost
        of finding object blobs in previously seen inputs.

        Searching for blobs of connected pixels and finding boxes can take a long time. When the dataset
        has few items, but item size is big, you can use caching to save the boxes and reuse them when
        the same input is seen again. The inputs are compared based on 256-bit hash, which is much faster
        to compute than to recalculate the object boxes.
    `class_weights` : float or list of float or TensorList of float, optional
        Relative probabilities of foreground classes.

        Each value corresponds to a class label in ``classes``. If ``classes`` are not specified,
        consecutive 1-based labels are assigned.

        The sum of the weights doesn't have to be equal to 1 - if it isn't the weights will be
        normalized .
    `classes` : int or list of int or TensorList of int, optional
        List of labels considered as foreground.

        If left unspecified, all labels not equal to ``background`` are considered foreground.
    `foreground_prob` : float or TensorList of float, optional, default = `1.0`
        Probability of selecting a foreground bounding box.
    `format` : str, optional, default = `'anchor_shape'`
        Format in which the data is returned.

        Possible choices are::
          * "anchor_shape" (the default) - there are two outputs: anchor and shape
          * "start_end" - there are two outputs: bounding box start and one-past-end coordinates
          * "box" - there is one output that contains concatenated start and end coordinates
    `ignore_class` : bool, optional, default = `False`
        If True, all objects are picked with equal probability,
        regardless of the class they belong to. Otherwise, a class is picked first and then an object is
        randomly selected from this class.

        This argument is incompatible with ``classes``, ``class_weights`` or ``output_class``.

        .. note::
          This flag only affects the probability with which blobs are selected. It does not cause
          blobs of different classes to be merged.
    `k_largest` : int, optional
        If specified, the boxes are sorted by decreasing volume
        and only ``k_largest`` are considered.

        If ``ignore_class`` is True, ``k_largest`` referes to all boxes; otherwise it refers to the
        selected class.
    `output_class` : bool, optional, default = `False`
        If True, an additional output is produced which contains the
        label of the class to which the selected box belongs, or background label if the selected box
        is not an object bounding box.

        The output may not be an object bounding box when any of the following conditions occur:
          - the sample was randomly (according to ``foreground_prob``) chosen not be be a foreground one
          - the sample contained no foreground objects
          - no bounding box met the required size threshold.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `threshold` : int or list of int or TensorList of int, optional
        Per-axis minimum size of the bounding boxes
        to return.

        If the selected class doesn't contain any bounding box that meets this condition, it is rejected
        and another class is picked. If no class contains a satisfactory box, the entire input area
        is returned.

    """
    ...

@overload
def random_object_bbox(
    __input: List[DataNode],
    /,
    *,
    background: Union[DataNode, TensorLikeArg, int, None] = 0,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    cache_objects: Union[bool, None] = False,
    class_weights: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    classes: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
    foreground_prob: Union[DataNode, TensorLikeArg, float, None] = 1.0,
    format: Union[str, None] = "anchor_shape",
    ignore_class: Union[bool, None] = False,
    k_largest: Union[int, None] = None,
    output_class: Union[bool, None] = False,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    threshold: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, Sequence[DataNode], List[DataNode], List[Sequence[DataNode]], None]:
    """
    Randomly selects an object from a mask and returns its bounding box.

    This operator takes a labeled segmentation map as its input. With probability ``foreground_prob``
    it randomly selects a label (uniformly or according to the distribution given as ``class_weights``),
    extracts connected blobs of pixels with the selected label and randomly selects one of the blobs.
    The blobs may be further filtered according to ``k_largest`` and ``threshold``.
    The output is a bounding box of the selected blob in one of the formats described in ``format``.

    With probability 1-foreground_prob, the entire area of the input is returned.

    Supported backends
     * 'cpu'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `background` : int or TensorList of int, optional, default = `0`
        Background label.

        If left unspecified, it's either 0 or any value not in ``classes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `cache_objects` : bool, optional, default = `False`
        Cache object bounding boxes to avoid the computational cost
        of finding object blobs in previously seen inputs.

        Searching for blobs of connected pixels and finding boxes can take a long time. When the dataset
        has few items, but item size is big, you can use caching to save the boxes and reuse them when
        the same input is seen again. The inputs are compared based on 256-bit hash, which is much faster
        to compute than to recalculate the object boxes.
    `class_weights` : float or list of float or TensorList of float, optional
        Relative probabilities of foreground classes.

        Each value corresponds to a class label in ``classes``. If ``classes`` are not specified,
        consecutive 1-based labels are assigned.

        The sum of the weights doesn't have to be equal to 1 - if it isn't the weights will be
        normalized .
    `classes` : int or list of int or TensorList of int, optional
        List of labels considered as foreground.

        If left unspecified, all labels not equal to ``background`` are considered foreground.
    `foreground_prob` : float or TensorList of float, optional, default = `1.0`
        Probability of selecting a foreground bounding box.
    `format` : str, optional, default = `'anchor_shape'`
        Format in which the data is returned.

        Possible choices are::
          * "anchor_shape" (the default) - there are two outputs: anchor and shape
          * "start_end" - there are two outputs: bounding box start and one-past-end coordinates
          * "box" - there is one output that contains concatenated start and end coordinates
    `ignore_class` : bool, optional, default = `False`
        If True, all objects are picked with equal probability,
        regardless of the class they belong to. Otherwise, a class is picked first and then an object is
        randomly selected from this class.

        This argument is incompatible with ``classes``, ``class_weights`` or ``output_class``.

        .. note::
          This flag only affects the probability with which blobs are selected. It does not cause
          blobs of different classes to be merged.
    `k_largest` : int, optional
        If specified, the boxes are sorted by decreasing volume
        and only ``k_largest`` are considered.

        If ``ignore_class`` is True, ``k_largest`` referes to all boxes; otherwise it refers to the
        selected class.
    `output_class` : bool, optional, default = `False`
        If True, an additional output is produced which contains the
        label of the class to which the selected box belongs, or background label if the selected box
        is not an object bounding box.

        The output may not be an object bounding box when any of the following conditions occur:
          - the sample was randomly (according to ``foreground_prob``) chosen not be be a foreground one
          - the sample contained no foreground objects
          - no bounding box met the required size threshold.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `threshold` : int or list of int or TensorList of int, optional
        Per-axis minimum size of the bounding boxes
        to return.

        If the selected class doesn't contain any bounding box that meets this condition, it is rejected
        and another class is picked. If no class contains a satisfactory box, the entire input area
        is returned.

    """
    ...

@overload
def select_masks(
    __mask_ids: Union[DataNode, TensorLikeIn],
    __polygons: Union[DataNode, TensorLikeIn],
    __vertices: Union[DataNode, TensorLikeIn],
    /,
    *,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    preserve: Union[bool, None] = False,
    reindex_masks: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Sequence[DataNode]:
    """
    Selects a subset of polygons by their mask ids.

    The operator expects three inputs describing multiple segmentation mask polygons belonging to different mask ids and
    a list of selected mask ids.

    Each sample can contain several polygons belonging to different masks, and each polygon can be composed by an arbitrary
    number of vertices (at least 3). The masks polygons are described  by the inputs ``polygons`` and ``vertices`` and
    the operator produces output ``polygons`` and ``vertices`` where only the polygons associated with the selected
    masks are present.

    .. note::

      The format of ``polygons`` and ``vertices`` is the same as produced by COCOReader.

    **Examples:**

    Let us assume the following input mask, where symbolic coordinates are used for a clearer example::

        polygons = [[0, 0, 3], [1, 3, 7], [2, 7, 10]]
        vertices = [[x0, y0], [x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5], [x6, y6], [x7, y7], [x8, y8], [x9, y9]]

    Example 1: Selecting a single mask with id ``1``, maintaining the original id::

        mask_ids = [1], ``reindex_masks`` = False
        out_polygons = [[1, 0, 4]]
        out_vertices = [[x3, y3], [x4, y4], [x5, y5], [x6, y6]]

    Example 2: Selecting two out of the three masks, replacing the mask ids with the indices at which
    they appeared in ``mask_ids`` input::

        mask_ids = [2, 0]
        reindex_masks = True
        out_polygons = [[0, 3, 6], [1, 0, 3]]
        out_vertices = [[x0, y0], [x1, y1], [x2, y2], [x7, y7], [x8, y8], [x9, y9]]


    Supported backends
     * 'cpu'


    Args
    ----
    `__mask_ids` : 1D TensorList of int
        List of identifiers of the masks to be selected. The list should not contain duplicates.
    `__polygons` : 2D TensorList of int
        Polygons, described by 3 columns::

            [[mask_id0, start_vertex_idx0, end_vertex_idx0],
             [mask_id1, start_vertex_idx1, end_vertex_idx1],
             ...,
             [mask_idn, start_vertex_idxn, end_vertex_idxn],]

        with ``mask_id`` being the identifier of the mask this polygon belongs to, and
        ``[start_vertex_idx, end_vertex_idx)`` describing the range of indices from ``vertices`` that belong to
        this polygon.
    `__vertices` : 2D TensorList
        Vertex data stored in interleaved format::

            [[x0, y0, ...],
             [x1, y1, ...],
             ... ,
             [xn, yn, ...]]

        The operator accepts vertices with arbitrary number of coordinates.


    Keyword args
    ------------
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `reindex_masks` : bool, optional, default = `False`
        If set to True, the output mask ids are replaced with the indices at which they appeared
        in ``mask_ids`` input.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def select_masks(
    __mask_ids: Union[List[DataNode], DataNode, TensorLikeIn],
    __polygons: Union[List[DataNode], DataNode, TensorLikeIn],
    __vertices: Union[List[DataNode], DataNode, TensorLikeIn],
    /,
    *,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    preserve: Union[bool, None] = False,
    reindex_masks: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[Sequence[DataNode], List[Sequence[DataNode]]]:
    """
    Selects a subset of polygons by their mask ids.

    The operator expects three inputs describing multiple segmentation mask polygons belonging to different mask ids and
    a list of selected mask ids.

    Each sample can contain several polygons belonging to different masks, and each polygon can be composed by an arbitrary
    number of vertices (at least 3). The masks polygons are described  by the inputs ``polygons`` and ``vertices`` and
    the operator produces output ``polygons`` and ``vertices`` where only the polygons associated with the selected
    masks are present.

    .. note::

      The format of ``polygons`` and ``vertices`` is the same as produced by COCOReader.

    **Examples:**

    Let us assume the following input mask, where symbolic coordinates are used for a clearer example::

        polygons = [[0, 0, 3], [1, 3, 7], [2, 7, 10]]
        vertices = [[x0, y0], [x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5], [x6, y6], [x7, y7], [x8, y8], [x9, y9]]

    Example 1: Selecting a single mask with id ``1``, maintaining the original id::

        mask_ids = [1], ``reindex_masks`` = False
        out_polygons = [[1, 0, 4]]
        out_vertices = [[x3, y3], [x4, y4], [x5, y5], [x6, y6]]

    Example 2: Selecting two out of the three masks, replacing the mask ids with the indices at which
    they appeared in ``mask_ids`` input::

        mask_ids = [2, 0]
        reindex_masks = True
        out_polygons = [[0, 3, 6], [1, 0, 3]]
        out_vertices = [[x0, y0], [x1, y1], [x2, y2], [x7, y7], [x8, y8], [x9, y9]]


    Supported backends
     * 'cpu'


    Args
    ----
    `__mask_ids` : 1D TensorList of int
        List of identifiers of the masks to be selected. The list should not contain duplicates.
    `__polygons` : 2D TensorList of int
        Polygons, described by 3 columns::

            [[mask_id0, start_vertex_idx0, end_vertex_idx0],
             [mask_id1, start_vertex_idx1, end_vertex_idx1],
             ...,
             [mask_idn, start_vertex_idxn, end_vertex_idxn],]

        with ``mask_id`` being the identifier of the mask this polygon belongs to, and
        ``[start_vertex_idx, end_vertex_idx)`` describing the range of indices from ``vertices`` that belong to
        this polygon.
    `__vertices` : 2D TensorList
        Vertex data stored in interleaved format::

            [[x0, y0, ...],
             [x1, y1, ...],
             ... ,
             [xn, yn, ...]]

        The operator accepts vertices with arbitrary number of coordinates.


    Keyword args
    ------------
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `reindex_masks` : bool, optional, default = `False`
        If set to True, the output mask ids are replaced with the indices at which they appeared
        in ``mask_ids`` input.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...
