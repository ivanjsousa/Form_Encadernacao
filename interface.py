import PySimpleGUI as Sg
import frames as fm
import input_users as iu
import abas as ab
import login as lg

# ------ AUTENTICAÇÃO USER\SENHA ------ #

autenticar = [lg.login()]

# ------ BARRA DE MENU ------ #

menu_def = [['&Arquivo', ['&Novo', '---', '&Salvar', '&Imprimir', 'Sai&r']],
            ['A&juda', '&Sobre...'], ]

# ------ LAYOUT DA INTERFACE GRÁFICA ------ #

layout = [
    [Sg.Menu(menu_def)],
    [iu.entradas_user],
    [fm.caract_projeto],
    [fm.papelao_capa],
    [ab.abas],
    [Sg.Output(size=(55, 5))],

    [Sg.Button('Novo'), Sg.SaveAs('Salvar'), Sg.Button('Imprimir'), Sg.Button('Sair')]
]

# ------ CHAMA A JANELA (INTERFACE GRÁFICA) ------ #

janela = Sg.Window("Projetos de Encadernação V1.0", layout, enable_close_attempted_event=True)


# ------ LAÇO QUE MANTEM A JANELA ATIVA ------ #
""" Aqui é colocado toda a lógica de funcionamento dos eventos e valores do aplicativo"""

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
        for tipo in fm.Lista_Tipo:
            if valor[tipo] is True:
                print(f'Tipo: {tipo}.')
        for item in fm.Lista_Acabamento:
            if valor[item] is True:
                print(f'Com: {item}.')
        for forma in fm.Lista_Impressao:
            if valor[forma] is True:
                print(f'Impressão: {forma}.')
        for capa in fm.Lista_Papelao:
            if valor[capa] is True:
                print(f'Papelão da Capa de: {capa}.')
        print(f'O projeto terá {valor[ab.quantidade]} unidades(s) no formato {valor[ab.formato]}, revestimento '
              f'em {valor[ab.revestimeno]} e papel {valor[ab.guarda]} para a guarda, o'
              f'miolo com papel {valor[ab.miolo]} e serão {valor[ab.paginas]} páginas.')


# ------ FECHAR A JANELA ------- #

janela.close()
