import cache_utils as cu
import dataclasses

@dataclasses.dataclass
class CacheTestCase:
    cache_type: cu.Cache
    items: list
    eviction_result: str

CACHE_TYPES_TEST_CASES = [
    CacheTestCase(cu.LRUCache, ["1", "2", "3"], "3"),
    CacheTestCase(cu.MRUCache, ["1", "2", "3"], -1),
    CacheTestCase(cu.FIFOCache, ["1", "2", "3"], "3"),
    CacheTestCase(cu.LIFOCache, ["1", "2", "3"], -1),
    CacheTestCase(cu.LFUCache, ["1", "2", "3"], "3"),
    # CacheTestCase(cu.RRCache, ["1", "2", "3"], -1),
    CacheTestCase(cu.TimeBasedCache, ["1", "2", "3"], "3"),
    # CacheTestCase(cu.ARCCache, ["1", "2", "3"], "3"),
    CacheTestCase(cu.SizeBasedCache, ["1", "2", "3"], "3"),
]


# Run tests for all cache eviction strategies
def test_cache_strategies():
    for test_case in CACHE_TYPES_TEST_CASES:
        print(f"Setup {test_case.cache_type.__name__}")
        cache = test_case.cache_type(3)
        # Add items
        for i, item in enumerate(test_case.items, start=1):
            cache.put(i, item)
        
        # Test access
        assert cache.get(1) == test_case.items[0]  # Accessing an existing key
        assert cache.get(2) == test_case.items[1]

        # Add another item and test eviction
        cache.put(4, "d")

        assert (
            cache.get(3) == test_case.eviction_result
        )
        print(f"Test passed for {test_case.cache_type.__name__}")
