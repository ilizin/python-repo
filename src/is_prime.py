def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

test_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, \
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

test_results = [False, False, True, False, True, False, True, False, False, False, \
                True, False, True, False, False, False, True, False, True, False]
for i in range(len(test_values)):
	value = test_values[i]
	print(value, " -> ", sep="", end="")
	result = is_prime(value)
	print("result=", result, ", expected=", test_results[i], ", ", sep="", end="")
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
