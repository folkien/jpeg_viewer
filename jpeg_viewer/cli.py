# bytes_to_jpeg/bytes_to_jpeg/cli.py

import argparse
import base64
from io import BytesIO
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description='Wyświetla obraz JPEG z podanego ciągu base64.')
    parser.add_argument('-i', '--input', required=True, help='Ciąg znaków zakodowany w base64 reprezentujący obraz JPEG.')
    args = parser.parse_args()

    try:
        # Dekodowanie ciągu base64 do bajtów
        image_data = base64.b64decode(args.input)
        
        # Otwarcie obrazu z wykorzystaniem BytesIO
        image = Image.open(BytesIO(image_data))
        
        # Wyświetlenie obrazu
        image.show()
    except Exception as e:
        print(f'Wystąpił błąd podczas przetwarzania obrazu: {e}')
