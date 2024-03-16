import os
import time

while True:
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    cpf_usuario = input('''CPF (Sem pontos ou traços)
    : ''')
    cpf_usuario = cpf_usuario.replace('.', '').replace('-', '')
    

    if cpf_usuario.isnumeric():
        cpf_usuario = cpf_usuario

    elif cpf_usuario.isnumeric() == False:
        print("ENTRADA INVÁLIDA")
        continue
    

    digitos_multiplicados = []
    contador_regressivo = 10

    for digito in cpf_usuario[ : 9]:
        digito_inteiro = int(digito)
        digitos_multiplicados.append(digito_inteiro * contador_regressivo)
        contador_regressivo -= 1

    adicao_primaria = 0
    for produto in digitos_multiplicados:
        adicao_primaria += produto

    variavel_de_modulo = adicao_primaria * 10

    primeiro_digito = variavel_de_modulo % 11

    if primeiro_digito > 9:
        primeiro_digito = 0

    else:
        primeiro_digito = primeiro_digito



#//////////////////////////////////////////////////////////////////////////////////////
#OBTENÇÃO DO SEGUNDO DIGITO DO CPF

    digitos_multiplicados = []
    contador_regressivo = 11

    for digito in cpf_usuario[ : 10]:
        digito_inteiro = int(digito)
        digitos_multiplicados.append(digito_inteiro * contador_regressivo)
        contador_regressivo -= 1

    adicao_secundaria = 0
    for produto in digitos_multiplicados:
        adicao_secundaria += produto

    variavel_de_modulo = adicao_secundaria * 10

    segundo_digito = variavel_de_modulo % 11

    if segundo_digito > 9:
        segundo_digito = 0
    

    else:
        segundo_digito = segundo_digito
    
    #VALIDAÇÃO FINAL
    validacao_final = str(primeiro_digito) + str(segundo_digito)

    cpf_comparador = cpf_usuario[:9] + validacao_final
    print('CPF VÁLIDO' if cpf_comparador == cpf_usuario else 'CPF INVÁLIDO')
    break