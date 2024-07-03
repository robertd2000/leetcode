class TimeLimitedCache {
  cache = new Map();

  constructor() {
    this.cache = new Map();
  }

  set(key: number, value: number, duration: number): boolean {
    const hasKey = this.cache.has(key);

    if (hasKey) clearTimeout(this.cache.get(key).timer);

    this.cache.set(key, {
      value,
      timer: setTimeout(() => this.cache.delete(key), duration),
    });

    return hasKey;
  }

  get(key: number): number {
    if (this.cache.has(key)) {
      return this.cache.get(key)?.value;
    }

    return -1;
  }

  count(): number {
    return this.cache.size;
  }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
