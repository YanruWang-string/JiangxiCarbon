import os
import re
import sys
from pathlib import Path
import requests

python_root = Path(sys.executable).parent  # python安装目录

base_url = 'http://npm.taobao.org/mirrors/chromedriver/'  # chromedriver在国内的镜像网站
version_re = re.compile(r'^[1-9]\d*\.\d*.\d*')  # 匹配前3位版本信息


def get_chrome_version():
    """通过/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version 查询Chrome版本号"""

    try:
        result = os.popen('/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version').read()
        version = result.split()[2]
        return '.'.join(version.split('.')[:-1])
    except Exception as e:
        return '0.0.0'  # 没有安装Chrome浏览器


def get_chrome_driver_version():
    try:
        result = os.popen('chromedriver --version').read()
        version = result.split()[1]
        return '.'.join(version.split('.')[:-1])
    except Exception as e:
        return '0.0.0'  # 没有安装ChromeDriver


def get_latest_chrome_driver(chrome_version):
    url = f'{base_url}LATEST_RELEASE_{chrome_version}'
    latest_version = requests.get(url).text
    download_url = f'{base_url}{latest_version}/chromedriver_mac64_m1.zip'

    # 下载chromedriver zip文件
    response = requests.get(download_url)
    local_file = python_root / 'chromedriver.zip'
    with open(local_file, 'wb') as zip_file:
        zip_file.write(response.content)

    # 解压缩zip文件到python安装目录
    command = 'unzip -o {}/{} -d {}'.format(python_root, 'chromedriver.zip', python_root)
    os.system(command)

    # 解压缩完成后删除zip文件
    local_file.unlink()


def check_chrome_driver_update():
    chrome_version = get_chrome_version()
    driver_version = get_chrome_driver_version()
    if chrome_version == driver_version:
        print('No need to update')
    else:
        try:
            get_latest_chrome_driver(chrome_version)
        except Exception as e:
            print(f'Fail to update: {e}')


if __name__ == '__main__':
    check_chrome_driver_update()

