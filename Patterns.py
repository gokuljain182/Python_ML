# for i in range(4):
#     for j in range(3):
#         print(1, end=" ")
#     print()

# for i in range(4):
#     for j in range(3):
#         print("*", end=" ")
#     print()

# for i in range(1, 5):
#     for j in range(1, 4):
#         print(i, end=" ")
#     print()

# for i in range(1, 5):
#     for j in range(1, 4):
#         print(j, end=" ")
#     print()

# for i in range(1, 5):
#     for j in range(1, 4):
#         print(j + 4, end=" ")
#     print()

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(i, end=" ")
#     print()
#
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print('*', end=" ")
#     print()

# for i in range(1, 5):
#     for j in range(5 - i):
#         print(i, end=" ")
#     print()

# for i in range(1, 5):
#     for j in range(i, 5):
#         print(i, end=" ")
#     print()

for i in range(1, 7):
    for j in range(1, 7):
        if i == j or i == 6 or j == 1:
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print()