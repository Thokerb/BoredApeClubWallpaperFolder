# This is a sample Python script.
import requests
import json
import random
import ctypes
import os
from PIL import Image

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    label = "bored-bunny--nft"
    folderName = f"C:/Temp/{label}"
    if not os.path.exists(folderName):
        os.mkdir(folderName)

    for i in range(0, 1):
        offset = 50*i
        url = f'https://api.opensea.io/api/v1/assets?order_direction=desc&offset={offset}&format=json&limit=50&collection={label}'

        response = requests.request("GET", url)
        collection = json.loads(response.text)
        assets = collection["assets"]
        counter = 0

        for asset in assets:
            image_url = asset["image_url"]
            response = requests.get(image_url)
            fileName = f'wallpaper_{label}_{asset["id"]}.png'
            fileName = os.path.join(folderName, fileName)

            file = open(fileName, "wb")
            absPath = file.name
            file.write(response.content)
            file.close()
            old_im = Image.open(fileName)
            old_im = old_im.resize((508, 508), Image.ANTIALIAS)
            # old_im.save(fileName)
            # old_im = Image.open(fileName)
            old_size = old_im.size

            new_size = (1920, 1080)
            new_im = Image.new("RGB", new_size)  ## luckily, this is already black!
            new_im.paste(old_im, ((new_size[0] - old_size[0]) // 2,
                                  (new_size[1] - old_size[1]) // 2))
            new_im.save(fileName)
            counter = counter + 1
            print(os.path.abspath(absPath))
        # just use last, cant set diashow with python :(
        # ctypes.windll.user32.SystemParametersInfoW(20, 0, fileName, 0)
