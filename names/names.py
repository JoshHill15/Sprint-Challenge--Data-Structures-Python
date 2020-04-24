import time


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


start_time = time.time()
duplicates = []  # Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements
# TIME: O(n^2)

for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
end_time = time.time()

print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


start_time2 = time.time()
duplicates2 = [x for x in names_1 if x in names_2]
end_time2 = time.time()
print(f"{len(duplicates2)} duplicates2:\n\n{', '.join(duplicates2)}\n\n")
print(f"runtime: {end_time2 - start_time2} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
