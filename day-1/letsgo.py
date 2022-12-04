with open("input.txt", "r") as f:
    text = f.read()

max_calories = 0
current_calories = 0
for line in text.split("\n"):
    if not line:
        if current_calories > max_calories:
            max_calories = current_calories
        current_calories = 0
        continue
    current_calories += int(line)

print(max_calories)