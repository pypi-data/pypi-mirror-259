
import os

from My_Package import Scan_PDF
from My_Package import Translate


def hi_babe():
    print('hi')


def main():
    print()
    print("-----------------------")
    print("Hello Packaging world !")
    print("-----------------------")
    print()
    
    
    
    input_file_path = input("Enter file path")
    input_file_path = input_file_path.replace('"', '').replace(os.sep, '/')
    
    path, file = os.path.split(input_file_path)
    target_filename =  "Anki_Flash_Cards_from_Highlights_of__" + file[:-2] + ".txt" 
    # os.chdir(os.path.expanduser('~/')+"x.txt"))     
    
    
    # input_file_path = input("Enter target file path")
    # input_file_path = input_file_path.replace('"', '').replace(os.sep, '/')
    
    print(input_file_path)
    highlighted_words = Scan_PDF.find_highlighted_words(input_file_path)
    print(highlighted_words)

    # Translate.Translate_and_Write_file(highlighted_words)
    
    
    

if __name__ == "__main__":
    main()