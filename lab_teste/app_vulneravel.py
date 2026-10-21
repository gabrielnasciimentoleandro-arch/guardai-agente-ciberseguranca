#!/usr/bin/env python3
"""
EXEMPLO DE APLICAÇÃO VULNERÁVEL PARA TESTE DE LABORATÓRIO
USO APENAS EM AMBIENTE ISOLADO, NUNCA RODAR ISSO EM PRODUÇÃO.

Essa aplicação tem um login vulnerável a SQL Injection, para demonstração.
"""
import sqlite3

def criar_banco_teste():
    """Cria um banco de dados de teste com um usuário administrador."""
    conexao = sqlite3.connect("banco_teste.db")
    cursor = conexao.cursor()
    cursor.execute("DROP TABLE IF EXISTS usuarios")
    cursor.execute("""
        CREATE TABLE usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            nome TEXT NOT NULL,
            is_admin INTEGER DEFAULT 0
        )
    """)
    cursor.execute("INSERT INTO usuarios (email, senha, nome, is_admin) VALUES (?, ?, ?, ?)",
                   ("admin@laboratorio.local", "senha_segura_admin_123", "Administrador", 1))
    cursor.execute("INSERT INTO usuarios (email, senha, nome, is_admin) VALUES (?, ?, ?, ?)",
                   ("usuario@laboratorio.local", "senha_comum", "Usuário Comum", 0))
    conexao.commit()
    conexao.close()
    print("✅ Banco de dados de teste criado com 2 usuários.")

def login_vulneravel(email_digitado, senha_digitada):
    """
    ❌ EXEMPLO DE CÓDIGO VULNERÁVEL
    Monta a consulta SQL juntando strings diretamente, sem parametrizar.
    Isso permite SQL Injection.
    """
    conexao = sqlite3.connect("banco_teste.db")
    cursor = conexao.cursor()

    # ISSO AQUI É A FALHA: concatenação direta da entrada do usuário
    consulta = f"SELECT * FROM usuarios WHERE email = '{email_digitado}' AND senha = '{senha_digitada}'"
    print(f"\n🔍 Consulta executada: {consulta}")

    cursor.execute(consulta)
    usuario_encontrado = cursor.fetchone()
    conexao.close()
    return usuario_encontrado

if __name__ == "__main__":
    criar_banco_teste()

    print("\n" + "="*60)
    print("TESTE DE LOGIN VULNERÁVEL A SQL INJECTION")
    print("="*60)

    # Teste normal, com credencial correta
    print("\n1. Teste com credencial correta:")
    resultado = login_vulneravel("usuario@laboratorio.local", "senha_comum")
    if resultado:
        print(f"✅ Login bem sucedido! Usuário: {resultado[3]} (admin = {bool(resultado[4])})")
    else:
        print("❌ Login falhou")

    # Teste de ataque: SQL Injection para logar sem saber a senha
    print("\n2. Teste de SQL Injection (payload: ' OR '1'='1):")
    injection_payload = "' OR '1'='1"
    resultado = login_vulneravel("admin@laboratorio.local", injection_payload)
    if resultado:
        print(f"⚠️  ATAQUE SUCEDIDO! Logamos como: {resultado[3]} (admin = {bool(resultado[4])})")
        print("   Isso aconteceu porque a entrada foi concatenada diretamente na SQL.")
    else:
        print("Login falhou")
