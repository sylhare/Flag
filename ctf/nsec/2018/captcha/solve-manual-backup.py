import os
import re
import subprocess

import requests
from PIL import Image
from pytesseract import image_to_string


def request_captcha(cookie):
    headers = {'Content-type': 'image/png'}
    img = requests.get('http://xn--5z8h.ctf:5000/captcha', cookies=cookie, headers=headers)

    if img.status_code == 200:
        img = img.content
    else:
        print('error: {}'.format(img.url))

    # print(image_to_string(Image.open(io.BytesIO(img))))
    return img


def send_captcha(request_cookie, captcha):
    url = 'http://xn--5z8h.ctf:5000/captcha'
    data = {'captcha': captcha}

    with requests.Session() as s:
        r = s.post(url, cookies=request_cookie, data=data)
        print(r.text)
        response_msg = re.search('<li>(.*?)</li>', r.text).group(1)
        response_cookie = requests.utils.dict_from_cookiejar(r.cookies)
        print("*********")
        print("Request Cookie: " + str(request_cookie))
        print("Data: " + str(data))
        print(response_msg)
        print("Response Cookie: " + str(response_cookie))
        print("*********")
        if "ERROR" in response_msg:
            return request_cookie
        if "have 5001 success" in response_msg:
            quit()
        return response_cookie


def clean_captcha(captcha):
    open('captcha.png', 'wb').write(captcha)
    os.system('convert captcha.png -compress none -threshold 99% img.png')
    os.system('convert captcha.png -negate -lat 20x20+2% -negate img1.png')
    os.system('convert captcha.png -unsharp 50x50 -negate -lat 50x50+5% -negate img2.png')
    os.system('./textcleaner  -e stretch -o 30 captcha.png img3.png')

    im = Image.open('img.png')
    im.save("img.pbm")


def captcha_tostring():
    img_text = []
    img_text.append(clean_text(subprocess.getoutput('gocr -m 2 -C "0123456789abcdefghijklmnopqrstuvwxyz" img.pbm')))
    img_text.append(clean_text(image_to_string(Image.open("img.png"),
                                               config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz -psm 6")))
    img_text.append(clean_text(image_to_string(Image.open("img1.png"),
                                               config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz -psm 6")))
    img_text.append(clean_text(image_to_string(Image.open("img2.png"),
                                               config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz -psm 6")))
    img_text.append(clean_text(image_to_string(Image.open("img3.png"),
                                               config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz -psm 6")))

    return img_text


def clean_text(text):
    text = re.sub('\|', 'l', text)
    text = text.replace("'", "i")
    text = text.replace(" ", "")
    text = text.replace("]", "j")
    text = text.replace("><", "x")
    return text.lower()


def new_captcha(cookie):
    img = request_captcha(cookie)
    clean_captcha(img)
    return captcha_tostring()


# ol92r9
# Sucess, you currently have 13 success. You need 5000 for the flag
# {'session': 'eyJibG9iIjp7IiBiIjoiVmt0QlFtUXlMME5JV2t0MFZHbHBURE4yTVhvM1FUMDkifX0.DeH3Tw.sPthtxjRyfyHZk1B1FXoShH4qUA'}
# kdl2hf
def solve():
    # 99
    first_cookie = cookies = {
        'session': 'eyJibG9iIjp7IiBiIjoiYkZBM0wzVkxTMU12YTNvMlpFRndPVFJzTDJkS2R6MDkifX0.DeIp2g.Wmpbvc8-zXrAkMQAgHDJgOrc2uo'}
    response_cookie = send_captcha(first_cookie, 'tvepjy')
    request_cookie = response_cookie

    for i in range(5000):
        img_text = new_captcha(request_cookie)
        print(str(img_text))
        for i in img_text:
            response_cookie = send_captcha(request_cookie, i)
            if response_cookie != request_cookie:
                break
        if response_cookie == request_cookie:
            while response_cookie == request_cookie:
                Image.open('img.png').show()
                captcha_manual = input("What is the captcha?")
                response_cookie = send_captcha(request_cookie, captcha_manual)
        request_cookie = response_cookie


if __name__ == '__main__':
    solve()
