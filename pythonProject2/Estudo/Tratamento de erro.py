def leiaint(valor):
    while True:
        entrada = input(valor).replace(',', '.').strip()

        try:
            if entrada.isalpha():
                print("\033[0;31mValor incorreto. Por favor, insira um número.\033[m")

            elif float(entrada) > 100:
                print("\033[0;31mValor não pode ser maior que 100.\033[m")

            else:
                return float(entrada)

        except ValueError as erro:
            if entrada == '':
                print("O usuário não informou nada, então o valor é 0.")
                return 0
            else:
                print(f'\033[0;31mErro ao converter o valor: {erro}\033[m')
                print('----> ERROS POSSÍVEIS <----')
                print('- Não incluído no nosso conjunto de caracteres')
                print('- Ultrapassou o limite de 100 reais')

# Example usage
valor_digitado = leiaint("Digite um valor: ")
print(f"Valor digitado: {valor_digitado}")