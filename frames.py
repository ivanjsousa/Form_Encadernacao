import PySimpleGUI as Sg

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


caract_projeto = [Sg.Frame('Tipo de Projeto', frame_tipo, key='t_projeto'),
                  Sg.Frame('Acabamento', frame_acabamento, key='t_acabamento'),
                  Sg.Frame('Tipo de Impressão', frame_impressao, key='t_impressao')],

papelao_capa = [Sg.Frame('Espessura do Papelão da Capa', frame_papelao, key='t_papelao')],
