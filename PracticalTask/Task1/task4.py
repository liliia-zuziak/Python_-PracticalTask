from collections import Counter

def count_characters(input_string):
    char_counts = Counter(input_string)
    
    formatted = ', '.join(f'{char}:{count}' for char, count in char_counts.items())
    return formatted

if __name__ == "__main__":
    print("Character Occurrence Counter")

    input_string = input("Enter a string to analyze: ").strip()

    if not input_string:
        print("Please enter a non-empty string.")
    else:
        result = count_characters(input_string)
        print(f"Character counts: {result}")
