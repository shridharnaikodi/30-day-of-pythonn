nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [num ** 2 for num in nums if num % 2 == 0]

print(result)





nums = [1, 2, 3, 4, 5, 6]

result = list(
    map(lambda x: x ** 2,
        filter(lambda x: x > 3, nums))
)

print(result)







def calculate(*args, **kwargs):

    operation = kwargs.get("operation")

    if operation == "sum":
        return sum(args)

    elif operation == "max":
        return max(args)

    elif operation == "min":
        return min(args)

    else:
        return "Invalid operation"


print(calculate(10, 20, 30, operation="sum"))
print(calculate(10, 20, 30, operation="max"))
print(calculate(10, 20, 30, operation="min"))