import pygame
import random
from typing import Tuple, List
from src.database.modules.level.repositories.level_repository import LevelRepository

pygame.init()

from ....shared.constants.colors import YELLOW, BLUE, BRANCO
from ....shared.images.images import COIN_IMAGE, COIN_IMAGE_1, LOGO
from ....shared.constants.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN

pygame.display.set_caption("PythonQuiz")

# Variáveis de estado do jogo
pergunta_atual = None
moedas = 0

def verify_answer(right_answer: str, selected_answer: str):
    return right_answer == selected_answer

# Função para exibir uma pergunta na SCREEN
def exibir_pergunta(alternativas: List[str], question: str, id: int):
    SCREEN.fill(BLUE)

    fonte = pygame.font.Font(None, 30)

    # Exibe o texto da pergunta
    texto_pergunta = fonte.render(f'{id}) {question}', True, BRANCO)
    SCREEN.blit(texto_pergunta, (100, 100))

    # Exibe as alternativas
    y = 200
    for alternativa in alternativas:
        texto_alternativa = fonte.render(alternativa, True, BRANCO)
        SCREEN.blit(texto_alternativa, (150, y))
        y += 50

    # Exibe a quantidade de moedas
    texto_moedas = fonte.render("Moedas: " + str(moedas), True, YELLOW)
    SCREEN.blit(texto_moedas, (100, 500))

    # Exibe a imagem da moeda
    SCREEN.blit(COIN_IMAGE, (70, 490))
    SCREEN.blit(COIN_IMAGE_1, (850, 480))

    # Exibe imagem do logo
    SCREEN.blit(LOGO, (SCREEN_WIDTH - 300, SCREEN_HEIGHT - 300))

    # Exibe o botão de pular pergunta

    pygame.draw.rect(SCREEN, YELLOW, (700, 480, 150, 50))
    texto_pular = fonte.render("Pular - 150", True, BLUE)
    SCREEN.blit(texto_pular, (725, 500))

    pygame.display.flip()


# Função para exibir uma mensagem na SCREEN
def exibir_mensagem(mensagem: str):
    SCREEN.fill(BLUE)

    fonte = pygame.font.Font(None, 50)

    texto = fonte.render(mensagem, True, BRANCO)
    texto_rect = texto.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    SCREEN.blit(texto, texto_rect)

    pygame.display.flip()

    # Aguarda 2 segundos antes de continuar
    pygame.time.wait(2000)

# Função para verificar o clique do mouse nas alternativas
def verificar_clique(posicao_mouse: Tuple[int, int], alternativas: List[str]) -> str:
    y = 200
    for i in range(len(alternativas)):
        if 150 <= posicao_mouse[0] <= 450 and y <= posicao_mouse[1] <= y + 40:
            return alternativas[i]
        y += 50

    return ''

# Função principal do jogo
def jogo(levelRepository: LevelRepository):
    global pergunta_atual, moedas
    levels = levelRepository.get_all()

    for level in levels:
        alternativas = [level.right_answer, level.wrong_answer_1, level.wrong_answer_2, level.wrong_answer_3]
        random.shuffle(alternativas)
        level_atual = level
        resposta_selecionada: str = ''

        while resposta_selecionada is '':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    posicao_mouse = pygame.mouse.get_pos()
                    resposta_selecionada = verificar_clique(posicao_mouse, alternativas)

                    if (
                        700 <= posicao_mouse[0] <= 900
                        and 500 <= posicao_mouse[1] <= 550
                    ):
                        if moedas >= 150:
                            moedas -= 150
                            exibir_mensagem("Pergunta pulada! -150 moedas")
                            resposta_selecionada = "Pular"
                        else:
                            exibir_mensagem("Você precisa de 150 moedas para pular!")
                            break

            if resposta_selecionada == "Pular":
                break

            exibir_pergunta(alternativas, level.question, level.id)

        if resposta_selecionada == "Pular":
            continue

        if verify_answer(level.right_answer, resposta_selecionada):
            moedas += level_atual.reward
            exibir_mensagem(f"Resposta correta! +{level_atual.reward} moedas")
        else:
            exibir_mensagem("Resposta incorreta!")

    exibir_mensagem("Fim do jogo. Você conseguiu " + str(moedas) + " moedas!")

