import pytesseract
from PIL import Image

img = Image.open("login.png")
text = pytesseract.image_to_string(img)


def image_ocr(image_path, output_txt_file_name):
    image_text = pytesseract.image_to_string(image_path, lang='eng+ces', config='--psm 1')
    with open(output_txt_file_name, 'w+', encoding='utf-8') as f:
        f.write(image_text)

image_ocr("login.png", "text.txt")
print(text)


def rot(*symbols):
    def _rot(n):
        encoded = ''.join(sy[n:] + sy[:n] for sy in symbols)
        lookup = str.maketrans(''.join(symbols), encoded)
        return lambda s: s.translate(lookup)

    return _rot


def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)


def rot_encode(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)


# print(rot_encode(7)(text))
# print(7, rot_encode(7)('vtxlt'))

if __name__ == '__main__':
    pass
