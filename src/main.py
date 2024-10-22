import argparse
import pytesseract
import cv2

def read(img_path):
    img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    return img

def ocr(img_path):
    img = read(img_path)
    extract = pytesseract.image_to_string(img)
    return extract

if __name__=='__main__':
    argparser = argparse.ArgumentParser(description="License Plate Recognition via Tesseract")
    argparser.add_argument('--img_path',type=str,required=True,help='Image path to be fed to OCR')

    args = argparser.parse_args()
    text = ocr(**vars(args))
    print(text)