def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def classificar_imc(imc):
    if imc <= 18.5:
        return 'ABAIXO DO PESO', 'Cuidado!'
    elif imc <= 24.9:
        return 'PESO IDEAL', 'Parabéns!'
    elif imc <= 29.9:
        return 'LEVEMENTE ACIMA DO PESO', 'Cuidado!'
    elif imc <= 34.9:
        return 'OBESIDADE GRAU I', 'Cuidado! Larga a cerveja.'
    elif imc <= 39.9:
        return 'OBESIDADE GRAU II (SEVERA)', 'Cuidado! Você está se arriscando.'
    else:
        return 'OBESIDADE GRAU III (MÓRBIDA)', 'Cuidado! você está quase morrendo.'


def main():
    peso = float(input('Informe seu peso em kg: '))
    altura = float(input('Digite sua altura em metros: '))

    imc = calcular_imc(peso, altura)
    classificacao, mensagem = classificar_imc(imc)

    print(f'Seu IMC é {imc:.2f}. A classificação é: {classificacao}\n{mensagem}')


if __name__ == "__main__":
    main()
