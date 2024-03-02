# failure-detector

A Pythonic implementation of the [Phi-Accrual Failure Detector][paper]. 

Phi-Accrual Failure Detectors detect system outages by statistically modeling inter-arrival times of heartbeat (ping) messages over time.
The system is declared as unavailable once heartbeats are significantly delayed compared to those recently observed.

## Usage

Install with `pip`:
```bash
$ pip install failure-detector
```

Detecting network outages works roughly as follows:

```python3
from failure_detector import PhiAccrualFailureDetector

detector = PhiAccrualFailureDetector(
    # suspicion threshold for which the detector declares the system unavailable
    threshold=7.0,
    # initial estimate of the mean heartbeat inter-arrival time (20ms)
    mean_estimate=20.0,
    # A lower bound for on the standard-deviation of heartbeat inter-arrival 
    # times. The computation of the phi-value uses #max(min_stddev, sample 
    # stddev); this prevents the estimated distribution from collapsing when 
    # e.g., all sampled heartbeats are the same
    mean_stddev=3.0,
    # size of the sample buffer of previous heartbeat inter-arrival times
    num_samples=30
)

while True:

    # perform heartbeat every second
    time.sleep(1)
    heartbeat_ms = ... # ping some endpoint

    if not detector.evaluate(heartbeat_ms):
        # report system as unavailable

    else:
        # add to sample buffer 
        detector.observe(heartbeat_ms)
```

<!-- References -->
[paper]: https://www.researchgate.net/publication/29682135_The_ph_accrual_failure_detector