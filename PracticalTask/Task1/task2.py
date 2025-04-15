def process_integer_list(int_list):
    unique_values = tuple(set(int_list))

    minimum = min(unique_values)
    maximum = max(unique_values)

    return unique_values, minimum, maximum

if __name__ == "__main__":
    print("Unique Integer Tuple Processor")

    input_str = input("Enter a list of integers separated by spaces: ").strip()

    try:
        numbers = list(map(int, input_str.split()))

        unique_tuple, minimum, maximum = process_integer_list(numbers)

        print(f"Tuple without duplicates: {unique_tuple}")
        print(f"Minimum value: {minimum}")
        print(f"Maximum value: {maximum}")

    except ValueError:
        print("Error: Please enter only valid integers separated by spaces.")
