# ============================================================
# 🏛️ SISTEMA DE BIBLIOTECA DIGITAL — Biblioteca FIAP
# Aula 05 — UML e Diagramas de Casos de Uso
# Cada seção = um Caso de Uso do diagrama UML
# ============================================================

# ----------------------------
# 🗂️ DADOS DO SISTEMA
# (imagine como o "banco de dados" por enquanto)
# ----------------------------
catalogo = [
    {"titulo": "Clean Code",              "autor": "Robert C. Martin", "disponivel": True},
    {"titulo": "The Pragmatic Programmer","autor": "Hunt & Thomas",    "disponivel": True},
    {"titulo": "Design Patterns",         "autor": "Gang of Four",     "disponivel": True},
]
emprestimos = []  # lista de {"leitor": ..., "livro": ...}

# ============================================================
# UC-01: LISTAR CATÁLOGO
# Ator: Leitor
# ============================================================
print("📚 Catálogo disponível:")
for livro in catalogo:
    status = "✅" if livro["disponivel"] else "❌"
    print(f"  {status} {livro['titulo']} — {livro['autor']}")

# ============================================================
# UC-02: BUSCAR LIVRO
# Ator: Leitor
# Pré-condição: catálogo não vazio
# ============================================================
print("\n🔍 Buscando livro...")
busca = "clean"  # o leitor digitou isso

resultados = [livro for livro in catalogo if busca.lower() in livro["titulo"].lower()]
if resultados:
    for livro in resultados:
        status = "✅" if livro["disponivel"] else "❌"
        print(f"  {status} Encontrado: {livro['titulo']} — {livro['autor']}")
else:
    print(f"  ❌ Nenhum livro encontrado com '{busca}'")

# ============================================================
# UC-03: EMPRESTAR LIVRO
# Ator: Leitor
# <<include>> UC-04 Verificar Disponibilidade (sempre acontece)
# ============================================================
print("\n📖 Empréstimo:")
leitor = "Ana Silva"
titulo = "Clean Code"

# <<include>> — verificar disponibilidade (sempre acontece)
livro_encontrado = None
for livro in catalogo:
    if livro["titulo"] == titulo:
        livro_encontrado = livro
        break

if livro_encontrado is None:
    print("  ❌ Livro não encontrado no catálogo.")
elif livro_encontrado["disponivel"] == False:
    # Fluxo de exceção
    print(f"  ⚠️  '{titulo}' já está emprestado!")
else:
    # Fluxo principal
    livro_encontrado["disponivel"] = False
    emprestimos.append({"leitor": leitor, "livro": titulo})
    print(f"  ✅ '{titulo}' emprestado para {leitor}!")

# ============================================================
# UC-04: DEVOLVER LIVRO
# Ator: Leitor
# <<extend>> UC-05 Aplicar Multa (só se atrasado)
# ============================================================
print("\n📬 Devolução:")
leitor_devolvendo = "Ana Silva"
titulo_devolvendo = "Clean Code"

# Passo 1: Procura na lista de empréstimos
registro = None
for emp in emprestimos:
    if emp["leitor"] == leitor_devolvendo and emp["livro"] == titulo_devolvendo:
        registro = emp
        break

if registro is None:
    print(f"  ❌ Nenhum empréstimo encontrado para '{titulo_devolvendo}' em nome de {leitor_devolvendo}.")
else:
    # Passo 2: Marca livro como disponível e remove o registro
    for livro in catalogo:
        if livro["titulo"] == titulo_devolvendo:
            livro["disponivel"] = True
            break
    emprestimos.remove(registro)
    print(f"  ✅ '{titulo_devolvendo}' devolvido por {leitor_devolvendo}!")

    # <<extend>>: Aplicar Multa (só acontece se houve atraso)
    houve_atraso = False  # mude para True para testar o fluxo de multa
    if houve_atraso:
        print("  💰 Multa aplicada por atraso na devolução!")

# ============================================================
# 🔎 ESTADO FINAL — confira o resultado
# ============================================================
print("\n📋 Catálogo após operações:")
for livro in catalogo:
    status = "✅" if livro["disponivel"] else "❌"
    print(f"  {status} {livro['titulo']}")
print(f"\n📌 Empréstimos ativos: {emprestimos}")

# ============================================================
# 🚀 DESAFIO EXTRA — versão OOP
# Cada classe representa uma entidade do diagrama UML
# ============================================================
print("\n" + "="*50)
print("🚀 VERSÃO OOP — Biblioteca com Classes")
print("="*50)

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __repr__(self):
        status = "✅" if self.disponivel else "❌"
        return f"[{status}] {self.titulo} — {self.autor}"

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.emprestimos = {}  # { nome_leitor: [livros] }

    # UC-01: Cadastrar Livro
    def cadastrar(self, titulo, autor):
        self.catalogo.append(Livro(titulo, autor))
        print(f"  📚 '{titulo}' cadastrado!")

    # UC-02: Listar Catálogo
    def listar(self):
        print("\n  📋 Catálogo:")
        for livro in self.catalogo:
            print(f"    {livro}")

    # UC-03: Emprestar Livro
    def emprestar(self, titulo, leitor):
        for livro in self.catalogo:
            if livro.titulo == titulo:
                if livro.disponivel:
                    livro.disponivel = False
                    self.emprestimos.setdefault(leitor, []).append(titulo)
                    print(f"  ✅ '{titulo}' emprestado para {leitor}!")
                else:
                    print(f"  ⚠️  '{titulo}' já está emprestado!")
                return
        print(f"  ❌ '{titulo}' não encontrado.")

    # UC-04: Devolver Livro
    def devolver(self, titulo, leitor):
        if leitor in self.emprestimos and titulo in self.emprestimos[leitor]:
            for livro in self.catalogo:
                if livro.titulo == titulo:
                    livro.disponivel = True
                    break
            self.emprestimos[leitor].remove(titulo)
            print(f"  ✅ '{titulo}' devolvido por {leitor}!")
        else:
            print(f"  ❌ Empréstimo não encontrado para '{titulo}' em nome de {leitor}.")

# --- Teste da versão OOP ---
bib = Biblioteca()
bib.cadastrar("Clean Code", "Robert C. Martin")
bib.cadastrar("Design Patterns", "Gang of Four")
bib.listar()
bib.emprestar("Clean Code", "Ana Silva")
bib.listar()
bib.devolver("Clean Code", "Ana Silva")
bib.listar()
