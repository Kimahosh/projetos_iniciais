
cpf_usuario = '165.483.017-81'
validacao_primaria = cpf_usuario[:11]
cpf_tratado = validacao_primaria.replace('.', '')

digitos_multiplicados = []
multiplicador = 10

for digito in cpf_tratado:
    digito_inteiro = int(digito)
    digitos_multiplicados.append(digito_inteiro * multiplicador)
    multiplicador -= 1

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