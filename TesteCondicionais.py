r1 = float(input('Primeira reta :\n'))
r2 = float(input('Segunda reta :\n'))
r3 = float(input('Terceira Reta :\n'))

M = max(r1, r2, r3)
S = r1 + r2 + r3
SM = S - M

if SM < M:
    print('\33[31mNão pode formar um Triângulo')
elif SM > M and r1 == r2 and r2 == r3:
    print('\33[36mPode formar um Triângulo\n\nSerá um Triângulo equilátero todos os lados são iguais')
elif SM > M and r1 == r2 or r1 == r3 or r2 == r3:
    print('\33[36mPode formar um Triângulo\n\nSerá um Triângulo Isósceles dois lados são iguais')
elif SM > M and r1 != r2 and r2 != r3 and r1 != r3:
    print('\33[36mPode formar um Triângulo\n\nSerá um Triângulo escaleno todos os lados são diferentes')

