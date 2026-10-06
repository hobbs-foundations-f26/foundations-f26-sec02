# Given a list called my_list (you can assume this already exists)

# Write code that if my_list has fewer than 10 elements print the first half of the list
# Else if the list has between 11 (inclusive) and 100 (inclusive) elements, print every other element
# Otherwise, print "too big"

if len(my_list) < 10:
    print(my_list[:len(my_list)//2])
elif 10 < len(my_list) <= 100:
    print(my_list[::2])
else:
    print("too big")