import PySimpleGUI as Sg


# ------ LAYOUT DAS ABAS - (TIPO PASTAS) ------ #

tab1_layout = [[Sg.T('Quantas cópias do produto?')],
               [Sg.In(key='quantidade', do_not_clear=False, size=(55, 5))]]

tab2_layout = [[Sg.T('Como pensa do Formato Aberto e Fechado?')],
               [Sg.In(key='formato', do_not_clear=False, size=(55, 5))]]

tab3_layout = [[Sg.T('Qual vai ser o Revestimento do Livro?')],
               [Sg.In(key='revest', do_not_clear=False, size=(55, 5))]]

tab4_layout = [[Sg.T('Como será a folha de Guarda?')],
               [Sg.In(key='guarda', do_not_clear=False, size=(55, 5))]]

tab5_layout = [[Sg.T('Descreva o Papel do Miolo?')],
               [Sg.In(key='miolo', do_not_clear=False, size=(55, 5))]]

tab6_layout = [[Sg.T('Serão quantas páginas?')],
               [Sg.In(key='caderno', do_not_clear=False, size=(55, 5))]]

abas = [Sg.TabGroup([[Sg.Tab('Quantidade', tab1_layout),
                      Sg.Tab('Formato', tab2_layout),
                      Sg.Tab('Revestimento', tab3_layout),
                      Sg.Tab('Guarda', tab4_layout),
                      Sg.Tab('Miolo', tab5_layout),
                      Sg.Tab('Páginas', tab6_layout)]])],

quantidade = 'quantidade'
formato = 'formato'
revestimeno = 'revest'
guarda = 'guarda'
miolo = 'miolo'
paginas = 'paginas'
