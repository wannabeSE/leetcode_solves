#same as aggressive cows
def maxDistance(position: list, m: int) -> int:
    def possible(minDist):
        last = position[0]
        ballCount = 1
        for i in range(1, len(position)):
            if position[i] - last >= minDist:
                last = position[i]
                ballCount += 1
                if ballCount >= m:
                    return True
        return False
    position.sort()
    l, r = 0, position[-1] - position[0]
    res = 0
    while l <= r:
        mid = (l + r) // 2
        if possible(mid):
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res
print(maxDistance([1,2,3,4,7], 3))
