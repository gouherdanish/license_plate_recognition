import argparse
import pytesseract
import cv2

def ocr(img_path):
    pass

if __name__=='__main__':
    argparser = argparse.ArgumentParser(description="License Plate Recognition via Tesseract")
    argparser.add_argument(name='--img_path',type='str',required=True,help='Image path to be fed to OCR')

    args = argparser.parse_args()
    ocr(vars(*args))