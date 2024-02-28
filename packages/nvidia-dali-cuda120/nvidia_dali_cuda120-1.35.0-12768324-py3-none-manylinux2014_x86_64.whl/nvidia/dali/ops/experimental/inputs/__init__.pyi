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

class Video:
    """

    Streams and decodes a video from a memory buffer. To be used with long and high resolution videos.

    Returns a batch of sequences of frames, with the layout: ``(F, H, W, C)``, where:

    * ``F`` - number of frames in a sequence,
    * ``H`` - height of the frame,
    * ``W`` - width of the frame,
    * ``C`` - number of channels in the frame.

    When using ``fn.inputs.video`` operator inside the DALI Pipeline, the user needs to provide the data
    using :meth:`Pipeline.feed_input`. When the Operator is fed with data, the Pipeline can be run
    multiple times and the ``fn.inputs.video`` operator will return consecutive sequences, as long as
    there is enough data to decode. When the source of the frames (the video file) depletes, user needs
    to call another ``feed_input`` again to provide the next video file to the operator. This Operator
    has an inner-queue for the data, so the ``feed_input`` may be called multiple times and when given
    video file ends, the Operator will fetch the next one automatically from the top of the queue.
    Running the pipeline while there is no data for the ``fn.inputs.video`` to run results in an error.

    This operator takes only one video as and input (i.e. ``input_batch_size=1``) and will return
    batches of sequences. Every output batch will have the ``max_batch_size`` samples, set during
    the Pipeline creation. When the number of frames in the video file does not allow to split
    the frames uniformly across batches, the last batch returned by this operator for a given video
    will be partial and the last sequence in this batch will be determined using
    ``last_sequence_policy`` parameter. For example::


        This is a video that consists of 67 frames (every '-' is a frame):
        -------------------------------------------------------------------


        User decided that there shall be 5 frames per sequence and the last_sequence_policy='partial':
        -------------------------------------------------------------------
        [   ][   ][   ][   ][   ][   ][   ][   ][   ][   ][   ][   ][   ][]
        -------------------------------------------------------------------
                          Since there are not enough frames, the last sequence comprises 2 frames.


        The Pipeline has max_batch_size=3, therefore the operator will return 5 batches of sequences.
        First 4 batches comprise 3 sequences and the last batch is partial and comprises 2 sequences.
        ---------------   ---------------   ---------------   ---------------   -------
        [   ][   ][   ]   [   ][   ][   ]   [   ][   ][   ]   [   ][   ][   ]   [   ][]
        ---------------   ---------------   ---------------   ---------------   -------


        With the last_sequence_policy='pad', the last sequence of the last batch will be padded with 0:
        ---------------   ---------------   ---------------   ---------------   -------000
        [   ][   ][   ]   [   ][   ][   ]   [   ][   ][   ]   [   ][   ][   ]   [   ][   ]
        ---------------   ---------------   ---------------   ---------------   -------000


    The difference between ``fn.inputs.video`` and ``fn.readers.video`` is that the former
    reads an encoded video from memory and the latter reads the encoded video from disk.

    The difference between ``fn.inputs.video`` and ``fn.decoders.video`` is that the former
    does not decode the whole video file in one go. This behaviour is needed for longer videos. E.g.
    5-min, 4k, 30fps decoded video takes about 1.7 TB of memory.

    This operator accepts most of the video containers and file formats. FFmpeg is used to parse
    the video container. In the situations, that the container does not contain required metadata
    (e.g. frames sizes, number of frames, etc...), the operator needs to find it out itself,
    which may result in a slowdown.


    Supported backends
     * 'cpu'
     * 'mixed'


    Keyword args
    ------------
    `sequence_length` : int

        Number of frames in each sequence.
    `affine` : bool, optional, default = `True`

        Applies only to the mixed backend type.
        If set to True, each thread in the internal thread pool will be tied to a specific CPU core.
         Otherwise, the threads can be reassigned to any CPU core by the operating system.
    `blocking` : bool, optional, default = `False`

        If ``True``, this operator will block until the data is available (e.g. by calling ``feed_input``).
        If ``False``, the operator will raise an error, if the data is not available.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `last_sequence_policy` : str, optional, default = `'partial'`

        Specifies, how to handle the last sequence in the video file.

        For a given number of frames in the video file and ``frames_per_sequence`` parameter,
        it might happen that the video can't be split uniformly across sequences. If the
        ``last_sequence_policy='partial'``, the last sequence might have fewer frames than
        ``frames_per_sequence`` value specified. If the ``last_sequence_policy='partial'``,
        the last sequence will always have ``frames_per_sequence`` frames and will
        be padded with empty frames.

        Allowed values are ``'partial'`` and ``'pad'``.
    `no_copy` : bool, optional, default = `False`

        Determines whether DALI should copy the buffer when ``feed_input`` is called.

        If set to True, DALI passes the user's memory directly to the pipeline, instead of copying it.
        It is the user's responsibility to keep the buffer alive and unmodified until it is
        consumed by the pipeline.

        The buffer can be modified or freed again after the outputs of the relevant iterations
        have been consumed. Effectively, it happens after ``prefetch_queue_depth`` or
        ``cpu_queue_depth * gpu_queue_depth`` (when they are not equal) iterations following
        the ``feed_input`` call.

        The memory location must match the specified ``device`` parameter of the operator.
        For the CPU, the provided memory can be one contiguous buffer or a list of contiguous Tensors.
        For the GPU, to avoid extra copy, the provided buffer must be contiguous. If you provide a list
        of separate Tensors, there will be an additional copy made internally, consuming both memory
        and bandwidth.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """

    def __init__(
        self,
        /,
        *,
        sequence_length: Union[int, None] = None,
        affine: Union[bool, None] = True,
        blocking: Union[bool, None] = False,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        last_sequence_policy: Union[str, None] = "partial",
        no_copy: Union[bool, None] = False,
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> None: ...
    def __call__(
        self,
        /,
        *,
        sequence_length: Union[int, None] = None,
        affine: Union[bool, None] = True,
        blocking: Union[bool, None] = False,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        last_sequence_policy: Union[str, None] = "partial",
        no_copy: Union[bool, None] = False,
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> DataNode:
        """__call__(**kwargs)

        Operator call to be used in graph definition. This operator doesn't have any inputs.

        """
        ...
