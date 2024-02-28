import numpy as np
from attrs import field, frozen
from numpy import typing as npt

from ._registry import RegistryBlockDecoder
from .BlockCode import BlockCode


@frozen
class BlockDecoder:
    r"""
    Decoder for [linear block codes](/ref/BlockCode).

    Attributes:

        code: The [block code](/ref/BlockCode) to be considered.
        method: The identifier of the method to be used for decoding. The default corresponds to `code.default_decoder`.
        decoder_kwargs: Additional keyword arguments to be passed to the decoder.

    Note:

        To see the default decoding method for a given code, use `code.default_decoder`; to see the available decoding methods for a given code, use `code.supported_decoders`.

    ??? info "Available decoding methods"

        **`bcjr`**: Bahl–Cocke–Jelinek–Raviv (BCJR)

        - Input type: soft
        - Output type: soft
        - Target: message
        - Supported by: [`TerminatedConvolutionalCode`](/ref/TerminatedConvolutionalCode).

        **`berlekamp`**: Berlekamp decoder

        - Input type: hard
        - Output type: hard
        - Target: codeword
        - Supported by: [`BCHCode`](/ref/BCHCode).

        **`exhaustive_search_hard`**: Exhaustive search (hard-decision). Minimum Hamming distance decoder

        - Input type: hard
        - Output type: hard
        - Target: codeword
        - Supported by: All codes.

        **`exhaustive_search_soft`**: Exhaustive search (soft-decision). Minimum Euclidean distance decoder

        - Input type: soft
        - Output type: hard
        - Target: codeword
        - Supported by: All codes.

        **`majority_logic_repetition_code`**: Majority-logic decoder. A hard-decision decoder for Repetition codes only.

        - Input type: hard
        - Output type: hard
        - Target: message
        - Supported by: [`RepetitionCode`](/ref/RepetitionCode).

        **`meggitt`**: Meggitt decoder

        - Input type: hard
        - Output type: hard
        - Target: codeword
        - Supported by: [`BCHCode`](/ref/BCHCode), [`CyclicCode`](/ref/CyclicCode).

        **`reed`**: Reed decoding algorithm for Reed–Muller codes. It's a majority-logic decoding algorithm.

        - Input type: hard
        - Output type: hard
        - Target: message
        - Supported by: [`ReedMullerCode`](/ref/ReedMullerCode).

        **`syndrome_table`**: Syndrome table decoder

        - Input type: hard
        - Output type: hard
        - Target: codeword
        - Supported by: All codes.

        **`viterbi_hard`**: Viterbi (hard-decision)

        - Input type: hard
        - Output type: hard
        - Target: message
        - Supported by: [`TerminatedConvolutionalCode`](/ref/TerminatedConvolutionalCode).

        **`viterbi_soft`**: Viterbi (soft-decision)

        - Input type: soft
        - Output type: hard
        - Target: message
        - Supported by: [`TerminatedConvolutionalCode`](/ref/TerminatedConvolutionalCode).

        **`wagner`**: Wagner decoder. A soft-decision decoder for SingleParityCheck codes only.

        - Input type: soft
        - Output type: hard
        - Target: codeword
        - Supported by: [`SingleParityCheckCode`](/ref/SingleParityCheckCode).

        **`weighted_reed`**: Weighted Reed decoding algorithm for Reed–Muller codes.

        - Input type: soft
        - Output type: hard
        - Target: message
        - Supported by: [`ReedMullerCode`](/ref/ReedMullerCode).

    Parameters: Input

        in0 (Array1D[int] | Array1D[float]): The (hard or soft) bit sequence to be decoded. Its length must be a multiple of the code's block length $n$.

    Parameters: Output:

        out0 (Array1D[int]): The decoded bit sequence. Its length is a multiple of the code's dimension $k$.

    Examples:

        >>> code = komm.HammingCode(3)
        >>> code.default_decoder
        'syndrome_table'
        >>> code.supported_decoders
        ['exhaustive_search_hard', 'exhaustive_search_soft', 'syndrome_table']

        >>> decoder = komm.BlockDecoder(code)
        >>> decoder([1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0])
        array([1, 1, 0, 0, 1, 0, 1, 1])

        >>> decoder = komm.BlockDecoder(code, method='exhaustive_search_soft')
        >>> decoder([-0.98, -0.85, 1.07, -0.78, 1.11, -0.95, -1.16, -0.87, 1.11, -0.83, -0.95, 0.94, 1.07, 0.91])
        array([1, 1, 0, 0, 1, 0, 1, 1])
    """
    code: BlockCode
    method: str | None = None
    decoder_kwargs: dict = field(factory=dict)

    def __attrs_post_init__(self) -> None:
        method = self.method or self.code.default_decoder
        help_message = f"To see the available decoding methods for a given code, use `code.supported_decoders`"
        if not RegistryBlockDecoder.is_registered(method):
            raise ValueError(f"Method '{method}' is unknown. {help_message}")
        if method not in self.code.supported_decoders:
            raise ValueError(
                f"Method '{method}' is not supported by the code. {help_message}"
            )

    def __call__(self, in0: npt.ArrayLike) -> np.ndarray:
        method = self.method or self.code.default_decoder
        decoder_data = RegistryBlockDecoder.get(method)
        if decoder_data["type_in"] == "hard" and not np.issubdtype(
            np.asarray(in0).dtype, np.integer
        ):
            raise TypeError(f"Input type must be 'int' for method '{method}'")
        if decoder_data["type_in"] == "soft" and not np.issubdtype(
            np.asarray(in0).dtype, np.floating
        ):
            raise TypeError(f"Input type must be 'float' for method '{method}'")
        r = np.reshape(in0, (-1, self.code.length))
        decoder = lambda r: decoder_data["decoder"](self.code, r, **self.decoder_kwargs)
        decoded = np.apply_along_axis(decoder, 1, r)
        if decoder_data["target"] == "codeword":
            u_hat = np.apply_along_axis(self.code.inv_enc_mapping, 1, decoded)
        else:
            u_hat = decoded
        out0 = np.reshape(u_hat, (-1,))
        return out0
