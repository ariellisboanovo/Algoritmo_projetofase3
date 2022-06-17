import matplotlib.pyplot as p     ## importei a função pyplot do módulo matplotlib e dei um 'apelido' curto para facilitar
import numpy as n                 ## importei numpy pra leitura de dados e apelidei de 'n'

informações_vendas = n.loadtxt('dias_e_valores.txt')    ## loadtxt é uma função do numpy para ler arquivos .txt

p.plot(informações_vendas[:,0], informações_vendas[:,1])  ## plotar os dados
p.show()               ## mostrar o gráfico