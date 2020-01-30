import requests, zipfile, io

url = 'https://github.com/NumberPiOso/deepFake/raw/master/read.zip'
req = requests.get(url)
file = zipfile.ZipFile(io.BytesIO(req.content))
file.extractall()
