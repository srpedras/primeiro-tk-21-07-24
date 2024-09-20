import sqlite3
import bcrypt

def criar_tabela_usuarios():
    """Cria a tabela de usuários no banco de dados SQLite."""
    conn = sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()

    # Cria a tabela com os campos: id (chave primária), nome de usuário e hash da senha
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash   
 TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def  inserir_usuario(username, password):
    """Insere um novo usuário no banco de dados."""
    conn = sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()

    # Hash da senha usando bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insere o usuário no banco de dados
    cursor.execute("INSERT INTO usuarios (username, password_hash) VALUES (?, ?)", (username, hashed_password))

    conn.commit()
    conn.close()

def verificar_credenciais(username, password):
    """Verifica se as credenciais do usuário estão corretas."""
    conn = sqlite3.connect('meu_banco.db')
    cursor = conn.cursor()

    # Busca o hash da senha do usuário
    cursor.execute("SELECT password_hash FROM usuarios WHERE username=?", (username,))
    resultado = cursor.fetchone()

    conn.close()

    if resultado is None:
        return False

    # Compara o hash fornecido com o hash armazenado
    return bcrypt.checkpw(password.encode('utf-8'), resultado[0])

# Cria a tabela de usuários (se ainda não existir)
criar_tabela_usuarios()

# Insere um novo usuário
inserir_usuario("alice", "minha_senha_forte")

# Verifica as credenciais
if verificar_credenciais("alice", "minha_senha_forte"):
    print("Autenticado!")
else:
    print("Acesso negado!")