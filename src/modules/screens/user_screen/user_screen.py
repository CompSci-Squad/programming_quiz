# instalar pygame: pip install pygame
# instalar mysql connector: pip install mysql-connector-python

import pygame
from src.shared.constants.images import LOGO
from src.shared.constants.colors import BLACK, BLUE, YELLOW
from src.shared.constants.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN
from src.shared.enums.field_enum import FieldEnum
from src.database.modules.user.repository.user_repository import UserRepository
from src.database.modules.user.dtos.create_user_dto import CreateUserDto
# Inicialização da janela
pygame.display.set_caption("Cadastro e Login")


# Função para exibir mensagens na janela
def exibir_mensagem(mensagem, cor, y_offset=0):
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render(mensagem, True, cor)
    texto_retangulo = texto.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset)
    )
    SCREEN.blit(texto, texto_retangulo)


# Função para cadastrar um usuário
def cadastrar(createUserPayload: CreateUserDto, userRepository: UserRepository):
    if userRepository.find_user("ra", createUserPayload["ra"]):
        return None
    else:
        user = userRepository.create(createUserPayload)
        return user


# Função para fazer login
def login(login_user_dict, userRepository: UserRepository):
    user = userRepository.find_user("ra", login_user_dict["ra"])
    if (
        user.ra == login_user_dict["ra"]
        and user.password == login_user_dict["password"]
    ):
        return user # Login bem-sucedido
    else:
        return None  # Login falhou


