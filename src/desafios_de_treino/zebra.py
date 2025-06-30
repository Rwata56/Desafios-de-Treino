from typing import Any
from constraint import Problem, AllDifferentConstraint


def solve_zebra_puzzle() -> dict[int, dict[Any, Any]]:
    problem = Problem()

    nacionalidades = ["inglês", "espanhol", "ucraniano", "norueguês", "japonês"]
    cores = ["vermelha", "verde", "branca", "amarela", "azul"]
    bebidas = ["café", "chá", "leite", "suco de laranja", "água"]
    cigarros = ["Kool", "Chesterfield", "Winston", "Lucky Strike", "Parliament"]
    animais = ["cachorro", "raposa", "cavalo", "caramujo", "zebra"]

    casas = range(1, 6)

    for var in nacionalidades + cores + bebidas + cigarros + animais:
        problem.addVariable(var, casas)

    problem.addConstraint(AllDifferentConstraint(), nacionalidades)
    problem.addConstraint(AllDifferentConstraint(), cores)
    problem.addConstraint(AllDifferentConstraint(), bebidas)
    problem.addConstraint(AllDifferentConstraint(), cigarros)
    problem.addConstraint(AllDifferentConstraint(), animais)

    # 1. O inglês vive na casa vermelha
    problem.addConstraint(lambda e, r: e == r, ("inglês", "vermelha"))
    # 2. O espanhol tem um cachorro
    problem.addConstraint(lambda s, d: s == d, ("espanhol", "cachorro"))
    # 3. O japonês é pintor (não afeta diretamente)
    # 4. O ucraniano bebe chá
    problem.addConstraint(lambda u, t: u == t, ("ucraniano", "chá"))
    # 5. O norueguês vive na primeira casa
    problem.addConstraint(lambda n: n == 1, ("norueguês",))
    # 6. O dono da casa verde bebe café
    problem.addConstraint(lambda g, c: g == c, ("verde", "café"))
    # 7. A casa verde está imediatamente à direita da casa branca
    problem.addConstraint(lambda g, w: g == w + 1, ("verde", "branca"))
    # 8. O fumante de Winston cria caramujos
    problem.addConstraint(lambda w, s: w == s, ("Winston", "caramujo"))
    # 9. O fumante de Kool vive na casa amarela
    problem.addConstraint(lambda k, y: k == y, ("Kool", "amarela"))
    # 10. O homem que bebe leite vive na casa do meio
    problem.addConstraint(lambda m: m == 3, ("leite",))
    # 11. O norueguês vive ao lado da casa azul
    problem.addConstraint(lambda n, b: abs(n - b) == 1, ("norueguês", "azul"))
    # 12. O fumante de Chesterfield vive ao lado da raposa
    problem.addConstraint(lambda ch, f: abs(ch - f) == 1, ("Chesterfield", "raposa"))
    # 13. O fumante de Kool vive ao lado do cavalo
    problem.addConstraint(lambda k, h: abs(k - h) == 1, ("Kool", "cavalo"))
    # 14. O fumante de Lucky Strike bebe suco de laranja
    problem.addConstraint(lambda l, j: l == j, ("Lucky Strike", "suco de laranja"))
    # 15. O japonês fuma Parliament (RESTRIÇÃO CRUCIAL ADICIONADA)
    problem.addConstraint(lambda j, p: j == p, ("japonês", "Parliament"))

    # Obtendo a solução
    solucao = problem.getSolution()

    # Invertendo o mapeamento para organizar por casa
    casas_solucao = {casa: {} for casa in casas}
    for var, casa in solucao.items():
        casas_solucao[casa][var] = True

    return casas_solucao


def zebra_owner():
    solucao = solve_zebra_puzzle()
    for casa, atributos in solucao.items():
        if "zebra" in atributos:
            for nacionalidade in [
                "inglês",
                "espanhol",
                "ucraniano",
                "norueguês",
                "japonês",
            ]:
                if nacionalidade in atributos:
                    return nacionalidade
    return None


def water_drinker():
    solucao = solve_zebra_puzzle()
    for casa, atributos in solucao.items():
        if "água" in atributos:
            for nacionalidade in [
                "inglês",
                "espanhol",
                "ucraniano",
                "norueguês",
                "japonês",
            ]:
                if nacionalidade in atributos:
                    return nacionalidade
    return None
