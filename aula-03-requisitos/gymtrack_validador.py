import time

print("🏋️ GymTrack — Validador de Treino")
print("=" * 40)

# --- DADOS DO TREINO (mude os valores para testar!) ---
exercicio = "Supino Reto"
peso_kg = 80
repeticoes = 10

# -------------------------------------------------------
# PARTE 1 — Classificação de Requisitos
# RF01: O sistema deve validar o nome do exercício
# RF02: O sistema deve validar o peso entre 1 e 300 kg
# RF03: O sistema deve validar as repetições entre 1 e 50
# RNF01: O registro deve ocorrer em menos de 200ms
# RNF02: O sistema deve rejeitar entradas vazias com mensagem clara
# RNF03: O sistema deve suportar ao menos 1000 registros simultâneos sem travar
# -------------------------------------------------------

# -------------------------------------------------------
# PARTE 2 — Código Python
# -------------------------------------------------------

# RF01 — O sistema deve validar o nome do exercício
# (não pode ser vazio)
if exercicio != "":
    print(f"✅ [RF01] Exercício válido: {exercicio}")
else:
    print(f"❌ [RF01] Exercício inválido: nome não pode ser vazio")

# RF02 — O peso deve estar entre 1 e 300 kg
if 1 <= peso_kg <= 300:
    print(f"✅ [RF02] Peso válido: {peso_kg}kg")
else:
    print(f"❌ [RF02] Peso inválido: {peso_kg}kg — deve estar entre 1 e 300kg")

# RF03 — As repetições devem estar entre 1 e 50
if 1 <= repeticoes <= 50:
    print(f"✅ [RF03] Repetições válidas: {repeticoes}")
else:
    print(f"❌ [RF03] Repetições inválidas: {repeticoes} — deve estar entre 1 e 50")

# RNF01 — O registro deve ocorrer em menos de 200ms
inicio = time.time()
# Simula o registro no banco de dados
time.sleep(0.05)
print(f"✅ Série registrada: {exercicio} | {peso_kg}kg x {repeticoes} reps")
fim = time.time()
tempo_ms = (fim - inicio) * 1000
if tempo_ms < 200:
    print(f"✅ [RNF01] Tempo de registro: {tempo_ms:.0f}ms ← dentro do limite!")
else:
    print(f"❌ [RNF01] Lento demais: {tempo_ms:.0f}ms ← limite é 200ms")

# -------------------------------------------------------
# PARTE 3 — Reflexão
# -------------------------------------------------------

# REFLEXÃO:
# 1. Qual a diferença entre RF e RNF que você percebeu na prática?
#    RF define O QUE o sistema faz (validar nome, peso, repetições).
#    RNF define COMO ele se comporta (velocidade < 200ms, mensagens claras).
#    Na prática, os RF são testáveis pela interface; os RNF exigem medição e monitoramento.

# 2. O que aconteceria se esquecêssemos o RNF de performance?
#    O sistema funcionaria corretamente, mas poderia travar ou ficar lento em uso real,
#    prejudicando a experiência do usuário — especialmente em academias com muitos alunos
#    registrando treinos ao mesmo tempo.

# 3. Cite 1 RNF que o GymTrack deveria ter mas que você não implementou:
#    RNF de Segurança: os dados do usuário (nome, histórico de treino) devem ser
#    armazenados com criptografia AES-256, garantindo privacidade mesmo em caso de
#    vazamento do banco de dados.
