from typing import List

from src.database import connect_to_database
from src.database.modules.level.repositories.level_repository import LevelRepository
from src.database.modules.level.dtos.create_level_dto import CreateLevelDto
from src.database.modules.user.entities.user_entity import UserEntity

PERGUNTAS: List[CreateLevelDto] = [
    {
        "question": "Qual o comando que exibe texto na tela?",
        "reward": 30,
        "right_answer": "B) print()",
        "wrong_answer": ("A) def()", "C) if", "D) input()"),
    },
    {
        "question": "Qual o comando que recebe dados digitados pelo usuário?",
        "reward": 50,
        "right_answer": "C) input()",
        "wrong_answer": ("A) while", "B) else", "D) for"),
    },
    {
        "question": "Quais comandos são usados para criar um loop?",
        "reward": 20,
        "right_answer": "D) while e for",
        "wrong_answer": (
            "A) while, for, if e elif",
            "B) somente o for",
            "C) somente o if",
        ),
    },
    {
        "question": "Qual a funcionalidade de um while loop?",
        "reward": 100,
        "right_answer": "C) Utilizada quando necessita que determinado bloco de código seja executado enquanto determinada condição for satisfeita",
        "wrong_answer": (
            "A) Executar somente uma linha",
            "B) Realizar um cálculo diversas vezes com diferentes números",
            "D) Executar o mesmo código para cada item em uma determinada sequência",
        ),
    },
    {
        "question": "Qual situação é mais adequada para se usar if/else?",
        "reward": 50,
        "right_answer": "A) Estrutura de decisão",
        "wrong_answer": (
            "B) Ao ser necessário repetir trecho de código",
            "C) Sempre dentro de um While loop",
            "D) Nunca se deve usar if/else, pois é extenso e deixa o código lento. Deve-se usar while loop",
        ),
    },
    {
        "question": "Qual a definição de tupla?",
        "reward": 70,
        "right_answer": "B) Valor imutável dentro do código",
        "wrong_answer": (
            "A) Conjunto de valores separados por ,",
            "C) Qualquer lista dentro de listas",
            "D) Valor sempre em String",
        ),
    },
    {
        "question": "Qual a estrutura correta de uma lista?",
        "reward": 30,
        "right_answer": "A) Dicionário = []",
        "wrong_answer": ("B) Lista = ()", "C) Lista = {}", "D) Lista = ([])"),
    },
    {
        "question": "Qual a principal função de um dicionário?",
        "reward": 20,
        "right_answer": "D) Manter valores acessá-los pelas suas chaves",
        "wrong_answer": (
            "A) Manter valores imutáveis",
            "B) Manter um conjunto de valores",
            "C) Adicionar valores à variáveis",
        ),
    },
    {
        "question": "Clique na alternativa que melhor descreva uma função",
        "reward": 40,
        "right_answer": "B) Sua principal função é permitir a flexibilidade e reutilização do código, além de facilitar a manutenção do mesmo.",
        "wrong_answer": (
            "A) Inicializada por def() e melhora a manutenção do código",
            "C) Permite a reutilização do código em diversos programas",
            "D) Executa um trecho de código ao ser chamada por nomeFuncao(atributos), como media(nota1, nota2, nota3)",
        ),
    },
    {
        "question": "Qual boa prática é a mais importante?",
        "reward": 50,
        "right_answer": "C) Indentação",
        "wrong_answer": (
            "A) Variáveis com letras inicias em minúsculo",
            "B) Comentários no código para explica-lo para quem está lendo",
            "D) Nomes de variáveis padronizados",
        ),
    },
    {
        "question": "O que significa a linha de um código: for numero in range(3,27,3)?",
        "reward": 70,
        "right_answer": "Serão inseridos temporariamente em numero valores entre 3 e 27, aumentando de 3 em 3",
        "wrong_answer": (
            "B) Serão inseridos em diversas variáveis numero valores entre 3 e 27, aumentando de 3 em 3",
            "C) Serão inseridos temporariamente em numero valores aleatórios entre 3 e 27, aumentando de 3 em 3",
            "D) Nenhuma das anteriores",
        ),
    },
    {
        "question": "Qual o significado de uma linha em um código: a, b = b, a % b?",
        "reward": 100,
        "right_answer": "C) troca de valores entre a e b (a vale o que b valia) e b vale o resto de a/b",
        "wrong_answer": (
            "A) Erro de compilação",
            "B) troca de valores entre b e a",
            "D) troca de valores entre b e a (b vale o que a valia) e a vale a elevado a b",
        ),
    },
    {
        "question": "Qual é o intuito da função random()?",
        "reward": 40,
        "right_answer": "C) A e B estão corretas",
        "wrong_answer": (
            "A) Gerar números aleatórios com ou sem intervalo",
            "B)  Pegar valores aleatórios de uma lista",
            "D) Nenhuma das anteriores",
        ),
    },
    {
        "question": "qual o significado desta linha dentro de um código, sendo lista1 e lista2 com o mesmo número de itens e sem declarar a variável item? for item in zip(lista1, lista2):",
        "reward": 100,
        "right_answer": "D) Criará valores correlacionados da lista1 e lista 2 em tuplas, como (valor1lista1, valor1lista2)",
        "wrong_answer": (
            "A) Criará dicionário com valores correlacionados da lista1 e lista 2 sendo chave e item, respectivamente, como {valor1lista1: valor1lista2}",
            "B) Criará lista de tuplas com valores correlacionados da lista1 e lista 2 em tuplas, como (valor1lista1, valor1lista2)",
            "C) erro, pois a variável item não foi declarada",
        ),
    },
    {
        "question": "O que ocorre se o return da função def loop(numero) FOR return numero * loop(numero-1) ?",
        "reward": 50,
        "right_answer": "B) Realizará a operação de numero vezes o resultado do return da função loop com numero-1",
        "wrong_answer": (
            "A) Realizará a operação de numero vezes o numero-1",
            "C) Realizará a operação de numero vezes o último caractere de número, como 22, usará o 2",
            "D) erro, pois não é possível chamar a própria função dentro dela mesma",
        ),
    },
]


def main():
    session = connect_to_database()

    if session:
        levelRepository = LevelRepository(session)

        for perguntaDict in PERGUNTAS:
            levelRepository.create(levelPayload=perguntaDict)


if __name__ == "__main__":
    main()
