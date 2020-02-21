def find(numbers):
    max = numbers[0]
    for items in numbers:
        if items > max:
            max = items
    print(max)