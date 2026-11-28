class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)

        # Step 1: Count how many items have each factor
        freq = [0] * (n + 1)

        min_price = float("inf")

        for factor, price in items:
            freq[factor] += 1
            min_price = min(min_price, price)

        # Step 2: Count items whose factors are multiples of each factor
        for factor in range(1, n + 1):
            for multiple in range(factor * 2, n + 1, factor):
                freq[factor] += freq[multiple]

        # Step 3: Sort items by price
        items.sort(key=lambda x: x[1])

        ans = 0

        # Step 4: Buy copies that provide a free item
        for factor, price in items:

            # A boosted copy costs at least twice the cheapest price
            if price >= 2 * min_price:
                break

            # Exclude the item itself
            free_count = freq[factor] - 1

            if free_count == 0:
                continue

            # Number of boosted copies we can afford
            take = min(free_count, budget // price)

            ans += take * 2
            budget -= take * price

        # Step 5: Spend remaining budget on the cheapest item
        ans += budget // min_price

        return ans
