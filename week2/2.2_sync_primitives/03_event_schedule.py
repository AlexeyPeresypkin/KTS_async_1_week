import asyncio
import datetime
from typing import Optional


class Scheduler:
    def __init__(self, timer: int):
        self.timer = timer
        self.is_running = True
        self._stop_event = asyncio.Event()
        self._scheduler_task: Optional[asyncio.Task] = None
        self._concurrent_workers = 0

    async def _worker(self):
        self._concurrent_workers += 1
        print('start', datetime.datetime.now())
        await asyncio.sleep(5)
        # какая-то полезная работа, которая занимает 5 секунд
        print('stop', datetime.datetime.now())
        self._concurrent_workers -= 1
        if not self.is_running and self._concurrent_workers == 0:
            # если планировщик остановлен и при этом это был последний запущенный worker, то нужно уведомить
            # корутину stop о том, что все _worker завершились
            self._stop_event.set()

    async def _scheduler(self):
        """
        планировщик запускается в фоне и просыпается раз в период времени timer
        """
        while self.is_running:
            asyncio.create_task(self._worker())
            await asyncio.sleep(self.timer)

    def start(self):
        self.is_running = True
        self._scheduler_task = asyncio.get_event_loop().create_task(
            self._scheduler())

    async def stop(self):
        """
        ставим is_running = False, чтобы планировщик не планировал новые запуски и отменяем его задачу
        ждем пока все _worker завершатся
        """
        self.is_running = False
        self._scheduler_task.cancel()
        await self._stop_event.wait()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    s = Scheduler(2)
    s.start()
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.run_until_complete(s.stop())
