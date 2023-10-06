from bs4 import BeautifulSoup
import argparse
import os;
import requests
import sys
import html
import time
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
pattern = r'^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$'

def args_parser() ->  argparse.Namespace:
    parser = argparse.ArgumentParser(description="The spider program allow you to extract all the images from a website, recursively, by providing a url as a parameter")
    parser.add_argument("URL", help='url to be scraped', type=str)
    parser.add_argument("-r", "--recursive", help="recursively downloads the images in a URL received as a parameter", action="store_true", )
    parser.add_argument("-l", "--level", help="maximum depth level of the recursive download.If not indicated, it will be 5", type=int, default=5)
    parser.add_argument("-p", "--path", help=": indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used", type=str, default="./data/")

    args = parser.parse_args()
    return args

def print_params(args) -> None:
    print("\nURL:", args.URL, "\npath:", args.path, "\ndepth level:", args.level, '\n')
    if (args.level < 0):
        print("Negative numbers are not valid.")
        sys.exit(0)

def get_file_name(path, f_id) -> str:
    path_parse = requests.utils.urlparse(path).path
    split_parsed_path = path_parse.split('/')
    listlen = len(split_parsed_path)
    return str(f_id) + '-' + split_parsed_path[listlen - 1]

def get_src_urls(args, level) -> list:
    src_urls = []

    for i in range(1, level + 1):
        sys.stdout.write(f'\rProcessing page {i}/{level}')
        sys.stdout.flush()
        url = str(args.URL) + f"?page={i}"
        response = requests.get(url=url, headers=headers, stream=True)
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.findAll('img')
        for image in images:
            if 'src' in image.attrs:
                src = html.unescape(image['src'])
                if re.match(pattern, src):
                    src_urls.append(src)
    return src_urls

def progress_bar(downloaded, total):
    bar_length = 100
    progress = (downloaded / total)
    barre = '=' * int(round(progress * bar_length)-1)
    spaces = ' ' * (bar_length - len(barre))
    
    sys.stdout.write('\rDownload images: [{}] {:.2f}%'.format(barre + spaces, progress * 100))
    sys.stdout.flush()

def spider(args) -> None:
    level = args.level
    downloaded = 0

    if not os.path.exists(args.path):
        os.mkdir(args.path)
    src_urls = get_src_urls(args=args, level=level)
    total_images = len(src_urls)
    time.sleep(0.5)
    print('\n')
    f_id = 0
    for src_url in src_urls:
        filename = get_file_name(path=src_url, f_id=f_id)
        data = requests.get(src_url).content
        f = open(args.path + filename, 'wb')
        f.write(data)
        f.close()
        f_id += 1
        downloaded += 1
        progress_bar(downloaded=downloaded, total=total_images)
        time.sleep(0.1)                 

def main():
    args = args_parser()
    if args.recursive:
        print_params(args=args)
        try:
            spider(args=args)
        except Exception as e:
            print(e)
    else:
        print("spider.py: error: the following arguments are required: -r")

if __name__ == '__main__':
    main()