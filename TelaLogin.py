#instalar pygame: pip install pygame
#instalar mysql connector: pip install mysql-connector-python

import pygame
from src.shared.constants.images import LOGO
from src.shared.constants.colors import BLACK, BLUE, YELLOW
from src.shared.constants.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from src.shared.enums.field_enum import FieldEnum
from src.database.modules.user.entities.user_entity import UserEntity
from src.database.modules.user.repository.user_repository import UserRepository
from src.database.modules.user.dtos.create_user_dto import CreateUserDto

# Inicialização do Pygame
pygame.init()

# Definição de cores

# Definição das dimensões da janela

# Inicialização da janela
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cadastro e Login")

# Função para exibir mensagens na janela
def exibir_mensagem(mensagem, cor, y_offset=0):
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render(mensagem, True, cor)
    texto_retangulo = texto.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
    window.blit(texto, texto_retangulo)

# Função para cadastrar um usuário
def cadastrar(createUserPayload: CreateUserDto, userRepository: UserRepository):
    if userRepository.find_user('ra', createUserPayload['ra']):
        return False
    else:
        userRepository.create(createUserPayload)
        return True

# Função para fazer login
def login(login_user_dict, userRepository: UserRepository):
    user = userRepository.find_user('ra', login_user_dict['ra'])
    if user.ra == login_user_dict['ra'] and user.password == login_user_dict['password']:
        return True  # Login bem-sucedido
    else:
        return False  # Login falhou

