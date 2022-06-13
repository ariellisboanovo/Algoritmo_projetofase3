time_de_futebol = input('Qual é o seu time?: ')  # variavel de escopo global


def func1():         # primeira função
    if time_de_futebol == "Flamengo":        # condicioanais 
        print(f'{time_de_futebol} é campeão mundial')
    else:
        print(f'{time_de_futebol} não é campeão mundial')

def func2():   # segunda função
   
    time_de_futebol = 'Palmeiras'     # escopo local / a variável muda de valor somente dentro dessa função
    print(f'{time_de_futebol} não é campeão mundial')
func1()
func2()