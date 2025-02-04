import collections
import random
import time


class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = collections.OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.order.move_to_end(key)  # Update access order for LRU
        return self.cache[key]

    def put(self, key, value):
        if len(self.cache) >= self.capacity:
            self.evict()
        self.cache[key] = value
        self.order[key] = time.time()

    def evict(self):
        pass


# 1. Least Recently Used (LRU)
class LRUCache(Cache):
    def evict(self):
        oldest = min(self.order, key=self.order.get)  # Evict least recently used
        del self.cache[oldest]
        del self.order[oldest]


# 2. Most Recently Used (MRU)
class MRUCache(Cache):
    def evict(self):
        most_recent = max(self.order, key=self.order.get)  # Evict most recently used
        del self.cache[most_recent]
        del self.order[most_recent]


# 3. First In, First Out (FIFO)
class FIFOCache(Cache):
    def evict(self):
        oldest = next(iter(self.cache))  # Evict first added
        del self.cache[oldest]
        del self.order[oldest]


# 4. Last In, First Out (LIFO)
class LIFOCache(Cache):
    def evict(self):
        last_added = list(self.cache.keys())[-1]  # Evict most recently added
        del self.cache[last_added]
        del self.order[last_added]


# 5. Least Frequently Used (LFU)
class LFUCache(Cache):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.frequency = collections.defaultdict(int)

    def get(self, key):
        if key not in self.cache:
            return -1
        self.frequency[key] += 1  # Increment usage frequency
        return self.cache[key]

    def evict(self):
        least_frequent = min(
            self.frequency, key=self.frequency.get
        )  # Evict least frequently used
        del self.cache[least_frequent]
        del self.order[least_frequent]
        del self.frequency[least_frequent]


# 6. Random Replacement (RR)
class RRCache(Cache):
    def evict(self):
        random_key = random.choice(list(self.cache.keys()))  # Evict randomly
        del self.cache[random_key]
        del self.order[random_key]


# 7. Time-based Expiration
class TimeBasedCache(Cache):
    def __init__(self, capacity, ttl=5):
        super().__init__(capacity)
        self.ttl = ttl

    def get(self, key):
        if key not in self.cache or time.time() - self.order[key] > self.ttl:
            return -1  # Expired
        return self.cache[key]

    def put(self, key, value):
        if len(self.cache) >= self.capacity:
            self.evict()
        self.cache[key] = value
        self.order[key] = time.time()

    def evict(self):
        expired = [
            key
            for key, timestamp in self.order.items()
            if time.time() - timestamp > self.ttl
        ]
        if expired:
            expired_key = expired[0]
            del self.cache[expired_key]
            del self.order[expired_key]


# 8. Adaptive Replacement Cache (ARC)
class ARCCache(Cache):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.lru = collections.OrderedDict()
        self.lfu = collections.OrderedDict()

    def evict(self):
        # Evict based on combined logic of LRU and LFU
        if len(self.lru) > len(self.lfu):
            key_to_evict = next(iter(self.lru))
            del self.cache[key_to_evict]
            del self.lru[key_to_evict]
        else:
            key_to_evict = min(self.lfu, key=self.lfu.get)
            del self.cache[key_to_evict]
            del self.lfu[key_to_evict]


# 9. Size-based Eviction
class SizeBasedCache(Cache):
    def __init__(self, capacity, max_size=3):
        super().__init__(capacity)
        self.max_size = max_size

    def put(self, key, value):
        if len(self.cache) >= self.capacity or len(self.cache) >= self.max_size:
            self.evict()
        self.cache[key] = value
        self.order[key] = time.time()

    def evict(self):
        oldest = min(self.order, key=self.order.get)  # Evict least recently used
        del self.cache[oldest]
        del self.order[oldest]
