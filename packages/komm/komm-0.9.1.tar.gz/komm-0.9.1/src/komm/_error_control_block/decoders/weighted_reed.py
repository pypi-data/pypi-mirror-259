import numpy as np
import numpy.typing as npt

from .._registry import RegistryBlockDecoder
from ..ReedMullerCode import ReedMullerCode


def decode_weighted_reed(code: ReedMullerCode, r: npt.ArrayLike) -> np.ndarray:
    # See [LC04, p. 440–442].
    r = np.asarray(r)
    u_hat = np.empty(code.dimension, dtype=int)
    bx = (r < 0).astype(int)
    for i, partition in enumerate(code.reed_partitions):
        checksums = np.count_nonzero(bx[partition], axis=1) % 2
        min_reliability = np.min(np.abs(r[partition]), axis=1)
        decision_var = np.dot(1 - 2 * checksums, min_reliability)
        u_hat[i] = decision_var < 0
        bx ^= u_hat[i] * code.generator_matrix[i]
    return u_hat


RegistryBlockDecoder.register(
    "weighted_reed",
    {
        "description": "Weighted Reed decoding algorithm for Reed–Muller codes.",
        "decoder": decode_weighted_reed,
        "type_in": "soft",
        "type_out": "hard",
        "target": "message",
    },
)
