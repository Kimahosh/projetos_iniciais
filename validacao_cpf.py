
cpf_usuario = '165.483.017-81'
validacao_primaria = cpf_usuario[:11]
cpf_tratado = validacao_primaria.replace('.', '')

digitos_multiplicados = []
contador_regressivo = 10

for digito in cpf_tratado:
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

print(primeiro_digito)

#//////////////////////////////////////////////////////////////////////////////////////
#OBTENÇÃO DO SEGUNDO DIGITO DO CPF
validacao_secundaria = cpf_usuario[:13]
cpf_tratado = validacao_secundaria.replace('.', '').replace('-', '')

digitos_multiplicados = []
contador_regressivo = 11

for digito in cpf_tratado:
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

print(segundo_digito)