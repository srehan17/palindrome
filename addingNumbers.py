print("ADD THREE NUMBERS")

input_requested = ["a", "b", "c"]
results = []

for input in input_requested:
    while True:
        user_input = raw_input("Please enter '{}': ".format(input))
        try:
            results.append(float(user_input))
        except ValueError:
            print("'{}' must be a number!".format(input))
            continue
        else:
            break

print(sum(i for i in results))
