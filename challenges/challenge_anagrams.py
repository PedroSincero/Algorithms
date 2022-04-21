# ref https://panda.ime.usp.br/panda/static/
# pythonds_pt/02-AnaliseDeAlgoritmos/
# ExemploDeDeteccaoDeAnagramas.html

def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    list_first_string = merge_sort(list(first_string))
    list_second_string = merge_sort(list(second_string))

    string_1 = "".join(list_first_string)
    string_2 = "".join(list_second_string)

    if string_1 == string_2 and len(string_1) == len(string_2):
        return True
    else:
        return False

# percorro a string e separo os seus valores, com isso percorro novamente.
# porém os comparando.
# se o valor do first_string[0]
# for igual ao second_string[0] aciona novamente a função
# Momento de parada, quanto first_string == second_string
# Agradecimentos a
# Gabriel Ribeiro - Turma 10 - Tribo B Pelo auxilio no entendimento do codigo

# Conteudo retirado do Course da Trybe > 35.3 > algoritmo de ordenação > Merge sort
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right, array.copy())


# função auxiliar que realiza a mistura dos dois arrays
def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


print(is_anagram('amor', 'romaa'))
