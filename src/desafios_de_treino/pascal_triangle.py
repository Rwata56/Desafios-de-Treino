def nth_row_pascal(n):
    """
    Retorna a n-ésima linha (0-indexed) do Triângulo de Pascal.
    
    Args:
        n (int): O índice da linha (começando de 0)
    
    Returns:
        list: A n-ésima linha do Triângulo de Pascal
    
    Raises:
        ValueError: Se n for negativo
    """
    if n < 0:
        raise ValueError("n deve ser um número não negativo")
    
    if n == 0:
        return [1]
    
    row = [1]
    
    for i in range(1, n + 1):
        # Calcula a próxima linha baseada na atual
        next_row = [1]
        for j in range(1, i):
            next_row.append(row[j - 1] + row[j])
        next_row.append(1)
        row = next_row
    
    return row

def nth_row_pascal_optimized(n):
    """
    Versão otimizada usando fórmula de combinação C(n, k).
    
    Args:
        n (int): O índice da linha (começando de 0)
    
    Returns:
        list: A n-ésima linha do Triângulo de Pascal
    """
    if n < 0:
        raise ValueError("n deve ser um número não negativo")
    
    row = [1]
    value = 1
    
    for k in range(1, n + 1):
        value = value * (n - k + 1) // k
        row.append(value)
    
    return row

# Função principal para demonstração
if __name__ == "__main__":
    print("Triângulo de Pascal - Enésima Linha")
    print("=" * 40)
    
    try:
        n = int(input("Digite o valor de n (0-indexed): "))
        row = nth_row_pascal_optimized(n)
        print(f"Linha {n}: {row}")
        
        # Mostrar algumas linhas como exemplo
        print("\nPrimeiras 6 linhas do Triângulo de Pascal:")
        for i in range(6):
            print(f"Linha {i}: {nth_row_pascal_optimized(i)}")
            
    except ValueError as e:
        print(f"Erro: {e}")