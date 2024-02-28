from .FormattingPulse import FormattingPulse


class RectangularPulse(FormattingPulse):
    r"""
    Rectangular pulse. It is a formatting pulse with impulse response given by
    $$
        h(t) =
        \begin{cases}
            1, & 0 \leq t < w, \\\\
            0, & \text{otherwise}.
        \end{cases},
    $$
    where $w$ is the *width* of the pulse, which must satisfy $0 \leq w \leq 1$. The rectangular pulse is depicted below for $w = 1$ (called the NRZ pulse), and for $w = 0.5$ (called the halfway RZ pulse).

    <div class="centered" markdown>
      <span>
        ![Rectangular NRZ pulse.](/figures/pulse_rectangular_nrz.svg)
      </span>
      <span>
        ![Rectangular RZ pulse.](/figures/pulse_rectangular_rz.svg)
      </span>
    </div>
    """

    def __init__(self, width=1.0):
        r"""
        Constructor for the class.

        Parameters:

            width (Optional[float]): The width $w$ of the pulse. Must satisfy $0 \leq w \leq 1$. The default value is `1.0`.

        Examples:

            >>> pulse = komm.RectangularPulse(width=1.0)  # NRZ pulse

            >>> pulse = komm.RectangularPulse(width=0.5)  # Halfway RZ pulse
        """
        w = self._width = float(width)

        def impulse_response(t):
            return 1.0 * (0 <= t < w)

        super().__init__(impulse_response, interval=(0.0, 1.0))

    def __repr__(self):
        args = "width={}".format(self._width)
        return "{}({})".format(self.__class__.__name__, args)

    @property
    def width(self):
        r"""
        The width $w$ of the pulse.
        """
        return self._width
