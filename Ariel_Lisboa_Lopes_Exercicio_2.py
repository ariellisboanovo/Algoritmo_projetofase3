times_de_futebol = ["Flamengo", "Fluminense", "Flamengo", "Santos", "Vasco", "Ceará", "Fluminense", "Real Madrid", "Bragantino"]
# lista com elementos duplicados

TimesNãoRepetidos = []      # nova lista que irá armazenar elementos únicos
 
for nome_do_time in times_de_futebol:        # loop for para percorrer a lista comnomes duplicados
    if nome_do_time not in TimesNãoRepetidos:  # condicional para determinar se o elemento será adicionada na nova lista
        TimesNãoRepetidos.append(nome_do_time) # o elemento só entra na nova lista sse não for repetido

print(TimesNãoRepetidos)