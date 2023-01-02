from utils import get_lang_tags

import PySimpleGUI as sg


def header_components():
    combo_box_lang = get_lang_tags()
    combo_box_lang_keys = list(combo_box_lang.keys())
    header_left_layout = [
        [
            sg.Text('Звуковий файл'),
            sg.In(size=(44, 1), disabled=True,
                  enable_events=True, key='-FILENAME READ-')
        ],
        [
            sg.Text('Мова', size=(4, 1)),
            sg.Combo(combo_box_lang_keys, size=(20, 1), default_value='Ukrainian (Ukraine)', enable_events=True, key='-CHOOSE LANG TAG-'),
            sg.FileBrowse(button_text='Вибрати файл', target='-FILENAME READ-', file_types=(
                ('Звуковий файл', '*.wav'),)),
            sg.Button('Видобути текст', enable_events=True,
                      key='-RECOGNITION-')
        ]
    ]
    header_right_layout = [
        [
            sg.Text('Файл конвертації'),
            sg.In(size=(30, 1), disabled=True,
                  enable_events=True, key='-FILENAME CONVERT-')
        ],
        [
            sg.FileBrowse(button_text='Вибрати файл', target='-FILENAME CONVERT-', file_types=(
                ('Звукові файли', '*.ogg *.mp3'),)),
            sg.Button('Конвертувати файл', enable_events=True,
                      key='-CONVERTATION-')
        ]
    ]
    header_layout = [
        [sg.Column(header_left_layout, expand_x=True,
                   element_justification='left'),
         sg.Column(header_right_layout, expand_x=True,
                   element_justification='left')]
    ]
    return header_layout

def body_components():
    multiline_menu = ['', ['Зберегти тут']]
    body_layout = [
        [sg.Multiline(size=(100, 50), key='-TEXT-', autoscroll=True,
                        disabled=True, enable_events=True, right_click_menu=multiline_menu)]
    ]
    return body_layout

def components():
    head_layout = header_components()
    body_layout = body_components()
    
    window_layout = [
        [sg.Column(head_layout, expand_x=True,
                   element_justification='center')],
        [sg.Column(body_layout, expand_x=True, element_justification='center')]
    ]
    
    return window_layout
