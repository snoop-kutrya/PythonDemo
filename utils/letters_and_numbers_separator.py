import re


def separat_letter_and_number(text_str):
    try:
        numbers = re.findall(r'\d+', text_str)
        return int(numbers[0])

    except ValueError:
        print("Invalid input. Please provide a valid string.")
        return None