# Função principal
def main(userRepository: UserRepository):
    user_dict: CreateUserDto = {'coins': 0, 'current_level_id': 1}
    login_user_dict = {'ra': '', 'password': ''}
    
    executando = True
    tela_atual = "inicio"  # Pode ser "inicio", "cadastro" ou "login"
    tela_anterior = "inicio"
    campo_email = ""
    campo_ra = ""
    campo_nome = ""
    campo_senha = ""
    campo_selecionado: FieldEnum  = FieldEnum.RA  # Pode ser "ra", "nome", "senha" ou "email"

    while executando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False

            if tela_atual == "inicio":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SCREEN_WIDTH // 2 - 100 <= event.pos[0] <= SCREEN_WIDTH // 2 + 100 and SCREEN_HEIGHT // 2 - 50 <= event.pos[1] <= SCREEN_HEIGHT // 2 - 10:
                        tela_anterior = "inicio"
                        tela_atual = "cadastro"
                    elif SCREEN_WIDTH // 2 - 100 <= event.pos[0] <= SCREEN_WIDTH // 2 + 100 and SCREEN_HEIGHT // 2 + 10 <= event.pos[1] <= SCREEN_HEIGHT // 2 + 50:
                        tela_anterior = "inicio"
                        tela_atual = "login"

            elif tela_atual == "cadastro":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if campo_selecionado == FieldEnum.RA:
                            user_dict['ra'] = user_dict['ra'][:-1]
                        elif campo_selecionado == FieldEnum.NOME:
                            user_dict['name'] = user_dict['name'][:-1]
                        elif campo_selecionado == FieldEnum.EMAIL:
                            user_dict["email"] = user_dict['email'][:-1]
                        elif campo_selecionado == FieldEnum.SENHA:
                            user_dict["password"] = user_dict['password'][:-1]
                       
                    elif event.key == pygame.K_UP:
                        if campo_selecionado == FieldEnum.NOME:
                            campo_selecionado = FieldEnum.RA
                        elif campo_selecionado == FieldEnum.SENHA:
                            campo_selecionado = FieldEnum.EMAIL
                        elif campo_selecionado == FieldEnum.EMAIL:
                            campo_selecionado = FieldEnum.NOME
                        
                    elif event.key == pygame.K_DOWN:
                        if campo_selecionado == FieldEnum.RA:
                            campo_selecionado = FieldEnum.NOME
                        elif campo_selecionado == FieldEnum.NOME:
                            campo_selecionado = FieldEnum.EMAIL
                        elif campo_selecionado == FieldEnum.EMAIL:
                            campo_selecionado = FieldEnum.SENHA
                        
                    else:
                        if event.unicode != "" and campo_selecionado == FieldEnum.RA:
                            user_dict["ra"] += event.unicode
                        elif event.unicode.isalpha() and campo_selecionado == FieldEnum.NOME:
                            user_dict['name'] += event.unicode
                        elif event.unicode != "" and campo_selecionado == FieldEnum.SENHA:
                            user_dict["password"] += event.unicode
                        elif event.unicode != "" and campo_selecionado == FieldEnum.EMAIL:
                            user_dict["email"] += event.unicode

            elif tela_atual == "login":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if campo_selecionado == FieldEnum.RA:
                            login_user_dict["ra"] = login_user_dict["ra"][:-1]
                        elif campo_selecionado == FieldEnum.SENHA:
                            login_user_dict["password"] = login_user_dict["password"][:-1]
                    elif event.key == pygame.K_UP:
                        if campo_selecionado == FieldEnum.SENHA:
                            campo_selecionado = FieldEnum.RA
                    elif event.key == pygame.K_DOWN:
                        if campo_selecionado == FieldEnum.RA:
                            campo_selecionado = FieldEnum.SENHA
                    else:
                        if event.unicode != "" and campo_selecionado == FieldEnum.RA:
                            login_user_dict["ra"] += event.unicode
                        elif event.unicode != "" and campo_selecionado == FieldEnum.SENHA:
                            login_user_dict["password"] += event.unicode

        window.fill(BLUE)
        window.blit(LOGO, (625, 25))

        if tela_atual == "inicio":
            # Botão de cadastro
            pygame.draw.rect(window, YELLOW, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 60, 200, 40))
            exibir_mensagem("CADASTRO", BLACK, -40)

            # Botão de login
            pygame.draw.rect(window, YELLOW, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20, 200, 40))
            exibir_mensagem("LOGIN", BLACK, 40)

        elif tela_atual == "cadastro":
            exibir_mensagem("RA: " + user_dict["ra"], BLACK, -30)
            exibir_mensagem("Nome: " + user_dict["name"], BLACK)
            exibir_mensagem("Email: " + user_dict["email"], BLACK, 30)
            exibir_mensagem("Senha: " + "*" * len(user_dict["password"]), BLACK, 60)
            

            if campo_selecionado == FieldEnum.RA:
                pygame.draw.rect(window, YELLOW, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 60, 300, 40), 2)
            elif campo_selecionado == FieldEnum.NOME:
                pygame.draw.rect(window, YELLOW, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 30, 300, 40), 2)
            elif campo_selecionado == FieldEnum.EMAIL:
                pygame.draw.rect(window, YELLOW, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 30), 2)
            elif campo_selecionado == FieldEnum.SENHA:
                pygame.draw.rect(window, YELLOW, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 40, 300, 40), 2)
           

            pygame.draw.rect(window, YELLOW, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 160, 200, 40))
            exibir_mensagem("CADASTRAR", BLACK, 260)
            pygame.draw.rect(window, YELLOW, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 40))
            exibir_mensagem("ARRASTE PARA VOLTAR", BLACK, 320)
            if SCREEN_WIDTH // 2 - 100 <= pygame.mouse.get_pos()[0] <= SCREEN_WIDTH // 2 + 100 and SCREEN_HEIGHT - 100 <= pygame.mouse.get_pos()[1] <= SCREEN_HEIGHT - 60:
                pygame.draw.rect(window, BLACK, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 40), 2)
                tela_atual = "inicio"

            if pygame.mouse.get_pressed()[1]:
                if SCREEN_WIDTH // 2 - 100 <= pygame.mouse.get_pos()[0] <= SCREEN_WIDTH // 2 + 100 and SCREEN_HEIGHT - 100 <= pygame.mouse.get_pos()[1] <= SCREEN_HEIGHT - 60:
                    if cadastrar(int(campo_ra), campo_nome, campo_email, campo_senha):
                        exibir_mensagem("Cadastro bem-sucedido", BLACK, 160)
                    else:
                        exibir_mensagem("RA já existe", BLACK, 160)
                    user_dict["ra"] = ""
                    user_dict["name"] = ""
                    user_dict["password"] = ""
                    user_dict["email"] = ""
                    campo_selecionado = FieldEnum.RA
                    
                    # Voltar para a tela de escolha de opção
                    tela_atual = "inicio"

        elif tela_atual == "login":
            
            pygame.draw.rect(window, YELLOW, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 160, 200, 40))
            
            exibir_mensagem("RA: " + login_user_dict["ra"], BLACK, -60)
            exibir_mensagem("Senha: " + "*" * len(login_user_dict["password"]), BLACK)

            if campo_selecionado == FieldEnum.RA:
                pygame.draw.rect(window, YELLOW, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 75, 300, 40), 2)
            elif campo_selecionado == FieldEnum.SENHA:
                pygame.draw.rect(window, YELLOW, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 20, 300, 40), 2)

            pygame.draw.rect(window, YELLOW, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 40))
            exibir_mensagem("LOGIN", BLACK, 260)

            if SCREEN_WIDTH // 2 - 100 <= pygame.mouse.get_pos()[0] <= SCREEN_WIDTH // 2 + 100 and SCREEN_HEIGHT - 100 <= pygame.mouse.get_pos()[1] <= SCREEN_HEIGHT - 60:
                pygame.draw.rect(window, BLACK, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 40), 2)
                tela_atual = "inicio"

            if pygame.mouse.get_pressed()[0]:
                if SCREEN_WIDTH // 2 - 100 <= pygame.mouse.get_pos()[0] <= SCREEN_WIDTH // 2 + 100 and SCREEN_HEIGHT - 100 <= pygame.mouse.get_pos()[1] <= SCREEN_HEIGHT - 60:
                    if login(int(campo_ra), campo_senha):
                        exibir_mensagem("Login bem-sucedido", BLACK, 160)
                    else:
                        exibir_mensagem("Login falhou", BLACK, 160)
                    login_user_dict["ra"] = ""
                    login_user_dict["password"] = ""
                    campo_selecionado = FieldEnum.RA
                    
                    # Voltar para a tela de escolha de opção
                    tela_atual = tela_anterior

            exibir_mensagem("ARRASTE PARA VOLTAR", BLACK, 320)

    

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
