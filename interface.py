import PySimpleGUI as Sg


# ------ BARRA DE MENU ------ #

menu_def = [['&Arquivo', ['&Novo', '---', '&Salvar', '&Imprimir', 'Sai&r']],
            ['A&juda', '&Sobre...'], ]

# ------ LAYOUT DOS FRAMES ------ #

frame_tipo = [
    [Sg.CB('Encadernação')],
    [Sg.CB('Papelaria')],
    [Sg.CB('Reencadernação')],
    [Sg.CB('Conservação')],
    [Sg.CB('Restauro')]]

frame_acabamento = [
    [Sg.CB('Elástico')],
    [Sg.CB('Cabeceado')],
    [Sg.CB('Marcador')],
    [Sg.CB('Ferragem')],
    [Sg.CB('Rebaixo')]]

frame_impressao = [
    [Sg.CB('Jato-de-Tinta')],
    [Sg.CB('Laser')],
    [Sg.CB('Indigo')],
    [Sg.CB('Serigrafia')],
    [Sg.CB('Latterpress')]]

frame_papelao = [
    [Sg.Radio('0,6mm', "RADIO1"), Sg.Radio('1,2mm', "RADIO1"),
     Sg.Radio('1,5mm', "RADIO1"), Sg.Radio('1,8mm', "RADIO1")],
    [Sg.Radio('2,0mm', "RADIO1"), Sg.Radio('2,3mm', "RADIO1"),
     Sg.Radio('2,5mm', "RADIO1"), Sg.Radio('2,8mm', "RADIO1")]]

# ------ LAYOUT DAS ABAS - (TIPO PASTAS) ------ #

tab1_layout = [[Sg.T('Quantas cópias do produto?')],
               [Sg.In(key='in', do_not_clear=False, size=(55, 5))]]

tab2_layout = [[Sg.T('Como pensa do Formato Aberto e Fechado?')],
               [Sg.In(key='in', do_not_clear=False, size=(55, 5))]]

tab3_layout = [[Sg.T('Qual vai ser o Revestimento do Livro?')],
               [Sg.In(key='in', do_not_clear=False, size=(55, 5))]]

tab4_layout = [[Sg.T('Como será a folha de Guarda?')],
               [Sg.In(key='in', do_not_clear=False, size=(55, 5))]]

tab5_layout = [[Sg.T('Descreva o Papel do Miolo?')],
               [Sg.In(key='in', do_not_clear=False, size=(55, 5))]]

tab6_layout = [[Sg.T('Quantos cadernos e/ou páginas?')],
               [Sg.In(key='in', do_not_clear=False, size=(55, 5))]]

# ------ LAYOUT DA INTERFACE GRÁFICA ------ #

layout = [
    [Sg.Menu(menu_def)],

    [Sg.Text('Projeto:', size=(6, 0)), Sg.InputText(do_not_clear=False, key='projeto')],

    [Sg.Text('Cliente:', size=(6, 0)), Sg.InputText(do_not_clear=False, key='cliente')],

    [Sg.Text('Tel:', size=(6, 0)), Sg.InputText(do_not_clear=False, key='tel', size=(12, 0)),
     Sg.Text('Email:', size=(5, 0)), Sg.InputText(do_not_clear=False, key='email', size=(23, 0))],

    [Sg.Frame('Tipo de Projeto', frame_tipo, key='t_projeto'),
     Sg.Frame('Acabamento', frame_acabamento, key='t_acabamento'),
     Sg.Frame('Tipo de Impressão', frame_impressao, key='t_impressao')],

    [Sg.Frame('Espessura do Papelão da Capa', frame_papelao, key='t_papelao')],

    [Sg.TabGroup([[Sg.Tab('Quantidade', tab1_layout, key='qualidade'), Sg.Tab('Formato', tab2_layout, key='formato'),
                   Sg.Tab('Revestimento', tab3_layout, key='revest'), Sg.Tab('Guarda', tab4_layout, key='guarda'),
                   Sg.Tab('Miolo', tab5_layout, key='miolo'), Sg.Tab('Cadernos', tab6_layout, key='caderno')]])],

    [Sg.Output(size=(55, 4))],

    [Sg.Button('Novo'), Sg.SaveAs('Salvar'), Sg.Button('Imprimir'), Sg.Button('Sair')]
]

# ------ CHAMA A JANELA (INTERFACE GRÁFICA) ------ #

janela = Sg.Window("Projetos de Encadernação V1.0", layout, enable_close_attempted_event=True)


# ------ LAÇO QUE MANTEM A JANELA ATIVA ------ #
""" Aqui é colocado toda a lógica de funcionamento dos eventos e cliques do aplicativo"""


while True:
    evento, valor = janela.read()
    sair = (evento == Sg.WIN_CLOSE_ATTEMPTED_EVENT or evento == 'Sair') and Sg.popup_yes_no('Deseja sair?')
    sair2 = (evento == Sg.Button('Sair'))

    if evento == Sg.WIN_CLOSED:
        break

    if sair or sair2 == 'Yes':
        break

    if evento == 'Novo' or evento == Sg.Button('Novo'):
        do_not_clear = True

    if evento == 'Imprimir':
        print(f'Projeto: ', valor['projeto'])
        print(f'Cliente: ', valor['cliente'])
        print(f'Telefone: ', valor['tel'])
        print(f'E-mail: ', valor['email'])


# ------ FECHAR A JANELA ------- #

janela.close()
