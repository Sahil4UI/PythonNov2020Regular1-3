def my_decorator(function):
    def body():
        x = function()
        x = x.upper()
        return x
    return body

@my_decorator
def inputString():
    x =input("enter String:")
    return x

result = inputString()
print(result)
# decorator = my_decorator(inputString)
# result = decorator()
# print(result)
