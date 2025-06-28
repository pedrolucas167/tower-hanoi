from typing import List, Tuple

def hanoi(n: int, origem: str, destino: str, auxiliar: str) -> List[Tuple[int, str, str]]:
    movimentos = []

    def resolver(discos: int, de: str, para: str, via: str):
        if discos == 1:
            movimentos.append((1, de, para))
        else:
            resolver(discos - 1, de, via, para)
            movimentos.append((discos, de, para))
            resolver(discos - 1, via, para, de)

    resolver(n, origem, destino, auxiliar)
    return movimentos


if __name__ == "__main__":
    resultado = hanoi(3, 'A', 'C', 'B')
    for disco, origem, destino in resultado:
        print(f"Mova o disco {disco} de {origem} para {destino}")
