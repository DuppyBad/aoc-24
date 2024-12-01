from collections import Counter

rhs = []
lhs = []
similarity = 0
with open("input.txt", "r") as puzzle:
    for line in puzzle:
        inputs = line.strip("\n").split(" ")
        rhs.append(inputs[3])
        lhs.append(inputs[0])
    lhs.sort()
    rhs.sort()
    sum = 0
    for i in range(len(lhs)):
        sum = sum + (abs(int(lhs[i]) - int(rhs[i])))
    print(f"Answer(part 1): {sum}")

    counts = Counter(rhs)
    for i in range(len(lhs)):
        num = int(lhs[i])
        similarity += num * counts[str(num)]
    print(f"Answer(Part 2): {similarity}")
