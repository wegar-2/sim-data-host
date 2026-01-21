import asyncio
from datetime import datetime
import logging
import math

import numpy as np

from sim_data_host.data_update import DataUpdate
from sim_data_host.constants import SECONDS_PER_DAY
from sim_data_host.config import GbmSimulationConfig

DataQueue: asyncio.Queue = asyncio.Queue()


async def gbm_simulation(config: GbmSimulationConfig):
    value: float = config.start_value

    value_rng = np.random.default_rng(config.value_seed)
    arrival_time_rng = np.random.default_rng(seed=config.arrival_time_seed)

    while True:

        d_time = float(
            arrival_time_rng.exponential(scale=config.lambda_arrival_time, size=1)[0])
        await asyncio.sleep(d_time)

        value = (
            value +
            config.mu_daily * (d_time / SECONDS_PER_DAY) +
            config.sigma_daily *
            math.sqrt(d_time / SECONDS_PER_DAY) *
            float(value_rng.normal(size=1)[0])
        )

        await DataQueue.put(DataUpdate(
            value=value,
            timestamp=datetime.now()
        ))
