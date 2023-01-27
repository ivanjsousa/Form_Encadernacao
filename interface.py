import PySimpleGUI as Sg
import frames as fm
import eventos as ev
import abas as ab
import login as lg


# ------ BARRA DE MENU ------ #

menu_def = [['&Arquivo', ['&Novo', '---', '&Salvar', '&Imprimir', 'Sai&r']],
            ['A&juda', '&Sobre...'], ]

# ------ LAYOUT DA INTERFACE GRÁFICA ------ #

layout = [
    [Sg.Menu(menu_def)],
    [ev.entradas_user],
    [fm.caract_projeto],
    [fm.papelao_capa],
    [ab.abas],
    [Sg.Output(size=(55, 5))],
    [Sg.Button('Novo'), Sg.SaveAs('Salvar'), Sg.Button('Imprimir'), Sg.Button('Sair')]
]

# ------ CHAMA A JANELA DO PROGRAMA ------- #
janela = Sg.Window("Projetos de Encadernação V1.0", layout, enable_close_attempted_event=True)


# ------ AUTENTICAÇÃO USER\SENHA ------ #

autenticar = [lg.login()]
if lg.status is True:

    while True:
        evento, valor = janela.read()
        sair = (evento == Sg.WIN_CLOSE_ATTEMPTED_EVENT or evento == 'Sair') and Sg.popup_yes_no('Deseja sair?')

        if sair == 'Yes':
            break

        if evento == 'Novo':
            do_not_clear = True

        if evento == 'Imprimir':
            print(f'Projeto: ', valor['projeto'])
            print(f'Cliente: ', valor['cliente'])
            print(f'Telefone: ', valor['tel'])
            print(f'E-mail: ', valor['email'])
            tipos = filter(lambda x: valor[x] is True, fm.Lista_Tipo)
            print(f'Tipo: {", ".join(tipos)}.')

            acabamentos = filter(lambda x: valor[x] is True, fm.Lista_Acabamento)
            print(f'Com: {", ".join(acabamentos)}.')

            impressoes = filter(lambda x: valor[x] is True, fm.Lista_Impressao)
            print(f'Impressão: {", ".join(impressoes)}.')

            capas = filter(lambda x: valor[x] is True, fm.Lista_Papelao)
            print(f'Papelão da Capa de: {", ".join(capas)}.')

            tipos = [x for x in fm.Lista_Tipo if valor[x] is True]
            print(f'Tipo: {", ".join(tipos)}.')

            acabamentos = [x for x in fm.Lista_Acabamento if valor[x] is True]
            print(f'Com: {", ".join(acabamentos)}.')

            impressoes = [x for x in fm.Lista_Impressao if valor[x] is True]
            print(f'Impressão: {", ".join(impressoes)}.')

            capas = [x for x in fm.Lista_Papelao if valor[x] is True]
            print(f'Papelão da Capa de: {", ".join(capas)}.')

            print(f'O projeto terá {valor[ab.quantidade]} unidades(s) no formato {valor[ab.formato]}, revestimento '
                  f'em {valor[ab.revestimeno]} e papel {valor[ab.guarda]} para a guarda, o'
                  f' miolo com papel {valor[ab.miolo]} e terá {valor[ab.paginas]} páginas.')

    # ------ FECHAR A JANELA ------- #

    janela.close()
