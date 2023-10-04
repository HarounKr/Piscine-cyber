import sys
import argparse
import os;
import requests

def parse_args() ->  argparse.Namespace:
    parser = argparse.ArgumentParser(description="The spider program allow you to extract all the images from a website, recursively, by providing a url as a parameter")
    parser.add_argument("URL", help='url to be scraped', type=str)
    parser.add_argument("-r", "--recursive", help="recursively downloads the images in a URL received as a parameter.", action="store_true")
    parser.add_argument("-l", "--level", help="maximum depth level of the recursive download.If not indicated, it will be 5", type=int, default=5)
    parser.add_argument("-p", "--path", help=": indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used", type=str, default="./data/")

    args = parser.parse_args()
    return args

def print_params(args) -> None:
    print("depth level: ", args.level, "\npath: ", args.path, "\nURL: ", args.URL)

def spider(args):
    if not os.path.exists(args.path):
        os.mkdir(args.path)
    r = requests.get(url=args.URL)
    print(r.text)

def main():

    args = parse_args()
    if args.recursive:
        print_params(args=args)
        try:
            spider(args=args)
        except Exception as e:
            print(e)
    else:
        print("The -r parameter must be specified")

if __name__ == '__main__':
    main()