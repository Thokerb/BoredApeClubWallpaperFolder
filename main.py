# This is a sample Python script.
import requests
import json
import random
import ctypes
import os
from PIL import Image

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    offset = random.randint(0, 200)
    url = f'https://api.opensea.io/api/v1/assets?order_direction=desc&offset={offset}&limit=20&collection=boredapeyachtclub'

    response = requests.request("GET", url)
    collection = json.loads(response.text)
    assets = collection["assets"]
    counter = 0
    if not os.path.exists("C:/Temp/BoredApeClubWallpaper"):
        os.mkdir("C:/Temp/BoredApeClubWallpaper")

    for asset in assets:
        image_url = asset["image_original_url"]
        response = requests.get(image_url)
        fileName = f'wallpaper_boredape_{asset["id"]}.png'
        fileName = os.path.join("C:/Temp/BoredApeClubWallpaper", fileName)

        file = open(fileName, "wb")
        absPath = file.name
        file.write(response.content)
        file.close()
        old_im = Image.open(fileName)
        old_size = old_im.size

        new_size = (1920, 1080)
        new_im = Image.new("RGB", new_size)  ## luckily, this is already black!
        new_im.paste(old_im, ((new_size[0] - old_size[0]) // 2,
                              (new_size[1] - old_size[1]) // 2))
        new_im.save(fileName)
        counter = counter + 1
        print(os.path.abspath(absPath))
    # just use last, cant set diashow with python :(
    #ctypes.windll.user32.SystemParametersInfoW(20, 0, fileName, 0)

