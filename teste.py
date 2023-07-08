import PySimpleGUI as sg

status = False

def autenticar_login(usuario, senha):
    usuario_correto = 'teste'
    senha_correta = '123'
    if usuario == usuario_correto and senha == senha_correta:
        sg.popup_ok('Login autenticado com sucesso!', no_titlebar=True)
        global status
        status = True
    else:
        sg.popup_cancel('Login ou senha incorreto', no_titlebar=True)
        

def fechar_janela(window):
    window.close()

layout = [
    [sg.Text('Usuário:'), sg.Input(key='inpt_user')],
    [sg.Text('Senha:'), sg.Input(key='inpt_senha', password_char='*')],
    [sg.Button('Login'), sg.Button('Sair')]
]

window = sg.Window('Exemplo', layout, return_keyboard_events=True)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Sair'):
        fechar_janela(window)
        break
    elif event == 'Login' or event == '\r':
        user = values['inpt_user']
        senha = values['inpt_senha']
        if autenticar_login(user, senha):
            fechar_janela(window)
            break

window.close()
