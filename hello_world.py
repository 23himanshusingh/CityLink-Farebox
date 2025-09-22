def is_prime(n: int) -> bool:
    """Return True if n is a prime (n >= 2)."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def print_primes_upto(limit: int) -> None:
    """Print all prime numbers <= limit, one per line."""
    if limit < 2:
        print("No primes")
        return
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num)

if __name__ == "__main__":
    # Example usage: prints primes up to 50
    print_primes_upto(50)    
    """
    Collection of common sorting algorithms with simple demos.
    
    Each function takes a sequence (list) and returns a new sorted list (original not mutated).
    For counting/radix sort input must be non-negative integers.
    
    Usage:
        from sorting_algorithms import bubble_sort, quick_sort
        sorted_list = quick_sort([3,1,2])
    """
    from typing import List
    import random
    import time
    import heapq
    import math
    
    
    def bubble_sort(a: List[int]) -> List[int]:
        arr = a.copy()
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
    
    
    def selection_sort(a: List[int]) -> List[int]:
        arr = a.copy()
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    
    
    def insertion_sort(a: List[int]) -> List[int]:
        arr = a.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    
    def merge_sort(a: List[int]) -> List[int]:
        arr = a.copy()
        if len(arr) <= 1:
            return arr
    
        def merge(left: List[int], right: List[int]) -> List[int]:
            i = j = 0
            out = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    out.append(left[i]); i += 1
                else:
                    out.append(right[j]); j += 1
            out.extend(left[i:]); out.extend(right[j:])
            return out
    
        mid = len(arr) // 2
        return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
    
    
    def quick_sort(a: List[int]) -> List[int]:
        arr = a.copy()
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
    
    def heap_sort(a: List[int]) -> List[int]:
        arr = a.copy()
        heapq.heapify(arr)
        return [heapq.heappop(arr) for _ in range(len(arr))]
    
    
    def counting_sort(a: List[int]) -> List[int]:
        if not a:
            return []
        if any(x < 0 for x in a):
            raise ValueError("counting_sort only supports non-negative integers")
        arr = a.copy()
        maxi = max(arr)
        counts = [0] * (maxi + 1)
        for x in arr:
            counts[x] += 1
        out = []
        for value, cnt in enumerate(counts):
            out.extend([value] * cnt)
        return out
    
    
    def radix_sort(a: List[int]) -> List[int]:
        """LSD radix sort for non-negative integers."""
        if not a:
            return []
        if any(x < 0 for x in a):
            raise ValueError("radix_sort only supports non-negative integers")
        arr = a.copy()
        max_val = max(arr)
        exp = 1
        base = 10
        while max_val // exp > 0:
            buckets = [[] for _ in range(base)]
            for num in arr:
                buckets[(num // exp) % base].append(num)
            arr = [num for bucket in buckets for num in bucket]
            exp *= base
        return arr
    
    
    # Utility to run a demo and basic timing
    ALGORITHMS = {
        "bubble": bubble_sort,
        "selection": selection_sort,
        "insertion": insertion_sort,
        "merge": merge_sort,
        "quick": quick_sort,
        "heap": heap_sort,
        "counting": counting_sort,
        "radix": radix_sort,
    }
    
    
    def demo_once(lst: List[int], algos: List[str] = None, show_time: bool = True) -> None:
        """Run provided algorithms on lst and print results (and timing if requested)."""
        algos = algos or list(ALGORITHMS.keys())
        print("Input:", lst)
        for name in algos:
            fn = ALGORITHMS[name]
            try:
                t0 = time.perf_counter()
                out = fn(lst)
                t1 = time.perf_counter()
                ok = out == sorted(lst)
                msg = f"{name:9s}: ok={ok}  output={out}"
                if show_time:
                    msg += f"  time={((t1 - t0)*1000):.3f}ms"
                print(msg)
            except Exception as e:
                print(f"{name:9s}: ERROR - {e}")
    
    
    if __name__ == "__main__":
        # small deterministic demo
        sample = [5, 3, 8, 1, 2, 9, 4, 7, 6]
        demo_once(sample)
    
        # random demo (non-negative) to show counting/radix
        rand_small = [random.randint(0, 50) for _ in range(15)]
        demo_once(rand_small)
    
        # larger random demo; avoid O(n^2) algos for large sizes
        large = [random.randint(0, 1000) for _ in range(1000)]
        print("\nLarge demo (only fast algorithms):")
        demo_once(large, algos=["merge", "quick", "heap", "radix"], show_time=True)
    ```# filepath: c:\Users\himanshusingh.r\CityLink Farebox\sorting_algorithms.py
    """
    Collection of common sorting algorithms with simple demos.
    
    Each function takes a sequence (list) and returns a new sorted list (original not mutated).
    For counting/radix sort input must be non-negative integers.
    
    Usage:
        from sorting_algorithms import bubble_sort, quick_sort
        sorted_list = quick_sort([3,1,2])
    """
    from typing import List
    import random
    import time
    import heapq
    import math
    
    
    def bubble_sort(a: List[int]) -> List[int]:
        arr = a.copy()
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr
    
    
    def selection_sort(a: List[int]) -> List[int]:
        arr = a.copy()
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    
    
    def insertion_sort(a: List[int]) -> List[int]:
        arr = a.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    
    def merge_sort(a: List[int]) -> List[int]:
        arr = a.copy()
        if len(arr) <= 1:
            return arr
    
        def merge(left: List[int], right: List[int]) -> List[int]:
            i = j = 0
            out = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    out.append(left[i]); i += 1
                else:
                    out.append(right[j]); j += 1
            out.extend(left[i:]); out.extend(right[j:])
            return out
    
        mid = len(arr) // 2
        return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))
    
    
    def quick_sort(a: List[int]) -> List[int]:
        arr = a.copy()
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
    
    def heap_sort(a: List[int]) -> List[int]:
        arr = a.copy()
        heapq.heapify(arr)
        return [heapq.heappop(arr) for _ in range(len(arr))]
    
    
    def counting_sort(a: List[int]) -> List[int]:
        if not a:
            return []
        if any(x < 0 for x in a):
            raise ValueError("counting_sort only supports non-negative integers")
        arr = a.copy()
        maxi = max(arr)
        counts = [0] * (maxi + 1)
        for x in arr:
            counts[x] += 1
        out = []
        for value, cnt in enumerate(counts):
            out.extend([value] * cnt)
        return out
    
    
    def radix_sort(a: List[int]) -> List[int]:
        """LSD radix sort for non-negative integers."""
        if not a:
            return []
        if any(x < 0 for x in a):
            raise ValueError("radix_sort only supports non-negative integers")
        arr = a.copy()
        max_val = max(arr)
        exp = 1
        base = 10
        while max_val // exp > 0:
            buckets = [[] for _ in range(base)]
            for num in arr:
                buckets[(num // exp) % base].append(num)
            arr = [num for bucket in buckets for num in bucket]
            exp *= base
        return arr
    
    
    # Utility to run a demo and basic timing
    ALGORITHMS = {
        "bubble": bubble_sort,
        "selection": selection_sort,
        "insertion": insertion_sort,
        "merge": merge_sort,
        "quick": quick_sort,
        "heap": heap_sort,
        "counting": counting_sort,
        "radix": radix_sort,
    }
    
    
    def demo_once(lst: List[int], algos: List[str] = None, show_time: bool = True) -> None:
        """Run provided algorithms on lst and print results (and timing if requested)."""
        algos = algos or list(ALGORITHMS.keys())
        print("Input:", lst)
        for name in algos:
            fn = ALGORITHMS[name]
            try:
                t0 = time.perf_counter()
                out = fn(lst)
                t1 = time.perf_counter()
                ok = out == sorted(lst)
                msg = f"{name:9s}: ok={ok}  output={out}"
                if show_time:
                    msg += f"  time={((t1 - t0)*1000):.3f}ms"
                print(msg)
            except Exception as e:
                print(f"{name:9s}: ERROR - {e}")
    
    
    if __name__ == "__main__":
        # small deterministic demo
        sample = [5, 3, 8, 1, 2, 9, 4, 7, 6]
        demo_once(sample)
    
        # random demo (non-negative) to show counting/radix
        rand_small = [random.randint(0, 50) for _ in range(15)]
        demo_once(rand_small)
    
        # larger random demo; avoid O(n^2) algos for large sizes
        large = [random.randint(0, 1000) for _ in range(1000)]
        print("\nLarge demo (only fast algorithms):")
        demo_once(large, algos=["merge", "quick",