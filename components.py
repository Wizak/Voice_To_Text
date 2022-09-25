import PySimpleGUI as sg


def components():
    header_left_layout = [
        [
            sg.Text('Звуковий файл'),
            sg.In(size=(30, 1), disabled=True,
                  enable_events=True, key='-FILENAME READ-')
        ],
        [
            sg.FileBrowse(button_text='Вибрати файл', target='-FILENAME READ-', file_types=(
                ('Звуковий файл', '*.wav'),)),
            sg.Button('Видобути текст', enable_events=True,
                      key='-RECOGNITION-')
        ]
    ]
    header_right_layout = [
        [
            sg.Text('Файл для конвертації'),
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
                   element_justification='center'),
         sg.Column(header_right_layout, expand_x=True,
                   element_justification='center')]
    ]
    
    multiline_menu = ['', ['Зберегти тут']]
    body_layout = [
        [sg.Multiline(size=(100, 50), key='-TEXT-', autoscroll=True,
                      disabled=True, enable_events=True, right_click_menu=multiline_menu)]
    ]
    
    window_layout = [
        [sg.Column(header_layout, expand_x=True,
                   element_justification='center')],
        [sg.Column(body_layout, expand_x=True, element_justification='center')]
    ]
    
    return window_layout
