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

from nvidia.dali.ops._operators.tfrecord import tfrecord as tfrecord

def coco(
    *,
    annotations_file: Union[str, None] = "",
    avoid_class_remapping: Union[bool, None] = False,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dont_use_mmap: Union[bool, None] = False,
    file_root: Union[str, None] = None,
    image_ids: Union[bool, None] = False,
    images: Union[Sequence[str], str, None] = None,
    include_iscrowd: Union[bool, None] = True,
    initial_fill: Union[int, None] = 1024,
    lazy_init: Union[bool, None] = False,
    ltrb: Union[bool, None] = False,
    num_shards: Union[int, None] = 1,
    pad_last_batch: Union[bool, None] = False,
    pixelwise_masks: Union[bool, None] = False,
    polygon_masks: Union[bool, None] = False,
    prefetch_queue_depth: Union[int, None] = 1,
    preprocessed_annotations: Union[str, None] = "",
    preserve: Union[bool, None] = False,
    random_shuffle: Union[bool, None] = False,
    ratio: Union[bool, None] = False,
    read_ahead: Union[bool, None] = False,
    save_preprocessed_annotations: Union[bool, None] = False,
    save_preprocessed_annotations_dir: Union[str, None] = "",
    seed: Union[int, None] = -1,
    shard_id: Union[int, None] = 0,
    shuffle_after_epoch: Union[bool, None] = False,
    size_threshold: Union[float, None] = 0.1,
    skip_cached_images: Union[bool, None] = False,
    skip_empty: Union[bool, None] = False,
    stick_to_shard: Union[bool, None] = False,
    tensor_init_bytes: Union[int, None] = 1048576,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, Sequence[DataNode], None]:
    """
    Reads data from a COCO dataset that is composed of a directory with
    images and annotation JSON files.

    This readers produces the following outputs::

        images, bounding_boxes, labels, ((polygons, vertices) | (pixelwise_masks)), (image_ids)

    * **images**
      Each sample contains image data with layout ``HWC`` (height, width, channels).
    * **bounding_boxes**
      Each sample can have an arbitrary ``M`` number of bounding boxes, each described by 4 coordinates::

        [[x_0, y_0, w_0, h_0],
         [x_1, y_1, w_1, h_1]
         ...
         [x_M, y_M, w_M, h_M]]

      or in ``[l, t, r, b]`` format if requested (see ``ltrb`` argument).
    * **labels**
      Each bounding box is associated with an integer label representing a category identifier::

        [label_0, label_1, ..., label_M]

    * **polygons** and **vertices** (Optional, present if ``polygon_masks`` is set to True)
      If ``polygon_masks`` is enabled, two extra outputs describing masks by a set of polygons.
      Each mask contains an arbitrary number of polygons ``P``, each associated with a mask index in the range [0, M) and
      composed by a group of ``V`` vertices. The output ``polygons`` describes the polygons as follows::

        [[mask_idx_0, start_vertex_idx_0, end_vertex_idx_0],
         [mask_idx_1, start_vertex_idx_1, end_vertex_idx_1],
         ...
         [mask_idx_P, start_vertex_idx_P, end_vertex_idx_P]]

      where ``mask_idx`` is the index of the mask the polygon, in the range ``[0, M)``, and ``start_vertex_idx`` and  ``end_vertex_idx``
      define the range of indices of vertices, as they appear in the output ``vertices``, belonging to this polygon.
      Each sample in ``vertices`` contains a list of vertices that composed the different polygons in the sample, as 2D coordinates::

        [[x_0, y_0],
         [x_1, y_1],
         ...
         [x_V, y_V]]

    * **pixelwise_masks** (Optional, present if argument ``pixelwise_masks`` is set to True)
      Contains image-like data, same shape and layout as ``images``, representing a pixelwise segmentation mask.
    * **image_ids** (Optional, present if argument ``image_ids`` is set to True)
      One element per sample, representing an image identifier.

    Supported backends
     * 'cpu'


    Keyword args
    ------------
    `annotations_file` : str, optional, default = `''`
        List of paths to the JSON annotations files.
    `avoid_class_remapping` : bool, optional, default = `False`
        If set to True, lasses ID values are returned directly as they are defined in the manifest file.

        Otherwise, classes' ID values are mapped to consecutive values in range 1-number of classes
        disregarding exact values from the manifest (0 is reserved for a special background class.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dont_use_mmap` : bool, optional, default = `False`
        If set to True, the Loader will use plain file I/O instead of trying to map
        the file in memory.

        Mapping provides a small performance benefit when accessing a local file system, but most network file
        systems, do not provide optimum performance.
    `file_root` : str, optional
        Path to a directory that contains the data files.

        If a file list is not provided, this argument is required.
    `image_ids` : bool, optional, default = `False`
        If set to True, the image IDs will be produced in an extra output.
    `images` : str or list of str, optional
        A list of image paths.

        If provided, it specifies the images that will be read.
        The images will be read in the same order as they appear in the list, and in case of
        duplicates, multiple copies of the relevant samples will be produced.

        If left unspecified or set to None, all images listed in the annotation file are read exactly once,
        ordered by their image id.

        The paths to be kept should match exactly those in the annotations file.

        Note: This argument is mutually exclusive with ``preprocessed_annotations``.
    `include_iscrowd` : bool, optional, default = `True`
        If set to True annotations marked as ``iscrowd=1`` are included as well.
    `initial_fill` : int, optional, default = `1024`
        Size of the buffer that is used for shuffling.

        If ``random_shuffle`` is False, this parameter is ignored.
    `lazy_init` : bool, optional, default = `False`
        Parse and prepare the dataset metadata only during the first run instead of
        in the constructor.
    `ltrb` : bool, optional, default = `False`
        If set to True, bboxes are returned as [left, top, right, bottom].

        If set to False, the bboxes are returned as [x, y, width, height].
    `masks` : bool, optional, default = `False`
        Enable polygon masks.

        .. warning::

            Use ``polygon_masks`` instead. Note that the polygon format has changed ``mask_id, start_coord, end_coord`` to ``mask_id, start_vertex, end_vertex`` where
            start_coord and end_coord are total number of coordinates, effectly ``start_coord = 2 * start_vertex`` and ``end_coord = 2 * end_vertex``.
            Example: A polygon with vertices ``[[x0, y0], [x1, y1], [x2, y2]]`` would be represented as ``[mask_id, 0, 6]`` when using the deprecated
            argument ``masks``, but ``[mask_id, 0, 3]`` when using the new argument ``polygon_masks``.
    `num_shards` : int, optional, default = `1`
        Partitions the data into the specified number of parts (shards).

        This is typically used for multi-GPU or multi-node training.
    `pad_last_batch` : bool, optional, default = `False`
        If set to True, pads the shard by repeating the last sample.

        .. note::
          If the number of batches differs across shards, this option can cause an entire batch of repeated
          samples to be added to the dataset.
    `pixelwise_masks` : bool, optional, default = `False`
        If true, segmentation masks are read and returned as pixel-wise masks. This argument is
        mutually exclusive with ``polygon_masks``.
    `polygon_masks` : bool, optional, default = `False`
        If set to True, segmentation mask polygons are read in the form of two outputs:
        ``polygons`` and ``vertices``. This argument is mutually exclusive with ``pixelwise_masks``.
    `prefetch_queue_depth` : int, optional, default = `1`
        Specifies the number of batches to be prefetched by the internal Loader.

        This value should be increased when the pipeline is CPU-stage bound, trading memory
        consumption for better interleaving with the Loader thread.
    `preprocessed_annotations` : str, optional, default = `''`
        Path to the directory with meta files that contain preprocessed COCO annotations.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_shuffle` : bool, optional, default = `False`
        Determines whether to randomly shuffle data.

        A prefetch buffer with a size equal to ``initial_fill`` is used to read data sequentially,
        and then samples are selected randomly to form a batch.
    `ratio` : bool, optional, default = `False`
        If set to True, the returned bbox and mask polygon coordinates are relative to the image dimensions.
    `read_ahead` : bool, optional, default = `False`
        Determines whether the accessed data should be read ahead.

        For large files such as LMDB, RecordIO, or TFRecord, this argument slows down the first access but
        decreases the time of all of the following accesses.
    `save_preprocessed_annotations` : bool, optional, default = `False`
        If set to True, the operator saves a set of files containing binary representations of the
        preprocessed COCO annotations.
    `save_preprocessed_annotations_dir` : str, optional, default = `''`
        Path to the directory in which to save the preprocessed COCO annotations files.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shard_id` : int, optional, default = `0`
        Index of the shard to read.
    `shuffle_after_epoch` : bool, optional, default = `False`
        If set to True, the reader shuffles the entire  dataset after each epoch.
    `size_threshold` : float, optional, default = `0.1`
        If the width or the height, in number of pixels, of a bounding box that represents an
        instance of an object is lower than this value, the object will be ignored.
    `skip_cached_images` : bool, optional, default = `False`
        If set to True, the loading data will be skipped when the sample is
        in the decoder cache.

        In this case, the output of the loader will be empty.
    `skip_empty` : bool, optional, default = `False`
        If true, reader will skip samples with no object instances in them
    `stick_to_shard` : bool, optional, default = `False`
        Determines whether the reader should stick to a data shard instead of going through
        the entire dataset.

        If decoder caching is used, it significantly reduces the amount of data to be cached, but
        might affect accuracy of the training.
    `tensor_init_bytes` : int, optional, default = `1048576`
        Hint for how much memory to allocate per image.
    `dump_meta_files` : bool
        .. warning::

            The argument ``dump_meta_files`` is a deprecated alias for ``save_preprocessed_annotations``. Use ``save_preprocessed_annotations`` instead.
    `dump_meta_files_path` : str
        .. warning::

            The argument ``dump_meta_files_path`` is a deprecated alias for ``save_preprocessed_annotations_dir``. Use ``save_preprocessed_annotations_dir`` instead.
    `meta_files_path` : str
        .. warning::

            The argument ``meta_files_path`` is a deprecated alias for ``preprocessed_annotations``. Use ``preprocessed_annotations`` instead.
    `save_img_ids` : bool
        .. warning::

            The argument ``save_img_ids`` is a deprecated alias for ``image_ids``. Use ``image_ids`` instead.

    """
    ...

