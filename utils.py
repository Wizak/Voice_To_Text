import os
import sys
import speech_recognition as sr

from pydub import AudioSegment


def convert_ogg_to_wav(file_path):
    input_file_path_splited = file_path.split('/')
    output_filename = input_file_path_splited[-1].replace('.ogg', '.wav')
    output_file_path = '/'.join(input_file_path_splited[:-1]) + \
        '/' + output_filename

    sound = AudioSegment.from_ogg(file_path)
    sound.export(output_file_path, format="wav")


def recognition(file_path, lang='uk-UA'):
    r = sr.Recognizer()
    audio_file = sr.AudioFile(file_path)

    with audio_file as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        recognited = r.recognize_google(audio, language=lang)

    return recognited


def save_extract_text(text, file_path=None):
    if file_path is None:
        file_path = os.path.join(os.getcwd(), 'Текст.txt')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


def get_file_path(filename):
    bundle_dir = getattr(
        sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    path_to_file = os.path.abspath(
        os.path.join(bundle_dir, 'static/' + filename))
    return path_to_file