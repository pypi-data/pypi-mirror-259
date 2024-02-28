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
def audio(
    __input: Union[DataNode, TensorLikeIn],
    /,
    *,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    downmix: Union[bool, None] = False,
    dtype: Union[DALIDataType, None] = DALIDataType.FLOAT,
    preserve: Union[bool, None] = False,
    quality: Union[float, None] = 50.0,
    sample_rate: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Sequence[DataNode]:
    """
    Decodes waveforms from encoded audio data.

    It supports the following audio formats: wav, flac and ogg.
    This operator produces the following outputs:

    * output[0]: A batch of decoded data
    * output[1]: A batch of sampling rates [Hz].


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
    `downmix` : bool, optional, default = `False`
        If set to True, downmix all input channels to mono.

        If downmixing is turned on, the decoder output is 1D.
        If downmixing is turned off, it produces 2D output with interleaved channels.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional, default = `DALIDataType.FLOAT`
        Output data type.

        Supported types: ``INT16``, ``INT32``, ``FLOAT``.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `quality` : float, optional, default = `50.0`
        Resampling quality, where 0 is the lowest, and 100 is
        the highest.

        0 gives 3 lobes of the sinc filter, 50 gives 16 lobes, and 100 gives 64 lobes.
    `sample_rate` : float or TensorList of float, optional, default = `0.0`
        If specified, the target sample rate, in Hz, to which the audio is resampled.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def audio(
    __input: List[DataNode],
    /,
    *,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    downmix: Union[bool, None] = False,
    dtype: Union[DALIDataType, None] = DALIDataType.FLOAT,
    preserve: Union[bool, None] = False,
    quality: Union[float, None] = 50.0,
    sample_rate: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    seed: Union[int, None] = -1,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[Sequence[DataNode], List[Sequence[DataNode]]]:
    """
    Decodes waveforms from encoded audio data.

    It supports the following audio formats: wav, flac and ogg.
    This operator produces the following outputs:

    * output[0]: A batch of decoded data
    * output[1]: A batch of sampling rates [Hz].


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
    `downmix` : bool, optional, default = `False`
        If set to True, downmix all input channels to mono.

        If downmixing is turned on, the decoder output is 1D.
        If downmixing is turned off, it produces 2D output with interleaved channels.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional, default = `DALIDataType.FLOAT`
        Output data type.

        Supported types: ``INT16``, ``INT32``, ``FLOAT``.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `quality` : float, optional, default = `50.0`
        Resampling quality, where 0 is the lowest, and 100 is
        the highest.

        0 gives 3 lobes of the sinc filter, 50 gives 16 lobes, and 100 gives 64 lobes.
    `sample_rate` : float or TensorList of float, optional, default = `0.0`
        If specified, the target sample rate, in Hz, to which the audio is resampled.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """
    ...

@overload
def image(
    __input: Union[DataNode, TensorLikeIn],
    /,
    *,
    affine: Union[bool, None] = True,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    cache_batch_copy: Union[bool, None] = True,
    cache_debug: Union[bool, None] = False,
    cache_size: Union[int, None] = 0,
    cache_threshold: Union[int, None] = 0,
    cache_type: Union[str, None] = "",
    device_memory_padding: Union[int, None] = 16777216,
    device_memory_padding_jpeg2k: Union[int, None] = 0,
    host_memory_padding: Union[int, None] = 8388608,
    host_memory_padding_jpeg2k: Union[int, None] = 0,
    hw_decoder_load: Union[float, None] = 0.65,
    hybrid_huffman_threshold: Union[int, None] = 1000000,
    jpeg_fancy_upsampling: Union[bool, None] = False,
    memory_stats: Union[bool, None] = False,
    output_type: Union[DALIImageType, None] = DALIImageType.RGB,
    preallocate_height_hint: Union[int, None] = 0,
    preallocate_width_hint: Union[int, None] = 0,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    use_fast_idct: Union[bool, None] = False,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Decodes images.

    For jpeg images, depending on the backend selected ("mixed" and "cpu"), the implementation uses
    the *nvJPEG* library or *libjpeg-turbo*, respectively. Other image formats are decoded
    with *OpenCV* or other specific libraries, such as *libtiff*.

    If used with a ``mixed`` backend, and the hardware is available, the operator will use
    a dedicated hardware decoder.

    .. warning::
      Due to performance reasons, hardware decoder is disabled for driver < 455.x

    The output of the decoder is in *HWC* layout.

    Supported formats: JPG, BMP, PNG, TIFF, PNM, PPM, PGM, PBM, JPEG 2000, WebP.
    Please note that GPU acceleration for JPEG 2000 decoding is only available for CUDA 11 and newer.

    .. note::
      WebP decoding currently only supports the simple file format (lossy and lossless compression).
      For details on the different WebP file formats, see
      https://developers.google.com/speed/webp/docs/riff_container

    .. note::
      EXIF orientation metadata is disregarded.

    Supported backends
     * 'cpu'
     * 'mixed'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `affine` : bool, optional, default = `True`
        Applies **only** to the ``mixed`` backend type.

        If set to True, each thread in the internal thread pool will be tied to a specific CPU core.
        Otherwise, the threads can be reassigned to any CPU core by the operating system.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `cache_batch_copy` : bool, optional, default = `True`
        Applies **only** to the ``mixed`` backend type.

        If set to True, multiple images from the cache are copied with a batched copy kernel call.
        Otherwise, unless the order in the batch is the same as in the cache, each image is
        copied with ``cudaMemcpy``.
    `cache_debug` : bool, optional, default = `False`
        Applies **only** to the ``mixed`` backend type.

        Prints the debug information about the decoder cache.
    `cache_size` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        Total size of the decoder cache in megabytes. When provided, the decoded images
        that are larger than ``cache_threshold`` will be cached in GPU memory.
    `cache_threshold` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The size threshold, in bytes, for decoded images to be cached. When an image is cached, it no
        longer needs to be decoded when it is encountered at the operator input saving processing time.
    `cache_type` : str, optional, default = `''`
        Applies **only** to the ``mixed`` backend type.

        Here is a list of the available cache types:

        * | ``threshold``: caches every image with a size that is larger than ``cache_threshold`` until
          | the cache is full.

          The warm-up time for threshold policy is 1 epoch.
        * | ``largest``: stores the largest images that can fit in the cache.
          | The warm-up time for largest policy is 2 epochs

          .. note::
            To take advantage of caching, it is recommended to configure readers with `stick_to_shard=True`
            to limit the amount of unique images seen by each decoder instance in a multi node environment.
    `device_memory_padding` : int, optional, default = `16777216`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates one device buffer of the
        requested size per thread. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `device_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `host_memory_padding` : int, optional, default = `8388608`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates two (because of double-buffering)
        host-pinned buffers of the requested size per thread. If selected correctly, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `host_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `hw_decoder_load` : float, optional, default = `0.65`
        The percentage of the image data to be processed by the HW JPEG decoder.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        Determines the percentage of the workload that will be offloaded to the hardware decoder,
        if available. The optimal workload depends on the number of threads that are provided to
        the DALI pipeline and should be found empirically. More details can be found at
        https://developer.nvidia.com/blog/loading-data-fast-with-dali-and-new-jpeg-decoder-in-a100
    `hybrid_huffman_threshold` : int, optional, default = `1000000`
        Applies **only** to the ``mixed`` backend type.

        Images with a total number of pixels (``height * width``) that is higher than this threshold will
        use the nvJPEG hybrid Huffman decoder. Images that have fewer pixels will use the nvJPEG host-side
        Huffman decoder.

        .. note::
          Hybrid Huffman decoder still largely uses the CPU.
    `jpeg_fancy_upsampling` : bool, optional, default = `False`
        Make the ``mixed`` backend use the same chroma upsampling approach as the ``cpu`` one.

        The option corresponds to the `JPEG fancy upsampling` available in libjpegturbo or
        ImageMagick.
    `memory_stats` : bool, optional, default = `False`
        Applies **only** to the ``mixed`` backend type.

        Prints debug information about nvJPEG allocations. The information about the largest
        allocation might be useful to determine suitable values for ``device_memory_padding`` and
        ``host_memory_padding`` for a dataset.

        .. note::
          The statistics are global for the entire process, not per operator instance, and include
          the allocations made during construction if the padding hints are non-zero.
    `output_type` : :class:`nvidia.dali.types.DALIImageType`, optional, default = `DALIImageType.RGB`
        The color space of the output image.

        Note: When decoding to YCbCr, the image will be decoded to RGB and then converted to YCbCr,
        following the YCbCr definition from ITU-R BT.601.
    `preallocate_height_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preallocate_width_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `split_stages` : bool
        .. warning::

            The argument ``split_stages`` is no longer used and will be removed in a future release.
    `use_chunk_allocator` : bool
        .. warning::

            The argument ``use_chunk_allocator`` is no longer used and will be removed in a future release.
    `use_fast_idct` : bool, optional, default = `False`
        Enables fast IDCT in the libjpeg-turbo based CPU decoder, used when ``device`` is set
        to "cpu" or when the it is set to "mixed" but the particular image can not be handled by
        the GPU implementation.

        According to the libjpeg-turbo documentation, decompression performance is improved by up to 14%
        with little reduction in quality.

    """
    ...

@overload
def image(
    __input: List[DataNode],
    /,
    *,
    affine: Union[bool, None] = True,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    cache_batch_copy: Union[bool, None] = True,
    cache_debug: Union[bool, None] = False,
    cache_size: Union[int, None] = 0,
    cache_threshold: Union[int, None] = 0,
    cache_type: Union[str, None] = "",
    device_memory_padding: Union[int, None] = 16777216,
    device_memory_padding_jpeg2k: Union[int, None] = 0,
    host_memory_padding: Union[int, None] = 8388608,
    host_memory_padding_jpeg2k: Union[int, None] = 0,
    hw_decoder_load: Union[float, None] = 0.65,
    hybrid_huffman_threshold: Union[int, None] = 1000000,
    jpeg_fancy_upsampling: Union[bool, None] = False,
    memory_stats: Union[bool, None] = False,
    output_type: Union[DALIImageType, None] = DALIImageType.RGB,
    preallocate_height_hint: Union[int, None] = 0,
    preallocate_width_hint: Union[int, None] = 0,
    preserve: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    use_fast_idct: Union[bool, None] = False,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, List[DataNode]]:
    """
    Decodes images.

    For jpeg images, depending on the backend selected ("mixed" and "cpu"), the implementation uses
    the *nvJPEG* library or *libjpeg-turbo*, respectively. Other image formats are decoded
    with *OpenCV* or other specific libraries, such as *libtiff*.

    If used with a ``mixed`` backend, and the hardware is available, the operator will use
    a dedicated hardware decoder.

    .. warning::
      Due to performance reasons, hardware decoder is disabled for driver < 455.x

    The output of the decoder is in *HWC* layout.

    Supported formats: JPG, BMP, PNG, TIFF, PNM, PPM, PGM, PBM, JPEG 2000, WebP.
    Please note that GPU acceleration for JPEG 2000 decoding is only available for CUDA 11 and newer.

    .. note::
      WebP decoding currently only supports the simple file format (lossy and lossless compression).
      For details on the different WebP file formats, see
      https://developers.google.com/speed/webp/docs/riff_container

    .. note::
      EXIF orientation metadata is disregarded.

    Supported backends
     * 'cpu'
     * 'mixed'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `affine` : bool, optional, default = `True`
        Applies **only** to the ``mixed`` backend type.

        If set to True, each thread in the internal thread pool will be tied to a specific CPU core.
        Otherwise, the threads can be reassigned to any CPU core by the operating system.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `cache_batch_copy` : bool, optional, default = `True`
        Applies **only** to the ``mixed`` backend type.

        If set to True, multiple images from the cache are copied with a batched copy kernel call.
        Otherwise, unless the order in the batch is the same as in the cache, each image is
        copied with ``cudaMemcpy``.
    `cache_debug` : bool, optional, default = `False`
        Applies **only** to the ``mixed`` backend type.

        Prints the debug information about the decoder cache.
    `cache_size` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        Total size of the decoder cache in megabytes. When provided, the decoded images
        that are larger than ``cache_threshold`` will be cached in GPU memory.
    `cache_threshold` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The size threshold, in bytes, for decoded images to be cached. When an image is cached, it no
        longer needs to be decoded when it is encountered at the operator input saving processing time.
    `cache_type` : str, optional, default = `''`
        Applies **only** to the ``mixed`` backend type.

        Here is a list of the available cache types:

        * | ``threshold``: caches every image with a size that is larger than ``cache_threshold`` until
          | the cache is full.

          The warm-up time for threshold policy is 1 epoch.
        * | ``largest``: stores the largest images that can fit in the cache.
          | The warm-up time for largest policy is 2 epochs

          .. note::
            To take advantage of caching, it is recommended to configure readers with `stick_to_shard=True`
            to limit the amount of unique images seen by each decoder instance in a multi node environment.
    `device_memory_padding` : int, optional, default = `16777216`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates one device buffer of the
        requested size per thread. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `device_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `host_memory_padding` : int, optional, default = `8388608`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates two (because of double-buffering)
        host-pinned buffers of the requested size per thread. If selected correctly, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `host_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `hw_decoder_load` : float, optional, default = `0.65`
        The percentage of the image data to be processed by the HW JPEG decoder.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        Determines the percentage of the workload that will be offloaded to the hardware decoder,
        if available. The optimal workload depends on the number of threads that are provided to
        the DALI pipeline and should be found empirically. More details can be found at
        https://developer.nvidia.com/blog/loading-data-fast-with-dali-and-new-jpeg-decoder-in-a100
    `hybrid_huffman_threshold` : int, optional, default = `1000000`
        Applies **only** to the ``mixed`` backend type.

        Images with a total number of pixels (``height * width``) that is higher than this threshold will
        use the nvJPEG hybrid Huffman decoder. Images that have fewer pixels will use the nvJPEG host-side
        Huffman decoder.

        .. note::
          Hybrid Huffman decoder still largely uses the CPU.
    `jpeg_fancy_upsampling` : bool, optional, default = `False`
        Make the ``mixed`` backend use the same chroma upsampling approach as the ``cpu`` one.

        The option corresponds to the `JPEG fancy upsampling` available in libjpegturbo or
        ImageMagick.
    `memory_stats` : bool, optional, default = `False`
        Applies **only** to the ``mixed`` backend type.

        Prints debug information about nvJPEG allocations. The information about the largest
        allocation might be useful to determine suitable values for ``device_memory_padding`` and
        ``host_memory_padding`` for a dataset.

        .. note::
          The statistics are global for the entire process, not per operator instance, and include
          the allocations made during construction if the padding hints are non-zero.
    `output_type` : :class:`nvidia.dali.types.DALIImageType`, optional, default = `DALIImageType.RGB`
        The color space of the output image.

        Note: When decoding to YCbCr, the image will be decoded to RGB and then converted to YCbCr,
        following the YCbCr definition from ITU-R BT.601.
    `preallocate_height_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preallocate_width_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `split_stages` : bool
        .. warning::

            The argument ``split_stages`` is no longer used and will be removed in a future release.
    `use_chunk_allocator` : bool
        .. warning::

            The argument ``use_chunk_allocator`` is no longer used and will be removed in a future release.
    `use_fast_idct` : bool, optional, default = `False`
        Enables fast IDCT in the libjpeg-turbo based CPU decoder, used when ``device`` is set
        to "cpu" or when the it is set to "mixed" but the particular image can not be handled by
        the GPU implementation.

        According to the libjpeg-turbo documentation, decompression performance is improved by up to 14%
        with little reduction in quality.

    """
    ...

@overload
def image_crop(
    __input: Union[DataNode, TensorLikeIn],
    /,
    *,
    affine: Union[bool, None] = True,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    crop: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    crop_d: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    crop_h: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    crop_pos_x: Union[DataNode, TensorLikeArg, float, None] = 0.5,
    crop_pos_y: Union[DataNode, TensorLikeArg, float, None] = 0.5,
    crop_pos_z: Union[DataNode, TensorLikeArg, float, None] = 0.5,
    crop_w: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    device_memory_padding: Union[int, None] = 16777216,
    device_memory_padding_jpeg2k: Union[int, None] = 0,
    host_memory_padding: Union[int, None] = 8388608,
    host_memory_padding_jpeg2k: Union[int, None] = 0,
    hw_decoder_load: Union[float, None] = 0.65,
    hybrid_huffman_threshold: Union[int, None] = 1000000,
    jpeg_fancy_upsampling: Union[bool, None] = False,
    memory_stats: Union[bool, None] = False,
    output_type: Union[DALIImageType, None] = DALIImageType.RGB,
    preallocate_height_hint: Union[int, None] = 0,
    preallocate_width_hint: Union[int, None] = 0,
    preserve: Union[bool, None] = False,
    rounding: Union[str, None] = "round",
    seed: Union[int, None] = -1,
    use_fast_idct: Union[bool, None] = False,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Decodes images and extracts regions-of-interest (ROI) that are specified
    by fixed window dimensions and variable anchors.

    When possible, the argument uses the ROI decoding APIs (for example, *libjpeg-turbo* and *nvJPEG*)
    to reduce the decoding time and memory usage. When the ROI decoding is not supported for a given
    image format, it will decode the entire image and crop the selected ROI.

    The output of the decoder is in *HWC* layout.

    Supported formats: JPG, BMP, PNG, TIFF, PNM, PPM, PGM, PBM, JPEG 2000, WebP.

    .. note::
      JPEG 2000 region-of-interest (ROI) decoding is not accelerated on the GPU, and will use
      a CPU implementation regardless of the selected backend. For a GPU accelerated implementation,
      consider using separate ``decoders.image`` and ``crop`` operators.

    .. note::
      EXIF orientation metadata is disregarded.

    Supported backends
     * 'cpu'
     * 'mixed'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `affine` : bool, optional, default = `True`
        Applies **only** to the ``mixed`` backend type.

        If set to True, each thread in the internal thread pool will be tied to a specific CPU core.
        Otherwise, the threads can be reassigned to any CPU core by the operating system.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `crop` : float or list of float or TensorList of float, optional
        Shape of the cropped image, specified as a list of values (for example,
        ``(crop_H, crop_W)`` for the 2D crop and ``(crop_D, crop_H, crop_W)`` for the volumetric crop).

        Providing crop argument is incompatible with providing separate arguments such as ``crop_d``,
        ``crop_h``, and ``crop_w``.
    `crop_d` : float or TensorList of float, optional, default = `0.0`
        Applies **only** to volumetric inputs; cropping window depth (in voxels).

        ``crop_w``, ``crop_h``, and ``crop_d`` must be specified together. Providing values
        for ``crop_w``, ``crop_h``, and ``crop_d`` is incompatible with providing the fixed crop
        window dimensions (argument `crop`).
    `crop_h` : float or TensorList of float, optional, default = `0.0`
        Cropping the window height (in pixels).

        Providing values for ``crop_w`` and ``crop_h`` is incompatible with providing fixed crop
        window dimensions (argument ``crop``).
    `crop_pos_x` : float or TensorList of float, optional, default = `0.5`
        Normalized (0.0 - 1.0) horizontal position of the cropping window
        (upper left corner).

        The actual position is calculated as ``crop_x = crop_x_norm * (W - crop_W)``, where `crop_x_norm`
        is the normalized position, ``W`` is the width of the image, and ``crop_W`` is the width of the
        cropping window.

        See ``rounding`` argument for more details on how ``crop_x`` is converted to an integral value.
    `crop_pos_y` : float or TensorList of float, optional, default = `0.5`
        Normalized (0.0 - 1.0) vertical position of the start of
        the cropping window (typically, the upper left corner).

        The actual position is calculated as ``crop_y = crop_y_norm * (H - crop_H)``, where ``crop_y_norm``
        is the normalized position, `H` is the height of the image, and ``crop_H`` is the height of the
        cropping window.

        See ``rounding`` argument for more details on how ``crop_y`` is converted to an integral value.
    `crop_pos_z` : float or TensorList of float, optional, default = `0.5`
        Applies **only** to volumetric inputs.

        Normalized (0.0 - 1.0) normal position of the cropping window (front plane).
        The actual position is calculated as ``crop_z = crop_z_norm * (D - crop_D)``, where ``crop_z_norm``
        is the normalized position, ``D`` is the depth of the image and ``crop_D`` is the depth of the
        cropping window.

        See ``rounding`` argument for more details on how ``crop_z`` is converted to an integral value.
    `crop_w` : float or TensorList of float, optional, default = `0.0`
        Cropping window width (in pixels).

        Providing values for ``crop_w`` and ``crop_h`` is incompatible with providing fixed crop window
        dimensions (argument ``crop``).
    `device_memory_padding` : int, optional, default = `16777216`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates one device buffer of the
        requested size per thread. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `device_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `host_memory_padding` : int, optional, default = `8388608`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates two (because of double-buffering)
        host-pinned buffers of the requested size per thread. If selected correctly, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `host_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `hw_decoder_load` : float, optional, default = `0.65`
        The percentage of the image data to be processed by the HW JPEG decoder.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        Determines the percentage of the workload that will be offloaded to the hardware decoder,
        if available. The optimal workload depends on the number of threads that are provided to
        the DALI pipeline and should be found empirically. More details can be found at
        https://developer.nvidia.com/blog/loading-data-fast-with-dali-and-new-jpeg-decoder-in-a100
    `hybrid_huffman_threshold` : int, optional, default = `1000000`
        Applies **only** to the ``mixed`` backend type.

        Images with a total number of pixels (``height * width``) that is higher than this threshold will
        use the nvJPEG hybrid Huffman decoder. Images that have fewer pixels will use the nvJPEG host-side
        Huffman decoder.

        .. note::
          Hybrid Huffman decoder still largely uses the CPU.
    `jpeg_fancy_upsampling` : bool, optional, default = `False`
        Make the ``mixed`` backend use the same chroma upsampling approach as the ``cpu`` one.

        The option corresponds to the `JPEG fancy upsampling` available in libjpegturbo or
        ImageMagick.
    `memory_stats` : bool, optional, default = `False`
        Applies **only** to the ``mixed`` backend type.

        Prints debug information about nvJPEG allocations. The information about the largest
        allocation might be useful to determine suitable values for ``device_memory_padding`` and
        ``host_memory_padding`` for a dataset.

        .. note::
          The statistics are global for the entire process, not per operator instance, and include
          the allocations made during construction if the padding hints are non-zero.
    `output_type` : :class:`nvidia.dali.types.DALIImageType`, optional, default = `DALIImageType.RGB`
        The color space of the output image.

        Note: When decoding to YCbCr, the image will be decoded to RGB and then converted to YCbCr,
        following the YCbCr definition from ITU-R BT.601.
    `preallocate_height_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preallocate_width_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `rounding` : str, optional, default = `'round'`
        Determines the rounding function used to convert the starting coordinate
        of the window to an integral value (see ``crop_pos_x``, ``crop_pos_y``, ``crop_pos_z``).

        Possible values are:

        * | ``"round"`` - Rounds to the nearest integer value, with halfway cases rounded away from zero.
        * | ``"truncate"`` - Discards the fractional part of the number (truncates towards zero).
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `split_stages` : bool
        .. warning::

            The argument ``split_stages`` is no longer used and will be removed in a future release.
    `use_chunk_allocator` : bool
        .. warning::

            The argument ``use_chunk_allocator`` is no longer used and will be removed in a future release.
    `use_fast_idct` : bool, optional, default = `False`
        Enables fast IDCT in the libjpeg-turbo based CPU decoder, used when ``device`` is set
        to "cpu" or when the it is set to "mixed" but the particular image can not be handled by
        the GPU implementation.

        According to the libjpeg-turbo documentation, decompression performance is improved by up to 14%
        with little reduction in quality.

    """
    ...

@overload
def image_crop(
    __input: List[DataNode],
    /,
    *,
    affine: Union[bool, None] = True,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    crop: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    crop_d: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    crop_h: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    crop_pos_x: Union[DataNode, TensorLikeArg, float, None] = 0.5,
    crop_pos_y: Union[DataNode, TensorLikeArg, float, None] = 0.5,
    crop_pos_z: Union[DataNode, TensorLikeArg, float, None] = 0.5,
    crop_w: Union[DataNode, TensorLikeArg, float, None] = 0.0,
    device_memory_padding: Union[int, None] = 16777216,
    device_memory_padding_jpeg2k: Union[int, None] = 0,
    host_memory_padding: Union[int, None] = 8388608,
    host_memory_padding_jpeg2k: Union[int, None] = 0,
    hw_decoder_load: Union[float, None] = 0.65,
    hybrid_huffman_threshold: Union[int, None] = 1000000,
    jpeg_fancy_upsampling: Union[bool, None] = False,
    memory_stats: Union[bool, None] = False,
    output_type: Union[DALIImageType, None] = DALIImageType.RGB,
    preallocate_height_hint: Union[int, None] = 0,
    preallocate_width_hint: Union[int, None] = 0,
    preserve: Union[bool, None] = False,
    rounding: Union[str, None] = "round",
    seed: Union[int, None] = -1,
    use_fast_idct: Union[bool, None] = False,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, List[DataNode]]:
    """
    Decodes images and extracts regions-of-interest (ROI) that are specified
    by fixed window dimensions and variable anchors.

    When possible, the argument uses the ROI decoding APIs (for example, *libjpeg-turbo* and *nvJPEG*)
    to reduce the decoding time and memory usage. When the ROI decoding is not supported for a given
    image format, it will decode the entire image and crop the selected ROI.

    The output of the decoder is in *HWC* layout.

    Supported formats: JPG, BMP, PNG, TIFF, PNM, PPM, PGM, PBM, JPEG 2000, WebP.

    .. note::
      JPEG 2000 region-of-interest (ROI) decoding is not accelerated on the GPU, and will use
      a CPU implementation regardless of the selected backend. For a GPU accelerated implementation,
      consider using separate ``decoders.image`` and ``crop`` operators.

    .. note::
      EXIF orientation metadata is disregarded.

    Supported backends
     * 'cpu'
     * 'mixed'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `affine` : bool, optional, default = `True`
        Applies **only** to the ``mixed`` backend type.

        If set to True, each thread in the internal thread pool will be tied to a specific CPU core.
        Otherwise, the threads can be reassigned to any CPU core by the operating system.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `crop` : float or list of float or TensorList of float, optional
        Shape of the cropped image, specified as a list of values (for example,
        ``(crop_H, crop_W)`` for the 2D crop and ``(crop_D, crop_H, crop_W)`` for the volumetric crop).

        Providing crop argument is incompatible with providing separate arguments such as ``crop_d``,
        ``crop_h``, and ``crop_w``.
    `crop_d` : float or TensorList of float, optional, default = `0.0`
        Applies **only** to volumetric inputs; cropping window depth (in voxels).

        ``crop_w``, ``crop_h``, and ``crop_d`` must be specified together. Providing values
        for ``crop_w``, ``crop_h``, and ``crop_d`` is incompatible with providing the fixed crop
        window dimensions (argument `crop`).
    `crop_h` : float or TensorList of float, optional, default = `0.0`
        Cropping the window height (in pixels).

        Providing values for ``crop_w`` and ``crop_h`` is incompatible with providing fixed crop
        window dimensions (argument ``crop``).
    `crop_pos_x` : float or TensorList of float, optional, default = `0.5`
        Normalized (0.0 - 1.0) horizontal position of the cropping window
        (upper left corner).

        The actual position is calculated as ``crop_x = crop_x_norm * (W - crop_W)``, where `crop_x_norm`
        is the normalized position, ``W`` is the width of the image, and ``crop_W`` is the width of the
        cropping window.

        See ``rounding`` argument for more details on how ``crop_x`` is converted to an integral value.
    `crop_pos_y` : float or TensorList of float, optional, default = `0.5`
        Normalized (0.0 - 1.0) vertical position of the start of
        the cropping window (typically, the upper left corner).

        The actual position is calculated as ``crop_y = crop_y_norm * (H - crop_H)``, where ``crop_y_norm``
        is the normalized position, `H` is the height of the image, and ``crop_H`` is the height of the
        cropping window.

        See ``rounding`` argument for more details on how ``crop_y`` is converted to an integral value.
    `crop_pos_z` : float or TensorList of float, optional, default = `0.5`
        Applies **only** to volumetric inputs.

        Normalized (0.0 - 1.0) normal position of the cropping window (front plane).
        The actual position is calculated as ``crop_z = crop_z_norm * (D - crop_D)``, where ``crop_z_norm``
        is the normalized position, ``D`` is the depth of the image and ``crop_D`` is the depth of the
        cropping window.

        See ``rounding`` argument for more details on how ``crop_z`` is converted to an integral value.
    `crop_w` : float or TensorList of float, optional, default = `0.0`
        Cropping window width (in pixels).

        Providing values for ``crop_w`` and ``crop_h`` is incompatible with providing fixed crop window
        dimensions (argument ``crop``).
    `device_memory_padding` : int, optional, default = `16777216`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates one device buffer of the
        requested size per thread. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `device_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `host_memory_padding` : int, optional, default = `8388608`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates two (because of double-buffering)
        host-pinned buffers of the requested size per thread. If selected correctly, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `host_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `hw_decoder_load` : float, optional, default = `0.65`
        The percentage of the image data to be processed by the HW JPEG decoder.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        Determines the percentage of the workload that will be offloaded to the hardware decoder,
        if available. The optimal workload depends on the number of threads that are provided to
        the DALI pipeline and should be found empirically. More details can be found at
        https://developer.nvidia.com/blog/loading-data-fast-with-dali-and-new-jpeg-decoder-in-a100
    `hybrid_huffman_threshold` : int, optional, default = `1000000`
        Applies **only** to the ``mixed`` backend type.

        Images with a total number of pixels (``height * width``) that is higher than this threshold will
        use the nvJPEG hybrid Huffman decoder. Images that have fewer pixels will use the nvJPEG host-side
        Huffman decoder.

        .. note::
          Hybrid Huffman decoder still largely uses the CPU.
    `jpeg_fancy_upsampling` : bool, optional, default = `False`
        Make the ``mixed`` backend use the same chroma upsampling approach as the ``cpu`` one.

        The option corresponds to the `JPEG fancy upsampling` available in libjpegturbo or
        ImageMagick.
    `memory_stats` : bool, optional, default = `False`
        Applies **only** to the ``mixed`` backend type.

        Prints debug information about nvJPEG allocations. The information about the largest
        allocation might be useful to determine suitable values for ``device_memory_padding`` and
        ``host_memory_padding`` for a dataset.

        .. note::
          The statistics are global for the entire process, not per operator instance, and include
          the allocations made during construction if the padding hints are non-zero.
    `output_type` : :class:`nvidia.dali.types.DALIImageType`, optional, default = `DALIImageType.RGB`
        The color space of the output image.

        Note: When decoding to YCbCr, the image will be decoded to RGB and then converted to YCbCr,
        following the YCbCr definition from ITU-R BT.601.
    `preallocate_height_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preallocate_width_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `rounding` : str, optional, default = `'round'`
        Determines the rounding function used to convert the starting coordinate
        of the window to an integral value (see ``crop_pos_x``, ``crop_pos_y``, ``crop_pos_z``).

        Possible values are:

        * | ``"round"`` - Rounds to the nearest integer value, with halfway cases rounded away from zero.
        * | ``"truncate"`` - Discards the fractional part of the number (truncates towards zero).
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `split_stages` : bool
        .. warning::

            The argument ``split_stages`` is no longer used and will be removed in a future release.
    `use_chunk_allocator` : bool
        .. warning::

            The argument ``use_chunk_allocator`` is no longer used and will be removed in a future release.
    `use_fast_idct` : bool, optional, default = `False`
        Enables fast IDCT in the libjpeg-turbo based CPU decoder, used when ``device`` is set
        to "cpu" or when the it is set to "mixed" but the particular image can not be handled by
        the GPU implementation.

        According to the libjpeg-turbo documentation, decompression performance is improved by up to 14%
        with little reduction in quality.

    """
    ...

@overload
def image_random_crop(
    __input: Union[DataNode, TensorLikeIn],
    /,
    *,
    affine: Union[bool, None] = True,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    device_memory_padding: Union[int, None] = 16777216,
    device_memory_padding_jpeg2k: Union[int, None] = 0,
    host_memory_padding: Union[int, None] = 8388608,
    host_memory_padding_jpeg2k: Union[int, None] = 0,
    hw_decoder_load: Union[float, None] = 0.65,
    hybrid_huffman_threshold: Union[int, None] = 1000000,
    jpeg_fancy_upsampling: Union[bool, None] = False,
    memory_stats: Union[bool, None] = False,
    num_attempts: Union[int, None] = 10,
    output_type: Union[DALIImageType, None] = DALIImageType.RGB,
    preallocate_height_hint: Union[int, None] = 0,
    preallocate_width_hint: Union[int, None] = 0,
    preserve: Union[bool, None] = False,
    random_area: Union[Sequence[float], float, None] = [0.08, 1.0],
    random_aspect_ratio: Union[Sequence[float], float, None] = [0.75, 1.333333],
    seed: Union[int, None] = -1,
    use_fast_idct: Union[bool, None] = False,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Decodes images and randomly crops them.

    The cropping window's area (relative to the entire image) and aspect ratio can be restricted to
    a range of values specified by ``area`` and ``aspect_ratio`` arguments, respectively.

    When possible, the operator uses the ROI decoding APIs (for example, *libjpeg-turbo* and *nvJPEG*)
    to reduce the decoding time and memory usage. When the ROI decoding is not supported for a given
    image format, it will decode the entire image and crop the selected ROI.

    The output of the decoder is in *HWC* layout.

    Supported formats: JPG, BMP, PNG, TIFF, PNM, PPM, PGM, PBM, JPEG 2000, WebP.

    .. note::
      JPEG 2000 region-of-interest (ROI) decoding is not accelerated on the GPU, and will use
      a CPU implementation regardless of the selected backend. For a GPU accelerated implementation,
      consider using separate ``decoders.image`` and ``random_crop`` operators.

    .. note::
      EXIF orientation metadata is disregarded.

    Supported backends
     * 'cpu'
     * 'mixed'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `affine` : bool, optional, default = `True`
        Applies **only** to the ``mixed`` backend type.

        If set to True, each thread in the internal thread pool will be tied to a specific CPU core.
        Otherwise, the threads can be reassigned to any CPU core by the operating system.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `device_memory_padding` : int, optional, default = `16777216`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates one device buffer of the
        requested size per thread. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `device_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `host_memory_padding` : int, optional, default = `8388608`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates two (because of double-buffering)
        host-pinned buffers of the requested size per thread. If selected correctly, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `host_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `hw_decoder_load` : float, optional, default = `0.65`
        The percentage of the image data to be processed by the HW JPEG decoder.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        Determines the percentage of the workload that will be offloaded to the hardware decoder,
        if available. The optimal workload depends on the number of threads that are provided to
        the DALI pipeline and should be found empirically. More details can be found at
        https://developer.nvidia.com/blog/loading-data-fast-with-dali-and-new-jpeg-decoder-in-a100
    `hybrid_huffman_threshold` : int, optional, default = `1000000`
        Applies **only** to the ``mixed`` backend type.

        Images with a total number of pixels (``height * width``) that is higher than this threshold will
        use the nvJPEG hybrid Huffman decoder. Images that have fewer pixels will use the nvJPEG host-side
        Huffman decoder.

        .. note::
          Hybrid Huffman decoder still largely uses the CPU.
    `jpeg_fancy_upsampling` : bool, optional, default = `False`
        Make the ``mixed`` backend use the same chroma upsampling approach as the ``cpu`` one.

        The option corresponds to the `JPEG fancy upsampling` available in libjpegturbo or
        ImageMagick.
    `memory_stats` : bool, optional, default = `False`
        Applies **only** to the ``mixed`` backend type.

        Prints debug information about nvJPEG allocations. The information about the largest
        allocation might be useful to determine suitable values for ``device_memory_padding`` and
        ``host_memory_padding`` for a dataset.

        .. note::
          The statistics are global for the entire process, not per operator instance, and include
          the allocations made during construction if the padding hints are non-zero.
    `num_attempts` : int, optional, default = `10`
        Maximum number of attempts used to choose random area and aspect ratio.
    `output_type` : :class:`nvidia.dali.types.DALIImageType`, optional, default = `DALIImageType.RGB`
        The color space of the output image.

        Note: When decoding to YCbCr, the image will be decoded to RGB and then converted to YCbCr,
        following the YCbCr definition from ITU-R BT.601.
    `preallocate_height_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preallocate_width_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_area` : float or list of float, optional, default = `[0.08, 1.0]`
        Range from which to choose random area fraction ``A``.

        The cropped image's area will be equal to ``A`` * original image's area.
    `random_aspect_ratio` : float or list of float, optional, default = `[0.75, 1.333333]`
        Range from which to choose random aspect ratio (width/height).
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `split_stages` : bool
        .. warning::

            The argument ``split_stages`` is no longer used and will be removed in a future release.
    `use_chunk_allocator` : bool
        .. warning::

            The argument ``use_chunk_allocator`` is no longer used and will be removed in a future release.
    `use_fast_idct` : bool, optional, default = `False`
        Enables fast IDCT in the libjpeg-turbo based CPU decoder, used when ``device`` is set
        to "cpu" or when the it is set to "mixed" but the particular image can not be handled by
        the GPU implementation.

        According to the libjpeg-turbo documentation, decompression performance is improved by up to 14%
        with little reduction in quality.

    """
    ...

@overload
def image_random_crop(
    __input: List[DataNode],
    /,
    *,
    affine: Union[bool, None] = True,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    device_memory_padding: Union[int, None] = 16777216,
    device_memory_padding_jpeg2k: Union[int, None] = 0,
    host_memory_padding: Union[int, None] = 8388608,
    host_memory_padding_jpeg2k: Union[int, None] = 0,
    hw_decoder_load: Union[float, None] = 0.65,
    hybrid_huffman_threshold: Union[int, None] = 1000000,
    jpeg_fancy_upsampling: Union[bool, None] = False,
    memory_stats: Union[bool, None] = False,
    num_attempts: Union[int, None] = 10,
    output_type: Union[DALIImageType, None] = DALIImageType.RGB,
    preallocate_height_hint: Union[int, None] = 0,
    preallocate_width_hint: Union[int, None] = 0,
    preserve: Union[bool, None] = False,
    random_area: Union[Sequence[float], float, None] = [0.08, 1.0],
    random_aspect_ratio: Union[Sequence[float], float, None] = [0.75, 1.333333],
    seed: Union[int, None] = -1,
    use_fast_idct: Union[bool, None] = False,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, List[DataNode]]:
    """
    Decodes images and randomly crops them.

    The cropping window's area (relative to the entire image) and aspect ratio can be restricted to
    a range of values specified by ``area`` and ``aspect_ratio`` arguments, respectively.

    When possible, the operator uses the ROI decoding APIs (for example, *libjpeg-turbo* and *nvJPEG*)
    to reduce the decoding time and memory usage. When the ROI decoding is not supported for a given
    image format, it will decode the entire image and crop the selected ROI.

    The output of the decoder is in *HWC* layout.

    Supported formats: JPG, BMP, PNG, TIFF, PNM, PPM, PGM, PBM, JPEG 2000, WebP.

    .. note::
      JPEG 2000 region-of-interest (ROI) decoding is not accelerated on the GPU, and will use
      a CPU implementation regardless of the selected backend. For a GPU accelerated implementation,
      consider using separate ``decoders.image`` and ``random_crop`` operators.

    .. note::
      EXIF orientation metadata is disregarded.

    Supported backends
     * 'cpu'
     * 'mixed'


    Args
    ----
    `__input` : TensorList
        Input to the operator.


    Keyword args
    ------------
    `affine` : bool, optional, default = `True`
        Applies **only** to the ``mixed`` backend type.

        If set to True, each thread in the internal thread pool will be tied to a specific CPU core.
        Otherwise, the threads can be reassigned to any CPU core by the operating system.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `device_memory_padding` : int, optional, default = `16777216`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates one device buffer of the
        requested size per thread. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `device_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `host_memory_padding` : int, optional, default = `8388608`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates two (because of double-buffering)
        host-pinned buffers of the requested size per thread. If selected correctly, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `host_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `hw_decoder_load` : float, optional, default = `0.65`
        The percentage of the image data to be processed by the HW JPEG decoder.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        Determines the percentage of the workload that will be offloaded to the hardware decoder,
        if available. The optimal workload depends on the number of threads that are provided to
        the DALI pipeline and should be found empirically. More details can be found at
        https://developer.nvidia.com/blog/loading-data-fast-with-dali-and-new-jpeg-decoder-in-a100
    `hybrid_huffman_threshold` : int, optional, default = `1000000`
        Applies **only** to the ``mixed`` backend type.

        Images with a total number of pixels (``height * width``) that is higher than this threshold will
        use the nvJPEG hybrid Huffman decoder. Images that have fewer pixels will use the nvJPEG host-side
        Huffman decoder.

        .. note::
          Hybrid Huffman decoder still largely uses the CPU.
    `jpeg_fancy_upsampling` : bool, optional, default = `False`
        Make the ``mixed`` backend use the same chroma upsampling approach as the ``cpu`` one.

        The option corresponds to the `JPEG fancy upsampling` available in libjpegturbo or
        ImageMagick.
    `memory_stats` : bool, optional, default = `False`
        Applies **only** to the ``mixed`` backend type.

        Prints debug information about nvJPEG allocations. The information about the largest
        allocation might be useful to determine suitable values for ``device_memory_padding`` and
        ``host_memory_padding`` for a dataset.

        .. note::
          The statistics are global for the entire process, not per operator instance, and include
          the allocations made during construction if the padding hints are non-zero.
    `num_attempts` : int, optional, default = `10`
        Maximum number of attempts used to choose random area and aspect ratio.
    `output_type` : :class:`nvidia.dali.types.DALIImageType`, optional, default = `DALIImageType.RGB`
        The color space of the output image.

        Note: When decoding to YCbCr, the image will be decoded to RGB and then converted to YCbCr,
        following the YCbCr definition from ITU-R BT.601.
    `preallocate_height_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preallocate_width_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_area` : float or list of float, optional, default = `[0.08, 1.0]`
        Range from which to choose random area fraction ``A``.

        The cropped image's area will be equal to ``A`` * original image's area.
    `random_aspect_ratio` : float or list of float, optional, default = `[0.75, 1.333333]`
        Range from which to choose random aspect ratio (width/height).
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `split_stages` : bool
        .. warning::

            The argument ``split_stages`` is no longer used and will be removed in a future release.
    `use_chunk_allocator` : bool
        .. warning::

            The argument ``use_chunk_allocator`` is no longer used and will be removed in a future release.
    `use_fast_idct` : bool, optional, default = `False`
        Enables fast IDCT in the libjpeg-turbo based CPU decoder, used when ``device`` is set
        to "cpu" or when the it is set to "mixed" but the particular image can not be handled by
        the GPU implementation.

        According to the libjpeg-turbo documentation, decompression performance is improved by up to 14%
        with little reduction in quality.

    """
    ...

@overload
def image_slice(
    __data: Union[DataNode, TensorLikeIn],
    __anchor: Union[DataNode, TensorLikeIn, None] = None,
    __shape: Union[DataNode, TensorLikeIn, None] = None,
    /,
    *,
    affine: Union[bool, None] = True,
    axes: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = [1, 0],
    axis_names: Union[str, None] = "WH",
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    device_memory_padding: Union[int, None] = 16777216,
    device_memory_padding_jpeg2k: Union[int, None] = 0,
    end: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
    host_memory_padding: Union[int, None] = 8388608,
    host_memory_padding_jpeg2k: Union[int, None] = 0,
    hw_decoder_load: Union[float, None] = 0.65,
    hybrid_huffman_threshold: Union[int, None] = 1000000,
    jpeg_fancy_upsampling: Union[bool, None] = False,
    memory_stats: Union[bool, None] = False,
    normalized_anchor: Union[bool, None] = True,
    normalized_shape: Union[bool, None] = True,
    output_type: Union[DALIImageType, None] = DALIImageType.RGB,
    preallocate_height_hint: Union[int, None] = 0,
    preallocate_width_hint: Union[int, None] = 0,
    preserve: Union[bool, None] = False,
    rel_end: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    rel_shape: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    rel_start: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    seed: Union[int, None] = -1,
    shape: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
    start: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
    use_fast_idct: Union[bool, None] = False,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> DataNode:
    """
    Decodes images and extracts regions of interest.

    The slice can be specified by proving the start and end coordinates, or start coordinates
    and shape of the slice. Both coordinates and shapes can be provided in absolute or relative terms.

    The slice arguments can be specified by the following named arguments:

    #. ``start``: Slice start coordinates (absolute)
    #. ``rel_start``: Slice start coordinates (relative)
    #. ``end``: Slice end coordinates (absolute)
    #. ``rel_end``: Slice end coordinates (relative)
    #. ``shape``: Slice shape (absolute)
    #. ``rel_shape``: Slice shape (relative)

    The slice can be configured by providing start and end coordinates or start and shape.
    Relative and absolute arguments can be mixed (for example, ``rel_start`` can be used with ``shape``)
    as long as start and shape or end are uniquely defined.

    Alternatively, two extra positional inputs can be provided, specifying ``anchor`` and ``shape``.
    When using positional inputs, two extra boolean arguments ``normalized_anchor``/``normalized_shape``
    can be used to specify the nature of the arguments provided. Using positional inputs for anchor
    and shape is incompatible with the named arguments specified above.

    The slice arguments should provide as many dimensions as specified by the ``axis_names`` or ``axes``
    arguments.

    By default, the :meth:`nvidia.dali.fn.decoders.image_slice` operator uses normalized coordinates
    and "WH" order for the slice arguments.

    When possible, the argument uses the ROI decoding APIs (for example, *libjpeg-turbo* and *nvJPEG*)
    to optimize the decoding time and memory usage. When the ROI decoding is not supported for a given
    image format, it will decode the entire image and crop the selected ROI.

    The output of the decoder is in the *HWC* layout.

    Supported formats: JPG, BMP, PNG, TIFF, PNM, PPM, PGM, PBM, JPEG 2000, WebP.

    .. note::
      JPEG 2000 region-of-interest (ROI) decoding is not accelerated on the GPU, and will use
      a CPU implementation regardless of the selected backend. For a GPU accelerated implementation,
      consider using separate ``decoders.image`` and ``slice`` operators.

    .. note::
      EXIF orientation metadata is disregarded.

    Supported backends
     * 'cpu'
     * 'mixed'


    Args
    ----
    `__data` : TensorList
        Batch that contains the input data.
    `__anchor` : 1D TensorList of float or int, optional
        Input that contains normalized or absolute coordinates for the starting
        point of the slice (x0, x1, x2, …).

        Integer coordinates are interpreted as absolute coordinates, while float coordinates can be
        interpreted as absolute or relative coordinates, depending on the value of
        ``normalized_anchor``.
    `__shape` : 1D TensorList of float or int, optional
        Input that contains normalized or absolute coordinates for the dimensions
        of the slice (s0, s1, s2, …).

        Integer coordinates are interpreted as absolute coordinates, while float coordinates can be
        interpreted as absolute or relative coordinates, depending on the value of
        ``normalized_shape``.


    Keyword args
    ------------
    `affine` : bool, optional, default = `True`
        Applies **only** to the ``mixed`` backend type.

        If set to True, each thread in the internal thread pool will be tied to a specific CPU core.
        Otherwise, the threads can be reassigned to any CPU core by the operating system.
    `axes` : int or list of int or TensorList of int, optional, default = `[1, 0]`
        Order of dimensions used for the anchor and shape slice inputs as dimension
        indices.

        Negative values are interpreted as counting dimensions from the back.
        Valid range: ``[-ndim, ndim-1]``, where ndim is the number of dimensions in the input data.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional, default = `'WH'`
        Order of the dimensions used for the anchor and shape slice inputs,
        as described in layout.

        If a value is provided, ``axis_names`` will have a higher priority than ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `device_memory_padding` : int, optional, default = `16777216`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates one device buffer of the
        requested size per thread. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `device_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `end` : int or list of int or TensorList of int, optional
        End coordinates of the slice.

        Note: Providing named arguments ``start``, ``end``, ``shape``, ``rel_start``, ``rel_end``, ``rel_shape``
        is incompatible with providing positional inputs anchor and shape.
    `host_memory_padding` : int, optional, default = `8388608`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates two (because of double-buffering)
        host-pinned buffers of the requested size per thread. If selected correctly, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `host_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `hw_decoder_load` : float, optional, default = `0.65`
        The percentage of the image data to be processed by the HW JPEG decoder.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        Determines the percentage of the workload that will be offloaded to the hardware decoder,
        if available. The optimal workload depends on the number of threads that are provided to
        the DALI pipeline and should be found empirically. More details can be found at
        https://developer.nvidia.com/blog/loading-data-fast-with-dali-and-new-jpeg-decoder-in-a100
    `hybrid_huffman_threshold` : int, optional, default = `1000000`
        Applies **only** to the ``mixed`` backend type.

        Images with a total number of pixels (``height * width``) that is higher than this threshold will
        use the nvJPEG hybrid Huffman decoder. Images that have fewer pixels will use the nvJPEG host-side
        Huffman decoder.

        .. note::
          Hybrid Huffman decoder still largely uses the CPU.
    `jpeg_fancy_upsampling` : bool, optional, default = `False`
        Make the ``mixed`` backend use the same chroma upsampling approach as the ``cpu`` one.

        The option corresponds to the `JPEG fancy upsampling` available in libjpegturbo or
        ImageMagick.
    `memory_stats` : bool, optional, default = `False`
        Applies **only** to the ``mixed`` backend type.

        Prints debug information about nvJPEG allocations. The information about the largest
        allocation might be useful to determine suitable values for ``device_memory_padding`` and
        ``host_memory_padding`` for a dataset.

        .. note::
          The statistics are global for the entire process, not per operator instance, and include
          the allocations made during construction if the padding hints are non-zero.
    `normalized_anchor` : bool, optional, default = `True`
        Determines whether the anchor positional input should be interpreted as normalized
        (range [0.0, 1.0]) or as absolute coordinates.

        .. note::
          This argument is only relevant when anchor data type is ``float``. For integer types,
          the coordinates are always absolute.
    `normalized_shape` : bool, optional, default = `True`
        Determines whether the shape positional input should be interpreted as normalized
        (range [0.0, 1.0]) or as absolute coordinates.

        .. note::
          This argument is only relevant when anchor data type is ``float``. For integer types,
          the coordinates are always absolute.
    `output_type` : :class:`nvidia.dali.types.DALIImageType`, optional, default = `DALIImageType.RGB`
        The color space of the output image.

        Note: When decoding to YCbCr, the image will be decoded to RGB and then converted to YCbCr,
        following the YCbCr definition from ITU-R BT.601.
    `preallocate_height_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preallocate_width_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `rel_end` : float or list of float or TensorList of float, optional
        End relative coordinates of the slice (range [0.0 - 1.0].

        Note: Providing named arguments ``start``, ``end``, ``shape``, ``rel_start``, ``rel_end``, ``rel_shape``
        is incompatible with providing positional inputs anchor and shape.
    `rel_shape` : float or list of float or TensorList of float, optional
        Relative shape of the slice (range [0.0 - 1.0]).

        Providing named arguments ``start``, ``end``, ``shape``, ``rel_start``, ``rel_end``, ``rel_shape``
        is incompatible with providing positional inputs anchor and shape.
    `rel_start` : float or list of float or TensorList of float, optional
        Start relative coordinates of the slice (range [0.0 - 1.0]).

        Note: Providing named arguments ``start``, ``end``, ``shape``, ``rel_start``, ``rel_end``, ``rel_shape``
        is incompatible with providing positional inputs anchor and shape.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shape` : int or list of int or TensorList of int, optional
        Shape of the slice.

        Providing named arguments ``start``, ``end``, ``shape``, ``rel_start``, ``rel_end``, ``rel_shape``
        is incompatible with providing positional inputs anchor and shape.
    `split_stages` : bool
        .. warning::

            The argument ``split_stages`` is no longer used and will be removed in a future release.
    `start` : int or list of int or TensorList of int, optional
        Start coordinates of the slice.

        Note: Providing named arguments ``start``/``end`` or ``start``/``shape`` is incompatible with
        providing positional inputs anchor and shape.
    `use_chunk_allocator` : bool
        .. warning::

            The argument ``use_chunk_allocator`` is no longer used and will be removed in a future release.
    `use_fast_idct` : bool, optional, default = `False`
        Enables fast IDCT in the libjpeg-turbo based CPU decoder, used when ``device`` is set
        to "cpu" or when the it is set to "mixed" but the particular image can not be handled by
        the GPU implementation.

        According to the libjpeg-turbo documentation, decompression performance is improved by up to 14%
        with little reduction in quality.

    """
    ...

@overload
def image_slice(
    __data: Union[List[DataNode], DataNode, TensorLikeIn],
    __anchor: Union[List[DataNode], DataNode, TensorLikeIn, None] = None,
    __shape: Union[List[DataNode], DataNode, TensorLikeIn, None] = None,
    /,
    *,
    affine: Union[bool, None] = True,
    axes: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = [1, 0],
    axis_names: Union[str, None] = "WH",
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    device_memory_padding: Union[int, None] = 16777216,
    device_memory_padding_jpeg2k: Union[int, None] = 0,
    end: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
    host_memory_padding: Union[int, None] = 8388608,
    host_memory_padding_jpeg2k: Union[int, None] = 0,
    hw_decoder_load: Union[float, None] = 0.65,
    hybrid_huffman_threshold: Union[int, None] = 1000000,
    jpeg_fancy_upsampling: Union[bool, None] = False,
    memory_stats: Union[bool, None] = False,
    normalized_anchor: Union[bool, None] = True,
    normalized_shape: Union[bool, None] = True,
    output_type: Union[DALIImageType, None] = DALIImageType.RGB,
    preallocate_height_hint: Union[int, None] = 0,
    preallocate_width_hint: Union[int, None] = 0,
    preserve: Union[bool, None] = False,
    rel_end: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    rel_shape: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    rel_start: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
    seed: Union[int, None] = -1,
    shape: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
    start: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
    use_fast_idct: Union[bool, None] = False,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, List[DataNode]]:
    """
    Decodes images and extracts regions of interest.

    The slice can be specified by proving the start and end coordinates, or start coordinates
    and shape of the slice. Both coordinates and shapes can be provided in absolute or relative terms.

    The slice arguments can be specified by the following named arguments:

    #. ``start``: Slice start coordinates (absolute)
    #. ``rel_start``: Slice start coordinates (relative)
    #. ``end``: Slice end coordinates (absolute)
    #. ``rel_end``: Slice end coordinates (relative)
    #. ``shape``: Slice shape (absolute)
    #. ``rel_shape``: Slice shape (relative)

    The slice can be configured by providing start and end coordinates or start and shape.
    Relative and absolute arguments can be mixed (for example, ``rel_start`` can be used with ``shape``)
    as long as start and shape or end are uniquely defined.

    Alternatively, two extra positional inputs can be provided, specifying ``anchor`` and ``shape``.
    When using positional inputs, two extra boolean arguments ``normalized_anchor``/``normalized_shape``
    can be used to specify the nature of the arguments provided. Using positional inputs for anchor
    and shape is incompatible with the named arguments specified above.

    The slice arguments should provide as many dimensions as specified by the ``axis_names`` or ``axes``
    arguments.

    By default, the :meth:`nvidia.dali.fn.decoders.image_slice` operator uses normalized coordinates
    and "WH" order for the slice arguments.

    When possible, the argument uses the ROI decoding APIs (for example, *libjpeg-turbo* and *nvJPEG*)
    to optimize the decoding time and memory usage. When the ROI decoding is not supported for a given
    image format, it will decode the entire image and crop the selected ROI.

    The output of the decoder is in the *HWC* layout.

    Supported formats: JPG, BMP, PNG, TIFF, PNM, PPM, PGM, PBM, JPEG 2000, WebP.

    .. note::
      JPEG 2000 region-of-interest (ROI) decoding is not accelerated on the GPU, and will use
      a CPU implementation regardless of the selected backend. For a GPU accelerated implementation,
      consider using separate ``decoders.image`` and ``slice`` operators.

    .. note::
      EXIF orientation metadata is disregarded.

    Supported backends
     * 'cpu'
     * 'mixed'


    Args
    ----
    `__data` : TensorList
        Batch that contains the input data.
    `__anchor` : 1D TensorList of float or int, optional
        Input that contains normalized or absolute coordinates for the starting
        point of the slice (x0, x1, x2, …).

        Integer coordinates are interpreted as absolute coordinates, while float coordinates can be
        interpreted as absolute or relative coordinates, depending on the value of
        ``normalized_anchor``.
    `__shape` : 1D TensorList of float or int, optional
        Input that contains normalized or absolute coordinates for the dimensions
        of the slice (s0, s1, s2, …).

        Integer coordinates are interpreted as absolute coordinates, while float coordinates can be
        interpreted as absolute or relative coordinates, depending on the value of
        ``normalized_shape``.


    Keyword args
    ------------
    `affine` : bool, optional, default = `True`
        Applies **only** to the ``mixed`` backend type.

        If set to True, each thread in the internal thread pool will be tied to a specific CPU core.
        Otherwise, the threads can be reassigned to any CPU core by the operating system.
    `axes` : int or list of int or TensorList of int, optional, default = `[1, 0]`
        Order of dimensions used for the anchor and shape slice inputs as dimension
        indices.

        Negative values are interpreted as counting dimensions from the back.
        Valid range: ``[-ndim, ndim-1]``, where ndim is the number of dimensions in the input data.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional, default = `'WH'`
        Order of the dimensions used for the anchor and shape slice inputs,
        as described in layout.

        If a value is provided, ``axis_names`` will have a higher priority than ``axes``.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `device_memory_padding` : int, optional, default = `16777216`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates one device buffer of the
        requested size per thread. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `device_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's device memory allocations, in bytes. This parameter helps to avoid
        reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs to be
        reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional allocations
        will occur during the pipeline execution. One way to find the ideal value is to do a complete
        run over the dataset with the ``memory_stats`` argument set to True and then copy the largest
        allocation value that was printed in the statistics.
    `end` : int or list of int or TensorList of int, optional
        End coordinates of the slice.

        Note: Providing named arguments ``start``, ``end``, ``shape``, ``rel_start``, ``rel_end``, ``rel_shape``
        is incompatible with providing positional inputs anchor and shape.
    `host_memory_padding` : int, optional, default = `8388608`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates two (because of double-buffering)
        host-pinned buffers of the requested size per thread. If selected correctly, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `host_memory_padding_jpeg2k` : int, optional, default = `0`
        Applies **only** to the ``mixed`` backend type.

        The padding for nvJPEG2k's host memory allocations, in bytes. This parameter helps to prevent
        the reallocation in nvJPEG2k when a larger image is encountered, and the internal buffer needs
        to be reallocated to decode the image.

        If a value greater than 0 is provided, the operator preallocates the necessary number of buffers
        according to the hint provided. If the value is correctly selected, no additional
        allocations will occur during the pipeline execution. One way to find the ideal value is to
        do a complete run over the dataset with the ``memory_stats`` argument set to True, and then copy
        the largest allocation value that is printed in the statistics.
    `hw_decoder_load` : float, optional, default = `0.65`
        The percentage of the image data to be processed by the HW JPEG decoder.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        Determines the percentage of the workload that will be offloaded to the hardware decoder,
        if available. The optimal workload depends on the number of threads that are provided to
        the DALI pipeline and should be found empirically. More details can be found at
        https://developer.nvidia.com/blog/loading-data-fast-with-dali-and-new-jpeg-decoder-in-a100
    `hybrid_huffman_threshold` : int, optional, default = `1000000`
        Applies **only** to the ``mixed`` backend type.

        Images with a total number of pixels (``height * width``) that is higher than this threshold will
        use the nvJPEG hybrid Huffman decoder. Images that have fewer pixels will use the nvJPEG host-side
        Huffman decoder.

        .. note::
          Hybrid Huffman decoder still largely uses the CPU.
    `jpeg_fancy_upsampling` : bool, optional, default = `False`
        Make the ``mixed`` backend use the same chroma upsampling approach as the ``cpu`` one.

        The option corresponds to the `JPEG fancy upsampling` available in libjpegturbo or
        ImageMagick.
    `memory_stats` : bool, optional, default = `False`
        Applies **only** to the ``mixed`` backend type.

        Prints debug information about nvJPEG allocations. The information about the largest
        allocation might be useful to determine suitable values for ``device_memory_padding`` and
        ``host_memory_padding`` for a dataset.

        .. note::
          The statistics are global for the entire process, not per operator instance, and include
          the allocations made during construction if the padding hints are non-zero.
    `normalized_anchor` : bool, optional, default = `True`
        Determines whether the anchor positional input should be interpreted as normalized
        (range [0.0, 1.0]) or as absolute coordinates.

        .. note::
          This argument is only relevant when anchor data type is ``float``. For integer types,
          the coordinates are always absolute.
    `normalized_shape` : bool, optional, default = `True`
        Determines whether the shape positional input should be interpreted as normalized
        (range [0.0, 1.0]) or as absolute coordinates.

        .. note::
          This argument is only relevant when anchor data type is ``float``. For integer types,
          the coordinates are always absolute.
    `output_type` : :class:`nvidia.dali.types.DALIImageType`, optional, default = `DALIImageType.RGB`
        The color space of the output image.

        Note: When decoding to YCbCr, the image will be decoded to RGB and then converted to YCbCr,
        following the YCbCr definition from ITU-R BT.601.
    `preallocate_height_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preallocate_width_hint` : int, optional, default = `0`
        Image width hint.

        Applies **only** to the ``mixed`` backend type in NVIDIA Ampere GPU and newer architecture.

        The hint is used to preallocate memory for the HW JPEG decoder.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `rel_end` : float or list of float or TensorList of float, optional
        End relative coordinates of the slice (range [0.0 - 1.0].

        Note: Providing named arguments ``start``, ``end``, ``shape``, ``rel_start``, ``rel_end``, ``rel_shape``
        is incompatible with providing positional inputs anchor and shape.
    `rel_shape` : float or list of float or TensorList of float, optional
        Relative shape of the slice (range [0.0 - 1.0]).

        Providing named arguments ``start``, ``end``, ``shape``, ``rel_start``, ``rel_end``, ``rel_shape``
        is incompatible with providing positional inputs anchor and shape.
    `rel_start` : float or list of float or TensorList of float, optional
        Start relative coordinates of the slice (range [0.0 - 1.0]).

        Note: Providing named arguments ``start``, ``end``, ``shape``, ``rel_start``, ``rel_end``, ``rel_shape``
        is incompatible with providing positional inputs anchor and shape.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shape` : int or list of int or TensorList of int, optional
        Shape of the slice.

        Providing named arguments ``start``, ``end``, ``shape``, ``rel_start``, ``rel_end``, ``rel_shape``
        is incompatible with providing positional inputs anchor and shape.
    `split_stages` : bool
        .. warning::

            The argument ``split_stages`` is no longer used and will be removed in a future release.
    `start` : int or list of int or TensorList of int, optional
        Start coordinates of the slice.

        Note: Providing named arguments ``start``/``end`` or ``start``/``shape`` is incompatible with
        providing positional inputs anchor and shape.
    `use_chunk_allocator` : bool
        .. warning::

            The argument ``use_chunk_allocator`` is no longer used and will be removed in a future release.
    `use_fast_idct` : bool, optional, default = `False`
        Enables fast IDCT in the libjpeg-turbo based CPU decoder, used when ``device`` is set
        to "cpu" or when the it is set to "mixed" but the particular image can not be handled by
        the GPU implementation.

        According to the libjpeg-turbo documentation, decompression performance is improved by up to 14%
        with little reduction in quality.

    """
    ...