def caffe(
    *,
    path: Union[Sequence[str], str],
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dont_use_mmap: Union[bool, None] = False,
    image_available: Union[bool, None] = True,
    initial_fill: Union[int, None] = 1024,
    label_available: Union[bool, None] = True,
    lazy_init: Union[bool, None] = False,
    num_shards: Union[int, None] = 1,
    pad_last_batch: Union[bool, None] = False,
    prefetch_queue_depth: Union[int, None] = 1,
    preserve: Union[bool, None] = False,
    random_shuffle: Union[bool, None] = False,
    read_ahead: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    shard_id: Union[int, None] = 0,
    skip_cached_images: Union[bool, None] = False,
    stick_to_shard: Union[bool, None] = False,
    tensor_init_bytes: Union[int, None] = 1048576,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, Sequence[DataNode], None]:
    """
    Reads (Image, label) pairs from a Caffe LMDB.

    Supported backends
     * 'cpu'


    Keyword args
    ------------
    `path` : str or list of str
        List of paths to the Caffe LMDB directories.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dont_use_mmap` : bool, optional, default = `False`
        If set to True, the Loader will use plain file I/O instead of trying to map
        the file in memory.

        Mapping provides a small performance benefit when accessing a local file system, but most network file
        systems, do not provide optimum performance.
    `image_available` : bool, optional, default = `True`
        Determines whether an image is available in this LMDB.
    `initial_fill` : int, optional, default = `1024`
        Size of the buffer that is used for shuffling.

        If ``random_shuffle`` is False, this parameter is ignored.
    `label_available` : bool, optional, default = `True`
        Determines whether a label is available.
    `lazy_init` : bool, optional, default = `False`
        Parse and prepare the dataset metadata only during the first run instead of
        in the constructor.
    `num_shards` : int, optional, default = `1`
        Partitions the data into the specified number of parts (shards).

        This is typically used for multi-GPU or multi-node training.
    `pad_last_batch` : bool, optional, default = `False`
        If set to True, pads the shard by repeating the last sample.

        .. note::
          If the number of batches differs across shards, this option can cause an entire batch of repeated
          samples to be added to the dataset.
    `prefetch_queue_depth` : int, optional, default = `1`
        Specifies the number of batches to be prefetched by the internal Loader.

        This value should be increased when the pipeline is CPU-stage bound, trading memory
        consumption for better interleaving with the Loader thread.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_shuffle` : bool, optional, default = `False`
        Determines whether to randomly shuffle data.

        A prefetch buffer with a size equal to ``initial_fill`` is used to read data sequentially,
        and then samples are selected randomly to form a batch.
    `read_ahead` : bool, optional, default = `False`
        Determines whether the accessed data should be read ahead.

        For large files such as LMDB, RecordIO, or TFRecord, this argument slows down the first access but
        decreases the time of all of the following accesses.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shard_id` : int, optional, default = `0`
        Index of the shard to read.
    `skip_cached_images` : bool, optional, default = `False`
        If set to True, the loading data will be skipped when the sample is
        in the decoder cache.

        In this case, the output of the loader will be empty.
    `stick_to_shard` : bool, optional, default = `False`
        Determines whether the reader should stick to a data shard instead of going through
        the entire dataset.

        If decoder caching is used, it significantly reduces the amount of data to be cached, but
        might affect accuracy of the training.
    `tensor_init_bytes` : int, optional, default = `1048576`
        Hint for how much memory to allocate per image.

    """
    ...

def caffe2(
    *,
    path: Union[Sequence[str], str],
    additional_inputs: Union[int, None] = 0,
    bbox: Union[bool, None] = False,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dont_use_mmap: Union[bool, None] = False,
    image_available: Union[bool, None] = True,
    initial_fill: Union[int, None] = 1024,
    label_type: Union[int, None] = 0,
    lazy_init: Union[bool, None] = False,
    num_labels: Union[int, None] = 1,
    num_shards: Union[int, None] = 1,
    pad_last_batch: Union[bool, None] = False,
    prefetch_queue_depth: Union[int, None] = 1,
    preserve: Union[bool, None] = False,
    random_shuffle: Union[bool, None] = False,
    read_ahead: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    shard_id: Union[int, None] = 0,
    skip_cached_images: Union[bool, None] = False,
    stick_to_shard: Union[bool, None] = False,
    tensor_init_bytes: Union[int, None] = 1048576,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, Sequence[DataNode], None]:
    """
    Reads sample data from a Caffe2 Lightning Memory-Mapped Database (LMDB).

    Supported backends
     * 'cpu'


    Keyword args
    ------------
    `path` : str or list of str
        List of paths to the Caffe2 LMDB directories.
    `additional_inputs` : int, optional, default = `0`
        Additional auxiliary data tensors that are provided for each sample.
    `bbox` : bool, optional, default = `False`
        Denotes whether the bounding-box information is present.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dont_use_mmap` : bool, optional, default = `False`
        If set to True, the Loader will use plain file I/O instead of trying to map
        the file in memory.

        Mapping provides a small performance benefit when accessing a local file system, but most network file
        systems, do not provide optimum performance.
    `image_available` : bool, optional, default = `True`
        Determines whether an image is available in this LMDB.
    `initial_fill` : int, optional, default = `1024`
        Size of the buffer that is used for shuffling.

        If ``random_shuffle`` is False, this parameter is ignored.
    `label_type` : int, optional, default = `0`
        Type of label stored in dataset.

        Here is a list of the available values:

        * 0 = SINGLE_LABEL: which is the integer label for the multi-class classification.
        * 1 = MULTI_LABEL_SPARSE: which is the sparse active label indices for multi-label classification.
        * 2 = MULTI_LABEL_DENSE: which is the dense label embedding vector for label embedding regression.
        * 3 = MULTI_LABEL_WEIGHTED_SPARSE: which is the sparse active label indices with per-label weights for multi-label classification.
        * 4 = NO_LABEL: where no label is available.
    `lazy_init` : bool, optional, default = `False`
        Parse and prepare the dataset metadata only during the first run instead of
        in the constructor.
    `num_labels` : int, optional, default = `1`
        Number of classes in the dataset.

        Required when sparse labels are used.
    `num_shards` : int, optional, default = `1`
        Partitions the data into the specified number of parts (shards).

        This is typically used for multi-GPU or multi-node training.
    `pad_last_batch` : bool, optional, default = `False`
        If set to True, pads the shard by repeating the last sample.

        .. note::
          If the number of batches differs across shards, this option can cause an entire batch of repeated
          samples to be added to the dataset.
    `prefetch_queue_depth` : int, optional, default = `1`
        Specifies the number of batches to be prefetched by the internal Loader.

        This value should be increased when the pipeline is CPU-stage bound, trading memory
        consumption for better interleaving with the Loader thread.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_shuffle` : bool, optional, default = `False`
        Determines whether to randomly shuffle data.

        A prefetch buffer with a size equal to ``initial_fill`` is used to read data sequentially,
        and then samples are selected randomly to form a batch.
    `read_ahead` : bool, optional, default = `False`
        Determines whether the accessed data should be read ahead.

        For large files such as LMDB, RecordIO, or TFRecord, this argument slows down the first access but
        decreases the time of all of the following accesses.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shard_id` : int, optional, default = `0`
        Index of the shard to read.
    `skip_cached_images` : bool, optional, default = `False`
        If set to True, the loading data will be skipped when the sample is
        in the decoder cache.

        In this case, the output of the loader will be empty.
    `stick_to_shard` : bool, optional, default = `False`
        Determines whether the reader should stick to a data shard instead of going through
        the entire dataset.

        If decoder caching is used, it significantly reduces the amount of data to be cached, but
        might affect accuracy of the training.
    `tensor_init_bytes` : int, optional, default = `1048576`
        Hint for how much memory to allocate per image.

    """
    ...

