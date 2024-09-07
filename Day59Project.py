def is_palindrome(word):
    """Determines whether a given string is a palindrome or not.
    
    A palindrome is a string that reads the same forwards and backwards.
    
    Parameters
    ----------
    word : str
        The string to check
    
    Returns
    -------
    bool
        Whether the string is a palindrome or not
    """
    if len(word) <= 1:    
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

word = input("Type a word to see if it is a palindrome: ").lower()

if is_palindrome(word):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
