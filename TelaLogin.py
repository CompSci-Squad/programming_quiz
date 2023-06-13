#instalar pygame: pip install pygame
#instalar mysql connector: pip install mysql-connector-python

import pygame
import mysql.connector

# Inicialização do Pygame
pygame.init()

# Definição de cores
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Definição das dimensões da janela
WIDTH = 1550
HEIGHT = 800

# Inicialização da janela
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cadastro e Login")

logo = pygame.image.load("public\logo.png") 
logo = pygame.transform.scale(logo, (300, 305))

# Conexão com o banco de dados MySQL
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="mysqlimt",
    database="dbpi"
)

# Criação da tabela "usuarios" no banco de dados
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (email varchar (50), ra INT, nome VARCHAR(255), senha VARCHAR(255))")

# Função para exibir mensagens na janela
def exibir_mensagem(mensagem, cor, y_offset=0):
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render(mensagem, True, cor)
    texto_retangulo = texto.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    window.blit(texto, texto_retangulo)

# Função para cadastrar um usuário
def cadastrar(ra, nome, email, senha):
    cursor.execute("SELECT * FROM usuarios WHERE ra = %s", (ra,))
    resultado = cursor.fetchone()
    if resultado:
        return False  # RA já existe
    else:
        cursor.execute("INSERT INTO usuarios (email, ra, nome, senha) VALUES (%s, %s, %s, %s)", (email, ra, nome, senha))
        db.commit()
        return True

# Função para fazer login
def login(ra, senha):
    cursor.execute("SELECT * FROM usuarios WHERE ra = %s AND senha = %s", (ra, senha))
    resultado = cursor.fetchone()
    if resultado:
        return True  # Login bem-sucedido
    else:
        return False  # Login falhou

