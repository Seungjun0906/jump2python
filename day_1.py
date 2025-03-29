str = "Life is to short"

# formatted_str = "this is a %-20s" % "정렬쓰"

formatted_str = f"hello{'승준':=^30}"

formatted_str = "hello %d %s" % (10, "승준")

# print(len(formatted_str))

# print(formatted_str)

# print(formatted_str.count("="))

a = [1,2,3,4,5]

b = sorted(a, key=lambda x:x ,reverse=True)

print(a)

a.sort(reverse=True)

print(a)