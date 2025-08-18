from __future__ import annotations
from typing import List, Tuple


class SignalTowers:
    def __init__(self, towers: List[Tuple[int, int]]) -> None:
        """
        towers: lista de torres (xi, ki)
        xi = posição da torre
        ki = coeficiente de força inicial
        """
        self.towers: List[Tuple[int, int]] = sorted(towers)

    def max_redundant(self) -> int:
        """
        Retorna o número máximo de torres que podem ser desligadas
        sem alterar o sinal recebido em nenhum ponto da reta.
        """

        n: int = len(self.towers)
        if n <= 2:
            return 0  # com 2 ou menos torres, nenhuma é redundante

        # Estratégia:
        # - O sinal é dado por: S(x) = 1 / (|x - xi| + ki)
        # - Torre i é redundante se, em todos os pontos x,
        #   existir outra torre com sinal >= Si(x).
        # - Isso equivale a analisar o "envelope superior" das funções.
        # Aqui, simplificação:
        # Usamos um "convex hull" sobre curvas (xi, ki).
        # A torre é útil apenas se define um limite visível.

        # Para eficiência, fazemos varredura da esquerda para direita
        keep: List[Tuple[int, int]] = []

        for tower in self.towers:
            while len(keep) >= 2 and self._is_redundant(keep[-2], keep[-1], tower):
                keep.pop()
            keep.append(tower)

        return n - len(keep)

    def _is_redundant(
        self, a: Tuple[int, int], b: Tuple[int, int], c: Tuple[int, int]
    ) -> bool:
        """
        Verifica se a torre b é redundante entre a e c.
        Ideia: se b nunca fornece sinal maior que a ou c, é redundante.
        """
        (xa, ka), (xb, kb), (xc, kc) = a, b, c

        # Aqui usamos a ideia de "convexidade":
        # condição derivada comparando pontos médios
        return (xb - xa) * (kc - kb) >= (xc - xb) * (kb - ka)
