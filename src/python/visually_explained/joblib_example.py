import time

# my_list = [1, 2, 3, 4]
# my_squares = []

# for i in my_list:
#     time.sleep(1)
#     squared = i * i
#     my_squares.append(squared)

# print(my_squares)


from python.visually_explained.joblib_example import Parallel, delayed

my_list = [1, 2, 3, 4]
my_squares = []

def slow_square(i):
    time.sleep(1)
    squared = i * i
    return squared

parallel_obj = Parallel(n_jobs=-1)
my_squares = parallel_obj(delayed(slow_square)(i) for i in my_list)

print(my_squares)
