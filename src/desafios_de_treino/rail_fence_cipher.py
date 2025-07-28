def encode(message: str, rails: int) -> str:
    if rails == 1:
        return message

    # Cria listas vazias para cada trilho
    fence = ["" for _ in range(rails)]
    rail = 0
    direction = 1

    for char in message:
        fence[rail] += char
        rail += direction

        # Inverta a direção se chegarmos ao topo ou à base
        if rail == 0 or rail == rails - 1:
            direction *= -1

    #     Rail 0: HOR
    #     Rail 1: ELWLD
    #     Rail 2: LO

    # exemplo:"HOR" + "ELWLD" + "LO" = "HORELWLDLO"

    return "".join(fence)


def decode(cipher: str, rails: int) -> str:
    if rails == 1:
        return cipher

    # Passo 1: Criar o padrão de trilhos
    pattern: list[int] = []
    # exemplo esperado [0, 1, 2, 1, 0, 1, 2, 1, 0, 1]
    rail = 0
    direction = 1
    for _ in cipher:
        pattern.append(rail)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Passo 2: Contar quantas letras vão para cada trilho
    rail_counts = [pattern.count(r) for r in range(rails)]

    # exemplo rail_counts = [0,1,2] [3, 5, 2]

    # Passo 3: Preencher os trilhos com as letras do cipher
    pos = 0
    rails_data: list[list[str]] = []
    for count in rail_counts:
        rails_data.append(list(cipher[pos : pos + count]))

        # exemplo list("HOR") → ["H", "O", "R"]

        pos += count

        # final rails_data = [ ["H", "O", "R"], ["E", "L", "W", "L", "D"], ["L", "O"] ]

    # Passo 4: Reconstruir a mensagem original
    result: list[str] = []
    rail_indices = [0] * rails
    for r in pattern:
        result.append(rails_data[r][rail_indices[r]])
        rail_indices[r] += 1

    #    result.append(rails_data[0][0])   Adiciona 'H'
    #    rail_indices[0] += 1

    #    result = ['H']
    #    rail_indices = [1, 0, 0]

    #   result.append(rails_data[1][0])  Adiciona 'E'
    #   rail_indices[1] += 1  Trilho 1 vai para o índice 1

    #   result = ['H', 'E']
    #   rail_indices = [1, 1, 0]

    #   ordem r[0, 1, 2, 1, 0, 1, 2, 1, 0, 1]

    return "".join(result)
