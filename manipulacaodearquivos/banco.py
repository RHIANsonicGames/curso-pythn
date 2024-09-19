
# Conectando ao banco de dados
conexao = sqlite3.connect('meu_banco_de_dados.db')
cursor = conexao.cursor()

# Criando a tabela de conquistas
cursor.execute('''
CREATE TABLE IF NOT EXISTS conquistas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL
)
''')

# Coletando conquistas do usuário
conquistas = []
while True:
    conquista = input("Digite uma conquista (ou 'começar' para terminar): ")
    if conquista.lower() == 'começar':
        break
    conquistas.append(conquista)

# Inserindo conquistas no banco de dados
for conquista in conquistas:
    cursor.execute('''
    INSERT INTO conquistas (descricao)
    VALUES (?)
    ''', (conquista,))

# Salvando as mudanças
conexao.commit()

# Recuperando conquistas do banco de dados
cursor.execute('SELECT * FROM conquistas')
todas_conquistas = cursor.fetchall()
print("\nSuas conquistas salvas no banco de dados são:")
for conquista in todas_conquistas:
    print(f"ID: {conquista[0]}, Descrição: {conquista[1]}")

# Fechando a conexão com o banco de dados
conexao.close()