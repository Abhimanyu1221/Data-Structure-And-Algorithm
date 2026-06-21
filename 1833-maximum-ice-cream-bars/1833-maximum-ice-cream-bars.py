class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)

        count = [0] * (max_cost + 1)

        # Count frequency of each cost
        for cost in costs:
            count[cost] += 1

        ans = 0

        # Buy from cheapest to costliest
        for cost in range(1, max_cost + 1):
            if count[cost] == 0:
                continue

            can_buy = min(count[cost], coins // cost)
            ans += can_buy
            coins -= can_buy * cost

            if coins < cost:
                break

        return ans