from Clients.Horoscope.ClientInterface import ClientInterface
from Services.Horoscope.HoroscopeInterface import HoroscopeInterface


class HoroscopeService(HoroscopeInterface):
    # Карта знаков зодиака и их API-эквиваленты
    zodiac_api_mapping = {
        "♈ Овен": "aries",
        "♉ Телец": "taurus",
        "♊ Близнецы": "gemini",
        "♋ Рак": "cancer",
        "♌ Лев": "leo",
        "♍ Дева": "virgo",
        "♎ Весы": "libra",
        "♏ Скорпион": "scorpio",
        "♐ Стрелец": "sagittarius",
        "♑ Козерог": "capricorn",
        "♒ Водолей": "aquarius",
        "♓ Рыбы": "pisces"
    }

    def __init__(self, client: ClientInterface):
        # Инициализация клиента
        self.client = client

    async def get_horoscope(self, zodiac: str) -> str:
        # Запрос гороскопа для знака зодиака
        response = await self.client.post(
            endpoint="/get-horoscope/daily",
            params={
                # Получаем API-имя знака
                "sign": self.zodiac_api_mapping[zodiac],
                # Текущий день
                "day": "today"
            }
        )
        return response
