from collections import namedtuple

Bar = namedtuple('Item', 'value weight')
bars = Bar(2, 2), Bar(7, 7), Bar(5, 5), Bar(9, 9)
capacity = 15  # max weight we can put into the knapsack


def best_value(number_of_items, weight_limit):
    if number_of_items == 0:  # no items
        return 0  # zero value
    elif bars[number_of_items - 1].weight > weight_limit:
        # new item is heavier than the current weight limit
        return best_value(number_of_items - 1, weight_limit)  # don't include new item
    else:
        return max(  # max of with and without the new item
            best_value(number_of_items - 1, weight_limit),  # without
            best_value(number_of_items - 1, weight_limit - bars[number_of_items - 1].weight)
            + bars[number_of_items - 1].value)  # with the new item


mas = []
result = 0
for i in reversed(range(len(bars))):
    if best_value(i + 1, capacity) > best_value(i, capacity):
        # better with the i-th item
        mas.append(bars[i])  # include it in the mas
        capacity -= bars[i].weight
for i in range(len(mas)):
    result += mas[i].weight
print("max weight = ", result)
