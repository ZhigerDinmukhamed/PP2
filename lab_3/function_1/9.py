def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens

        total_legs = 2 * num_chickens + 4 * num_rabbits

        if total_legs == numlegs:
            return num_chickens, num_rabbits

num_heads_input = 35
num_legs_input = 94

chickens, rabbits = solve(num_heads_input, num_legs_input)

if chickens is not None and rabbits is not None:
    print(chickens)
    print(rabbits)
else:
    print("No solution found.")