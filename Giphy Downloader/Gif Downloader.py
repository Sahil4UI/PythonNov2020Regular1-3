import urllib.request as url
import json

choice = input("Enter Gif you wanna Download...")
choice = choice.replace(" ","+")

path = "https://api.giphy.com/v1/gifs/search?q="+choice+"&api_key=VcVTKDqklqKuCkrIsWgbdRj4XnMulOIC"


res = url.urlopen(path)

data = json.load(res)

data = data['data']

for i in range(len(data)):
    img = data[i]['images']
    img_url = img['original']['url']


    url.urlretrieve(img_url,f'img{i}.gif')
    

