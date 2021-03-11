import os
import re
import time
from shutil import copyfile

import requests
from PIL import Image

cookies = {
    'PHPSESSID': '6d0db2cd2vrv651h42mo5md1gr',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

animal = {
    'result': 'animal'
}

thing = {
    'result': 'thing'
}

catchat = os.path.join(os.getcwd(), "/FLAG-bXlyZXBvc2l0b3J5dG9maW5kZmxhZ3M/NSEC2019/catchat")
things_path = os.path.join(catchat, "/samples/things")
animals_path = os.path.join(catchat, "/samples/animals")


def image_compare(i1, i2):
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

    ncomponents = i1.size[0] * i1.size[1] * 3
    return (dif / 255.0 * 100) / ncomponents


def in_things():
    result = False
    for filename in os.listdir(things_path):
        if filename.endswith(".png"):
            pre_result = image_compare(Image.open(os.path.join(catchat, "sample.png")),
                                       Image.open(os.path.join(things_path, filename)))
            if pre_result < 10:
                result = True
    print("in Things? " + str(result))
    return result


def if_wrong_save_image(congrats_regex, image_type="things"):
    if congrats_regex is None:
        print("new {}".format(image_type))
        new_image = "thing" + time.strftime("%Y%m%d-%H%M%S") + ".png"
        copyfile(os.path.join(catchat, "sample.png"),
                 os.path.join(os.path.join(catchat, "/samples/{}".format(image_type)), new_image))


def save_output():
    file = open("result.txt", "a")
    file.write(str(post.text))
    file.write("\n\n")


if __name__ == '__main__':
    while True:
        response = requests.get('http://vision.ctf/catchat.php', headers=headers, cookies=cookies)

        with open(os.path.join(catchat, "sample.png"), 'wb') as f:
            f.write(response.content)

        if not in_things():
            post = requests.post('http://vision.ctf/index.php', headers=headers, cookies=cookies, data=animal)
            status = re.search("(C.* 15 000<)+", str(post.content))
            if_wrong_save_image(status)

        else:
            post = requests.post('http://vision.ctf/index.php', headers=headers, cookies=cookies, data=thing)
            status = re.search("(C.* 15 000<)+", str(post.content))
            if_wrong_save_image(status, image_type="animals")

        save_output()

        try:
            print(status.group(0))
        except Exception as a:
            print("retry")
