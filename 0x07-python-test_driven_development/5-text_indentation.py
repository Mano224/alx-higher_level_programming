def text_indentation(text):
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading and trailing spaces
    text = text.strip()

    # Initialize result string
    result = ""

    # Iterate over each character in the input text
    for char in text:
        # Append the character to the result string
        result += char

        # If the character is ., ?, or :, add two new lines
        if char in ".?:":  # Add two new lines after ., ? and :
            result += "\n\n"

    # Print the result
    print(result)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
