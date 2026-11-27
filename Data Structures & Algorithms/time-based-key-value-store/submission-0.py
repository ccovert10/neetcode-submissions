class TimeMap:

    def __init__(self):
        # Maps key -> list of [timestamp, value] pairs
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        # Binary search for the largest timestamp <= target timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]  # Valid candidate; record it
                l = mid + 1           # Try to find a closer (larger) timestamp on the right
            else:
                r = mid - 1           # Timestamp is too large; search the left half

        return res