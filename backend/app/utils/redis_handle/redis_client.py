import os
import redis

class RedisClient:

    @staticmethod
    def client():
        return redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=int(os.getenv("REDIS_PORT", 6380)),
            password=os.getenv("REDIS_PASSWORD"),
            ssl=True,
            decode_responses=True
        )
