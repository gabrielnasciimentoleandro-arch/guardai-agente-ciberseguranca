#!/usr/bin/env python3
"""
EXEMPLO DE APLICAÇÃO CORRIGIDA
Usa consulta parametrizada para mitigar o SQL Injection completamente.
"""
import sqlite3
from app_vulneravel import criar_banco_teste

def login_seguro(email_digitado, senha_digitada):
    """
    ✅ CÓDIGO SEGURO
    Usa consulta parametrizada: o banco de dados trata a entrada como dado,
    nunca como código SQL, então injection não funciona.
    """
    conexao = sqlite3.connect("banco_teste.db")
    cursor = conexao.cursor()

    # NÃO concatenamos strings: usamos placeholders ? e passamos valores como tupla
    consulta = "SELECT * FROM usuarios WHERE email = ? AND senha = ?"
    print(f"\n🔍 Consulta executada: {consulta}")
    print(f"   Valores recebidos: ({email_digitado}, {senha_digitada})")

    cursor.execute(consulta, (email_digitado, senha_digitada))
    usuario_encontrado = cursor.fetchone()
    conexao.close()
    return usuario_encontrado

if __name__ == "__main__":
    criar_banco_teste()

    print("\n" + "="*60)
    print("TESTE DE LOGIN SEGURO - SQL INJECTION MITIGADO")
    print("="*60)

    # Teste normal, com credencial correta
    print("\n1. Teste com credencial correta:")
    resultado = login_seguro("usuario@laboratorio.local", "senha_comum")
    if resultado:
        print(f"✅ Login bem sucedido! Usuário: {resultado[3]} (admin = {bool(resultado[4])})")
    else:
        print("❌ Login falhou")

    # Tentativa de ataque: SQL Injection
    print("\n2. Tentativa de SQL Injection com o mesmo payload:")
    injection_payload = "' OR '1'='1"
    resultado = login_seguro("admin@laboratorio.local", injection_payload)
    if resultado:
        print(f"⚠️  Ainda vulnerável! Usuário: {resultado[3]}")
    else:
        print("✅ ATAQUE BLOQUEADO! O payload é tratado só como texto de senha, não como SQL.")
        print("   Nenhum login é feito sem a senha correta.")
