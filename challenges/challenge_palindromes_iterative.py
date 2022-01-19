def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False
    elif word[0] != word[-1]:
        return False
    elif len(word) <= 2:
         return True
    else:
        result = word[1:-1]
        return is_palindrome_iterative(result)

    # return True
    # return False

# se a letra inicial for igual a final
# vá para outra casa
#  se a string acabar, retorne True
#  se a letra inicial nao for igual a final, retorne false
