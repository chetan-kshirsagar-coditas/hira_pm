import redis


class RedisClient:

    @staticmethod
    def client():
        return redis.Redis(host='localhost', port=6379, db=0)
    
    