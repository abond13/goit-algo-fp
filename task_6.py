def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(),
                          key=lambda x: x[1]['calories'] / x[1]['cost'],
                          reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            cost = items[list(items.keys())[i - 1]]['cost']
            calories = items[list(items.keys())[i - 1]]['calories']
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(list(items.keys())[i - 1])
            w -= items[list(items.keys())[i - 1]]['cost']

    total_cost_dp = sum(items[item]['cost'] for item in selected_items)
    return selected_items, dp[n][budget], total_cost_dp


if __name__ == '__main__':

    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100
    selected_items, total_cost, total_calories = greedy_algorithm(items, budget)
    print(f"Selected items: {selected_items}")
    print(f"Total cost: {total_cost}")
    print(f"Total calories: {total_calories}")
    print()
    selected_items_dp, total_calories_dp, total_cost_dp = dynamic_programming(items, budget)
    print(f"Selected items (dynamic programming): {selected_items_dp}")
    print(f"Total cost (dynamic programming): {total_cost_dp}")
    print(f"Total calories (dynamic programming): {total_calories_dp}")
