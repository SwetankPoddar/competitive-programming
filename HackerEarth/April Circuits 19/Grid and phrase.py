import numpy as np

# Get the size of the grid
n, m = input().split()
m = int(m)  # Col
n = int(n)  # Row

# Word to search for
word_to_search = "saba"

no_of_time_appeared = 0

## Create a 2D array
word_array = list()
for i in range(n):
    string = input()
    word_array.append(list(string))

# Check horizontally
for i in range(n):
    no_of_time_appeared += ''.join(word_array[i]).count(word_to_search)

# Check vertically
for i in range(m):
    col_string = ''.join(row[i] for row in word_array)
    no_of_time_appeared += col_string.count(word_to_search)

# Check diagonal
word_array = np.array(word_array)
diags = [word_array[::-1, :].diagonal(i) for i in range(-word_array.shape[0] + 1, word_array.shape[1])]
diags.extend(word_array.diagonal(i) for i in range(word_array.shape[1] - 1, -word_array.shape[0], -1))

for diag in diags:
    if (len(diag) >= len(word_to_search)):
        diag = diag.tolist()
        diag = ''.join(diag)
        no_of_time_appeared += diag.count(word_to_search)

print(no_of_time_appeared)