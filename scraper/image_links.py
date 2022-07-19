from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://go.updates.iata.org/l/123902/2022-04-21/fqjqt3')
bs = BeautifulSoup(html, 'html.parser')

images_img_src = bs.find_all('img', {'src':re.compile('.png|.svg|.jpg')})
images_img_srcset = bs.find_all('img', {'srcset':re.compile('.png|.svg|.jpg')})
images_sorce_srcset = bs.find_all('source', {'srcset':re.compile('.png|.svg|.jpg')})
images_img_lazy = bs.find_all('img', {'data-lazy':re.compile('.png|.svg|.jpg')})

# for image in images_img_src: 
#     print(image['src'])
for image in images_img_srcset: 
    print(image['srcset'])
# for image in images_sorce_srcset: 
#     print(image['srcset'])
# for image in images_img_lazy: 
#     print(image['data-lazy'])