# Função principal
def user_screen(userRepository: UserRepository):
    user_dict: CreateUserDto = {
        "ra": "",
        "email": "",
        "name": "",
        "password": "",
        "coins": 0,
        "current_level_id": 1,
    }
    login_user_dict = {"ra": "", "password": ""}

    executando = True
    tela_atual = "inicio"  # Pode ser "inicio", "cadastro" ou "login"
    tela_anterior = "inicio"
    campo_selecionado: FieldEnum = (
        FieldEnum.RA
    )  # Pode ser "ra", "nome", "senha" ou "email"

    while executando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False
            if tela_atual == "inicio":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (
                        SCREEN_WIDTH // 2 - 100
                        <= event.pos[0]
                        <= SCREEN_WIDTH // 2 + 100
                        and SCREEN_HEIGHT // 2 - 50
                        <= event.pos[1]
                        <= SCREEN_HEIGHT // 2 - 10
                    ):
                        tela_anterior = "inicio"
                        tela_atual = "cadastro"
                    elif (
                        SCREEN_WIDTH // 2 - 100
                        <= event.pos[0]
                        <= SCREEN_WIDTH // 2 + 100
                        and SCREEN_HEIGHT // 2 + 10
                        <= event.pos[1]
                        <= SCREEN_HEIGHT // 2 + 50
                    ):
                        tela_anterior = "inicio"
                        tela_atual = "login"

            elif tela_atual == "cadastro":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if campo_selecionado == FieldEnum.RA:
                            user_dict["ra"] = user_dict["ra"][:-1]
                        elif campo_selecionado == FieldEnum.NOME:
                            user_dict["name"] = user_dict["name"][:-1]
                        elif campo_selecionado == FieldEnum.EMAIL:
                            user_dict["email"] = user_dict["email"][:-1]
                        elif campo_selecionado == FieldEnum.SENHA:
                            user_dict["password"] = user_dict["password"][:-1]

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
                        elif (
                            event.unicode.isalpha()
                            and campo_selecionado == FieldEnum.NOME
                        ):
                            user_dict["name"] += event.unicode
                        elif (
                            event.unicode != "" and campo_selecionado == FieldEnum.SENHA
                        ):
                            user_dict["password"] += event.unicode
                        elif (
                            event.unicode != "" and campo_selecionado == FieldEnum.EMAIL
                        ):
                            user_dict["email"] += event.unicode

            elif tela_atual == "login":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if campo_selecionado == FieldEnum.RA:
                            login_user_dict["ra"] = login_user_dict["ra"][:-1]
                        elif campo_selecionado == FieldEnum.SENHA:
                            login_user_dict["password"] = login_user_dict["password"][
                                :-1
                            ]
                    elif event.key == pygame.K_UP:
                        if campo_selecionado == FieldEnum.SENHA:
                            campo_selecionado = FieldEnum.RA
                    elif event.key == pygame.K_DOWN:
                        if campo_selecionado == FieldEnum.RA:
                            campo_selecionado = FieldEnum.SENHA
                    else:
                        if event.unicode != "" and campo_selecionado == FieldEnum.RA:
                            login_user_dict["ra"] += event.unicode
                        elif (
                            event.unicode != "" and campo_selecionado == FieldEnum.SENHA
                        ):
                            login_user_dict["password"] += event.unicode

        SCREEN.fill(BLUE)
        SCREEN.blit(LOGO, (625, 25))

        if tela_atual == "inicio":
            # Botão de cadastro
            pygame.draw.rect(
                SCREEN,
                YELLOW,
                (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 60, 200, 40),
            )
            exibir_mensagem("CADASTRO", BLACK, -40)

            # Botão de login
            pygame.draw.rect(
                SCREEN,
                YELLOW,
                (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20, 200, 40),
            )
            exibir_mensagem("LOGIN", BLACK, 40)

        elif tela_atual == "cadastro":
            exibir_mensagem("RA: " + user_dict["ra"], BLACK, -30)
            exibir_mensagem("Nome: " + user_dict["name"], BLACK)
            exibir_mensagem("Email: " + user_dict["email"], BLACK, 30)
            exibir_mensagem("Senha: " + "*" * len(user_dict["password"]), BLACK, 60)

            if campo_selecionado == FieldEnum.RA:
                pygame.draw.rect(
                    SCREEN,
                    YELLOW,
                    (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 60, 300, 40),
                    2,
                )
            elif campo_selecionado == FieldEnum.NOME:
                pygame.draw.rect(
                    SCREEN,
                    YELLOW,
                    (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 30, 300, 40),
                    2,
                )
            elif campo_selecionado == FieldEnum.EMAIL:
                pygame.draw.rect(
                    SCREEN,
                    YELLOW,
                    (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 30),
                    2,
                )
            elif campo_selecionado == FieldEnum.SENHA:
                pygame.draw.rect(
                    SCREEN,
                    YELLOW,
                    (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 40, 300, 40),
                    2,
                )

            pygame.draw.rect(
                SCREEN, YELLOW, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 160, 200, 40)
            )
            exibir_mensagem("CADASTRAR", BLACK, 260)
            pygame.draw.rect(
                SCREEN, YELLOW, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 40)
            )
            exibir_mensagem("ARRASTE PARA VOLTAR", BLACK, 320)
            if (
                SCREEN_WIDTH // 2 - 100
                <= pygame.mouse.get_pos()[0]
                <= SCREEN_WIDTH // 2 + 100
                and SCREEN_HEIGHT - 100
                <= pygame.mouse.get_pos()[1]
                <= SCREEN_HEIGHT - 60
            ):
                pygame.draw.rect(
                    SCREEN,
                    BLACK,
                    (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 40),
                    2,
                )
                tela_atual = "inicio"

            if pygame.mouse.get_pressed()[0]:
                print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                if (
                    SCREEN_WIDTH // 2 - 100
                    <= pygame.mouse.get_pos()[0]
                    <= SCREEN_WIDTH // 2 + 100
                    and SCREEN_HEIGHT - 200
                    <= pygame.mouse.get_pos()[1]
                    <= SCREEN_HEIGHT - 100
                ):
                    user = cadastrar(user_dict, userRepository)
                    if user is not None:
                        exibir_mensagem("Cadastro bem-sucedido", BLACK, 160)
                        executando = False
                        return user
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
            pygame.draw.rect(
                SCREEN, YELLOW, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 160, 200, 40)
            )

            exibir_mensagem("RA: " + login_user_dict["ra"], BLACK, -60)
            exibir_mensagem("Senha: " + "*" * len(login_user_dict["password"]), BLACK)

            if campo_selecionado == FieldEnum.RA:
                pygame.draw.rect(
                    SCREEN,
                    YELLOW,
                    (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 75, 300, 40),
                    2,
                )
            elif campo_selecionado == FieldEnum.SENHA:
                pygame.draw.rect(
                    SCREEN,
                    YELLOW,
                    (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 20, 300, 40),
                    2,
                )

            pygame.draw.rect(
                SCREEN, YELLOW, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 40)
            )
            exibir_mensagem("LOGIN", BLACK, 260)

            if (
                SCREEN_WIDTH // 2 - 100
                <= pygame.mouse.get_pos()[0]
                <= SCREEN_WIDTH // 2 + 100
                and SCREEN_HEIGHT - 100
                <= pygame.mouse.get_pos()[1]
                <= SCREEN_HEIGHT - 60
            ):
                pygame.draw.rect(
                    SCREEN,
                    BLACK,
                    (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 40),
                    2,
                )
                tela_atual = "inicio"

            if pygame.mouse.get_pressed()[0]:
                if (
                    SCREEN_WIDTH // 2 - 100
                    <= pygame.mouse.get_pos()[0]
                    <= SCREEN_WIDTH // 2 + 100
                    and SCREEN_HEIGHT - 200
                    <= pygame.mouse.get_pos()[1]
                    <= SCREEN_HEIGHT - 100
                ):
                    user = login(login_user_dict, userRepository)
                    if user is not None:
                        exibir_mensagem("Login bem-sucedido", BLACK, 160)
                        executando = False
                        return user
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