# Função principal
def main():
    
    executando = True
    tela_atual = "inicio"  # Pode ser "inicio", "cadastro" ou "login"
    tela_anterior = "inicio"
    campo_email = ""
    campo_ra = ""
    campo_nome = ""
    campo_senha = ""
    campo_selecionado = "ra"  # Pode ser "ra", "nome" ou "senha"

    while executando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False

            if tela_atual == "inicio":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if WIDTH // 2 - 100 <= event.pos[0] <= WIDTH // 2 + 100 and HEIGHT // 2 - 50 <= event.pos[1] <= HEIGHT // 2 - 10:
                        tela_anterior = "inicio"
                        tela_atual = "cadastro"
                    elif WIDTH // 2 - 100 <= event.pos[0] <= WIDTH // 2 + 100 and HEIGHT // 2 + 10 <= event.pos[1] <= HEIGHT // 2 + 50:
                        tela_anterior = "inicio"
                        tela_atual = "login"

            elif tela_atual == "cadastro":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if campo_selecionado == "ra":
                            campo_ra = campo_ra[:-1]
                        elif campo_selecionado == "nome":
                            campo_nome = campo_nome[:-1]
                        elif campo_selecionado == "email":
                            campo_email = campo_email[:-1]
                        elif campo_selecionado == "senha":
                            campo_senha = campo_senha[:-1]
                       
                    elif event.key == pygame.K_UP:
                        if campo_selecionado == "nome":
                            campo_selecionado = "ra"
                        elif campo_selecionado == "senha":
                            campo_selecionado = "email"
                        elif campo_selecionado == "email":
                            campo_selecionado = "nome"
                        
                    elif event.key == pygame.K_DOWN:
                        if campo_selecionado == "ra":
                            campo_selecionado = "nome"
                        elif campo_selecionado == "nome":
                            campo_selecionado = "email"
                        elif campo_selecionado == "email":
                            campo_selecionado = "senha"
                        
                    else:
                        if event.unicode.isdigit() and campo_selecionado == "ra":
                            campo_ra += event.unicode
                        elif event.unicode.isalpha() and campo_selecionado == "nome":
                            campo_nome += event.unicode
                        elif event.unicode != "" and campo_selecionado == "senha":
                            campo_senha += event.unicode
                        elif event.unicode != "" and campo_selecionado == "email":
                            campo_email += event.unicode

            elif tela_atual == "login":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if campo_selecionado == "ra":
                            campo_ra = campo_ra[:-1]
                        elif campo_selecionado == "senha":
                            campo_senha = campo_senha[:-1]
                    elif event.key == pygame.K_UP:
                        if campo_selecionado == "senha":
                            campo_selecionado = "ra"
                    elif event.key == pygame.K_DOWN:
                        if campo_selecionado == "ra":
                            campo_selecionado = "senha"
                    else:
                        if event.unicode.isdigit() and campo_selecionado == "ra":
                            campo_ra += event.unicode
                        elif event.unicode != "" and campo_selecionado == "senha":
                            campo_senha += event.unicode

        window.fill(BLUE)
        window.blit(logo, (625, 25))

        if tela_atual == "inicio":
            # Botão de cadastro
            pygame.draw.rect(window, YELLOW, (WIDTH // 2 - 100, HEIGHT // 2 - 60, 200, 40))
            exibir_mensagem("CADASTRO", BLACK, -40)

            # Botão de login
            pygame.draw.rect(window, YELLOW, (WIDTH // 2 - 100, HEIGHT // 2 + 20, 200, 40))
            exibir_mensagem("LOGIN", BLACK, 40)

        elif tela_atual == "cadastro":
            exibir_mensagem("RA: " + campo_ra, BLACK, -30)
            exibir_mensagem("Nome: " + campo_nome, BLACK)
            exibir_mensagem("Email: " + campo_email, BLACK, 30)
            exibir_mensagem("Senha: " + "*" * len(campo_senha), BLACK, 60)
            

            if campo_selecionado == "ra":
                pygame.draw.rect(window, YELLOW, (WIDTH // 2 - 150, HEIGHT // 2 - 60, 300, 40), 2)
            elif campo_selecionado == "nome":
                pygame.draw.rect(window, YELLOW, (WIDTH // 2 - 150, HEIGHT // 2 - 30, 300, 40), 2)
            elif campo_selecionado == "email":
                pygame.draw.rect(window, YELLOW, (WIDTH // 2 - 150, HEIGHT // 2, 300, 30), 2)
            elif campo_selecionado == "senha":
                pygame.draw.rect(window, YELLOW, (WIDTH // 2 - 150, HEIGHT // 2 + 40, 300, 40), 2)
           

            pygame.draw.rect(window, YELLOW, (WIDTH // 2 - 100, HEIGHT - 160, 200, 40))
            exibir_mensagem("CADASTRAR", BLACK, 260)
            pygame.draw.rect(window, YELLOW, (WIDTH // 2 - 100, HEIGHT - 100, 200, 40))
            exibir_mensagem("ARRASTE PARA VOLTAR", BLACK, 320)
            if WIDTH // 2 - 100 <= pygame.mouse.get_pos()[0] <= WIDTH // 2 + 100 and HEIGHT - 100 <= pygame.mouse.get_pos()[1] <= HEIGHT - 60:
                pygame.draw.rect(window, BLACK, (WIDTH // 2 - 100, HEIGHT - 100, 200, 40), 2)
                tela_atual = "inicio"

            if pygame.mouse.get_pressed()[0]:
                if WIDTH // 2 - 100 <= pygame.mouse.get_pos()[0] <= WIDTH // 2 + 100 and HEIGHT - 100 <= pygame.mouse.get_pos()[1] <= HEIGHT - 60:
                    if cadastrar(int(campo_ra), campo_nome, campo_email, campo_senha):
                        exibir_mensagem("Cadastro bem-sucedido", BLACK, 160)
                    else:
                        exibir_mensagem("RA já existe", BLACK, 160)
                    campo_ra = ""
                    campo_nome = ""
                    campo_senha = ""
                    campo_email = ""
                    campo_selecionado = "ra"
                    
                    # Voltar para a tela de escolha de opção
                    tela_atual = "inicio"

        elif tela_atual == "login":
            
            pygame.draw.rect(window, YELLOW, (WIDTH // 2 - 100, HEIGHT - 160, 200, 40))
            
            exibir_mensagem("RA: " + campo_ra, BLACK, -60)
            exibir_mensagem("Senha: " + "*" * len(campo_senha), BLACK)

            if campo_selecionado == "ra":
                pygame.draw.rect(window, YELLOW, (WIDTH // 2 - 150, HEIGHT // 2 - 75, 300, 40), 2)
            elif campo_selecionado == "senha":
                pygame.draw.rect(window, YELLOW, (WIDTH // 2 - 150, HEIGHT // 2 - 20, 300, 40), 2)

            pygame.draw.rect(window, YELLOW, (WIDTH // 2 - 100, HEIGHT - 100, 200, 40))
            exibir_mensagem("LOGIN", BLACK, 260)

            if WIDTH // 2 - 100 <= pygame.mouse.get_pos()[0] <= WIDTH // 2 + 100 and HEIGHT - 100 <= pygame.mouse.get_pos()[1] <= HEIGHT - 60:
                pygame.draw.rect(window, BLACK, (WIDTH // 2 - 100, HEIGHT - 100, 200, 40), 2)
                tela_atual = "inicio"

            if pygame.mouse.get_pressed()[0]:
                if WIDTH // 2 - 100 <= pygame.mouse.get_pos()[0] <= WIDTH // 2 + 100 and HEIGHT - 100 <= pygame.mouse.get_pos()[1] <= HEIGHT - 60:
                    if login(int(campo_ra), campo_senha):
                        exibir_mensagem("Login bem-sucedido", BLACK, 160)
                    else:
                        exibir_mensagem("Login falhou", BLACK, 160)
                    campo_ra = ""
                    campo_senha = ""
                    campo_selecionado = "ra"
                    
                    # Voltar para a tela de escolha de opção
                    tela_atual = tela_anterior

            exibir_mensagem("ARRASTE PARA VOLTAR", BLACK, 320)

    

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
