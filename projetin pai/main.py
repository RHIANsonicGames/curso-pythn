import pandas as pd

data = {'nome': ['alice', 'bob', 'david', 'charlie'],
        'idade': [25, 30, 35, 40],
        'profissao': ['emgemheiro', 'analista', 'gerente', 'diretor']}

df = pd.DataFrame(data)

print(df)

media_idade = df['idade'].mean()
print('Media de idade:', media_idade)