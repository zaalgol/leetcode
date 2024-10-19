import time
import math
import random

# Generating a random huge number (200 bits)
x = random.getrandbits(200)

# Iterative approach
def closest_power_of_two_iterative(x):
    if x < 1:
        return 1
    power = 1
    while power * 2 <= x:
        power *= 2
    next_power = power * 2
    return power if (x - power) < (next_power - x) else next_power

# Logarithmic approach
def closest_power_of_two_logarithmic(x):
    if x < 1:
        return 1
    lower_power = 2 ** math.floor(math.log(x, 2))
    higher_power = 2 ** math.ceil(math.log(x, 2))
    return lower_power if (x - lower_power) < (higher_power - x) else higher_power

# Bitwise approach
def closest_power_of_two_bitwise(x):
    if x < 1:
        return 1
    power = 1 << (x.bit_length() - 1)
    next_power = power << 1
    return power if (x - power) < (next_power - x) else next_power

# Measure execution time for each algorithm
# def measure_time(func, x):
#     start = time.time()
#     result = func(x)
#     end = time.time()
#     return result, end - start
def measure_time(func, x):
    start = time.perf_counter()
    result = func(x)
    end = time.perf_counter()
    return result, end - start

# Running and measuring the time of all 3 algorithms
iterative_result, iterative_time = measure_time(closest_power_of_two_iterative, x)
logarithmic_result, logarithmic_time = measure_time(closest_power_of_two_logarithmic, x)
bitwise_result, bitwise_time = measure_time(closest_power_of_two_bitwise, x)

# Print the results and execution times
results = {
    "random_number": x,
    "iterative_result": iterative_result,
    "iterative_time": iterative_time,
    "logarithmic_result": logarithmic_result,
    "logarithmic_time": logarithmic_time,
    "bitwise_result": bitwise_result,
    "bitwise_time": bitwise_time
}

print(results)
