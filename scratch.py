a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)

sentence = 'this is a test sentence for title'

print(sentence.title())


def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


def lowest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return min(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
func_output_highest = highest_even([10, 2, 3, 4, 6, 8, 11, 12])
print(func_output_highest)

print(lowest_even([10, 2, 3, 4, 8, 11]))
func_output_lowest = lowest_even([10, 2, 3, 4, 6, 8, 11, 12])
print(func_output_lowest)

total = 0


def count():
    global total
    total += 1
    return total


print(total)
print(count())
print(total)
