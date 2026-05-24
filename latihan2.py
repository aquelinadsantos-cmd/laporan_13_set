# List menjadi Set
data_list = [1, 2, 3, 2, 4, 5, 1]

print("Data List:")
print(data_list)

data_set = set(data_list)

print("\nHasil konversi List ke Set:")
print(data_set)

# Set menjadi List
list_baru = list(data_set)

print("\nHasil konversi Set ke List:")
print(list_baru)

# Tuple menjadi Set
data_tuple = ("apel", "mangga", "apel", "jeruk")

print("\nData Tuple:")
print(data_tuple)

set_buah = set(data_tuple)

print("\nHasil konversi Tuple ke Set:")
print(set_buah)

# Set menjadi Tuple
tuple_baru = tuple(set_buah)

print("\nHasil konversi Set ke Tuple:")
print(tuple_baru)