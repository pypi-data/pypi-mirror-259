from typing import Dict, List


class Neo4jSummarizerCache:
    def __init__(self, size: int = 2**20) -> None:
        self.papers: Dict[str, Dict] = dict()
        self.keys: List[str] = []
        self.size = size

    def try_get_paper(self, key: str, data: Dict):
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
