def solve(n: int, k: int, stalls: list) -> int:
    def possible(min_dist: int):
        last_cow_pos = stalls[0]
        cow_count = 1
        for i in range(1, len(stalls)):
            if stalls[i] - last_cow_pos >= min_dist:
                cow_count += 1
                last_cow_pos = stalls[i]
                if cow_count >= k:
                    return True
        return False 
    stalls.sort()
    l, r = 0, stalls[n - 1] - stalls[0] # assigning high, low with array values as we are working with distances. Not like usual pointers for BS 
    max_dist = 0
    while l <= r:
        mid = (l + r) // 2
        if possible(mid):
            max_dist = mid
            l = mid + 1
        else:
            r = mid - 1

    return max_dist

print(solve(6, 5, [2, 12, 11, 3, 26, 7])) #2,3,7,11,12,26