import os
from datetime import datetime

# cores do terminal
ROXO    = "\033[35m"
ROXO_F  = "\033[95m"
BRANCO  = "\033[97m"
VERDE   = "\033[92m"
VERMELHO= "\033[91m"
CINZA   = "\033[90m"
NEGRITO = "\033[1m"
RESET   = "\033[0m"

# lista principal que guarda todas as materias
materias = []


# limpa a tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")


# imprime uma linha separadora roxa
def linha():
    print(ROXO + "  " + "-" * 45 + RESET)


# limpa a tela e mostra o titulo da secao
def titulo(texto):
    limpar()
    print()
    print(ROXO_F + NEGRITO + "  == " + texto.upper() + " ==" + RESET)
    print()


# imprime uma mensagem do bot
def bot(texto):
    print(ROXO_F + "  [FrameLab] " + RESET + texto)


# imprime mensagem de sucesso em verde
def ok(texto):
    print(VERDE + "  OK: " + texto + RESET)


# imprime mensagem de erro em vermelho
def erro(texto):
    print(VERMELHO + "  ERRO: " + texto + RESET)


# pausa ate o usuario apertar Enter
def voltar():
    input(CINZA + "\n  [Enter] para voltar " + RESET)


# funcao auxiliar que busca uma materia pelo nome na lista
# retorna o indice da materia ou -1 se nao encontrar
def achar_materia(nome):
    for i in range(len(materias)):
        if materias[i]["nome"].lower() == nome.lower():
            return i
    return -1


# cadastra uma nova materia na lista principal
def cadastrar_materia():
    titulo("Nova Materia")
    bot("Qual o nome da materia?")
    print()

    nome = input("  >> ").strip()

    # valida se o nome nao esta vazio
    if nome == "":
        erro("Nome nao pode ser vazio.")
        voltar()
        return

    # verifica se ja existe uma materia com esse nome
    if achar_materia(nome) != -1:
        erro("Essa materia ja existe!")
        voltar()
        return

    # cria o dicionario da materia e adiciona na lista
    nova_materia = {"nome": nome, "fotos": []}
    materias.append(nova_materia)

    print()
    ok(f"Materia '{nome}' criada com sucesso!")
    voltar()


