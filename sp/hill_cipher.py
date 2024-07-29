# Ressources
# https://www.youtube.com/watch?v=mNGj_skw7Ck'

# A = 0, Z = 26
def get_codes_from_string(key:str) -> list[int]:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = key.lower()
    return [alphabet.index(letter) for letter in key]
    
    # Alternative :
    # result = []
    # for letter in key:
    #     result.append(alphabet.index(letter))
    # return result

def get_letter_from_code(code:int) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet[code]

def get_2x2_matrix_from_codes(codes:list) -> list:
    result = []
    result.append(codes[:2])
    result.append(codes[2:])

    return result

# 2 letters by 2 letters
def get_matrix_from_message(message:str, vector_size:int) -> list[list[int]]:
    result = []
    for i in range(0, len(message), vector_size):
        result.append(get_codes_from_string(message[i]+ message[i+1]))

    return result

def adjoint_2x2_matrix(matrix:list[list[int]]) -> list[list[int]]:
    return [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]

def determinant(matrix):
    return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

# 1/|K| = 1 pour la clé IJDK
def multiplicative_inverse():
    return 1

def invert_2x2_matrix(matrix:list[list[int]], multiplicative_inverse:int) -> list[list[int]]:
    adjoint_matrix = adjoint_2x2_matrix(matrix)
    return [
        [(adjoint_matrix[0][0] * multiplicative_inverse),  (adjoint_matrix[0][1] * multiplicative_inverse)],
        [(adjoint_matrix[1][0] * multiplicative_inverse),  (adjoint_matrix[1][1] * multiplicative_inverse)],
    ]

# Chiffre de Hill, chiffrement symétrique,
# la clé pour chiffrer et pour déchiffrer reste identique
def hill_cipher(message:str, key:str) -> str:
    key_matrix = get_2x2_matrix_from_codes(get_codes_from_string(key))
    inverted_key_matrix = invert_2x2_matrix(key_matrix, multiplicative_inverse())
    ciphered_message_codes = get_codes_from_string(message)

    result = ''
    for i in range(0, len(message), 2):
        code_letter_1 = ((inverted_key_matrix[0][0] * ciphered_message_codes[i]) + (inverted_key_matrix[0][1] * ciphered_message_codes[i+1])) % 26
        result += get_letter_from_code(code_letter_1)

        code_letter_2 = ((inverted_key_matrix[1][0] * ciphered_message_codes[i]) + (inverted_key_matrix[1][1] * ciphered_message_codes[i+1])) % 26
        result += get_letter_from_code(code_letter_2)
        
    return result

# yzhxvq : "python" chiffré avec Hill avec la clé : "IJDK"
print(hill_cipher('yzhxvq', 'IJDK'))

