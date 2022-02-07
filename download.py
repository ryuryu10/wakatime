from bs4 import BeautifulSoup
import urllib.request as req # 특정 웹사이트로 접속하기 위해
import pyvips

url = "http://127.0.0.1:5000/page1"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser') #분석 용이하게 파싱
print(soup)
image = pyvips.Image.new_from_file(soup, dpi=300)
image.write_to_file("img.png")
