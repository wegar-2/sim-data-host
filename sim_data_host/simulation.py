import asyncio
from datetime import datetime
import math

import numpy as np

from sim_data_host.data_update import DataUpdate
from sim_data_host.constants import SECONDS_PER_DAY

DataQueue: asyncio.Queue = asyncio.Queue()


async def simulate_gbm(
    start_value: float = 100,
    mu_daily: float = 0.005,
    sigma_daily: float = 0.02,
    value_seed: int = 654_321,
    lambda_arrival_time: float = 5,
    arrival_time_seed: int = 123_456
):
    value: float = start_value

    value_rng = np.random.default_rng(value_seed)
    arrival_time_rng = np.random.default_rng(seed=arrival_time_seed)

    while True:

        d_time = float(
            arrival_time_rng.exponential(scale=arrival_time_seed, size=1)[0])
        await asyncio.sleep(d_time)

        value = (
            value +
            mu_daily * (d_time / SECONDS_PER_DAY) +
            sigma_daily *
            math.sqrt(d_time / SECONDS_PER_DAY) *
            float(value_rng.normal(size=1)[0])
        )

        await DataQueue.put(DataUpdate(
            value=value,
            timestamp=datetime.now()
        ))
