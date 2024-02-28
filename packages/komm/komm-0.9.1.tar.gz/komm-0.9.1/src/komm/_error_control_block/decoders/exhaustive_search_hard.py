import numpy as np
import numpy.typing as npt

from .._registry import RegistryBlockDecoder
from ..BlockCode import BlockCode


def decode_exhaustive_search_hard(code: BlockCode, r: npt.ArrayLike) -> np.ndarray:
    codewords = code.codewords
    metrics = np.count_nonzero(r != codewords, axis=1)
    v_hat = codewords[np.argmin(metrics)]
    return v_hat


RegistryBlockDecoder.register(
    "exhaustive_search_hard",
    {
        "description": "Exhaustive search (hard-decision). Minimum Hamming distance decoder",
        "decoder": decode_exhaustive_search_hard,
        "type_in": "hard",
        "type_out": "hard",
        "target": "codeword",
    },
)
