# genObj = (i for i in range(1,11))
# print(list(genObj))

def Even(x):
    for i in x:
        if i%2==0:
            yield i

result = Even([1,2,3,4,5])
# print(list(result))
for i in result:
    print(i)