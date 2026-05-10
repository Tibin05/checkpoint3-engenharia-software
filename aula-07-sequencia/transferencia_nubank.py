# ============================================================
# 💜 TRANSFERÊNCIA NUBANK — Diagrama de Sequência
# Aula 07 — Diagramas de Sequência · FIAP
# Cada classe = um participante do diagrama
# Cada método = uma mensagem trocada entre participantes
# ============================================================

# ============================================================
# Célula 1 — BancoDeDados (Participante 4)
# ============================================================
class BancoDeDados:
    def __init__(self):
        # Dicionário de saldos — simula o banco de dados
        self.saldos = {
            "user_123": 500.0
        }

    def verificar_saldo(self, user_id: str) -> float:
        # Retorna o saldo do usuário (0.0 se não encontrado)
        return self.saldos.get(user_id, 0.0)

    def debitar(self, user_id: str, valor: float) -> bool:
        # [alt] saldo suficiente → debita e retorna True
        # [else] saldo insuficiente → retorna False
        saldo_atual = self.verificar_saldo(user_id)
        if saldo_atual >= valor:
            self.saldos[user_id] = saldo_atual - valor
            return True
        return False

# ============================================================
# Célula 2 — ServidorNubank (Participante 3)
# ============================================================
class ServidorNubank:
    def __init__(self):
        self.banco = BancoDeDados()

    def processar_transferencia(self, user_id: str, valor: float) -> dict:
        # Verifica saldo no banco de dados
        saldo_atual = self.banco.verificar_saldo(user_id)

        # Fragmento [alt] do diagrama de sequência:
        # [alt] saldo suficiente
        if self.banco.debitar(user_id, valor):
            saldo_restante = self.banco.verificar_saldo(user_id)
            return {"status": "aprovado", "saldo_restante": saldo_restante}
        # [else] saldo insuficiente
        else:
            return {"status": "recusado", "motivo": "saldo insuficiente"}

# ============================================================
# Célula 3 — AppNubank (Participante 2)
# ============================================================
class AppNubank:
    def __init__(self):
        self.servidor = ServidorNubank()

    def transferir(self, user_id: str, valor: float):
        # Usuário → App: solicita transferência
        print(f"[APP] Iniciando transferência de R$ {valor:.2f}...")

        # App → Servidor: processa transferência
        resultado = self.servidor.processar_transferencia(user_id, valor)

        # Servidor → App: retorna resultado (fragmento [alt])
        if resultado["status"] == "aprovado":
            print(f"[APP] ✅ Transferência aprovada! Saldo: R$ {resultado['saldo_restante']:.2f}")
        else:
            print(f"[APP] ❌ Transferência recusada: {resultado['motivo']}")

# ============================================================
# Célula 4 — Testes (não altere, apenas execute)
# ============================================================
app = AppNubank()

print("=== Teste 1: Transferência dentro do saldo ===")
app.transferir("user_123", 200.0)   # Esperado: aprovado

print("\n=== Teste 2: Transferência acima do saldo ===")
app.transferir("user_123", 500.0)   # Esperado: recusado

print("\n=== Teste 3: Múltiplas transferências ===")
app.transferir("user_123", 100.0)   # Esperado: aprovado (saldo agora 200)
app.transferir("user_123", 250.0)   # Esperado: recusado (saldo insuficiente)
