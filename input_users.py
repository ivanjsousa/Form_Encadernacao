import PySimpleGUI as Sg

entradas_user = [Sg.Text('Projeto:', size=(6, 0)), Sg.InputText(do_not_clear=False, key='projeto')], \
                [Sg.Text('Cliente:', size=(6, 0)), Sg.InputText(do_not_clear=False, key='cliente')],\
                [Sg.Text('Tel:', size=(6, 0)), Sg.InputText(do_not_clear=False, key='tel', size=(12, 0)),
                 Sg.Text('Email:', size=(5, 0)), Sg.InputText(do_not_clear=False, key='email', size=(23, 0))],
