import pygame
import random

pygame.init()

AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)

largura_tela = 1550
altura_tela = 800
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("PythonQuiz")

imagem_moeda = pygame.image.load("public\moeda.png")
imagem_moeda = pygame.transform.scale(imagem_moeda, (30, 30))

logo = pygame.image.load("public\logo.png") 
logo = pygame.transform.scale(logo, (300, 305))

imagem_moeda1 = pygame.image.load("public\moeda1.png")
imagem_moeda1 = pygame.transform.scale(imagem_moeda1, (45, 50))

# Classe para representar uma pergunta
class Pergunta:
    def __init__(self, texto, alternativas, resposta):
        self.texto = texto
        self.alternativas = alternativas
        self.resposta = resposta

    def verificar_resposta(self, alternativa_selecionada):
        return alternativa_selecionada == self.resposta

perguntas = [
    Pergunta("Qual o comando que exibe texto na tela?", 
             ["a) print()", "b) def()", "c) if", "d) input()"], 
             "a) print()"),
    Pergunta("Qual o comando que recebe dados digitados pelo usuário?", 
             ["a) While", "b) else", "c) input()", "d) for"], 
             "c) input()"),
    Pergunta("Quais comandos são usados para criar um loop?", 
             ["a) while, for, if e elif", "b) somente o for", "c) somente o if", "d) while e for"], 
             "d) while e for"),
    Pergunta("Qual a funcionalidade de um while loop?", 
             ["a) Executar somente uma linha", "b) Realizar um cálculo diversas vezes com diferentes números", "c) Utilizada quando necessita que determinado bloco de código seja executado enquanto determinada condição for satisfeita", "d) Executar o mesmo código para cada item em uma determinada sequência"], 
             "c) Utilizada quando necessita que determinado bloco de código seja executado enquanto determinada condição for satisfeita"),
    Pergunta("Qual situação é mais adequada para se usar if/else?", 
             ["a) Estrutura de decisão", "b) Ao ser necessário repetir trecho de código", "c) Sempre dentro de um While loop", "d)  Nunca se deve usar if/else, pois é extenso e deixa o código lento. Deve-se usar while loop."],
             "a) Estrutura de decisão"),
    Pergunta("Qual a definição de tupla?",
             ["a) Conjunto de valores separados por ,", "b) Valor imutável dentro do código", "c) Qualquer lista dentro de listas", "d) Valor sempre em String"],
             "b) Valor imutável dentro do código"),
    Pergunta("Qual a estrutura correta de uma lista?",
             ["a) Dicionário = []", "b) Lista = ()", "c) Lista = {}", "d) Lista = ([])"],
             "a) Dicionário = []"),
    Pergunta("Qual a principal função de um dicionário?",
             ["a) Manter valores imutáveis", "b) Manter um conjunto de valores", "c) Adicionar valores à variáveis", "d) Manter valores acessá-los pelas suas chaves"],
             "d) Manter valores acessá-los pelas suas chaves"),
    Pergunta("Clique na alternativa que melhor descreva uma função",
             ["a) Inicializada por def() e melhora a manutenção do código", "b) Sua principal função é permitir a flexibilidade e reutilização do código, além de facilitar a manutenção do mesmo", "c) Permite a reutilização do código em diversos programas", "d) Executa um trecho de código ao ser chamada por nomeFuncao(atributos), como media(nota1, nota2, nota3)"],
             "b) Sua principal função é permitir a flexibilidade e reutilização do código, além de facilitar a manutenção do mesmo"),
    Pergunta("Qual boa prática é a mais importante?",
             ["a) Variáveis com letras inicias em minúsculo", "b) Comentários no código para explica-lo para quem está lendo", "c) Indentação", "d) Nomes de variáveis padronizados"],
             "c) Indentação"),
    Pergunta("Qual é o intuito da função random()?", 
             ["a) Gerar números aleatórios com ou sem intervalo", "b) Pegar valores aleatórios de uma lista", "c) Todas as anteriores estão corretas", "d) Nenhuma das anteriores"], 
             "c) Todas as anteriores estão corretas"),
    Pergunta("O que significa a linha de um código: for numero in range(3,27,3)?", 
             ["a) Serão inseridos temporariamente em numero valores entre 3 e 27, aumentando de 3 em 3", "b) Serão inseridos em diversas variáveis numero valores entre 3 e 27, aumentando de 3 em 3", "c) Serão inseridos temporariamente em numero valores aleatórios entre 3 e 27, aumentando de 3 em 3", "d) Nenhuma das anteriores"], 
             "a) Serão inseridos temporariamente em numero valores entre 3 e 27, aumentando de 3 em 3"),
    Pergunta("Qual o significado de uma linha em um código: a, b = b, a % b", 
             ["a) Erro de compilação", "b) troca de valores entre b e a (b vale o que a valia) e a vale a/b", "c) troca de valores entre a e b (a vale o que b valia) e b vale o resto de a/b", "d) troca de valores entre b e a (b vale o que a valia) e a vale a elevado a b"], 
             "c) troca de valores entre a e b (a vale o que b valia) e b vale o resto de a/b"),
    Pergunta("Qual o significado desta linha dentro de um código, sendo lista1 e lista2 com o mesmo número de itens e sem declarar a variável item?: For item in zip(lista1, lista2):", 
             ["a) Criará dicionário com valores correlacionados da lista1 e lista 2 sendo chave e item, respectivamente, como {valor1lista1: valor1lista2}", "b) Criará lista de tuplas com valores correlacionados da lista1 e lista 2 em tuplas, como (valor1lista1, valor1lista2)", "c) erro, pois a variável item não foi declarada", "d) Criará valores correlacionados da lista1 e lista 2 em tuplas, como (valor1lista1, valor1lista2)"], 
             "d) Criará valores correlacionados da lista1 e lista 2 em tuplas, como (valor1lista1, valor1lista2)"),
    Pergunta("O que ocorre se o return da função def loop(numero) FOR return numero * loop(numero-1) ?", 
             ["a) Realizará a operação de numero vezes o numero-1", "b) Realizará a operação de numero vezes o resultado do return da função loop com numero-1", "c) Realizará a operação de numero vezes o último caractere de número, como 22, usará o 2", "d) erro, pois não é possível chamar a própria função dentro dela mesma"], 
             "b) Realizará a operação de numero vezes o resultado do return da função loop com numero-1"),                 
]

