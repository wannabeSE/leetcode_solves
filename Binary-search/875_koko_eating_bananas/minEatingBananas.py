import math
def minEatingSpeed(piles: list, h: int) -> int:
    maxPile = max(piles)
    l, r = 1, maxPile #l starts at 1 cause Koko cannot eat 0 banana
    res = maxPile
    while l <= r:
        k = (l + r) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        if hours > h:
            l = k + 1
        else:
            res = min(res, k) #minium needs to be calculated when time taken < given time
            r = k - 1
    return res

print(minEatingSpeed([312884470], 968709470))
 