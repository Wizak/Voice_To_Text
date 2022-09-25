import PySimpleGUI as sg

from components import components

from utils import convert_ogg_to_wav
from utils import recognition
from utils import save_extract_text
from utils import get_file_path


def window_program():
    EXTRACT = ''

    layout = components()
    icon = get_file_path('icon.ico')
    window = sg.Window('Аудіо в Текст', layout, size=(800, 600), icon=icon)
    timeout = int(1000/60)

    while True:
        event, values = window.read(timeout=timeout)

        if event == sg.WIN_CLOSED:
            break

        if event == '-RECOGNITION-':
            if values['-FILENAME READ-'] != '':
                EXTRACT = recognition(values['-FILENAME READ-'])
                window['-TEXT-'].update(EXTRACT)
            else:
                sg.Popup('Оберіть звуковий файл для видобування тексту',
                         title='Помилка !')

        if event == '-CONVERTATION-':
            if values['-FILENAME CONVERT-'] != '':
                convert_ogg_to_wav(values['-FILENAME CONVERT-'])
            else:
                sg.Popup('Оберіть звуковий файл для конвертації',
                         title='Помилка !')

        if event == 'Зберегти тут':
            save_extract_text(EXTRACT)

    window.close()


if __name__ == '__main__':
    window_program()
