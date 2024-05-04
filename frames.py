import PySimpleGUI as Sg

#LAYOUT DOS FRAMES#

frame_tipo = [
    [Sg.CB('Encadernação', key='Encadernação')],
    [Sg.CB('Papelaria', key='Papelaria')],
    [Sg.CB('Reencadernação', key='Reencadernação')],
    [Sg.CB('Conservação', key='Conservação')],
    [Sg.CB('Restauro', key='Restauro')]]

key_1 = 'Encadernação'
key_2 = 'Papelaria'
key_3 = 'Reencadernação'
key_4 = 'Conservação'
key_5 = 'Restauro'
Lista_Tipo = [key_1, key_2, key_3, key_4, key_5]

frame_acabamento = [
    [Sg.CB('Elástico', key='Elastico')],
    [Sg.CB('Cabeceado', key='Cabeceado')],
    [Sg.CB('Marcador', key='Marcador')],
    [Sg.CB('Ferragem', key='Ferragem')],
    [Sg.CB('Rebaixo', key='Rebaixo')]]

key_6 = 'Elastico'
key_7 = 'Cabeceado'
key_8 = 'Marcador'
key_9 = 'Ferragem'
key_10 = 'Rebaixo'
Lista_Acabamento = [key_6, key_7, key_8, key_9, key_10]

frame_impressao = [
    [Sg.CB('Jato-de-Tinta', key='Jato-de-Tinta')],
    [Sg.CB('Laser', key='Laser')],
    [Sg.CB('Indigo', key='Indigo')],
    [Sg.CB('Serigrafia', key='Serigrafia')],
    [Sg.CB('Latterpress', key='Latterpress')]]

key_11 = 'Jato-de-Tinta'
key_12 = 'Laser'
key_13 = 'Indigo'
key_14 = 'Serigrafia'
key_15 = 'Latterpress'
Lista_Impressao = [key_11, key_12, key_13, key_14, key_15]

frame_papelao = [
    [Sg.Radio('0,6mm', "RADIO1", key='0,6mm'), Sg.Radio('1,2mm', "RADIO1", key='1,2mm'),
     Sg.Radio('1,5mm', "RADIO1", key='1,5mm'), Sg.Radio('1,8mm', "RADIO1", key='1,8mm')],
    [Sg.Radio('2,0mm', "RADIO1", key='2,0mm'), Sg.Radio('2,3mm', "RADIO1", key='2,3mm'),
     Sg.Radio('2,5mm', "RADIO1", key='2,5mm'), Sg.Radio('2,8mm', "RADIO1", key='2,8mm')]]

key_16 = '0,6mm'
key_17 = '1,2mm'
key_18 = '1,5mm'
key_19 = '1,8mm'
key_20 = '2,0mm'
key_21 = '2,3mm'
key_22 = '2,5mm'
key_23 = '2,8mm'
Lista_Papelao = [key_16, key_17, key_18, key_19, key_20, key_21, key_22, key_23]

caract_projeto = [Sg.Frame('Tipo de Projeto  ', frame_tipo, key='t_projeto'),
                  Sg.Frame('Acabamento', frame_acabamento, key='t_acabamento'),
                  Sg.Frame('Tipo de Impressão', frame_impressao, key='t_impressao')],

papelao_capa = [Sg.Frame('Espessura do Papelão da Capa', frame_papelao, key='t_papelao')],
