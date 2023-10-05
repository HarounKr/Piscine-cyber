from bs4 import BeautifulSoup
import argparse
import os;
import requests
import sys
import html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

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

def spider(args):
    url = args.URL
    if not os.path.exists(args.path):
        os.mkdir(args.path)
    response = requests.get(url=url, headers=headers)
    url_parse = requests.utils.urlparse(url=url)
    new_url = url_parse.scheme + '://' + url_parse.netloc
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        span = soup.find(class_= 'JO4Dw2C5EjCB3iovKUcw')
        pages = int(span.text)
        if args.level > pages:
            print("The number of levels exceeds the number of pages.")
            sys.exit(0)
        sources = soup.findAll('source')
        for source in sources:
            print(html.unescape(source['srcset']), '\n\n')

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