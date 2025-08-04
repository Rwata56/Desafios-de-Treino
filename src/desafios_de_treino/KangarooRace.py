class KangarooRace:
    """Classe para resolver o problema dos cangurus saltadores."""

    def __init__(self, kanga1: int, rate1: int, kanga2: int, rate2: int) -> None:
        """
        Inicializa a corrida de cangurus.

        Args:
            kanga1: Posição inicial do primeiro canguru
            rate1: Velocidade do primeiro canguru (saltos/etapa)
            kanga2: Posição inicial do segundo canguru
            rate2: Velocidade do segundo canguru (saltos/etapa)
        """
        self.kanga1_pos: int = kanga1
        self.rate1: int = rate1
        self.kanga2_pos: int = kanga2
        self.rate2: int = rate2

    def will_meet(self) -> bool:
        """
        Determina se os cangurus se encontrarão no mesmo ponto ao mesmo tempo.

        Returns:
            True se os cangurus se encontrarem, False caso contrário
        """
        # Caso especial: já estão na mesma posição inicial
        if self.kanga1_pos == self.kanga2_pos:
            return True

        # Caso especial: mesma velocidade mas posições diferentes
        if self.rate1 == self.rate2:
            return False

        # Calcula o tempo necessário para se encontrarem
        time_to_meet: float = (self.kanga2_pos - self.kanga1_pos) / (
            self.rate1 - self.rate2
        )

        # Verifica se o tempo é positivo e inteiro (número de saltos)
        return time_to_meet > 0 and time_to_meet.is_integer()


def kangaroo(kanga1: int, rate1: int, kanga2: int, rate2: int) -> bool:
    """Função principal para verificar se os cangurus se encontram."""
    return KangarooRace(kanga1, rate1, kanga2, rate2).will_meet()
