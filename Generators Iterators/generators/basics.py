def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter_1 = count_up_to(10)

# Automatic iteration over the generator
for number in counter_1:
    print("Counter iteration:", number)


counter_2 = count_up_to(3)
# Manual access to the generator values
print("Manual access:", next(counter_2))
print("Manual access:", next(counter_2))
