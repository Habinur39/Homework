#1
immutable_var = 1, 2, 3, True, 'string'
print('Immutable tuple:' ,immutable_var)
#immutable_var[0] = 228
#print(immutable_var)


#2
mutable_list = [1, 2, 3, 5, 10, 15, 20]
print('Mutable list: ' ,mutable_list)
mutable_list [0] = 456
mutable_list [-1] = 'hello'
print('Mutable list new: ' ,mutable_list)