import requests
import sys

# image generation
url = "https://thispersondoesnotexist.com/"
r = requests.get(url)
name = sys.argv[1]
print(name)
file = r"C:\Users\USER\Downloads\ism\images\{}.png".format(name)
#file = f"C:\\Users\\USER\\Downloads\\ism\\images\\{name}.png"
with open(file,'wb') as f: 
    f.write(r.content) 
print("Done")

