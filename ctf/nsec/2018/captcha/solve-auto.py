import re

import cv2
import numpy as np
import requests
from IPython.display import display
from pytesseract import image_to_string
from scipy.misc import toimage


def request_captcha_test():
    headers = {'Content-type': 'image/png'}
    cookie = {
        'session': 'eyJibG9iIjp7IiBiIjoiTDFaR1ZsRlZRMG8zWjJwR2RsRnFVRmhOU21kdFFUMDkifX0.DeEzmQ.E6q0lzlAkeGeJ4FnLKzZXYFydoA'}
    img = requests.get('http://xn--5z8h.ctf:5000/captcha', cookies=cookie, headers=headers)

    if img.status_code == 200:
        img = img.content
    else:
        print('error: {}'.format(img.url))

    # print(image_to_string(Image.open(io.BytesIO(img))))
    return img


def send_captcha_test():
    url = 'http://xn--5z8h.ctf:5000/captcha'
    cookies = {
        'session': 'eyJibG9iIjp7IiBiIjoiTDFaR1ZsRlZRMG8zWjJwR2RsRnFVRmhOU21kdFFUMDkifX0.DeEzmQ.E6q0lzlAkeGeJ4FnLKzZXYFydoA'}
    data = {'captcha': '977rll'}

    with requests.Session() as s:
        r = s.post(url, cookies=cookies, data=data)
        # print(r.text)
        return requests.utils.dict_from_cookiejar(s.cookies)
        # print(requests.utils.dict_from_cookiejar(s.cookies))
        # rint(requests.utils.dict_from_cookiejar(r.cookies))


def request_captcha(cookie):
    headers = {'Content-type': 'image/png'}
    img = requests.get('http://xn--5z8h.ctf:5000/captcha', cookies=cookie, headers=headers)

    if img.status_code == 200:
        img = img.content
    else:
        print('error: {}'.format(img.url))

    # print(image_to_string(Image.open(io.BytesIO(img))))
    return img


def send_captcha(cookie, captcha):
    url = 'http://xn--5z8h.ctf:5000/captcha'
    data = {'captcha': captcha}

    with requests.Session() as s:
        r = s.post(url, cookies=cookie, data=data)
        print(re.search('<li>(.*?)</li>', r.text).group(1))
        return requests.utils.dict_from_cookiejar(r.cookies)


def clean_captcha(captcha):
    print(type(captcha))
    # Convert the image file to a Numpy array and read it into a OpenCV file.
    captcha = np.asarray(bytearray(captcha), dtype="uint8")

    # Grayscale
    captcha = cv2.imdecode(captcha, cv2.IMREAD_GRAYSCALE)

    # Let's first see what the original image looks like.
    # print('before:')
    # display(toimage(captcha))

    # Convert the captcha to black and white.
    (thresh, captcha) = cv2.threshold(captcha, 210, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Erode the image to remove dot noise and that wierd line. I use a 3x3 rectengal as the kernal.
    captcha = cv2.erode(captcha, np.ones((3, 3), dtype=np.uint8))

    # Convert the image to black and white and again to further remove noise.
    (thresh, captcha) = cv2.threshold(captcha, 210, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Some cosmetic
    captcha = cv2.fastNlMeansDenoising(captcha, h=30)

    # Turn the Numpy array back into a image
    captcha = toimage(captcha)
    captcha = captcha.resize([captcha.width * 10, captcha.height * 10])

    # Check the result of our cleaning process
    # print('after:')
    display(captcha)

    return captcha


def captcha_tostring(captcha):
    text = image_to_string(captcha, config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz -psm 6")
    # text = captcha
    text = re.sub('\|', 'l', text)
    text = text.replace("‘", "i")
    text = text.replace(" ", "")
    text = text.replace("]", "j")
    text = text.replace("><", "x")
    text = text.lower()
    print(text)
    return text


def new_captcha(cookie):
    img = request_captcha(cookie)
    captcha = clean_captcha(img)
    return captcha_tostring(captcha)


def solve():
    first_cookie = cookies = {
        'session': 'eyJibG9iIjp7IiBiIjoiTDFaR1ZsRlZRMG8zWjJwR2RsRnFVRmhOU21kdFFUMDkifX0.DeEzmQ.E6q0lzlAkeGeJ4FnLKzZXYFydoA'}
    next_cookie = send_captcha(first_cookie, '977rll')

    for i in range(5000):
        next_cookie = send_captcha(next_cookie, new_captcha(next_cookie))


if __name__ == '__main__':
    solve()
