import logging

from sim_data_host.simulation import DataQueue
from sim_data_host.data_update import DataUpdate

logger = logging.getLogger(__name__)

clients: set = set()


async def broadcaster():

    while True:

        du: DataUpdate = await DataQueue.get()
        message: str = str(du)

        to_remove: list = []

        for writer in clients:
            try:
                writer.write(message)
                await writer.drain()
            except Exception:
                to_remove.append(writer)

        for wtr in to_remove:
            clients.remove(wtr)
            try:
                wtr.close()
                await wtr.wait_closed()
            except:
                pass
