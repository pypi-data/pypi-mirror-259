import os

import numpy
import torch

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
torch.ops.load_library(f"{SCRIPT_DIR}/lib/libnm_ops.so")

QUANT_SUPPORTED_NUM_BITS = [4, 8]
QUANT_SUPPORTED_GROUP_SIZES = [32, 64, 128]


def quantize_symmetric(w: torch.Tensor, num_bits: int, groupsize: int):
    assert w.is_floating_point()
    assert num_bits == 4 or num_bits == 8
    assert groupsize == -1 or groupsize == 128 or groupsize == 64 or groupsize == 32

    # Number of quantized elements in a single 32 bit integer
    pack_factor = 32 // num_bits

    max_q_val = 2**num_bits - 1
    half_q_val = (max_q_val + 1) // 2

    k, n = w.shape

    # For K smaller than groupsize, simply use K as the groupsize
    if groupsize != -1 and k < groupsize:
        groupsize = -1

    # Reshape to [groupsize, -1]
    if groupsize != -1:
        w = w.reshape((-1, groupsize, n))
        w = w.permute(1, 0, 2)
        w = w.reshape((groupsize, -1))

    # Compute scale for each group
    s = torch.max(torch.abs(w), 0, keepdim=True)[0]
    s *= 2 / max_q_val  # 2 => symmetric

    # Quantize
    q_w = torch.round(w / s).int()
    q_w += half_q_val
    q_w = torch.clamp(q_w, 0, max_q_val)

    # Compute ref (dequantized)
    w_ref = (q_w - half_q_val).half() * s

    # Restore original shapes
    s = s.reshape((-1, n)).contiguous()
    if groupsize != -1:

        def reshape(w):
            w = w.reshape((groupsize, -1, n))
            w = w.permute(1, 0, 2)
            w = w.reshape((k, n)).contiguous()
            return w

        w_ref = reshape(w_ref)
        q_w = reshape(q_w)

    assert (
        q_w.shape[1] % pack_factor == 0
    ), f"q_w.shape = {q_w.shape} has shape[1] = {q_w.shape[1]} and it must be divisible by pack_factor = {pack_factor}"

    q_res = numpy.zeros((q_w.shape[0], q_w.shape[1] // pack_factor), dtype=numpy.uint32)
    q_w = q_w.cpu().numpy().astype(numpy.uint32)

    # Pack the elements
    for i in range(pack_factor):
        q_res |= q_w[:, i::pack_factor] << (i * num_bits)

    q_res = torch.from_numpy(q_res.astype(numpy.int32)).to(w.device)
    s = s.to(w.device)

    return w_ref, q_res, s


def dequant_b_q_weight(
    b_q_weight: torch.Tensor,
    b_scales: torch.Tensor,
    num_bits: int,
    group_size: int,
    a_ref: torch.Tensor,
    size_m: int,
    size_n: int,
    size_k: int,
):
    return torch.ops.nm_ops.dequant_b_q_weight(
        b_q_weight, b_scales, num_bits, group_size, a_ref, size_m, size_n, size_k
    )


def quant_gemm(
    a: torch.Tensor,
    b_q_weight: torch.Tensor,
    b_scales: torch.Tensor,
    num_bits: int,
    group_size: int,
    size_m: int,
    size_n: int,
    size_k: int,
):
    return torch.ops.nm_ops.quant_gemm(
        a, b_q_weight, b_scales, num_bits, group_size, size_m, size_n, size_k
    )


def cublas_gemm(a: torch.Tensor, b_weight: torch.Tensor):
    return torch.ops.nm_ops.cublas_gemm(a, b_weight)
