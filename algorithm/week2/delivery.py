menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]

orders = ["오뎅", "콜라", "만두"]

menus.sort()
orders.sort()

# def is_available_order():
#     available = []
#     for order in orders:
#         # O(A)
#         if order in menus:
#             print(order)
#             # O(B)
#             available.append(order)

#     # O (A * B)
#     if len(available) == len(orders):
#         return True
#     else:
#         return False


# result = is_available_order()

# print(result)


# def is_available_order_with_binary():

#     available = []

#     for order in orders:
#         min_idx, max_idx = 0, len(menus) - 1
#         cur_idx = (min_idx + max_idx) // 2

#         while min_idx <= max_idx:

#             cur_val = menus[cur_idx]

#             if cur_val == order:
#                 available.append(order)
#                 break
#             elif order < cur_val:
#                 max_idx = cur_idx - 1
#             elif order > cur_val:
#                 min_idx = cur_idx + 1

#             cur_idx = (min_idx + max_idx) // 2

#     print(available)

#     if len(available) == len(orders):
#         return True

#     return False


# result = is_available_order_with_binary()
# print(result)


def is_available_order_with_map():
    menu_map = {}
    available = []

    for menu in menus:
        menu_map[menu] = True

    for order in orders:
        if menu_map[order]:
            available.append(order)

    return len(available) == len(orders)


test = is_available_order_with_map()

print(test)
