import pyqrcode
import png

source_url = "https://github.com/dayatarvibha"
url = pyqrcode.create(source_url)
url.svg("mygithub.svg", scale = 8)
url.png('mygithub.png', scale = 8)