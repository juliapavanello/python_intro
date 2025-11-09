def hash_imagem_horner(pixels, tamanho_tabela, d=257):
    """
    pixels: lista de 400 valores [0-255]
    tamanho_tabela: tamanho da tabela hash
    d: base usada no polinômio (geralmente um número primo)
    """
    h = 0
    for p in pixels:
        h = (h * d + p) % tamanho_tabela  # mantém o valor controlado
    return h
