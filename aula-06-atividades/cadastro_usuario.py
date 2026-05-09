# ============================================================
# 👤 CADASTRO E APROVAÇÃO DE USUÁRIO
# Aula 06 — Diagramas de Atividades
# Cada bloco = uma atividade do Diagrama de Atividades
# ============================================================

# ------------------------------------------------------------
# PARTE 1 — Exemplo da aula: Login com Google OAuth
# ------------------------------------------------------------
def processo_login_google(usuario_autorizou: bool, token_valido: bool) -> str:
    """
    Simula o fluxo do Diagrama de Atividades de Login com Google.
    Cada if = uma decisão (losango) do diagrama.
    """
    print("▶ Iniciando processo de login...")
    print("→ Redirecionando para Google Auth")

    # Decisão 1: Usuário autoriza? ◆
    if not usuario_autorizou:
        print("✗ Usuário não autorizou → Redirecionando com erro")
        return "ERRO: Acesso negado"

    print("→ Token de acesso recebido")

    # Decisão 2: Token válido? ◆
    if not token_valido:
        print("✗ Token inválido → Exibindo erro")
        return "ERRO: Token inválido"

    print("→ Sessão criada")
    print("→ Redirecionando ao dashboard")
    print("⊗ Processo concluído")
    return "SUCESSO: Login realizado"

print("=" * 45)
print("🔐 TESTE — Login com Google OAuth")
print("=" * 45)
print(processo_login_google(True, True))
print("---")
print(processo_login_google(True, False))
print("---")
print(processo_login_google(False, True))

# ------------------------------------------------------------
# PARTE 2 — Exercício: Cadastro e Aprovação de Usuário
# Swimlanes: Usuário | Sistema
# Decisões: [e-mail válido?] [já cadastrado?] [confirmou e-mail?]
# ------------------------------------------------------------
def cadastro_usuario(email: str, senha: str, email_ja_existe: bool, confirmou_email: bool) -> str:
    """
    Fluxo do Diagrama de Atividades — Cadastro de Usuário.

    SWIMLANE USUÁRIO: Preenche formulário, confirma e-mail
    SWIMLANE SISTEMA: Valida, verifica duplicidade, cria conta,
                      envia confirmação, libera ou expira acesso
    """
    # Nó inicial ●
    print("\n▶ Iniciando cadastro...")
    print(f"→ [Usuário] Preencheu formulário: {email}")

    # Decisão 1: E-mail válido? ◆
    email_valido = "@" in email and "." in email
    if not email_valido:
        print("✗ [Sistema] E-mail inválido → Exibe erro no formulário")
        print("⊗ Cadastro encerrado")
        return "ERRO: E-mail inválido"

    print("✓ [Sistema] E-mail válido")

    # Decisão 2: Já cadastrado? ◆
    if email_ja_existe:
        print("✗ [Sistema] E-mail já cadastrado → Sugere login ou recuperação")
        print("⊗ Cadastro encerrado")
        return "ERRO: E-mail já cadastrado"

    print("✓ [Sistema] E-mail disponível")
    print("→ [Sistema] Conta criada com sucesso")
    print(f"→ [Sistema] E-mail de confirmação enviado para {email}")

    # Decisão 3: Confirmou e-mail? ◆
    if not confirmou_email:
        print("✗ [Sistema] Confirmação não realizada → Cadastro expirado")
        print("⊗ Cadastro encerrado")
        return "ERRO: Confirmação não realizada — cadastro expirado"

    print("✓ [Sistema] E-mail confirmado → Acesso liberado!")
    print("→ [Sistema] Redirecionando para o dashboard")
    print("⊗ Processo concluído")
    return "SUCESSO: Usuário cadastrado e aprovado!"

# Testes
print("\n" + "=" * 45)
print("📋 TESTE — Cadastro e Aprovação de Usuário")
print("=" * 45)

print("\n[Teste 1] E-mail válido, novo, confirmado:")
print(cadastro_usuario("joao@email.com", "senha123", False, True))

print("\n[Teste 2] E-mail inválido:")
print(cadastro_usuario("email-invalido", "senha123", False, True))

print("\n[Teste 3] E-mail já cadastrado:")
print(cadastro_usuario("joao@email.com", "senha123", True, True))

print("\n[Teste 4] Não confirmou o e-mail:")
print(cadastro_usuario("maria@email.com", "senha456", False, False))
