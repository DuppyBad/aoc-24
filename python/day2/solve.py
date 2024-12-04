nums = []
safe_counter = []
unsafe_counter = []
with open("example.txt", "r") as puzzle:
    for line in puzzle:
        line = list(line.strip("\n").strip(" "))
        for i in range(len(line)):
            if line[i] > line[i+1]:
