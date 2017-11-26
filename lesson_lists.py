import random

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 101]

# for elem in lst:
#     elem *= 2
#     print(elem)
#
# print(lst)
# print("_________")
#
# for i, elem in enumerate(lst):
#     print(i, elem)
#     lst[i] *= 2
#
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])
# print(lst[4])
# print("_________")
#
#
# print(id(lst))
#
# for i in range(len(lst)):
#     print(lst[i])
#     lst[i] *= 2
#
# print(lst)
# print(id(lst))
# print("_________")
#
#
# for i in range(len(lst)):
#     lst[i] **= 2
#
# print(lst)
# print(id(lst))
# print("_________")


def multiply_list(lst, coeff):
    for i in range(len(lst)):
        print(i, lst[i])
        lst[i] *= coeff

multiply_list(lst, coeff= 4)

print(id(lst))
print(lst)
# lst = [0] *100
# print(id(lst), lst)
print("_________")


zeros_lst = [0]*100
#print (zeros_lst)

def fill_list(lst, lower_bound, upper_bount):
    for i in range(len(lst)):
      lst[i] = random.randint(lower_bound, upper_bount)

fill_list(zeros_lst, 10, 20)
print(id(zeros_lst), zeros_lst)
print("_________")

def nulify_lst (lst):
    for i in range(len(lst)):
        lst[i] *= 0

print(id(lst), lst)