def file(
    *,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    case_sensitive_filter: Union[bool, None] = False,
    dont_use_mmap: Union[bool, None] = False,
    file_filters: Union[Sequence[str], str, None] = [
        "*.jpg",
        "*.jpeg",
        "*.png",
        "*.bmp",
        "*.tif",
        "*.tiff",
        "*.pnm",
        "*.ppm",
        "*.pgm",
        "*.pbm",
        "*.jp2",
        "*.webp",
        "*.flac",
        "*.ogg",
        "*.wav",
    ],
    file_list: Union[str, None] = None,
    file_root: Union[str, None] = None,
    files: Union[Sequence[str], str, None] = None,
    initial_fill: Union[int, None] = 1024,
    labels: Union[Sequence[int], int, None] = None,
    lazy_init: Union[bool, None] = False,
    num_shards: Union[int, None] = 1,
    pad_last_batch: Union[bool, None] = False,
    prefetch_queue_depth: Union[int, None] = 1,
    preserve: Union[bool, None] = False,
    random_shuffle: Union[bool, None] = False,
    read_ahead: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    shard_id: Union[int, None] = 0,
    shuffle_after_epoch: Union[bool, None] = False,
    skip_cached_images: Union[bool, None] = False,
    stick_to_shard: Union[bool, None] = False,
    tensor_init_bytes: Union[int, None] = 1048576,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Sequence[DataNode]:
    """
    Reads file contents and returns file-label pairs.

    This operator can be used in the following modes:

    1. Listing files from a directory, assigning labels based on subdirectory structure.

    In this mode, the directory indicated in ``file_root`` argument should contain one or more
    subdirectories. The files in these subdirectories are listed and assigned labels based on
    lexicographical order of the subdirectory. If you provide ``file_filters`` argument with
    a list of glob strings, the operator will list files matching at least one of the patterns.
    Otherwise, a default set of filters is used (see the default value of ``file_filters`` for
    details).

    For example, this directory structure::

      <file_root>/0/image0.jpg
      <file_root>/0/world_map.jpg
      <file_root>/0/antarctic.png
      <file_root>/1/cat.jpeg
      <file_root>/1/dog.tif
      <file_root>/2/car.jpeg
      <file_root>/2/truck.jp2

    by default will yield the following outputs::

      <contents of 0/image0.jpg>        0
      <contents of 0/world_map.jpg>     0
      <contents of 0/antarctic.png>     0
      <contents of 1/cat.jpeg>          1
      <contents of 1/dog.tif>           1
      <contents of 2/car.jpeg>          2
      <contents of 2/truck.jp2>         2

    and with ``file_filters = ["*.jpg", "*.jpeg"]`` will yield the following outputs::

      <contents of 0/image0.jpg>        0
      <contents of 0/world_map.jpg>     0
      <contents of 1/cat.jpeg>          1
      <contents of 2/car.jpeg>          2

    2. Use file names and labels stored in a text file.

    ``file_list`` argument points to a file which contains one file name and label per line.
    Example::

      dog.jpg 0
      cute kitten.jpg 1
      doge.png 0

    The file names can contain spaces in the middle, but cannot contain trailing whitespace.

    3. Use file names and labels provided as a list of strings and integers, respectively.

    As with other readers, the (file, label) pairs returned by this operator can be randomly shuffled
    and various sharding strategies can be applied. See documentation of this operator's arguments
    for details.


    Supported backends
     * 'cpu'


    Keyword args
    ------------
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `case_sensitive_filter` : bool, optional, default = `False`
        If set to True, the filter will be matched
        case-sensitively, otherwise case-insensitively.
    `dont_use_mmap` : bool, optional, default = `False`
        If set to True, the Loader will use plain file I/O instead of trying to map
        the file in memory.

        Mapping provides a small performance benefit when accessing a local file system, but most network file
        systems, do not provide optimum performance.
    `file_filters` : str or list of str, optional, default = `['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tif', '*.tiff', '*.pnm', '*.ppm', '*.pgm', '*.pbm', '*.jp2', '*.webp', '*.flac', '*.ogg', '*.wav']`
        A list of glob strings to filter the
        list of files in the sub-directories of the ``file_root``.

        This argument is ignored when file paths are taken from ``file_list`` or ``files``.
    `file_list` : str, optional
        Path to a text file that contains one whitespace-separated ``filename label``
        pair per line. The filenames are relative to the location of that file or to ``file_root``,
        if specified.

        This argument is mutually exclusive with ``files``.
    `file_root` : str, optional
        Path to a directory that contains the data files.

        If not using ``file_list`` or ``files``, this directory is traversed to discover the files.
        ``file_root`` is required in this mode of operation.
    `files` : str or list of str, optional
        A list of file paths to read the data from.

        If ``file_root`` is provided, the paths are treated as being relative to it.
        When using ``files``, the labels are taken from ``labels`` argument or, if it was not supplied,
        contain indices at which given file appeared in the ``files`` list.

        This argument is mutually exclusive with ``file_list``.
    `initial_fill` : int, optional, default = `1024`
        Size of the buffer that is used for shuffling.

        If ``random_shuffle`` is False, this parameter is ignored.
    `labels` : int or list of int, optional
        Labels accompanying contents of files listed in
        ``files`` argument.

        If not used, sequential 0-based indices are used as labels
    `lazy_init` : bool, optional, default = `False`
        Parse and prepare the dataset metadata only during the first run instead of
        in the constructor.
    `num_shards` : int, optional, default = `1`
        Partitions the data into the specified number of parts (shards).

        This is typically used for multi-GPU or multi-node training.
    `pad_last_batch` : bool, optional, default = `False`
        If set to True, pads the shard by repeating the last sample.

        .. note::
          If the number of batches differs across shards, this option can cause an entire batch of repeated
          samples to be added to the dataset.
    `prefetch_queue_depth` : int, optional, default = `1`
        Specifies the number of batches to be prefetched by the internal Loader.

        This value should be increased when the pipeline is CPU-stage bound, trading memory
        consumption for better interleaving with the Loader thread.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_shuffle` : bool, optional, default = `False`
        Determines whether to randomly shuffle data.

        A prefetch buffer with a size equal to ``initial_fill`` is used to read data sequentially,
        and then samples are selected randomly to form a batch.
    `read_ahead` : bool, optional, default = `False`
        Determines whether the accessed data should be read ahead.

        For large files such as LMDB, RecordIO, or TFRecord, this argument slows down the first access but
        decreases the time of all of the following accesses.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shard_id` : int, optional, default = `0`
        Index of the shard to read.
    `shuffle_after_epoch` : bool, optional, default = `False`
        If set to True, the reader shuffles the entire dataset after each epoch.

        ``stick_to_shard`` and ``random_shuffle`` cannot be used when this argument is set to True.
    `skip_cached_images` : bool, optional, default = `False`
        If set to True, the loading data will be skipped when the sample is
        in the decoder cache.

        In this case, the output of the loader will be empty.
    `stick_to_shard` : bool, optional, default = `False`
        Determines whether the reader should stick to a data shard instead of going through
        the entire dataset.

        If decoder caching is used, it significantly reduces the amount of data to be cached, but
        might affect accuracy of the training.
    `tensor_init_bytes` : int, optional, default = `1048576`
        Hint for how much memory to allocate per image.

    """
    ...

def mxnet(
    *,
    index_path: Union[Sequence[str], str],
    path: Union[Sequence[str], str],
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dont_use_mmap: Union[bool, None] = False,
    initial_fill: Union[int, None] = 1024,
    lazy_init: Union[bool, None] = False,
    num_shards: Union[int, None] = 1,
    pad_last_batch: Union[bool, None] = False,
    prefetch_queue_depth: Union[int, None] = 1,
    preserve: Union[bool, None] = False,
    random_shuffle: Union[bool, None] = False,
    read_ahead: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    shard_id: Union[int, None] = 0,
    skip_cached_images: Union[bool, None] = False,
    stick_to_shard: Union[bool, None] = False,
    tensor_init_bytes: Union[int, None] = 1048576,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Sequence[DataNode]:
    """
    Reads the data from an MXNet RecordIO.

    Supported backends
     * 'cpu'


    Keyword args
    ------------
    `index_path` : str or list of str
        List (of length 1) that contains a path to the index (.idx) file.

        The file is generated by the MXNet's ``im2rec.py`` script with the RecordIO file. The list can
        also be generated by using the ``rec2idx`` script that is distributed with DALI.
    `path` : str or list of str
        List of paths to the RecordIO files.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dont_use_mmap` : bool, optional, default = `False`
        If set to True, the Loader will use plain file I/O instead of trying to map
        the file in memory.

        Mapping provides a small performance benefit when accessing a local file system, but most network file
        systems, do not provide optimum performance.
    `initial_fill` : int, optional, default = `1024`
        Size of the buffer that is used for shuffling.

        If ``random_shuffle`` is False, this parameter is ignored.
    `lazy_init` : bool, optional, default = `False`
        Parse and prepare the dataset metadata only during the first run instead of
        in the constructor.
    `num_shards` : int, optional, default = `1`
        Partitions the data into the specified number of parts (shards).

        This is typically used for multi-GPU or multi-node training.
    `pad_last_batch` : bool, optional, default = `False`
        If set to True, pads the shard by repeating the last sample.

        .. note::
          If the number of batches differs across shards, this option can cause an entire batch of repeated
          samples to be added to the dataset.
    `prefetch_queue_depth` : int, optional, default = `1`
        Specifies the number of batches to be prefetched by the internal Loader.

        This value should be increased when the pipeline is CPU-stage bound, trading memory
        consumption for better interleaving with the Loader thread.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_shuffle` : bool, optional, default = `False`
        Determines whether to randomly shuffle data.

        A prefetch buffer with a size equal to ``initial_fill`` is used to read data sequentially,
        and then samples are selected randomly to form a batch.
    `read_ahead` : bool, optional, default = `False`
        Determines whether the accessed data should be read ahead.

        For large files such as LMDB, RecordIO, or TFRecord, this argument slows down the first access but
        decreases the time of all of the following accesses.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shard_id` : int, optional, default = `0`
        Index of the shard to read.
    `skip_cached_images` : bool, optional, default = `False`
        If set to True, the loading data will be skipped when the sample is
        in the decoder cache.

        In this case, the output of the loader will be empty.
    `stick_to_shard` : bool, optional, default = `False`
        Determines whether the reader should stick to a data shard instead of going through
        the entire dataset.

        If decoder caching is used, it significantly reduces the amount of data to be cached, but
        might affect accuracy of the training.
    `tensor_init_bytes` : int, optional, default = `1048576`
        Hint for how much memory to allocate per image.

    """
    ...

def nemo_asr(
    *,
    manifest_filepaths: Union[Sequence[str], str],
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dont_use_mmap: Union[bool, None] = False,
    downmix: Union[bool, None] = True,
    dtype: Union[DALIDataType, None] = DALIDataType.FLOAT,
    initial_fill: Union[int, None] = 1024,
    lazy_init: Union[bool, None] = False,
    max_duration: Union[float, None] = 0.0,
    min_duration: Union[float, None] = 0.0,
    num_shards: Union[int, None] = 1,
    pad_last_batch: Union[bool, None] = False,
    prefetch_queue_depth: Union[int, None] = 1,
    preserve: Union[bool, None] = False,
    quality: Union[float, None] = 50.0,
    random_shuffle: Union[bool, None] = False,
    read_ahead: Union[bool, None] = False,
    read_idxs: Union[bool, None] = False,
    read_sample_rate: Union[bool, None] = True,
    read_text: Union[bool, None] = True,
    sample_rate: Union[float, None] = -1.0,
    seed: Union[int, None] = -1,
    shard_id: Union[int, None] = 0,
    shuffle_after_epoch: Union[bool, None] = False,
    skip_cached_images: Union[bool, None] = False,
    stick_to_shard: Union[bool, None] = False,
    tensor_init_bytes: Union[int, None] = 1048576,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, Sequence[DataNode], None]:
    """
    Reads automatic speech recognition (ASR) data (audio, text) from an
    NVIDIA NeMo compatible manifest.

    Example manifest file::

        {"audio_filepath": "path/to/audio1.wav", "duration": 3.45, "text": "this is a nemo tutorial"}
        {"audio_filepath": "path/to/audio1.wav", "offset": 3.45, "duration": 1.45, "text": "same audio file but using offset"}
        {"audio_filepath": "path/to/audio2.wav", "duration": 3.45, "text": "third transcript in this example"}

    .. note::
        Only ``audio_filepath`` is field mandatory. If ``duration`` is not specified, the whole audio file will be used. A missing ``text`` field
        will produce an empty string as a text.

    .. warning::
        Handling of ``duration`` and ``offset`` fields is not yet implemented. The current implementation always reads the whole audio file.

    This reader produces between 1 and 3 outputs:

    - Decoded audio data: float, ``shape=(audio_length,)``
    - (optional, if ``read_sample_rate=True``) Audio sample rate: float, ``shape=(1,)``
    - (optional, if ``read_text=True``) Transcript text as a null terminated string: uint8, ``shape=(text_len + 1,)``
    - (optional, if ``read_idxs=True``) Index of the manifest entry: int64, ``shape=(1,)``



    Supported backends
     * 'cpu'


    Keyword args
    ------------
    `manifest_filepaths` : str or list of str
        List of paths to NeMo's compatible manifest files.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dont_use_mmap` : bool, optional, default = `False`
        If set to True, the Loader will use plain file I/O instead of trying to map
        the file in memory.

        Mapping provides a small performance benefit when accessing a local file system, but most network file
        systems, do not provide optimum performance.
    `downmix` : bool, optional, default = `True`
        If True, downmix all input channels to mono. If downmixing is turned on, decoder will produce always 1-D output
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional, default = `DALIDataType.FLOAT`
        Output data type.

        Supported types: ``INT16``, ``INT32``, and ``FLOAT``.
    `initial_fill` : int, optional, default = `1024`
        Size of the buffer that is used for shuffling.

        If ``random_shuffle`` is False, this parameter is ignored.
    `lazy_init` : bool, optional, default = `False`
        Parse and prepare the dataset metadata only during the first run instead of
        in the constructor.
    `max_duration` : float, optional, default = `0.0`
        If a value greater than 0 is provided, it specifies the maximum allowed duration,
        in seconds, of the audio samples.

        Samples with a duration longer than this value will be ignored.
    `min_duration` : float, optional, default = `0.0`
        If a value greater than 0 is provided, it specifies the minimum allowed duration,
         in seconds, of the audio samples.

        Samples with a duration shorter than this value will be ignored.
    `normalize_text` : bool
        .. warning::

            The argument ``normalize_text`` is no longer used and will be removed in a future release.
    `num_shards` : int, optional, default = `1`
        Partitions the data into the specified number of parts (shards).

        This is typically used for multi-GPU or multi-node training.
    `pad_last_batch` : bool, optional, default = `False`
        If set to True, pads the shard by repeating the last sample.

        .. note::
          If the number of batches differs across shards, this option can cause an entire batch of repeated
          samples to be added to the dataset.
    `prefetch_queue_depth` : int, optional, default = `1`
        Specifies the number of batches to be prefetched by the internal Loader.

        This value should be increased when the pipeline is CPU-stage bound, trading memory
        consumption for better interleaving with the Loader thread.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `quality` : float, optional, default = `50.0`
        Resampling quality, 0 is lowest, 100 is highest.

          0 corresponds to 3 lobes of the sinc filter; 50 gives 16 lobes and 100 gives 64 lobes.
    `random_shuffle` : bool, optional, default = `False`
        Determines whether to randomly shuffle data.

        A prefetch buffer with a size equal to ``initial_fill`` is used to read data sequentially,
        and then samples are selected randomly to form a batch.
    `read_ahead` : bool, optional, default = `False`
        Determines whether the accessed data should be read ahead.

        For large files such as LMDB, RecordIO, or TFRecord, this argument slows down the first access but
        decreases the time of all of the following accesses.
    `read_idxs` : bool, optional, default = `False`
        Whether to output the indices of samples as they occur in the manifest file
         as a separate output
    `read_sample_rate` : bool, optional, default = `True`
        Whether to output the sample rate for each sample as a separate output
    `read_text` : bool, optional, default = `True`
        Whether to output the transcript text for each sample as a separate output
    `sample_rate` : float, optional, default = `-1.0`
        If specified, the target sample rate, in Hz, to which the audio is resampled.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shard_id` : int, optional, default = `0`
        Index of the shard to read.
    `shuffle_after_epoch` : bool, optional, default = `False`
        If true, reader shuffles whole dataset after each epoch
    `skip_cached_images` : bool, optional, default = `False`
        If set to True, the loading data will be skipped when the sample is
        in the decoder cache.

        In this case, the output of the loader will be empty.
    `stick_to_shard` : bool, optional, default = `False`
        Determines whether the reader should stick to a data shard instead of going through
        the entire dataset.

        If decoder caching is used, it significantly reduces the amount of data to be cached, but
        might affect accuracy of the training.
    `tensor_init_bytes` : int, optional, default = `1048576`
        Hint for how much memory to allocate per image.

    """
    ...

def numpy(
    *,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    cache_header_information: Union[bool, None] = False,
    dont_use_mmap: Union[bool, None] = False,
    file_filter: Union[str, None] = "*.npy",
    file_list: Union[str, None] = None,
    file_root: Union[str, None] = None,
    files: Union[Sequence[str], str, None] = None,
    fill_value: Union[float, None] = 0.0,
    initial_fill: Union[int, None] = 1024,
    lazy_init: Union[bool, None] = False,
    num_shards: Union[int, None] = 1,
    out_of_bounds_policy: Union[str, None] = "error",
    pad_last_batch: Union[bool, None] = False,
    prefetch_queue_depth: Union[int, None] = 1,
    preserve: Union[bool, None] = False,
    random_shuffle: Union[bool, None] = False,
    read_ahead: Union[bool, None] = False,
    register_buffers: Union[bool, None] = True,
    rel_roi_end: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    rel_roi_shape: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    rel_roi_start: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    roi_axes: Union[Sequence[int], int, None] = [],
    roi_end: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
    roi_shape: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
    roi_start: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
    seed: Union[int, None] = -1,
    shard_id: Union[int, None] = 0,
    shuffle_after_epoch: Union[bool, None] = False,
    skip_cached_images: Union[bool, None] = False,
    stick_to_shard: Union[bool, None] = False,
    tensor_init_bytes: Union[int, None] = 1048576,
    use_o_direct: Union[bool, None] = False,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Reads Numpy arrays from a directory.

    This operator can be used in the following modes:

    1. Read all files from a directory indicated by ``file_root`` that match given ``file_filter``.
    2. Read file names from a text file indicated in ``file_list`` argument.
    3. Read files listed in ``files`` argument.

    .. note::
      The ``gpu`` backend requires cuFile/GDS support (418.x driver family or newer). which is
      shipped with the CUDA toolkit starting from CUDA 11.4. Please check the GDS documentation
      for more details.

      The ``gpu`` reader reads the files in chunks. The size of the chunk can be controlled
      process-wide with an environment variable ``DALI_GDS_CHUNK_SIZE``. Valid values are powers of 2
      between 4096 and 16M, with the default being 2M. For convenience, the value can be specified
      with a k or M suffix, applying a multiplier of 1024 and 2^20, respectively.


    Supported backends
     * 'cpu'
     * 'gpu'


    Keyword args
    ------------
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `cache_header_information` : bool, optional, default = `False`
        If set to True, the header information for each file is cached, improving access
        speed.
    `dont_use_mmap` : bool, optional, default = `False`
        If set to True, the Loader will use plain file I/O instead of trying to map
        the file in memory.

        Mapping provides a small performance benefit when accessing a local file system, but most network file
        systems, do not provide optimum performance.
    `file_filter` : str, optional, default = `'*.npy'`
        If a value is specified, the string is interpreted as glob string to filter the
        list of files in the sub-directories of the ``file_root``.

        This argument is ignored when file paths are taken from ``file_list`` or ``files``.
    `file_list` : str, optional
        Path to a text file that contains filenames (one per line)
        where the filenames are relative to the location of that file or to ``file_root``, if specified.

        This argument is mutually exclusive with ``files``.
    `file_root` : str, optional
        Path to a directory that contains the data files.

        If not using ``file_list`` or ``files``, this directory is traversed to discover the files.
        ``file_root`` is required in this mode of operation.
    `files` : str or list of str, optional
        A list of file paths to read the data from.

        If ``file_root`` is provided, the paths are treated as being relative to it.

        This argument is mutually exclusive with ``file_list``.
    `fill_value` : float, optional, default = `0.0`
        Determines the padding value when ``out_of_bounds_policy`` is set to “pad”.
    `initial_fill` : int, optional, default = `1024`
        Size of the buffer that is used for shuffling.

        If ``random_shuffle`` is False, this parameter is ignored.
    `lazy_init` : bool, optional, default = `False`
        Parse and prepare the dataset metadata only during the first run instead of
        in the constructor.
    `num_shards` : int, optional, default = `1`
        Partitions the data into the specified number of parts (shards).

        This is typically used for multi-GPU or multi-node training.
    `out_of_bounds_policy` : str, optional, default = `'error'`
        Determines the policy when reading outside of the bounds of the numpy array.

        Here is a list of the supported values:

        - ``"error"`` (default): Attempting to read outside of the bounds of the image will produce an error.
        - ``"pad"``: The array will be padded as needed with zeros or any other value that is specified
          with the ``fill_value`` argument.
        - ``"trim_to_shape"``: The ROI will be cut to the bounds of the array.
    `pad_last_batch` : bool, optional, default = `False`
        If set to True, pads the shard by repeating the last sample.

        .. note::
          If the number of batches differs across shards, this option can cause an entire batch of repeated
          samples to be added to the dataset.
    `prefetch_queue_depth` : int, optional, default = `1`
        Specifies the number of batches to be prefetched by the internal Loader.

        This value should be increased when the pipeline is CPU-stage bound, trading memory
        consumption for better interleaving with the Loader thread.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_shuffle` : bool, optional, default = `False`
        Determines whether to randomly shuffle data.

        A prefetch buffer with a size equal to ``initial_fill`` is used to read data sequentially,
        and then samples are selected randomly to form a batch.
    `read_ahead` : bool, optional, default = `False`
        Determines whether the accessed data should be read ahead.

        For large files such as LMDB, RecordIO, or TFRecord, this argument slows down the first access but
        decreases the time of all of the following accesses.
    `register_buffers` : bool, optional, default = `True`
        Applies **only** to the ``gpu`` backend type.

        .. warning::
            This argument is temporarily disabled and left for backward compatibility.
            It will be reenabled in the future releases.

        If true, the device I/O buffers will be registered with cuFile. It is not recommended if the sample
        sizes vary a lot.
    `rel_roi_end` : float or list of float or TensorList of float, optional
        End of the region-of-interest, in relative coordinates (range [0.0 - 1.0]).

        This argument is incompatible with "roi_end", "roi_shape" and "rel_roi_shape".
    `rel_roi_shape` : float or list of float or TensorList of float, optional
        Shape of the region-of-interest, in relative coordinates (range [0.0 - 1.0]).

        This argument is incompatible with "roi_shape", "roi_end" and "rel_roi_end".
    `rel_roi_start` : float or list of float or TensorList of float, optional
        Start of the region-of-interest, in relative coordinates (range [0.0 - 1.0]).

        This argument is incompatible with "roi_start".
    `roi_axes` : int or list of int, optional, default = `[]`
        Order of dimensions used for the ROI anchor and shape arguments, as dimension indices.

        If not provided, all the dimensions should be specified in the ROI arguments.
    `roi_end` : int or list of int or TensorList of int, optional
        End of the region-of-interest, in absolute coordinates.

        This argument is incompatible with "rel_roi_end", "roi_shape" and "rel_roi_shape".
    `roi_shape` : int or list of int or TensorList of int, optional
        Shape of the region-of-interest, in absolute coordinates.

        This argument is incompatible with "rel_roi_shape", "roi_end" and "rel_roi_end".
    `roi_start` : int or list of int or TensorList of int, optional
        Start of the region-of-interest, in absolute coordinates.

        This argument is incompatible with "rel_roi_start".
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shard_id` : int, optional, default = `0`
        Index of the shard to read.
    `shuffle_after_epoch` : bool, optional, default = `False`
        If set to True, the reader shuffles the entire dataset after each epoch.

        ``stick_to_shard`` and ``random_shuffle`` cannot be used when this argument is set to True.
    `skip_cached_images` : bool, optional, default = `False`
        If set to True, the loading data will be skipped when the sample is
        in the decoder cache.

        In this case, the output of the loader will be empty.
    `stick_to_shard` : bool, optional, default = `False`
        Determines whether the reader should stick to a data shard instead of going through
        the entire dataset.

        If decoder caching is used, it significantly reduces the amount of data to be cached, but
        might affect accuracy of the training.
    `tensor_init_bytes` : int, optional, default = `1048576`
        Hint for how much memory to allocate per image.
    `use_o_direct` : bool, optional, default = `False`
        If set to True, the data will be read directly from the storage bypassing system
        cache.

        Mutually exclusive with ``dont_use_mmap=False``.

    """
    ...

def sequence(
    *,
    file_root: str,
    sequence_length: int,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dont_use_mmap: Union[bool, None] = False,
    image_type: Union[DALIImageType, None] = DALIImageType.RGB,
    initial_fill: Union[int, None] = 1024,
    lazy_init: Union[bool, None] = False,
    num_shards: Union[int, None] = 1,
    pad_last_batch: Union[bool, None] = False,
    prefetch_queue_depth: Union[int, None] = 1,
    preserve: Union[bool, None] = False,
    random_shuffle: Union[bool, None] = False,
    read_ahead: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    shard_id: Union[int, None] = 0,
    skip_cached_images: Union[bool, None] = False,
    step: Union[int, None] = 1,
    stick_to_shard: Union[bool, None] = False,
    stride: Union[int, None] = 1,
    tensor_init_bytes: Union[int, None] = 1048576,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Reads [Frame] sequences from a directory representing a collection of streams.

    This operator expects ``file_root`` to contain a set of directories, where each directory represents
    an extracted video stream. This stream is represented by one file for each frame,
    sorted lexicographically. Sequences do not cross the stream boundary and only complete sequences
    are considered, so there is no padding.

    Example directory structure::

      - file_root
        - 0
          - 00001.png
          - 00002.png
          - 00003.png
          - 00004.png
          - 00005.png
          - 00006.png
          ....

        - 1
          - 00001.png
          - 00002.png
          - 00003.png
          - 00004.png
          - 00005.png
          - 00006.png
          ....

    .. note::
      This operator is an analogue of VideoReader working on video frames extracted as separate images.
      It's main purpose is for test baseline. For regular usage, the VideoReader is
      the recommended approach.

    This operator allows sequence inputs.

    Supported backends
     * 'cpu'


    Keyword args
    ------------
    `file_root` : str
        Path to a directory containing streams, where the directories
        represent streams.
    `sequence_length` : int
        Length of sequence to load for each sample.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dont_use_mmap` : bool, optional, default = `False`
        If set to True, the Loader will use plain file I/O instead of trying to map
        the file in memory.

        Mapping provides a small performance benefit when accessing a local file system, but most network file
        systems, do not provide optimum performance.
    `image_type` : :class:`nvidia.dali.types.DALIImageType`, optional, default = `DALIImageType.RGB`
        The color space of input and output image.
    `initial_fill` : int, optional, default = `1024`
        Size of the buffer that is used for shuffling.

        If ``random_shuffle`` is False, this parameter is ignored.
    `lazy_init` : bool, optional, default = `False`
        Parse and prepare the dataset metadata only during the first run instead of
        in the constructor.
    `num_shards` : int, optional, default = `1`
        Partitions the data into the specified number of parts (shards).

        This is typically used for multi-GPU or multi-node training.
    `pad_last_batch` : bool, optional, default = `False`
        If set to True, pads the shard by repeating the last sample.

        .. note::
          If the number of batches differs across shards, this option can cause an entire batch of repeated
          samples to be added to the dataset.
    `prefetch_queue_depth` : int, optional, default = `1`
        Specifies the number of batches to be prefetched by the internal Loader.

        This value should be increased when the pipeline is CPU-stage bound, trading memory
        consumption for better interleaving with the Loader thread.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_shuffle` : bool, optional, default = `False`
        Determines whether to randomly shuffle data.

        A prefetch buffer with a size equal to ``initial_fill`` is used to read data sequentially,
        and then samples are selected randomly to form a batch.
    `read_ahead` : bool, optional, default = `False`
        Determines whether the accessed data should be read ahead.

        For large files such as LMDB, RecordIO, or TFRecord, this argument slows down the first access but
        decreases the time of all of the following accesses.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shard_id` : int, optional, default = `0`
        Index of the shard to read.
    `skip_cached_images` : bool, optional, default = `False`
        If set to True, the loading data will be skipped when the sample is
        in the decoder cache.

        In this case, the output of the loader will be empty.
    `step` : int, optional, default = `1`
        Distance between first frames of consecutive sequences.
    `stick_to_shard` : bool, optional, default = `False`
        Determines whether the reader should stick to a data shard instead of going through
        the entire dataset.

        If decoder caching is used, it significantly reduces the amount of data to be cached, but
        might affect accuracy of the training.
    `stride` : int, optional, default = `1`
        Distance between consecutive frames in a sequence.
    `tensor_init_bytes` : int, optional, default = `1048576`
        Hint for how much memory to allocate per image.

    """
    ...

def video(
    *,
    sequence_length: int,
    additional_decode_surfaces: Union[int, None] = 2,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    channels: Union[int, None] = 3,
    dont_use_mmap: Union[bool, None] = False,
    dtype: Union[DALIDataType, None] = DALIDataType.UINT8,
    enable_frame_num: Union[bool, None] = False,
    enable_timestamps: Union[bool, None] = False,
    file_list: Union[str, None] = "",
    file_list_frame_num: Union[bool, None] = False,
    file_list_include_preceding_frame: Union[bool, None] = False,
    file_root: Union[str, None] = "",
    filenames: Union[Sequence[str], str, None] = [],
    image_type: Union[DALIImageType, None] = DALIImageType.RGB,
    initial_fill: Union[int, None] = 1024,
    labels: Union[Sequence[int], int, None] = None,
    lazy_init: Union[bool, None] = False,
    normalized: Union[bool, None] = False,
    num_shards: Union[int, None] = 1,
    pad_last_batch: Union[bool, None] = False,
    pad_sequences: Union[bool, None] = False,
    prefetch_queue_depth: Union[int, None] = 1,
    preserve: Union[bool, None] = False,
    random_shuffle: Union[bool, None] = False,
    read_ahead: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    shard_id: Union[int, None] = 0,
    skip_cached_images: Union[bool, None] = False,
    skip_vfr_check: Union[bool, None] = False,
    step: Union[int, None] = -1,
    stick_to_shard: Union[bool, None] = False,
    stride: Union[int, None] = 1,
    tensor_init_bytes: Union[int, None] = 1048576,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, Sequence[DataNode], None]:
    """
    Loads and decodes video files using FFmpeg and NVDECODE, which is
    the hardware-accelerated video decoding feature in the NVIDIA(R) GPU.

    The video streams can be in most of the container file formats. FFmpeg is used to parse video
    containers and returns a batch of sequences of ``sequence_length`` frames with shape
    ``(N, F, H, W, C)``, where ``N`` is the batch size, and ``F`` is the number of frames).
    This class only supports constant frame rate videos.

    .. note::
      Containers which doesn't support indexing, like mpeg, requires DALI to seek to the sequence  when
      each new sequence needs to be decoded.

    Supported backends
     * 'gpu'


    Keyword args
    ------------
    `sequence_length` : int
        Frames to load per sequence.
    `additional_decode_surfaces` : int, optional, default = `2`
        Additional decode surfaces to use beyond minimum required.

        This argument is ignored when the decoder cannot determine the minimum number of
        decode surfaces

        .. note::

          This can happen when the driver is an older version.

        This parameter can be used to trade off memory usage with performance.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `channels` : int, optional, default = `3`
        Number of channels.
    `dont_use_mmap` : bool, optional, default = `False`
        If set to True, the Loader will use plain file I/O instead of trying to map
        the file in memory.

        Mapping provides a small performance benefit when accessing a local file system, but most network file
        systems, do not provide optimum performance.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional, default = `DALIDataType.UINT8`
        Output data type.

        Supported types: ``UINT8`` or ``FLOAT``.
    `enable_frame_num` : bool, optional, default = `False`
        If the ``file_list`` or ``filenames`` argument is passed, returns the frame number
        output.
    `enable_timestamps` : bool, optional, default = `False`
        If the ``file_list`` or ``filenames`` argument is passed, returns the timestamps
        output.
    `file_list` : str, optional, default = `''`
        Path to the file with a list of ``file label [start_frame [end_frame]]`` values.

        Positive value means the exact frame, negative counts as a Nth frame from the end (it follows
        python array indexing schema), equal values for the start and end frame would yield an empty
        sequence and a warning. This option is mutually exclusive with ``filenames``
        and ``file_root``.
    `file_list_frame_num` : bool, optional, default = `False`
        If the start/end timestamps are provided in file_list, you can interpret them
        as frame numbers instead of as timestamps.

        If floating point values have been provided, the start frame number will be rounded up and
        the end frame number will be rounded down.

        Frame numbers start from 0.
    `file_list_include_preceding_frame` : bool, optional, default = `False`
        Changes the behavior how ``file_list`` start and end frame timestamps are translated
        to a frame number.

        If the start/end timestamps are provided in file_list as timestamps, the start frame is
        calculated as ``ceil(start_time_stamp * FPS)`` and the end as ``floor(end_time_stamp * FPS)``.
        If this argument is set to True, the equation changes to ``floor(start_time_stamp * FPS)`` and
        ``ceil(end_time_stamp * FPS)`` respectively. In effect, the first returned frame is not later, and
        the end frame not earlier, than the provided timestamps. This behavior is more aligned with how the visible
        timestamps are correlated with displayed video frames.

        .. note::

          When ``file_list_frame_num`` is set to True, this option does not take any effect.

        .. warning::

          This option is available for legacy behavior compatibility.
    `file_root` : str, optional, default = `''`
        Path to a directory that contains the data files.

        This option is mutually exclusive with ``filenames`` and ``file_list``.
    `filenames` : str or list of str, optional, default = `[]`
        File names of the video files to load.

        This option is mutually exclusive with ``file_list`` and ``file_root``.
    `image_type` : :class:`nvidia.dali.types.DALIImageType`, optional, default = `DALIImageType.RGB`
        The color space of the output frames (RGB or YCbCr).
    `initial_fill` : int, optional, default = `1024`
        Size of the buffer that is used for shuffling.

        If ``random_shuffle`` is False, this parameter is ignored.
    `labels` : int or list of int, optional
        Labels associated with the files listed in
        ``filenames`` argument.

        If an empty list is provided, sequential 0-based indices are used as labels. If not provided,
        no labels will be yielded.
    `lazy_init` : bool, optional, default = `False`
        Parse and prepare the dataset metadata only during the first run instead of
        in the constructor.
    `normalized` : bool, optional, default = `False`
        Gets the output as normalized data.
    `num_shards` : int, optional, default = `1`
        Partitions the data into the specified number of parts (shards).

        This is typically used for multi-GPU or multi-node training.
    `pad_last_batch` : bool, optional, default = `False`
        If set to True, pads the shard by repeating the last sample.

        .. note::
          If the number of batches differs across shards, this option can cause an entire batch of repeated
          samples to be added to the dataset.
    `pad_sequences` : bool, optional, default = `False`
        Allows creation of incomplete sequences if there is an insufficient number
        of frames at the very end of the video.

        Redundant frames are zeroed. Corresponding time stamps and frame numbers are set to -1.
    `prefetch_queue_depth` : int, optional, default = `1`
        Specifies the number of batches to be prefetched by the internal Loader.

        This value should be increased when the pipeline is CPU-stage bound, trading memory
        consumption for better interleaving with the Loader thread.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_shuffle` : bool, optional, default = `False`
        Determines whether to randomly shuffle data.

        A prefetch buffer with a size equal to ``initial_fill`` is used to read data sequentially,
        and then samples are selected randomly to form a batch.
    `read_ahead` : bool, optional, default = `False`
        Determines whether the accessed data should be read ahead.

        For large files such as LMDB, RecordIO, or TFRecord, this argument slows down the first access but
        decreases the time of all of the following accesses.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shard_id` : int, optional, default = `0`
        Index of the shard to read.
    `skip_cached_images` : bool, optional, default = `False`
        If set to True, the loading data will be skipped when the sample is
        in the decoder cache.

        In this case, the output of the loader will be empty.
    `skip_vfr_check` : bool, optional, default = `False`
        Skips the check for the variable frame rate (VFR) videos.

        Use this flag to suppress false positive detection of VFR videos.

        .. warning::

          When the dataset indeed contains VFR files, setting this flag may cause the decoder to
          malfunction.
    `step` : int, optional, default = `-1`
        Frame interval between each sequence.

        When the value is less than 0, ``step`` is set to ``sequence_length``.
    `stick_to_shard` : bool, optional, default = `False`
        Determines whether the reader should stick to a data shard instead of going through
        the entire dataset.

        If decoder caching is used, it significantly reduces the amount of data to be cached, but
        might affect accuracy of the training.
    `stride` : int, optional, default = `1`
        Distance between consecutive frames in the sequence.
    `tensor_init_bytes` : int, optional, default = `1048576`
        Hint for how much memory to allocate per image.

    """
    ...

def video_resize(
    *,
    sequence_length: int,
    additional_decode_surfaces: Union[int, None] = 2,
    antialias: Union[bool, None] = True,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    channels: Union[int, None] = 3,
    dont_use_mmap: Union[bool, None] = False,
    dtype: Union[DALIDataType, None] = DALIDataType.UINT8,
    enable_frame_num: Union[bool, None] = False,
    enable_timestamps: Union[bool, None] = False,
    file_list: Union[str, None] = "",
    file_list_frame_num: Union[bool, None] = False,
    file_list_include_preceding_frame: Union[bool, None] = False,
    file_root: Union[str, None] = "",
    filenames: Union[Sequence[str], str, None] = [],
    image_type: Union[DALIImageType, None] = DALIImageType.RGB,
    initial_fill: Union[int, None] = 1024,
    interp_type: Union[
        DataNode, TensorLikeArg, DALIInterpType, None
    ] = DALIInterpType.INTERP_LINEAR,
    labels: Union[Sequence[int], int, None] = None,
    lazy_init: Union[bool, None] = False,
    mag_filter: Union[DataNode, TensorLikeArg, DALIInterpType, None] = DALIInterpType.INTERP_LINEAR,
    max_size: Union[Sequence[float], float, None] = None,
    min_filter: Union[DataNode, TensorLikeArg, DALIInterpType, None] = DALIInterpType.INTERP_LINEAR,
    minibatch_size: Union[int, None] = 32,
    mode: Union[str, None] = "default",
    normalized: Union[bool, None] = False,
    num_shards: Union[int, None] = 1,
    pad_last_batch: Union[bool, None] = False,
    pad_sequences: Union[bool, None] = False,
    prefetch_queue_depth: Union[int, None] = 1,
    preserve: Union[bool, None] = False,
    random_shuffle: Union[bool, None] = False,
    read_ahead: Union[bool, None] = False,
    resize_longer: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    resize_shorter: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    resize_x: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    resize_y: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    resize_z: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    roi_end: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    roi_relative: Union[bool, None] = False,
    roi_start: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    seed: Union[int, None] = -1,
    shard_id: Union[int, None] = 0,
    size: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    skip_cached_images: Union[bool, None] = False,
    skip_vfr_check: Union[bool, None] = False,
    step: Union[int, None] = -1,
    stick_to_shard: Union[bool, None] = False,
    stride: Union[int, None] = 1,
    subpixel_scale: Union[bool, None] = True,
    temp_buffer_hint: Union[int, None] = 0,
    tensor_init_bytes: Union[int, None] = 1048576,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, Sequence[DataNode], None]:
    """
    Loads, decodes and resizes video files with FFmpeg and NVDECODE, which is
    NVIDIA GPU's hardware-accelerated video decoding.

    The video streams can be in most of the container file formats. FFmpeg is used to parse video
    containers and returns a batch of sequences with shape ``(N, F, H, W, C)``, with N being
    the batch size, and F the number of frames in the sequence.

    This operator combines the features of :meth:`nvidia.dali.fn.video_reader` and :meth:`nvidia.dali.fn.resize`.

    .. note::
      The decoder supports only constant frame-rate videos.


    Supported backends
     * 'gpu'


    Keyword args
    ------------
    `sequence_length` : int
        Frames to load per sequence.
    `additional_decode_surfaces` : int, optional, default = `2`
        Additional decode surfaces to use beyond minimum required.

        This argument is ignored when the decoder cannot determine the minimum number of
        decode surfaces

        .. note::

          This can happen when the driver is an older version.

        This parameter can be used to trade off memory usage with performance.
    `antialias` : bool, optional, default = `True`
        If enabled, it applies an antialiasing filter when scaling down.

        .. note::
          Nearest neighbor interpolation does not support antialiasing.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `channels` : int, optional, default = `3`
        Number of channels.
    `dont_use_mmap` : bool, optional, default = `False`
        If set to True, the Loader will use plain file I/O instead of trying to map
        the file in memory.

        Mapping provides a small performance benefit when accessing a local file system, but most network file
        systems, do not provide optimum performance.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional, default = `DALIDataType.UINT8`
        Output data type.

        Supported types: ``UINT8`` or ``FLOAT``.
    `enable_frame_num` : bool, optional, default = `False`
        If the ``file_list`` or ``filenames`` argument is passed, returns the frame number
        output.
    `enable_timestamps` : bool, optional, default = `False`
        If the ``file_list`` or ``filenames`` argument is passed, returns the timestamps
        output.
    `file_list` : str, optional, default = `''`
        Path to the file with a list of ``file label [start_frame [end_frame]]`` values.

        Positive value means the exact frame, negative counts as a Nth frame from the end (it follows
        python array indexing schema), equal values for the start and end frame would yield an empty
        sequence and a warning. This option is mutually exclusive with ``filenames``
        and ``file_root``.
    `file_list_frame_num` : bool, optional, default = `False`
        If the start/end timestamps are provided in file_list, you can interpret them
        as frame numbers instead of as timestamps.

        If floating point values have been provided, the start frame number will be rounded up and
        the end frame number will be rounded down.

        Frame numbers start from 0.
    `file_list_include_preceding_frame` : bool, optional, default = `False`
        Changes the behavior how ``file_list`` start and end frame timestamps are translated
        to a frame number.

        If the start/end timestamps are provided in file_list as timestamps, the start frame is
        calculated as ``ceil(start_time_stamp * FPS)`` and the end as ``floor(end_time_stamp * FPS)``.
        If this argument is set to True, the equation changes to ``floor(start_time_stamp * FPS)`` and
        ``ceil(end_time_stamp * FPS)`` respectively. In effect, the first returned frame is not later, and
        the end frame not earlier, than the provided timestamps. This behavior is more aligned with how the visible
        timestamps are correlated with displayed video frames.

        .. note::

          When ``file_list_frame_num`` is set to True, this option does not take any effect.

        .. warning::

          This option is available for legacy behavior compatibility.
    `file_root` : str, optional, default = `''`
        Path to a directory that contains the data files.

        This option is mutually exclusive with ``filenames`` and ``file_list``.
    `filenames` : str or list of str, optional, default = `[]`
        File names of the video files to load.

        This option is mutually exclusive with ``file_list`` and ``file_root``.
    `image_type` : :class:`nvidia.dali.types.DALIImageType`, optional, default = `DALIImageType.RGB`
        The color space of the output frames (RGB or YCbCr).
    `initial_fill` : int, optional, default = `1024`
        Size of the buffer that is used for shuffling.

        If ``random_shuffle`` is False, this parameter is ignored.
    `interp_type` : :class:`nvidia.dali.types.DALIInterpType` or TensorList of :class:`nvidia.dali.types.DALIInterpType`, optional, default = `DALIInterpType.INTERP_LINEAR`
        Type of interpolation to be used.

        Use ``min_filter`` and ``mag_filter`` to specify different filtering for downscaling and upscaling.

        .. note::
          Usage of INTERP_TRIANGULAR is now deprecated and it should be replaced by a combination of
        INTERP_LINEAR with ``antialias`` enabled.
    `labels` : int or list of int, optional
        Labels associated with the files listed in
        ``filenames`` argument.

        If an empty list is provided, sequential 0-based indices are used as labels. If not provided,
        no labels will be yielded.
    `lazy_init` : bool, optional, default = `False`
        Parse and prepare the dataset metadata only during the first run instead of
        in the constructor.
    `mag_filter` : :class:`nvidia.dali.types.DALIInterpType` or TensorList of :class:`nvidia.dali.types.DALIInterpType`, optional, default = `DALIInterpType.INTERP_LINEAR`
        Filter used when scaling up.
    `max_size` : float or list of float, optional
        Limit of the output size.

        When the operator is configured to keep aspect ratio and only the smaller dimension is specified,
        the other(s) can grow very large. This can happen when using ``resize_shorter`` argument
        or "not_smaller" mode or when some extents are left unspecified.

        This parameter puts a limit to how big the output can become. This value can be specified per-axis
        or uniformly for all axes.

        .. note::
          When used with "not_smaller" mode or ``resize_shorter`` argument, ``max_size`` takes
          precedence and the aspect ratio is kept - for example, resizing with
          ``mode="not_smaller", size=800, max_size=1400`` an image of size 1200x600 would be resized to
          1400x700.
    `min_filter` : :class:`nvidia.dali.types.DALIInterpType` or TensorList of :class:`nvidia.dali.types.DALIInterpType`, optional, default = `DALIInterpType.INTERP_LINEAR`
        Filter used when scaling down.
    `minibatch_size` : int, optional, default = `32`
        Maximum number of images that are processed in
        a kernel call.
    `mode` : str, optional, default = `'default'`
        Resize mode.

          Here is a list of supported modes:

          * | ``"default"`` - image is resized to the specified size.
            | Missing extents are scaled with the average scale of the provided ones.
          * | ``"stretch"`` - image is resized to the specified size.
            | Missing extents are not scaled at all.
          * | ``"not_larger"`` - image is resized, keeping the aspect ratio, so that no extent of the
              output image exceeds the specified size.
            | For example, a 1280x720, with a desired output size of 640x480, actually produces
              a 640x360 output.
          * | ``"not_smaller"`` - image is resized, keeping the aspect ratio, so that no extent of the
              output image is smaller than specified.
            | For example, a 640x480 image with a desired output size of 1920x1080, actually produces
              a 1920x1440 output.

            This argument is mutually exclusive with ``resize_longer`` and ``resize_shorter``
    `normalized` : bool, optional, default = `False`
        Gets the output as normalized data.
    `num_shards` : int, optional, default = `1`
        Partitions the data into the specified number of parts (shards).

        This is typically used for multi-GPU or multi-node training.
    `pad_last_batch` : bool, optional, default = `False`
        If set to True, pads the shard by repeating the last sample.

        .. note::
          If the number of batches differs across shards, this option can cause an entire batch of repeated
          samples to be added to the dataset.
    `pad_sequences` : bool, optional, default = `False`
        Allows creation of incomplete sequences if there is an insufficient number
        of frames at the very end of the video.

        Redundant frames are zeroed. Corresponding time stamps and frame numbers are set to -1.
    `prefetch_queue_depth` : int, optional, default = `1`
        Specifies the number of batches to be prefetched by the internal Loader.

        This value should be increased when the pipeline is CPU-stage bound, trading memory
        consumption for better interleaving with the Loader thread.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_shuffle` : bool, optional, default = `False`
        Determines whether to randomly shuffle data.

        A prefetch buffer with a size equal to ``initial_fill`` is used to read data sequentially,
        and then samples are selected randomly to form a batch.
    `read_ahead` : bool, optional, default = `False`
        Determines whether the accessed data should be read ahead.

        For large files such as LMDB, RecordIO, or TFRecord, this argument slows down the first access but
        decreases the time of all of the following accesses.
    `resize_longer` : float or TensorList of float, optional, default = `0.0`
        The length of the longer dimension of the resized image.

        This option is mutually exclusive with ``resize_shorter`` and explicit size arguments, and
        the operator keeps the aspect ratio of the original image.
        This option is equivalent to specifying the same size for all dimensions and ``mode="not_larger"``.
    `resize_shorter` : float or TensorList of float, optional, default = `0.0`
        The length of the shorter dimension of the resized image.

        This option is mutually exclusive with ``resize_longer`` and explicit size arguments, and
        the operator keeps the aspect ratio of the original image.
        This option is equivalent to specifying the same size for all dimensions and ``mode="not_smaller"``.
        The longer dimension can be bounded by setting the ``max_size`` argument.
        See ``max_size`` argument doc for more info.
    `resize_x` : float or TensorList of float, optional, default = `0.0`
        The length of the X dimension of the resized image.

        This option is mutually exclusive with ``resize_shorter``, ``resize_longer`` and ``size``.
        If the ``resize_y`` is unspecified or 0, the operator keeps the aspect ratio of the original image.
        A negative value flips the image.
    `resize_y` : float or TensorList of float, optional, default = `0.0`
        The length of the Y dimension of the resized image.

        This option is mutually exclusive with ``resize_shorter``, ``resize_longer`` and ``size``.
        If the ``resize_x`` is unspecified or 0, the operator keeps the aspect ratio of the original image.
        A negative value flips the image.
    `resize_z` : float or TensorList of float, optional, default = `0.0`
        The length of the Z dimension of the resized volume.

        This option is mutually exclusive with ``resize_shorter``, ``resize_longer`` and ``size``.
        If the ``resize_x`` and ``resize_y`` are left unspecified or 0, then the op will keep
        the aspect ratio of the original volume. Negative value flips the volume.
    `roi_end` : float or list of float or TensorList of float, optional
        End of the input region of interest (ROI).

        Must be specified together with ``roi_start``. The coordinates follow the tensor shape order, which is
        the same as ``size``. The coordinates can be either absolute (in pixels, which is the default) or
        relative (0..1), depending on the value of ``relative_roi`` argument. If the ROI origin is greater
        than the ROI end in any dimension, the region is flipped in that dimension.
    `roi_relative` : bool, optional, default = `False`
        If true, ROI coordinates are relative to the input size,
        where 0 denotes top/left and 1 denotes bottom/right
    `roi_start` : float or list of float or TensorList of float, optional
        Origin of the input region of interest (ROI).

        Must be specified together with ``roi_end``. The coordinates follow the tensor shape order, which is
        the same as ``size``. The coordinates can be either absolute (in pixels, which is the default) or
        relative (0..1), depending on the value of ``relative_roi`` argument. If the ROI origin is greater
        than the ROI end in any dimension, the region is flipped in that dimension.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shard_id` : int, optional, default = `0`
        Index of the shard to read.
    `size` : float or list of float or TensorList of float, optional
        The desired output size.

        Must be a list/tuple with one entry per spatial dimension, excluding video frames and channels.
        Dimensions with a 0 extent are treated as absent, and the output size will be calculated based on
        other extents and ``mode`` argument.
    `skip_cached_images` : bool, optional, default = `False`
        If set to True, the loading data will be skipped when the sample is
        in the decoder cache.

        In this case, the output of the loader will be empty.
    `skip_vfr_check` : bool, optional, default = `False`
        Skips the check for the variable frame rate (VFR) videos.

        Use this flag to suppress false positive detection of VFR videos.

        .. warning::

          When the dataset indeed contains VFR files, setting this flag may cause the decoder to
          malfunction.
    `step` : int, optional, default = `-1`
        Frame interval between each sequence.

        When the value is less than 0, ``step`` is set to ``sequence_length``.
    `stick_to_shard` : bool, optional, default = `False`
        Determines whether the reader should stick to a data shard instead of going through
        the entire dataset.

        If decoder caching is used, it significantly reduces the amount of data to be cached, but
        might affect accuracy of the training.
    `stride` : int, optional, default = `1`
        Distance between consecutive frames in the sequence.
    `subpixel_scale` : bool, optional, default = `True`
        If True, fractional sizes, directly specified or
        calculated, will cause the input ROI to be adjusted to keep the scale factor.

        Otherwise, the scale factor will be adjusted so that the source image maps to
        the rounded output size.
    `temp_buffer_hint` : int, optional, default = `0`
        Initial size in bytes, of a temporary buffer for resampling.

        .. note::
          This argument is ignored for the CPU variant.
    `tensor_init_bytes` : int, optional, default = `1048576`
        Hint for how much memory to allocate per image.

    """
    ...

def webdataset(
    *,
    ext: Union[Sequence[str], str],
    paths: Union[Sequence[str], str],
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    case_sensitive_extensions: Union[bool, None] = True,
    dont_use_mmap: Union[bool, None] = False,
    dtypes: Union[Sequence[DALIDataType], DALIDataType, None] = None,
    index_paths: Union[Sequence[str], str, None] = [],
    initial_fill: Union[int, None] = 1024,
    lazy_init: Union[bool, None] = False,
    missing_component_behavior: Union[str, None] = "",
    num_shards: Union[int, None] = 1,
    pad_last_batch: Union[bool, None] = False,
    prefetch_queue_depth: Union[int, None] = 1,
    preserve: Union[bool, None] = False,
    random_shuffle: Union[bool, None] = False,
    read_ahead: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    shard_id: Union[int, None] = 0,
    skip_cached_images: Union[bool, None] = False,
    stick_to_shard: Union[bool, None] = False,
    tensor_init_bytes: Union[int, None] = 1048576,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, Sequence[DataNode], None]:
    """
    A reader for the webdataset format.

    The webdataset format is a way of providing efficient access to datasets stored in tar archives.

    Storing data in POSIX tar archives greatly speeds up I/O operations on mechanical storage devices
    and on network file systems because it allows the operating system to reduce the number of I/O
    operations and to read the data ahead.

    WebDataset fulfils a similar function to Tensorflow's TFRecord/tf.Example classes, but is much
    easier to adopt because it does not actually require any data conversion. The data is stored in
    exactly the same format inside tar files as it is on disk, and all preprocessing and data
    augmentation code remains unchanged.

    The dataset consists of one or more tar archives, each of which is further split into samples.
    A sample contains one or more components that correspond to the actual files contained within
    the archive. The components that belong to a specific sample are aggregated by filename without
    extension (for the specifics about the extensions please read the description of the ``ext`` parameter
    below). Note that samples with their filename starting with a dot will not be loaded, as well as
    entries that are not regular files.

    In addition to the tar archive with data, each archive should come with a corresponding index file.
    The index file can be generated using a dedicated script::

        <path_to_dali>/tools/wds2idx.py <path_to_archive> <path_to_index_file>

    If the index file is not provided, it will be automatically inferred from the tar file.
    Keep in mind though that it will add considerable startup time for big datasets.

    The format of the index file is::

        v1.2 <num_samples>
        <component1_ext> <component1_data_offset> <component1_size> <component2_ext> <component2_data_offset> <component2_size> ...
        ...


    Based on https://github.com/webdataset/webdataset

    Supported backends
     * 'cpu'


    Keyword args
    ------------
    `ext` : str or list of str
        The extension sets for each of the outputs produced.

        The number of extension sets determines the number of outputs of the reader.
        The extensions of the components are counted as the text after the first dot in the name of the file
        (excluding the samples starting with a dot). The different extension options should be separated
        with a semicolon (';') and may contain dots.

        Example: "left.png;right.jpg"
    `paths` : str or list of str
        The list of (one or more) paths to the webdataset archives.

        Has to be the same length as the ``index_paths`` argument.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `case_sensitive_extensions` : bool, optional, default = `True`
        Determines whether the extensions provided via the `ext` should be case sensitive.

        Allows mixing case sizes in the `ext` argument as well as in the webdataset container. For example
        when turned off: jpg, JPG, jPG should work.

        If the extension characters cannot be represented as ASCI the result of turing this option off
        is undefined.
    `dont_use_mmap` : bool, optional, default = `False`
        If set to True, the Loader will use plain file I/O instead of trying to map
        the file in memory.

        Mapping provides a small performance benefit when accessing a local file system, but most network file
        systems, do not provide optimum performance.
    `dtypes` : nvidia.dali.types.DALIDataType or list of nvidia.dali.types.DALIDataType, optional
        Data types of the respective outputs.

        The default output data types are UINT8. However, if set, each output data type should be specified.
        Moreover, the tar file should be constructed so that it will only output a sample with its byte size
        divisible by the size of the data type.
    `index_paths` : str or list of str, optional, default = `[]`
        The list of the index files corresponding to the respective webdataset archives.

        Has to be the same length as the ``paths`` argument. In case it is not provided,
        it will be inferred automatically from the webdataset archive.
    `initial_fill` : int, optional, default = `1024`
        Size of the buffer that is used for shuffling.

        If ``random_shuffle`` is False, this parameter is ignored.
    `lazy_init` : bool, optional, default = `False`
        Parse and prepare the dataset metadata only during the first run instead of
        in the constructor.
    `missing_component_behavior` : str, optional, default = `''`
        Specifies what to do in case there is not any file in a sample corresponding to a certain output.

        Possible behaviors:
          - "empty" (default) - in that case the output that was not set will just contain an empty tensor
          - "skip" - in that case the entire sample will just be skipped (no penalty to performance except for reduced caching of the archive)
          - "error" - in that case an exception will be raised and te execution stops
    `num_shards` : int, optional, default = `1`
        Partitions the data into the specified number of parts (shards).

        This is typically used for multi-GPU or multi-node training.
    `pad_last_batch` : bool, optional, default = `False`
        If set to True, pads the shard by repeating the last sample.

        .. note::
          If the number of batches differs across shards, this option can cause an entire batch of repeated
          samples to be added to the dataset.
    `prefetch_queue_depth` : int, optional, default = `1`
        Specifies the number of batches to be prefetched by the internal Loader.

        This value should be increased when the pipeline is CPU-stage bound, trading memory
        consumption for better interleaving with the Loader thread.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_shuffle` : bool, optional, default = `False`
        Determines whether to randomly shuffle data.

        A prefetch buffer with a size equal to ``initial_fill`` is used to read data sequentially,
        and then samples are selected randomly to form a batch.
    `read_ahead` : bool, optional, default = `False`
        Determines whether the accessed data should be read ahead.

        For large files such as LMDB, RecordIO, or TFRecord, this argument slows down the first access but
        decreases the time of all of the following accesses.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shard_id` : int, optional, default = `0`
        Index of the shard to read.
    `skip_cached_images` : bool, optional, default = `False`
        If set to True, the loading data will be skipped when the sample is
        in the decoder cache.

        In this case, the output of the loader will be empty.
    `stick_to_shard` : bool, optional, default = `False`
        Determines whether the reader should stick to a data shard instead of going through
        the entire dataset.

        If decoder caching is used, it significantly reduces the amount of data to be cached, but
        might affect accuracy of the training.
    `tensor_init_bytes` : int, optional, default = `1048576`
        Hint for how much memory to allocate per image.

    """
    ...
