def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    index = 0
    output = ""
    for s in text:
        if index == 0:
            if not(s.isupper()):
                output = s.upper()
            else:
                output = s

        if index > 0:
            output = output + s

        index += 1

    if output[-1] != ".":
        output = output + "."

    return output


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    
    print("Coding complete? Click 'Check' to earn cool rewards!")