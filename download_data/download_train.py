import requests, zipfile, io

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                print('one chunck')
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
    return local_filename

import requests
import shutil

def download_file2(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename


if __name__ == '__main__':
    url = 'https://www.kaggle.com/c/16880/datadownload/dfdc_train_part_00.zip'
    file_name = download_file2(url)
    print(file_name)