# Solution 2
list_of_words = ["hello", "yes", "goodbye", "last"]

# for i in range(4):
#     to_print += list_of_words[i]
#     if i != 3:
#         to_print += ","

to_print = ""

for i in range(len(list_of_words)):
    to_print += list_of_words[i]
    if i != (len(list_of_words) - 1):
        to_print += ","

print(to_print)