# Variáveis de estado do jogo
pergunta_atual = None
moedas = 0

# Função para exibir uma pergunta na tela
def exibir_pergunta(pergunta):
    tela.fill(AZUL)
    
    fonte = pygame.font.Font(None, 30)
    
    # Exibe o texto da pergunta
    texto_pergunta = fonte.render(pergunta.texto, True, BRANCO)
    tela.blit(texto_pergunta, (100, 100))
    
    # Exibe as alternativas
    y = 200
    for alternativa in pergunta.alternativas:
        texto_alternativa = fonte.render(alternativa, True, BRANCO)
        tela.blit(texto_alternativa, (150, y))
        y += 50

    # Exibe a quantidade de moedas
    texto_moedas = fonte.render("Moedas: " + str(moedas), True, AMARELO)
    tela.blit(texto_moedas, (100, 500))

    # Exibe a imagem da moeda
    tela.blit(imagem_moeda, (70, 490))
    tela.blit(imagem_moeda1, (850, 480))

    # Exibe imagem do logo
    tela.blit(logo, (largura_tela - 300, altura_tela - 300))

    # Exibe o botão de pular pergunta
    
    pygame.draw.rect(tela, AMARELO, (700, 480, 150, 50))
    texto_pular = fonte.render("Pular - 150", True, AZUL)
    tela.blit(texto_pular, (725, 500))
    
    pygame.display.flip()

# Função para exibir uma mensagem na tela
def exibir_mensagem(mensagem):
    tela.fill(AZUL)
    
    fonte = pygame.font.Font(None, 50)
    
    texto = fonte.render(mensagem, True, BRANCO)
    texto_rect = texto.get_rect(center=(largura_tela/2, altura_tela/2))
    tela.blit(texto, texto_rect)
    
    pygame.display.flip()
    
    # Aguarda 2 segundos antes de continuar
    pygame.time.wait(2000)

# Função principal do jogo
def jogo():
    global pergunta_atual, moedas
    
    # Embaralha a lista de perguntas
    random.shuffle(perguntas)

    for pergunta in perguntas:
        pergunta_atual = pergunta
        resposta_selecionada = None

        while resposta_selecionada is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    posicao_mouse = pygame.mouse.get_pos()
                    resposta_selecionada = verificar_clique(posicao_mouse)
                    
                    if 700 <= posicao_mouse[0] <= 900 and 500 <= posicao_mouse[1] <= 550:
                        if moedas >= 150:
                            moedas -= 150
                            exibir_mensagem("Pergunta pulada! -150 moedas")
                            resposta_selecionada = "Pular"
                        else:
                            exibir_mensagem("Você precisa de 150 moedas para pular!")
                            break
            
            if resposta_selecionada == "Pular":
                break
            
            exibir_pergunta(pergunta_atual)
        
        if resposta_selecionada == "Pular":
            continue
         
        if pergunta_atual.verificar_resposta(resposta_selecionada):
            moedas += 30
            exibir_mensagem("Resposta correta! +30 moedas")
        else:
            exibir_mensagem("Resposta incorreta!")
        

    exibir_mensagem("Fim do jogo. Você conseguiu " + str(moedas) + " moedas!")

# Função para verificar o clique do mouse nas alternativas
def verificar_clique(posicao_mouse):
    y = 200
    for i in range(len(pergunta_atual.alternativas)):
        if 150 <= posicao_mouse[0] <= 450 and y <= posicao_mouse[1] <= y + 40:
            return pergunta_atual.alternativas[i]
        y += 50
    
    return None
# Executa o jogo
jogo()
