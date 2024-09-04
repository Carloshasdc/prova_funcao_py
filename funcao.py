def maior_numero(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3
    
n1= int(input('Digite o primeiro numero: '))
n2= int(input('Digite o segundo numero: '))
n3= int(input('Digite o terceiro numero: '))

print(f'O maior numero é {maior_numero(n1,n2,n3)}')