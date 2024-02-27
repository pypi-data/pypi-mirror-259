import logging
import pickle
from typing import Dict, List
import redis.asyncio as redis

logger = logging.getLogger("cache")


class Neo4jSummarizerCache:
    def __init__(self, size: int = 2**20) -> None:
        self.papers: Dict[str, Dict] = dict()
        self.keys: List[str] = []
        self.size = size

    async def try_get_paper(self, key: str, data: Dict):
        if key not in self.papers:
            self.papers[key] = data
            self.keys.append(key)
            if len(self.keys) > self.size:
                key = self.keys.pop(0)
                del self.papers[key]
            return False
        same = True
        old_data = self.papers[key]
        for k in data:
            if k not in old_data or old_data[k] != data[k]:
                old_data[k] = data[k]
                same = False
        self.papers[key] = old_data
        return same


class Neo4jSummarizerRedisCache(Neo4jSummarizerCache):
    def __init__(self, client: redis.Redis) -> None:
        super().__init__()
        self.client = client

    async def try_get_paper(self, key: str, data: Dict):
        old_data_bin = await self.client.hget('papers', key)
        if old_data_bin is None:
            try:
                data_bin = pickle.dumps(data)
                await self.client.hset('papers', key, data_bin)
            except Exception as e:
                logger.error(f"Cannot set cache: {e}, {data}")
            return False
        try:
            old_data = pickle.loads(old_data_bin)
        except Exception as e:
            logger.error(f"Cannot get cache: {e}, {old_data_bin}")
            return False
        same = True
        for k in data:
            if k not in old_data or old_data[k] != data[k]:
                old_data[k] = data[k]
                same = False
        if not same:
            try:
                data_bin = pickle.dumps(old_data)
                await self.client.hset('papers', key, data_bin)
            except Exception as e:
                logger.error(f"Cannot update cache: {e}, {old_data}")
        return same
