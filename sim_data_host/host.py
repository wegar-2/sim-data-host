import asyncio
import logging

from sim_data_host.config import GbmSimulationConfig
from sim_data_host.simulation import gbm_simulation
from sim_data_host.broadcaster import broadcaster
from sim_data_host.client_handler import client_handler

logger = logging.getLogger(__name__)


async def host(
        gbm_sim_config: GbmSimulationConfig,
        port: int = 9000
):
    logger.info(f"")

    asyncio.create_task(gbm_simulation(config=gbm_sim_config))
    asyncio.create_task(broadcaster())

    server = await asyncio.start_server(client_handler, host="0.0.0.0", port=port)

    async with server:
        await server.serve_forever()
