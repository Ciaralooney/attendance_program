def get_non_empty_string(prompt):
    """
    This receives one prompt message and will check to ensure the user inputs a string.
    If the user inputs nothing it will tell the user this and keep prompting them to enter until
    a non-empty string is inputted.
    :param prompt: str containing a relevant prompt on what the user should enter
    :return: phrase (str) that is a non-empty string
    """
    while True:
        phrase = input(prompt)
        # if the input is longer than 0 it breaks from the loop
        if len(phrase) > 0:
            break
        # otherwise it tells the user the input is not valid and asks again
        else:
            print("This is empty")

    return phrase


def number_range(lower_range, higher_range, prompt):
    """
    The user is asked to input a number. This function checks that the input is between the lower and higher range.
    If it isn't then the user will be prompted to enter again.
    :param lower_range: int that is the lowest number the user can enter
    :param higher_range: int that is the highest number the user can enter
    :param prompt: str containing a relevant prompt on what the user should enter
    :return: an int that is within the range specified
    """
    while True:
        try:
            number = int(input(prompt))
            # if the number is within range it breaks from the loop
            if lower_range <= number <= higher_range:
                break
            # if the number is not within the range
            else:
                print(f"Please enter a number between the range {lower_range}-{higher_range}.")
        except ValueError:
            print("Please enter a numeric value.")

    return number
