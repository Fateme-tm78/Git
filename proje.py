inp = input()


inp = input().split()

for i, v in enumerate(inp):
    inp[i] = int(v)

amount = map(int, input().split())

z = []
f = []

arr1 = set()
arr2 = set()

for i in amount:
    if i > 0:
        if i % 2 = 0:
            arr1.add(i)
        else:
            arr2.add(i)

print('this is output arr1')
print(*arr1, sep='\n')

print('this is output arr2')
print(*arr2, sep='\n')