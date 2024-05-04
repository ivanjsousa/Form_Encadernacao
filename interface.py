import PySimpleGUI as Sg
import frames as fm
import eventos_entrada as ev
import abas as ab
import login as lg
import logging
from gerar_pedido import gerar_conteudo
from imprimir import imprimir


logging.basicConfig(filename='log_error.log', level=logging.ERROR)

try:
    # Seu código que pode gerar um erro aqui
    raise ValueError("Exemplo de erro")
except Exception as e:
    logging.error(str(e), exc_info=True)


# BARRA DE MENU
menu_def = [['&Arquivo', ['&Novo', '---', '&Salvar', '&Imprimir', 'Sai&r']],
            ['A&juda', '&Sobre...'], ]


# LAYOUT DA INTERFACE GRÁFICA
layout = [
    [Sg.Menu(menu_def)],
    [ev.entradas_user],
    [fm.caract_projeto],
    [fm.papelao_capa],
    [ab.abas],    
    [Sg.Output(size=(55, 5))],
    [Sg.Button('Novo'), Sg.Button('Salvar'), Sg.Button('Gerar'), Sg.Button('Sair')]
]

# CHAMA A JANELA DO PROGRAMA 
janela = Sg.Window("Projetos de Encadernação V1.0", layout, enable_close_attempted_event=True)


# AUTENTICAÇÃO USER\SENHA
autenticar = [lg.login()]
if lg.status is True:

    while True:
        evento, valor = janela.read() # type: ignore
        sair = (evento == Sg.WIN_CLOSE_ATTEMPTED_EVENT or evento == 'Sair') and Sg.popup_yes_no('Deseja sair?')

        if sair == 'Yes':
            break

        if evento == 'Novo':
            do_not_clear = True

        if evento == 'Gerar':
            conteudo = gerar_conteudo(valor, fm, ab)
            print(conteudo)

        if evento == 'Imprimir':
            imprimir()

# FECHAR A JANELA
    janela.close()
