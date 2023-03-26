#triple numbers of a given list of integers using map function

nums = (1,2,3,4,5,6,7)
print("Original list:",nums)
result = map(lambda x : x + x + x,nums)
print(list(result))


#write a python program to square of the elements using mapo()


def square_num(n):
    return n * n
nums = [4,5,2,9]
print("Original List:",nums)
result = map(square_num,nums)
print("Square the element of thesaid list using map():")
print(list(result))


