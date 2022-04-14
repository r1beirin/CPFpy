from random import randint

def geraCpfPrimeiroDigito(cpf):
    cpfMultiplicado = []
    mult = 10
    soma = 0

    for i in range(0, 9):
        cpfMultiplicado.append(int(cpf[i]) * mult)
        mult -= 1
        soma += cpfMultiplicado[i]

    if (soma % 11) < 2:
        return 0
    else:
        return 11 - (soma % 11)

def geraCpfSegundoDigito(cpf, primeiroDigito):
    cpfCopy = cpf.copy()
    cpfCopy.append(primeiroDigito)
    cpfMultiplicado = []
    mult = 11
    soma = 0

    for i in range(0, 10):
        cpfMultiplicado.append(int(cpfCopy[i]) * mult)
        mult -= 1
        soma += cpfMultiplicado[i]
    
    if (soma % 11) < 2:
        return 0
    else:
        return 11 - (soma % 11)

def separaCpf(cpf):
    cpf = list(cpf)
    for i in cpf:
        if i == '.' or i == '-':
            cpf.remove(i)
    return cpf

def validaPrimeiroDigito(cpfSeparado):
    primary = cpfSeparado[0:9]
    multiplicado = []
    mult = 10
    cont = 0
    soma = 0

    while cont < 9:
        multiplicado.append(int(primary[cont]) * mult)
        cont += 1
        mult -= 1

    for i in range(0, len(multiplicado)):
        soma += multiplicado[i]
    
    if (soma % 11) < 2:
        return str(0)
    else:
        return str((11 - (soma % 11)))

def validaSegundoDigito(cpfSeparado):
    primary = cpfSeparado[0:10]
    multiplicado = []
    mult = 11
    cont = 0
    soma = 0

    while cont < 10:
        multiplicado.append(int(primary[cont]) * mult)
        cont += 1
        mult -= 1

    for i in range(0, len(multiplicado)):
        soma += multiplicado[i]
   
    if (soma % 11) < 2:
        return str(0)
    else:
        return str(11 - (soma % 11))

def validaCpf(cpf, novoCPF):
    if novoCPF == cpf:
        return True
    else:
        return False

def verificaDigitos(cpf, novoCPF):
    # Caso de teste para validar repetição: 111.111.111-11
    if len(cpf) > 14 or novoCPF == list(novoCPF[0]) * len(novoCPF):
        print('Digite o CPF novamente.')
        return True

if __name__ == '__main__':
    while True:
        print('==='*15)
        print('1. Validar CPF')
        print('2. Gerar CPF')
        print('3. Sair')
        opcao = int(input('Digite sua opção: '))
        print('==='*15)

        if opcao == 1:
            try:
                cpf = input('Digite o CPF: ')

                novoCPF = separaCpf(cpf)[0:9]
                novoCPF.append(validaPrimeiroDigito(separaCpf(cpf)))
                novoCPF.append(validaSegundoDigito(separaCpf(cpf)))

                if verificaDigitos(cpf, novoCPF):
                    continue

                if validaCpf(separaCpf(cpf), novoCPF):
                    print(f'O CPF {cpf} é valido.')
                else:
                    print(f'O CPF {cpf} não é valido')
            except:
                print('Digite o CPF novamente.')

        if opcao == 2:
            cpfGerado = []
            for i in range(0, 9):
                cpfGerado.append(randint(1, 9))
                
            cpfGerado.append(geraCpfPrimeiroDigito(cpfGerado))
            cpfGerado.append(geraCpfSegundoDigito(cpfGerado, geraCpfPrimeiroDigito(cpfGerado)))

            for i, v in enumerate(cpfGerado):
                if i == 2 or i == 6:
                    cpfGerado.insert(i+1, '.')
                elif i == 10:
                    cpfGerado.insert(i+1, '-')
                print(v, end='')

            print()
        if opcao == 3:
            break