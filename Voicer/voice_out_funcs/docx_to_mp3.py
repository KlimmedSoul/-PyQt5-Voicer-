from docx import Document
from pathlib import Path
from gtts import gTTS

#Функция, озвучивающая .docx и сохраняющая его в .mp3 файл
#A function that voices a .docx and saves it to an .mp3 file
def docx_to_mp3(file_path="test.docx", language="en", save_path=r"C:\\Users"):
    #Проверка на существование файла и на его расширение
    #Checking for the existence of a file and its extension
    if Path(file_path).is_file() and Path(file_path).suffix == ".docx":
        
        docx_document = Document(file_path)   
        print(f"[+] File {Path(file_path).name} was successfully found and is being processed...")
        full_text = []
        #Чтение файла и добавление всего текста в массив full_text
        #Reading a file and adding all text to the full_text array
        for parag in docx_document.paragraphs:
            full_text.append(parag.text)
        print("[+] File read successfully.")
        #С помощью метода join конкатируем все элементы в строку
        #Use the join method to concatenate all elements into a string
        text_from_file = ''.join(full_text)
        #Заменяем переносы строк на пробелы
        #Replace line breaks with spaces
        text_from_file = text_from_file.replace('\n', ' ')
        #Озвучиваем текст с помощью Google Text-to-Speech
        #Voicing text with Google Text-to-Speech
        voice_out_docx_file = gTTS(text=text_from_file, lang=language)
        #Название файла без его расширения
        #The final path component, without its suffix
        mp3_file_name = Path(file_path).stem
        #Сохранение файла в формате .mp3
        #Saving a file in .mp3 format
        print(f"[+] The {mp3_file_name}.mp3 file is being saved now. This may take some time...")
        voice_out_docx_file.save(f"{save_path}/{mp3_file_name}.mp3")
        print(f"[+] File {mp3_file_name}.mp3 was successfully saved in {save_path}. Thank you for using my script! (o˘◡˘o) (codded by KlimmedSoul. Link to my GitHub => https://github.com/KlimmedSoul)")
        return True
    else: 
        print("[+] File are occured or not exists. (codded by KlimmedSoul. Link to my GitHub => https://github.com/KlimmedSoul)")
        return False