import random

def simulate_dice_rolls(num_rolls):
    counts = [0]*13
    probabilities = [0]*13
    for _ in range(num_rolls):
        curr = random.randint(1, 6) + random.randint(1, 6)
        counts[curr] += 1
        probabilities[curr] = (counts[curr] / num_rolls) * 100
    return probabilities

if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        print("-"*10)
        print(f"{accuracy:^10}")
        print("-"*10)
        val = 2
        for res in simulate_dice_rolls(accuracy)[2:]:
            print(f"{val:<2}  {res:.2f}")
            val += 1
        print("-"*10)

