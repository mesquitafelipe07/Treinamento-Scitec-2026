## Desafio:
# Crie uma lista chamada valores_brutos com os números: [10, 50, 150, 20, 300]
# Crie uma função com Type Hints que percorra essa lista
# Se o valor for maior que 100, coloque-o em uma nova lista chamada alertas
# No final, use um if para printar: "Sistema Seguro" (se não houver alertas) ou "⚠️ Revisar valores: {lista}" (se houver)

from typing import List # Tipo de variável List (lista) importado para Type Hint correto

valores_brutos: List[int] = [10, 50, 150, 20, 300]

def verificar_segurança(lista: List[int]) -> None: # o "-> None" indica que não há um tipo de variável a ser retornada pela função
    alertas: List[int] = []

    for valor in lista:
        if valor > 100:
            alertas.append(valor) # aprendi em Algoritmos em Bioinformática

    if not alertas: # not alertas -> alertas está vazio
        print("Sistema Seguro")
    else:
        print(f"⚠️ Revisar valores: {lista}")

verificar_segurança(valores_brutos)