def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if word[low_index] != word[high_index]:
        return False
    elif len(word) <= 2:
        return True
    else:
        return is_palindrome_recursive(word[1: -1], 0, -1)
