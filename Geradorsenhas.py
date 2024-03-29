import random
import string


def gerar_senha(comprimento: object = 12, usar_maiusculas: object = True, usar_minusculas: object = True, usar_digitos: object = True,
                usar_caracteres_especiais: object = True) -> object:
    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_digitos:
        caracteres += string.digits
    if usar_caracteres_especiais:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Nenhum tipo de caractere selecionado para a senha.")

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha


senha_gerada = gerar_senha(comprimento= 16, usar_maiusculas=True, usar_minusculas=True, usar_digitos=True,
                           usar_caracteres_especiais=True)
print("Senha gerada:\33[31m",senha_gerada)
