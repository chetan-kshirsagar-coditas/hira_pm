import os
import redis

class RedisClient:

    @staticmethod
    def client():
        return redis.from_url(
            os.getenv("REDIS_URL"),
            decode_responses=True
        )
