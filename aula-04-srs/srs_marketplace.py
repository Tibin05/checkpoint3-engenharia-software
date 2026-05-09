# ============================================================
# SRS em Python — Aula 04 — Engenharia de Software · FIAP
# Missão: Construir o SRS do "FIAP Marketplace"
# ============================================================
from dataclasses import dataclass, field
from typing import List
from enum import Enum

class Prioridade(Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"

@dataclass
class RequisitoFuncional:
    id: str
    nome: str
    descricao: str
    prioridade: Prioridade
    ator: str
    pre_condicao: str
    pos_condicao: str

@dataclass
class RequisitoNaoFuncional:
    id: str
    categoria: str
    descricao: str
    criterio_aceitacao: str

@dataclass
class SRS:
    projeto: str
    versao: str
    descricao: str
    requisitos_funcionais: List[RequisitoFuncional] = field(default_factory=list)
    requisitos_nao_funcionais: List[RequisitoNaoFuncional] = field(default_factory=list)

    def adicionar_rf(self, req: RequisitoFuncional):
        self.requisitos_funcionais.append(req)
        print(f"✅ RF '{req.id}' adicionado!")

    def adicionar_rnf(self, req: RequisitoNaoFuncional):
        self.requisitos_nao_funcionais.append(req)
        print(f"✅ RNF '{req.id}' adicionado!")

    def relatorio(self):
        print(f"\n{'='*55}")
        print(f"📋 SRS — {self.projeto} v{self.versao}")
        print(f"{'='*55}")
        print(f"📌 {self.descricao}\n")

        print(f"✅ REQUISITOS FUNCIONAIS ({len(self.requisitos_funcionais)})")
        for rf in self.requisitos_funcionais:
            print(f"  [{rf.id}] {rf.nome} — Prioridade: {rf.prioridade.value}")
            print(f"       Ator: {rf.ator}")
            print(f"       📝 {rf.descricao}\n")

        print(f"⚡ REQUISITOS NÃO-FUNCIONAIS ({len(self.requisitos_nao_funcionais)})")
        for rnf in self.requisitos_nao_funcionais:
            print(f"  [{rnf.id}] {rnf.categoria}")
            print(f"       📝 {rnf.descricao}")
            print(f"       ✔  Critério: {rnf.criterio_aceitacao}\n")

# -------------------------------------------------------
# PARTE 1 — Criando o SRS do FIAP Marketplace
# -------------------------------------------------------
srs = SRS(
    projeto="FIAP Marketplace",
    versao="1.0",
    descricao="Marketplace interno onde alunos podem vender produtos artesanais entre si."
)

# --- REQUISITOS FUNCIONAIS ---

# RF-001: Cadastro de Produto
srs.adicionar_rf(RequisitoFuncional(
    id="RF-001",
    nome="Cadastro de Produto",
    descricao="O sistema deve permitir que o vendedor cadastre produtos com nome, descrição, preço e até 5 fotos.",
    prioridade=Prioridade.ALTA,
    ator="Vendedor (Aluno)",
    pre_condicao="Usuário autenticado com perfil de vendedor ativo",
    pos_condicao="Produto salvo e visível na vitrine do marketplace"
))

# RF-002: Busca por Categoria
srs.adicionar_rf(RequisitoFuncional(
    id="RF-002",
    nome="Busca por Categoria",
    descricao="O sistema deve permitir filtrar produtos por categoria (ex: artesanato, comida, tecnologia) em menos de 2 segundos.",
    prioridade=Prioridade.ALTA,
    ator="Comprador (Aluno)",
    pre_condicao="Usuário autenticado na plataforma",
    pos_condicao="Lista de produtos filtrada exibida em ordem de relevância"
))

# RF-003: Checkout e Pagamento
srs.adicionar_rf(RequisitoFuncional(
    id="RF-003",
    nome="Checkout e Pagamento",
    descricao="O sistema deve processar o pagamento via PIX ou cartão, confirmando a compra em até 10 segundos.",
    prioridade=Prioridade.ALTA,
    ator="Comprador (Aluno)",
    pre_condicao="Carrinho com pelo menos 1 item e usuário autenticado",
    pos_condicao="Pedido criado, vendedor notificado e comprovante enviado ao comprador"
))

# --- REQUISITOS NÃO-FUNCIONAIS ---

# RNF-001: Disponibilidade
srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-001",
    categoria="Disponibilidade",
    descricao="O sistema deve estar disponível 99,9% do tempo em regime mensal (máx. 43,8 min de downtime/mês).",
    criterio_aceitacao="Monitoramento via AWS CloudWatch com alertas automáticos e relatório mensal de uptime"
))

# RNF-002: Conformidade com LGPD
srs.adicionar_rnf(RequisitoNaoFuncional(
    id="RNF-002",
    categoria="Segurança / LGPD",
    descricao="Todos os dados pessoais dos alunos devem ser armazenados e tratados conforme a Lei nº 13.709/2018 (LGPD).",
    criterio_aceitacao="Auditoria de segurança semestral e criptografia AES-256 nos dados sensíveis"
))

# Exibe o relatório completo
srs.relatorio()

# -------------------------------------------------------
# PARTE 2 — Função de validação de requisitos (análise crítica)
# -------------------------------------------------------
def validar_requisito(rf: RequisitoFuncional) -> dict:
    """
    Valida se um requisito funcional segue as boas práticas SMART.
    Retorna um dict com os resultados da validação.
    """
    resultados = {}

    # Dica 1: descrição com mais de 20 caracteres (evitar requisitos vagos)
    resultados["descricao_suficiente"] = len(rf.descricao) > 20

    # Dica 2: pré-condição definida (não vazia)
    resultados["pre_condicao_definida"] = rf.pre_condicao != ""

    # Dica 3: critério mensurável (checar se tem números na descrição)
    resultados["criterio_mensuravel"] = any(char.isdigit() for char in rf.descricao)

    return resultados

# Validando os requisitos criados
print("\n" + "="*55)
print("🔍 VALIDAÇÃO DOS REQUISITOS")
print("="*55)
for rf in srs.requisitos_funcionais:
    resultado = validar_requisito(rf)
    print(f"\n[{rf.id}] {rf.nome}")
    print(f"  Descrição suficiente (>20 chars): {'✅' if resultado['descricao_suficiente'] else '❌'}")
    print(f"  Pré-condição definida:            {'✅' if resultado['pre_condicao_definida'] else '❌'}")
    print(f"  Critério mensurável (tem número): {'✅' if resultado['criterio_mensuravel'] else '❌'}")
