import PySimpleGUI as sg

from components import components

from utils import convert_ogg_to_wav
from utils import recognition
from utils import save_extract_text
from utils import get_file_path
from utils import get_lang_tags


def window_program():
    EXTRACT = ''
    timeout = int(1000/60)
    
    layout = components()
    lang_tags = get_lang_tags()
    icon = get_file_path('icon.ico')
    
    window = sg.Window('Аудіо в Текст', layout, size=(800, 600), icon=icon)

    while True:
        event, values = window.read(timeout=timeout)

        if event == sg.WIN_CLOSED:
            break

        if event == '-RECOGNITION-':
            if values['-FILENAME READ-'] != '':
                chs_lang_tag = values['-CHOOSE LANG TAG-']
                
                if chs_lang_tag in lang_tags:
                    lang = lang_tags[chs_lang_tag]
                    try:
                        EXTRACT = recognition(values['-FILENAME READ-'], lang=lang)
                        window['-TEXT-'].update(EXTRACT)
                    except Exception as e:
                        sg.Popup('Короткий або довгий аудіо файл!', title='Помилка !')
                        
                else:
                    sg.Popup('Неправильно обрана мова!',
                         title='Помилка !')
            else:
                sg.Popup('Оберіть звуковий файл для видобування тексту',
                         title='Помилка !')

        if event == '-CONVERTATION-':
            if values['-FILENAME CONVERT-'] != '':
                convert_ogg_to_wav(values['-FILENAME CONVERT-'])
            else:
                sg.Popup('Оберіть звуковий файл для конвертації',
                         title='Помилка !')
        
        if event == '-CHOOSE LANG TAG-':
            chs_lang_tag = values['-CHOOSE LANG TAG-']
            window['-CHOOSE LANG TAG-'].update(chs_lang_tag)
        
        if event == 'Зберегти тут':
            save_extract_text(EXTRACT)

    window.close()


if __name__ == '__main__':
    window_program()
