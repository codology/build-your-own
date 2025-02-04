# Cache Eviction Strategies

This project implements various cache eviction strategies in Python. Cache eviction is used to determine which items to remove from the cache when it becomes full. The following strategies are included in this implementation:

## Eviction Strategies

### 1. **Least Recently Used (LRU)**
   - **Description:** The LRU strategy removes the **least recently used** item when the cache reaches its limit.
   - **Use case:** Ideal for scenarios where data accessed most recently is more likely to be accessed again soon.
   - **How it works:** Each time an item is accessed or added, it is moved to the end of an ordered list. The item at the front (oldest accessed) is evicted.

### 2. **Most Recently Used (MRU)**
   - **Description:** The MRU strategy evicts the **most recently used** item when the cache is full.
   - **Use case:** Useful when the most recently used data is less likely to be used again in the near future.
   - **How it works:** The most recently accessed item (added or read) is removed when eviction occurs.

### 3. **First In, First Out (FIFO)**
   - **Description:** The FIFO strategy evicts the **first inserted item** when the cache is full.
   - **Use case:** A simple strategy suitable for cases where the order of insertion matters, but no other access patterns are important.
   - **How it works:** The first added item is evicted when the cache reaches capacity.

### 4. **Last In, First Out (LIFO)**
   - **Description:** The LIFO strategy evicts the **last inserted item** from the cache.
   - **Use case:** Used in situations where the most recently added data is considered least likely to be reused.
   - **How it works:** The most recently inserted item is evicted when the cache reaches its limit.

### 5. **Least Frequently Used (LFU)**
   - **Description:** The LFU strategy removes the **least frequently accessed** item.
   - **Use case:** Useful for cases where frequently accessed items are more likely to be reused.
   - **How it works:** Each time an item is accessed, its frequency is incremented. The item with the lowest frequency is evicted when the cache is full.

### 6. **Random Replacement (RR)**
   - **Description:** The RR strategy randomly selects an item to evict from the cache when space is needed.
   - **Use case:** A simple and fast eviction strategy where eviction decision is random.
   - **How it works:** A random item from the cache is evicted when the cache is full.

### 7. **Time-based Expiration**
   - **Description:** Items are evicted based on their **age**, i.e., when they exceed a specified time-to-live (TTL).
   - **Use case:** Suitable for caches where the data is only valid for a specific period of time (e.g., session tokens, temporary data).
   - **How it works:** If an item has existed in the cache longer than the TTL, it is removed.

### 8. **Adaptive Replacement Cache (ARC)**
   - **Description:** ARC combines **LRU** and **LFU** strategies by maintaining two separate lists: one for recently used items and one for frequently used items.
   - **Use case:** Ideal for balancing both recent access and frequency of access, providing a more sophisticated eviction mechanism.
   - **How it works:** It dynamically adjusts between LRU and LFU strategies, depending on the system’s access pattern.

### 9. **Size-based Eviction**
   - **Description:** Items are evicted based on the **cache size**. Once the cache exceeds a specified size or item count, evictions happen.
   - **Use case:** Useful when the cache size is the primary constraint, regardless of access patterns.
   - **How it works:** The cache evicts items based on either their size or the total number of items once the cache reaches the maximum allowable capacity.

---

## How to Use

### Example Usage

```python
# Example: LRU Cache
cache = LRUCache(3)  # Create a cache with a capacity of 3

# Add items
cache.put(1, 'a')
cache.put(2, 'b')
cache.put(3, 'c')

# Access an item
print(cache.get(1))  # Output: 'a'

# Add another item, triggering eviction
cache.put(4, 'd')

# Check which item was evicted (LRU should be evicted)
print(cache.get(2))  # Output: -1 (Item 2 was evicted)
```

## Tests
```
pytest -vv .
```