# assignment-4 

# r= lambda a : a+25
# print(r(10))

# # Q-2
# numbers = [20,47,61,16,81,88]
# print('original list:',numbers)
# result= map (lambda x:x+x+x, numbers)
# print("\ntriple of said list numbers:")
# print(list(result))

# # Q-3
def square_numbers(n):
    return n*n
numbers=[20,30,12,8,4]
print("original List:",numbers)
result=map(square_numbers,numbers)
print("square the elements of said list:")
print(list(result))