from vec import Vec
import time
import operator

def vec_vec_performance(size: int, func):
    start_time = time.time()

    v1 = Vec.uniform(size)
    v2 = Vec.uniform(size)


    v3 = func(v1, v2)

    end_time = time.time()

    duration = end_time - start_time

    print(f"Total time for {size}k {func.__name__} is {duration * 1000:.2f} ms")

sizes = [2**i for i in range(11, 17)] 

v_v_operators = [
    operator.add,
    operator.sub,
]

for op in v_v_operators:
    print(f"\n----- {op.__name__.upper()} -----")
    for size in sizes:
        vec_vec_performance(size, op)


def vec_scalar_performance(size: int, func):
    start_time = time.time()
    v1 = Vec.uniform(size)

    v2 = func(67, v1)
    end_time = time.time()
    
    duration = end_time - start_time
    print(f"Total time for {size}k {func.__name__} is {duration * 1000:.2f} ms")

v_s_operators = [
    operator.imul,
    operator.iadd,
]

for op in v_s_operators:
    print(f"\n----- {op.__name__.upper()} -----")
    for size in sizes:
        vec_scalar_performance(size, op)