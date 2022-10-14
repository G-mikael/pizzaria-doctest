import pandas as pd
import funcoes as fc

Colunas = {'ingrediente':'farinha', 'preço':50}
Indice = ['oi']
df = pd.DataFrame(data= Colunas, index= Indice)
print(df)

print(fc.cadastrar_ingrediente('molho', 'Molho de tomate', '5', df))
