from pdfplumber import PDF
from pathlib import Path
from gtts import gTTS

#Функция, озвучивающая .pdf и сохраняющая его в .mp3 файл
#A function that voices a .pdf and saves it to an .mp3 file
def pdf_to_mp3(file_path = "test.pdf", language = "en", save_path=r"C:\\User"):
    # Если файл существует и имеет расширение .docx то выполняем тело функции иначе return
    #If the file exists and has the extension .docx, then execute the body of the function, else return
    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":
        print(f"[+] File {Path(file_path).name} was successfully found and is being processed...")
        #Открываем .pdf файл и сохраняем весь его текст в массив
        #Open a .pdf file and save all its text in an array
        with PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        #С помощью метода join конкатируем все элементы в строку
        #Use the join method to concatenate all elements into a string
        text_from_file = ''.join(pages)
        #Заменяем переносы строк на пробелы
        #Replace line breaks with spaces
        text_from_file = text_from_file.replace("\n", ' ')
        #Озвучиваем текст с помощью Google Text-to-Speech
        #Voicing text with Google Text-to-Speech
        voice_out_pdf_file = gTTS(text=text_from_file, lang=language)
        #Название файла без его расширения
        #The final path component, without its suffix
        mp3_file_name = Path(file_path).stem
        #Сохранение файла в формате .mp3
        # Saving a file in .mp3 format
        save_path = save_path.replace('\\', '\\\\')
        print(f"[+] The {mp3_file_name}.mp3 file is being saved now. This may take some time...")
        voice_out_pdf_file.save(f"{save_path}/{mp3_file_name}.mp3")
        print(f"[+] File {mp3_file_name}.mp3 was successfully saved in {save_path}. Thank you for using my script! (o˘◡˘o) (codded by KlimmedSoul. Link to my GitHub => https://github.com/KlimmedSoul)")
        return True
    else: 
        print("[+] File are occured or not exists. (codded by KlimmedSoul. Link to my GitHub => https://github.com/KlimmedSoul)")
        return False