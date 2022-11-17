import PySimpleGUI as Sg

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

abas = [Sg.TabGroup([[Sg.Tab('Quantidade', tab1_layout, key='qualidade'),
                      Sg.Tab('Formato', tab2_layout, key='formato'),
                      Sg.Tab('Revestimento', tab3_layout, key='revest'),
                      Sg.Tab('Guarda', tab4_layout, key='guarda'),
                      Sg.Tab('Miolo', tab5_layout, key='miolo'),
                      Sg.Tab('Cadernos', tab6_layout, key='caderno')]])],
