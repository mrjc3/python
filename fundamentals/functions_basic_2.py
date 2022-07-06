# Countdown 
# def countdown(num):
#     list = []
#     for i in range(num,-1, -1):
#         list.append(i)
#     return list
# print(countdown(5))



# Print and Return
# def print_and_return(arr):
#     print(arr[0])
#     return arr[1]
# secondNum = print_and_return([1,2])
# print(secondNum)



# First Plus Length
# def first_plus_length(arr):
#     return arr[0] + len(arr)
# print(first_plus_length([1,2,3,4,5]))


# Values greater than Second
# def values_greater_than_second(arr):
#     newarr = []
#     if len(arr) < 2:
#         return False
    
#     for num in arr:
#         if num > arr[1]:
#             print(num)
#             newarr.append(num)
#     return newarr
# print(values_greater_than_second([5,2,3,2,1, 4]))

# length and value
def length_value(size, value):
    list = []
    for i in range(size):
        list.append(value)
    return list

print(length_value(6,2))
print(length_value(4,7))