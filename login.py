import PySimpleGUI as sg

status = False


def login():
    layout = [
        [sg.Text('Usuário', key='usuario')],
        [sg.InputText(key='inpt_user')],
        [sg.Text('Senha', key='senha')],
        [sg.InputText(key='inpt_senha', password_char='*')],
        [sg.Button('Login', bind_return_key=True), sg.Button('Sair')],
    ]

    # ------ CHAMAR JANELA ------ #

    janela = sg.Window('Login', layout, no_titlebar=True, return_keyboard_events=True)

    # ------ LOOP DA JANELA ------ #

    while True:
        event, values = janela.read()
        if event in (sg.WINDOW_CLOSED, 'Sair'):
            break
        elif event == 'Login' or (event == '__TIMEOUT__' and values['__key__'] == '\r'):
            usuario_correto = 'teste'
            senha_correta = '123'
            user = values['inpt_user']
            senha = values['inpt_senha']
            if user == usuario_correto and senha == senha_correta:
                global status
                status = True
                janela.close()
            else:
                sg.popup_cancel('Login ou Senha Incorreto', no_titlebar=True)

    janela.close()
