import os
from typing import Any

from aiogram.client.session import aiohttp
from dotenv import load_dotenv, find_dotenv

from Clients.Horoscope.ClientInterface import ClientInterface

# TEMP: Загружаем переменные окружения
load_dotenv(find_dotenv())


class Client(ClientInterface):
    def __init__(self):
        # Получаем URL API из переменных окружения
        self.url = os.getenv("HOROSCOPE_API_URL")

    async def post(self, endpoint: str, params: dict) -> Any | None:
        # Формируем полный URL для запроса
        api_url = self.url + endpoint
        try:
            # Создаем сессию aiohttp
            async with aiohttp.ClientSession() as session:
                # Выполняем GET-запрос с параметрами
                async with session.get(api_url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        # Возвращаем данные или сообщение о отсутствии данных
                        return data.get("data", {}).get(
                            "horoscope_data", "Нет данных 😢"
                        )
                    else:
                        return None
        except Exception:
            return None
