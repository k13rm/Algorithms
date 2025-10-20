# n = 10

# for i in range(n+6):
#     print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


n = 10
for i in range(1, n):
    print(i)


# Type 1: for i in range(n): [0, 1, 2, 3, ..., n-1], increases by 1 every time
# Type 2: for i in range(a,b): the for loop starts at a, ends at b-1, increases by 1 every time. So the total number or rounds is (b - a)
# Type 3: for i in range(a,b,c):