import math
import hashlib

class BloomFilter:
    def __init__(self, expected_elements: int, false_positive_rate: float) -> None: # Добавлено -> None
        self.n: int = expected_elements
        self.p: float = false_positive_rate
        self.m: int = 1000  
        self.k: int = 3     
        self.bit_array: bytearray = bytearray(math.ceil(self.m / 8))
        print(f"Инициализирован фильтр Блума: m={self.m}, k={self.k}")
        
    def _get_hashes(self, item: str) -> list[int]: # Добавлено -> list[int]
        indices: list[int] = []
        for i in range(self.k):
            raw_hash = hashlib.md5(f"{item}_{i}".encode('utf-8')).hexdigest()
            indices.append(int(raw_hash, 16) % self.m)
        return indices

    def add(self, item: str) -> None: # Добавлено -> None
        pass

    def contains(self, item: str) -> bool: # Добавлено -> bool
        return True
