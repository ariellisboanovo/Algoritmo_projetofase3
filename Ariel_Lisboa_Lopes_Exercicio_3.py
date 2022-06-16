# Módulo 1
from datetime import date             ## importei a classe date do módulo datetime
Data_Hoje = date.today()              ## usei o método today para retornar a data atual

# Módulo 2

import secrets                      ## o módulo secrets é usado para gerar números aleatórios criptograficamente forte
senha = secrets.token_hex(4)        ## retorna uma string aleatória hexadecimal. Cada byte convertido em dois dígitos hexadecimais.
## como eu coloquei o parâmetro '4', me retornará uma sena de 8 caracteres aleatórios
  
  
# Módulo 3
from random import randint         ## imporei a função randint do módulo random para retorna uma valor inteiro de acordo com os parâmetros passados abaixo
digitos_aleatorios = str(randint(100000000, 999999999))   ## converti para string e passei parâmetros

CPF_novo = digitos_aleatorios
reverso = 10                     ## contador reverso
total = 0
                                 ## cálculos para gerar cpf
for v1 in range(19):
    if v1 > 8:                   ## primeiro índice vai de 0 a 9,
        v1 = v1 - 9              ## são os primeiros dígitos do cpf
    total += int(CPF_novo[v1]) * reverso  ## valor ttotal da multiplicação

    reverso = reverso - 1        ## decrementa o contador reverso
    if reverso < 2: 
        reverso = 11
        d = 11 - (total % 11)
        if d > 9:               ## se o digito for maior que 9 o valor é 0
            d = 0
        CPF_novo += str(d)      ## concatena o dígito gernado novo cpf
        total = 0               ## zera o total

print(f'Olá! Na data de hoje: {Data_Hoje}, você gerou uma nova senha: {senha}! E também gerou um novo CPF: {CPF_novo}')