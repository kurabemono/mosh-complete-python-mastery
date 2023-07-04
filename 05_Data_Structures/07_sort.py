numbers = [5, 18, 27, -2, 8]
print(sorted(numbers, reverse=True))

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
