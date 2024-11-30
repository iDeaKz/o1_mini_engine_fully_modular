from redis import StrictRedis
from config import settings

class CacheManager:
    def __init__(self):
        self.client = StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

    def set_data(self, key: str, value: str, expire: int = 3600):
        self.client.setex(key, expire, value)

    def get_data(self, key: str):
        return self.client.get(key)

cache_manager = CacheManager()
