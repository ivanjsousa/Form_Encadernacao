import PySimpleGUI as Sg

status = False


def login():
    layout = [
        [Sg.Text('Usuário', key='usuario')],
        [Sg.InputText(key='inpt_user')],
        [Sg.Text('Senha', key='senha')],
        [Sg.InputText(key='inpt_senha', password_char='*')],
        [Sg.Button('Login'), Sg.Button('Sair')],
        ]

    # ------ CHAMAR JANELA ------ #

    janela = Sg.Window('Login', layout, no_titlebar=True)

    # ------ LOOP DA JANELA ------ #

    while True:
        evento, valor = janela.read()
        if evento == Sg.WIN_CLOSED:
            break
        elif evento == 'Sair':
            break
        elif evento == 'Login':
            usuario_correto = 'teste'
            senha_correta = '123'
            user = valor['inpt_user']
            senha = valor['inpt_senha']
            if user == usuario_correto and senha == senha_correta:
                global status
                status = True
                Sg.popup_ok('Login Autenticado com sucesso!', no_titlebar=True)
                janela.close()
            else:
                Sg.popup_cancel('Login ou Senha Incorreto', no_titlebar=True)

    janela.close()
