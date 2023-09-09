from pathlib import Path
from gtts import gTTS
#Функция, озвучивающая .txt и сохраняющая его в .mp3 файл
#A function that voices a .pdf and saves it to an .mp3 file
def txt_to_mp3(file_path="text.txt", language="en", save_path = r"C:\\User"):
    if Path(file_path).is_file() and Path(file_path).suffix == ".txt":
        #Открываем текстовый файл для чтения
        #Open a text file for reading
        txt_file = open(f"{file_path}", mode = 'r', encoding="utf-8")
        print(f"[+] File {Path(file_path).name} was successfully found and is being processed...")
        #Записываем весь текст в переменную и заменяем переносы строк на пробелы
        #Write all text into a variable and replace line breaks with spaces
        text_from_file = txt_file.read()
        text_from_file = text_from_file.replace('\n', ' ')
        #Озвучиваем текст с помощью Google Text-to-Speech
        #Voicing text with Google Text-to-Speech
        voice_out_txt_file = gTTS(text=text_from_file, lang=language)
        #Название файла без его расширения
        #The final path component, without its suffix
        mp3_file_name = Path(file_path).stem
        #Сохранение файла в формате .mp3
        #Saving a file to .mp3 format
        save_path = save_path.replace('\\', '\\\\')
        print(f"[+] The {mp3_file_name}.mp3 file is being saved now. This may take some time...")
        voice_out_txt_file.save(f"{save_path}/{mp3_file_name}.mp3")
        print(f"[+] File {mp3_file_name}.mp3 was successfully saved in {save_path}. Thank you for using my script! (o˘◡˘o) (codded by KlimmedSoul. Link to my GitHub => https://github.com/KlimmedSoul)")
        return True
    else: 
        print("[+] File are occured or not exists. (codded by KlimmedSoul. Link to my GitHub => https://github.com/KlimmedSoul)")
        return False