# adiciona uma foto em uma materia existente
def adicionar_foto():
    titulo("Adicionar Foto")

    # verifica se tem alguma materia cadastrada antes de continuar
    if len(materias) == 0:
        bot("Voce nao tem nenhuma materia ainda. Crie uma primeiro!")
        voltar()
        return

    bot("Em qual materia quer salvar a foto?")
    print()

    # mostra a lista numerada de materias para o usuario escolher
    for i in range(len(materias)):
        total = len(materias[i]["fotos"])
        print(f"  [{i + 1}] {materias[i]['nome']}  ({total} foto(s))")

    print()
    escolha = input("  >> ").strip()

    # valida se o usuario digitou um numero valido
    if not escolha.isdigit():
        erro("Digite um numero valido.")
        voltar()
        return

    indice = int(escolha) - 1

    # verifica se o indice esta dentro do range da lista
    if indice < 0 or indice >= len(materias):
        erro("Opcao invalida.")
        voltar()
        return

    # pega a materia escolhida direto pelo indice da lista
    materia = materias[indice]

    print()
    bot("Qual o tema da foto?")
    bot("Exemplos: Resumo, Formula, Exercicio, Mapa mental, Prova")
    print()
    tema = input("  >> ").strip()

    # se nao digitar tema usa um padrao
    if tema == "":
        tema = "Sem tema"

    # gera um nome de arquivo com a data e hora pra nao repetir
    agora = datetime.now().strftime("%d%m%Y_%H%M%S")
    nome_arquivo = f"foto_{agora}.jpg"

    # cria o dicionario da foto
    foto = {
        "nome": nome_arquivo,
        "tema": tema,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    # adiciona a foto na lista de fotos da materia
    materia["fotos"].append(foto)

    print()
    ok(f"Foto salva em '{materia['nome']}' com tema '{tema}'!")
    voltar()


# mostra todas as materias e suas fotos
def ver_fotos():
    titulo("Minhas Fotos")

    if len(materias) == 0:
        bot("Nenhuma materia cadastrada ainda.")
        voltar()
        return

    # percorre a lista de materias com for
    for materia in materias:
        print(NEGRITO + f"  {materia['nome']}" + RESET + CINZA + f"  ({len(materia['fotos'])} foto(s))" + RESET)
        linha()

        # verifica se a materia tem fotos
        if len(materia["fotos"]) == 0:
            print(CINZA + "    Nenhuma foto ainda." + RESET)
        else:
            # percorre a lista de fotos da materia
            for i in range(len(materia["fotos"])):
                f = materia["fotos"][i]
                print(ROXO_F + f"    [{i + 1}] foto: " + RESET + f"{f['nome']}")
                print(CINZA + f"    tema: {f['tema']}  |  {f['data']}" + RESET)

        print()

    voltar()


# remove uma foto de uma materia
def remover_foto():
    titulo("Remover Foto")

    if len(materias) == 0:
        bot("Nenhuma materia cadastrada ainda.")
        voltar()
        return

    bot("De qual materia quer remover uma foto?")
    print()

    # lista as materias que tem pelo menos uma foto
    disponiveis = []
    for i in range(len(materias)):
        if len(materias[i]["fotos"]) > 0:
            disponiveis.append(i)
            print(f"  [{len(disponiveis)}] {materias[i]['nome']}  ({len(materias[i]['fotos'])} foto(s))")

    # se nenhuma materia tiver foto avisa e volta
    if len(disponiveis) == 0:
        bot("Nenhuma materia tem fotos ainda.")
        voltar()
        return

    print()
    escolha = input("  >> ").strip()

    if not escolha.isdigit():
        erro("Digite um numero valido.")
        voltar()
        return

    idx_disp = int(escolha) - 1

    if idx_disp < 0 or idx_disp >= len(disponiveis):
        erro("Opcao invalida.")
        voltar()
        return

    # pega a materia selecionada usando o indice da lista de disponiveis
    materia = materias[disponiveis[idx_disp]]

    print()
    bot(f"Qual foto de '{materia['nome']}' quer remover?")
    print()

    # mostra as fotos da materia escolhida
    for i in range(len(materia["fotos"])):
        f = materia["fotos"][i]
        print(f"  [{i + 1}] {f['tema']}  |  {f['data']}")

    print()
    escolha2 = input("  >> ").strip()

    if not escolha2.isdigit():
        erro("Digite um numero valido.")
        voltar()
        return

    idx_foto = int(escolha2) - 1

    if idx_foto < 0 or idx_foto >= len(materia["fotos"]):
        erro("Opcao invalida.")
        voltar()
        return

    # remove a foto da lista usando pop com o indice
    foto_removida = materia["fotos"].pop(idx_foto)

    print()
    ok(f"Foto '{foto_removida['tema']}' removida de '{materia['nome']}'!")
    voltar()


# exibe os resultados de uma busca
def mostrar_resultados(encontrados):
    print()
    if len(encontrados) == 0:
        bot("Nenhuma foto encontrada.")
    else:
        ok(f"{len(encontrados)} foto(s) encontrada(s):")
        print()
        for materia_nome, f in encontrados:
            print(NEGRITO + f"  {materia_nome}" + RESET + CINZA + f"  >  {f['tema']}" + RESET)
            print(ROXO_F + f"  {f['nome']}" + RESET + CINZA + f"  |  {f['data']}" + RESET)
            linha()


# busca fotos por materia, tema ou palavra geral
def buscar():
    titulo("Buscar Fotos")

    if len(materias) == 0:
        bot("Nenhuma materia cadastrada ainda.")
        voltar()
        return

    bot("Como quer buscar?")
    print()
    print(f"  [1] Por materia")
    print(f"  [2] Por tema")
    print(f"  [3] Por palavra (busca em tudo)")
    print()

    opcao = input("  >> ").strip()

    # busca por materia: mostra todas as fotos de uma materia
    if opcao == "1":
        print()
        bot("Qual materia?")
        print()

        for i in range(len(materias)):
            total = len(materias[i]["fotos"])
            print(f"  [{i + 1}] {materias[i]['nome']}  ({total} foto(s))")

        print()
        escolha = input("  >> ").strip()

        if not escolha.isdigit():
            erro("Digite um numero valido.")
            voltar()
            return

        indice = int(escolha) - 1

        if indice < 0 or indice >= len(materias):
            erro("Opcao invalida.")
            voltar()
            return

        materia = materias[indice]
        encontrados = [(materia["nome"], f) for f in materia["fotos"]]
        mostrar_resultados(encontrados)

    # busca por tema: filtra fotos pelo tema digitado
    elif opcao == "2":
        print()
        bot("Qual tema? (ex: Resumo, Prova, Formula)")
        print()
        busca = input("  >> ").strip().lower()

        if busca == "":
            erro("Digite alguma coisa.")
            voltar()
            return

        # percorre a lista de materias e a lista de fotos de cada uma
        encontrados = []
        for materia in materias:
            for f in materia["fotos"]:
                if busca in f["tema"].lower():
                    encontrados.append((materia["nome"], f))

        mostrar_resultados(encontrados)

    # busca geral: procura em nome da materia e no tema da foto
    elif opcao == "3":
        print()
        bot("Digite uma palavra para buscar em materia e tema:")
        print()
        busca = input("  >> ").strip().lower()

        if busca == "":
            erro("Digite alguma coisa.")
            voltar()
            return

        encontrados = []
        for materia in materias:
            for f in materia["fotos"]:
                if busca in materia["nome"].lower() or busca in f["tema"].lower():
                    encontrados.append((materia["nome"], f))

        mostrar_resultados(encontrados)

    else:
        erro("Opcao invalida.")

    voltar()


# menu principal com loop while
def menu():
    limpar()
    print()

    print(ROXO_F + NEGRITO + """
  ╔══════════════════════════════╗
  ║         FrameLab             ║
  ║        Modo Estudo           ║
  ╚══════════════════════════════╝
""" + RESET)

    nome = input("  Qual seu nome? ").strip()

    # se nao digitar nome usa um padrao
    if nome == "":
        nome = "Estudante"

    # loop principal do programa - so para quando o usuario digitar 0
    while True:
        limpar()
        print()
        print(ROXO_F + NEGRITO + f"  Ola, {nome}!" + RESET)
        print()

        # conta o total de fotos somando o tamanho da lista de cada materia
        total_fotos = 0
        for materia in materias:
            total_fotos += len(materia["fotos"])

        print(CINZA + f"  {len(materias)} materia(s)  |  {total_fotos} foto(s)" + RESET)
        print()
        linha()
        print()

        print(f"  [1] Cadastrar materia")
        print(f"  [2] Adicionar foto")
        print(f"  [3] Ver fotos")
        print(f"  [4] Buscar foto")
        print(f"  [5] Remover foto")
        print()
        print(CINZA + "  [0] Sair" + RESET)
        print()
        linha()

        opcao = input("  Escolha: ").strip()

        # estrutura match-case para chamar a funcao certa
        match opcao:
            case "1":
                cadastrar_materia()
            case "2":
                adicionar_foto()
            case "3":
                ver_fotos()
            case "4":
                buscar()
            case "5":
                remover_foto()
            case "0":
                limpar()
                print()
                print(ROXO_F + f"  Ate logo, {nome}! Bons estudos!" + RESET)
                print()
                break
            case _:
                erro("Opcao invalida.")
                input()

# inicia o programa
menu()