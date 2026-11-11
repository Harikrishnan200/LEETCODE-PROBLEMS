# 3789. Minimum Cost to Acquire Required Items (leetcode)

# You are given five integers cost1, cost2, costBoth, need1, and need2.

# There are three types of items available:

# An item of type 1 costs cost1 and contributes 1 unit to the type 1 requirement only.
# An item of type 2 costs cost2 and contributes 1 unit to the type 2 requirement only.
# An item of type 3 costs costBoth and contributes 1 unit to both type 1 and type 2 requirements.
# You must collect enough items so that the total contribution toward type 1 is at least need1 and the total contribution toward type 2 is at least need2.

# Return an integer representing the minimum possible total cost to achieve these requirements.

 

# Example 1:

# Input: cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2

# Output: 3

# Explanation:

# After buying three type 3 items, which cost 3 * 1 = 3, the total contribution to type 1 is 3 (>= need1 = 3) and to type 2 is 3 (>= need2 = 2).
# Any other valid combination would cost more, so the minimum total cost is 3.

# Example 2:

# Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3

# Output: 22

# Explanation:

# We buy need1 = 2 items of type 1 and need2 = 3 items of type 2: 2 * 5 + 3 * 4 = 10 + 12 = 22.
# Any other valid combination would cost more, so the minimum total cost is 22.

# Example 3:

# Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0

# Output: 0

# Explanation:

# Since no items are required (need1 = need2 = 0), we buy nothing and pay 0.



class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):

        option1 = max(need1, need2) * costBoth

        option2 = need1 * cost1 + need2 * cost2

        rem_qty = abs(need1 - need2)

        if need1 > need2:
            rem_rate = cost1
        else:
            rem_rate = cost2

        option3 = min(need1, need2) * costBoth + rem_rate * rem_qty

        return min(option1, option2, option3)


print(Solution().minimumCost(50, 55, 72, 5, 3))


# Explanation:

# Understand the three possibilities
# Let's take:
# cost1 = 5cost2 = 4costBoth = 3need1 = 3need2 = 2



# Option 1: Buy combined items for the overlapping requirements.
# both = min(need1, need2)     = min(3, 2)     = 2



# So:
# - Buy 2 Type 3 items.
# - Buy 1 additional Type 1 item.
# Cost:
# 2 * 3 + 1 * 5 = 11



# Option 2: Buy only Type 3 items.

# We buy enough Type 3 items to satisfy the larger requirement.
# max(need1, need2) * costBoth= 3 * 3= 9



# Option 3: Buy only individual items.
# need1 * cost1 + need2 * cost2= 3 * 5 + 2 * 4= 23



# Now select the minimum:
# min(11, 9, 23)



# Answer:
# 9



# 4. Why do we need three options?
# Option	Strategy	Cost
# 1	Combined items for overlap, individual items for remainder	11
# 2	Only combined items	9
# 3	Only individual items	23

# We check all three possibilities and return the cheapest.
# 5. Complexity
# - Time: O(1) – Only a fixed number of calculations.
# - Space: O(1) – No additional data structures.

    