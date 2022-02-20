import asyncio
import csv
from faker import Faker  # библиотека нужна для генерации рандомных значений

fake = Faker()


async def request_users_data(uid: int) -> dict:
    await asyncio.sleep(0.5)
    return {"id": uid, "name": fake.name(),
            "email": fake.email()}  # c помощью faker генерируем осмысленные значения


ids = [i for i in range(1, 11)]
loop = asyncio.get_event_loop()  # получаем loop, тк ранее он не существовал - создаем новый
with open("../out.csv", "w") as fh:  # открываем фаил для записи
    fieldnames = ["id", "name", "email"]  # названия колонок в csv файле
    writer = csv.DictWriter(fh, fieldnames=fieldnames)
    # объект для записи данных в csv формате
    writer.writeheader()  # записываем название колонок
    for uid in ids:
        writer.writerow(loop.run_until_complete(request_users_data(uid)))
        # запускаем короутину в loop и дожидаемся ее результата
