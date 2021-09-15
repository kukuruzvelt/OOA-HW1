from collections import namedtuple

Item = namedtuple('Item', 'value weight')
items = Item(9, 9), Item(8, 8), Item(5, 5), Item(2, 2)
capacity = 15  # max weight we can put into the knapsack


def best_value(number_of_item, weight_limit):
    if number_of_item == 0:  # no items
        return 0  # zero value
    elif items[number_of_item - 1].weight > weight_limit:
        # new item is heavier than the current weight limit
        return best_value(number_of_item - 1, weight_limit)  # don't include new item
    else:
        return max(  # max of with and without the new item
            best_value(number_of_item - 1, weight_limit),  # without
            best_value(number_of_item - 1, weight_limit - items[number_of_item - 1].weight)
            + items[number_of_item - 1].value)  # with the new item


result = []
for i in reversed(range(len(items))):
    if best_value(i + 1, capacity) > best_value(i, capacity):
        # better with the i-th item
        result.append(items[i])  # include it in the result
        capacity -= items[i].weight
print(result)
