from collections import deque
import math


class PhiAccrualFailureDetector:
    """A statistical detector for detecting failures in distributed systems.

    Phi-Accrual Failure Detectors detect system outages by statistically
    modeling inter-arrival times of heartbeat (ping) messages over time.
    The system is declared as unavailable once heartbeats are significantly
    delayed compared to those recently observed.
    See `Hayashibara et al. 2014`_ for more details.

    This implementation is loosely based on that in the Akka project.

    Example:
        Using this detector to classify network outages roughly works as
        follows::

            d = PhiAccrualFailureDetector(...)

            while True:

                # periodically perform heartbeat
                time.sleep(1)
                heartbeat_ms = ping(...)

                if not d.evaluate(heartbeat_ms):
                    # report system as unavailable

                # it can be a good idea to not `observe` heartbeats during
                # outages, to not degrade the sample buffer, hence the `else`
                else:
                    d.observe(heartbeat_ms)

    Args:
        threshold (float): The suspicion threshold for which the detector
            declares the system as unavailable
        mean_estimate (float): An initial estimate of the mean heartbeat
            inter-arrival time
        min_stddev (float): An initial estimate of the standard deviation of
            heartbeat inter-arrival times
        num_samples (int): The size of the sample buffer of previous heartbeat
            inter-arrival times

    .. _Hayashibara et al. 2014:
       https://www.researchgate.net/publication/29682135_The_ph_accrual_failure_detector
    """

    def __init__(
        self,
        threshold: float,
        mean_estimate: float,
        min_stddev: float,
        num_samples: int = 30,
    ):
        if threshold <= 0.0:
            raise ValueError("threshold must be nonnegative")

        if mean_estimate <= 0.0:
            raise ValueError("mean_heartbeat_estimate must be positive")

        if min_stddev <= 0.0:
            raise ValueError("min_heartbeat_stddev must be positive")

        if num_samples <= 0:
            raise ValueError("num_samples must be positive")

        self._threshold = threshold
        self._min_stddev = min_stddev

        # Initialize sample buffer with estimates
        stddev_estimate = mean_estimate / 2.0
        samples = [
            mean_estimate - stddev_estimate,
            mean_estimate + stddev_estimate,
        ]
        self._samples = deque(samples, num_samples)

        # Cached sample mean and stddev
        self._mean: float = mean_estimate
        self._stddev: float = stddev_estimate

    @property
    def samples(self) -> list[float]:
        return list(self._samples)

    @property
    def mean(self) -> float:
        return self._mean

    @property
    def stddev(self) -> float:
        return self._stddev

    def observe(self, heartbeat: float):
        """Adds a new heartbeat to the sample buffer."""

        self._samples.append(heartbeat)
        mean = sum(self._samples) / len(self._samples)

        # Compute stddev using the variance identity: Var(X) = E[X^2] - E[X]^2
        second_moment = sum(x * x for x in self._samples) / len(self._samples)
        variance = second_moment - (mean * mean)
        stddev = math.sqrt(variance)

        self._mean = mean
        self._stddev = stddev

    def suspicion(self, heartbeat: float) -> float:
        """Computes the suspicion level for the given heartbeat."""
        stddev = max(self.stddev, self._min_stddev)
        return self._phi(heartbeat, self.mean, stddev)

    @staticmethod
    def _phi(heartbeat: float, mean: float, stddev: float):
        """Computes the Phi value for a given heartbeat, mean and stddev.

        This function computes the Phi value::

            phi(x) = -log_10(1.0 - F_{mean, stddev}(x))

        for the given heartbeat, where `F_{mean, stddev}` is the CDF of a Normal
        distribution with respective mean and stddev.
        """
        # This implementation uses the logistic approximation to the CDF of a
        # standardized normal distribution:
        #   F \approx 1.0 / (1.0 + math.exp(-z * (1.5976 + 0.070566 * z * z)))
        # where z is the z_score of the given heartbeat.

        # Note that a naive implementation of this approximation to compute
        # phi(x) is numerically unstable, as
        #   phi = -log10(1.0 - F) = -log10(1.0 - 1.0 /(1.0 + v)) -> \infty
        # for small values of v.
        # This implementation uses the numerically robust iplementation from
        # Akka, see https://github.com/akka/akka/issues/1821

        z = (heartbeat - mean) / stddev
        v = math.exp(-z * (1.5976 + 0.070566 * z * z))

        if heartbeat > mean:
            return -math.log10(v / (1.0 + v))
        else:
            return -math.log10(1.0 - 1.0 / (1.0 + v))

    def evaluate(self, heartbeat: float) -> bool:
        """Decides whether the system is available, given the heartbeat."""
        return self.suspicion(heartbeat) < self._threshold
