# ============================================================
# 🎬 SISTEMA DE STREAMING — tipo Netflix/Prime
# Aula 08 — Diagramas de Classes · FIAP
# Cada classe = uma entidade do Diagrama de Classes UML
# Relacionamentos: Associação →  Agregação ◇  Composição ◆
# ============================================================

class Filme:
    def __init__(self, titulo: str, duracao: int, genero: str):
        self.titulo   = titulo    # - privado
        self.duracao  = duracao   # - privado (em minutos)
        self.genero   = genero    # - privado

    def __repr__(self):
        return f" {self.titulo} ({self.duracao}min | {self.genero})"


class Avaliacao:
    def __init__(self, nota: float, comentario: str):
        self.nota       = nota        # - privado
        self.comentario = comentario  # - privado

    def __repr__(self):
        return f" {self.nota}/10 — \"{self.comentario}\""


class Catalogo:
    def __init__(self, titulo: str, qtd_filmes: int):
        self.titulo     = titulo
        self.qtd_filmes = qtd_filmes
        self._filmes: list[Filme] = []   # composição: criados internamente

    def add_filme(self, filme: Filme):
        self._filmes.append(filme)
        self.qtd_filmes = len(self._filmes)
        print(f"   Filme '{filme.titulo}' adicionado ao catálogo '{self.titulo}'")

    def listar_filmes(self):
        print(f"\n Catálogo: {self.titulo} ({self.qtd_filmes} filmes)")
        for filme in self._filmes:
            print(f"  {filme}")


class Usuario:
    def __init__(self, nome: str, email: str, plano: str):
        self.nome   = nome    # - privado
        self.email  = email   # - privado
        self.plano  = plano   # - privado
        self._avaliacoes: list[dict] = []

    def avaliar(self, filme: Filme, avaliacao: Avaliacao):
        self._avaliacoes.append({"filme": filme, "avaliacao": avaliacao})
        print(f"   {self.nome} avaliou '{filme.titulo}': {avaliacao}")

    def ver_avaliacoes(self):
        print(f"\n Avaliações de {self.nome}:")
        for item in self._avaliacoes:
            print(f"  {item['filme'].titulo} → {item['avaliacao']}")


class Plataforma:
    def __init__(self, nome: str, pais: str):
        self.nome  = nome
        self.pais  = pais
        self._catalogos: list[Catalogo] = []

    def add_catalogo(self, catalogo: Catalogo):
        self._catalogos.append(catalogo)
        print(f"   Catálogo '{catalogo.titulo}' vinculado à plataforma '{self.nome}'")

    def info(self):
        print(f"\n Plataforma: {self.nome} ({self.pais})")
        print(f"   Catálogos: {len(self._catalogos)}")



print("=" * 50)
print(" SISTEMA DE STREAMING — FIAP 2026")
print("=" * 50)


netflix = Plataforma("Netflix", "EUA")


catalogo = Catalogo("Filmes em Destaque", 0)


filme1 = Filme("Oppenheimer", 180, "Drama")
filme2 = Filme("Barbie", 114, "Comédia")


print("\n Adicionando filmes ao catálogo:")
catalogo.add_filme(filme1)
catalogo.add_filme(filme2)


print("\n Vinculando catálogo à plataforma:")
netflix.add_catalogo(catalogo)
netflix.info()


usuario = Usuario("Ana", "ana@email.com", "Premium")


print("\n Avaliações:")
avaliacao = Avaliacao(9.5, "Incrível! Assisti duas vezes")
usuario.avaliar(filme1, avaliacao)


catalogo.listar_filmes()


usuario.ver_avaliacoes()

print("\n Sistema funcionando corretamente!")
