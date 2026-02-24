n, h = input().split()
n = int(n)
h = int(h)

heights = input().split()

width = 0

for i in range(n):
    if int(heights[i]) > h:
        width = width + 2
    else:
        width = width + 1

print(width)
