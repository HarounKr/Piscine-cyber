import argparse
import os
import glob
import requests

extensions = (
    '.jpg', '.rtf', '.doc', '.js', '.sch', '.3dm', '.jsp', '.sh', '.3ds', '.key',
    '.sldm', '.3g2', '.lay', '.sldm', '.3gp', '.lay6', '.sldx', '.7z', '.ldf', '.slk',
    '.accdb', '.m3u', '.sln', '.aes', '.m4u', '.snt', '.ai', '.max', '.sql', '.ARC',
    '.mdb', '.sqlite3', '.asc', '.mdf', '.sqlitedb', '.asf', '.mid', '.stc', '.asm',
    '.mkv', '.std', '.asp', '.mml', '.sti', '.avi', '.mov', '.stw', '.backup', '.mp3',
    '.suo', '.bak', '.mp4', '.svg', '.bat', '.mpeg', '.swf', '.bmp', '.mpg', '.sxc',
    '.brd', '.msg', '.sxd', '.bz2', '.myd', '.sxi', '.c', '.Myi', '.sxm', '.cgm',
    '.nef', '.sxw', '.class', '.odb', '.tar', '.cmd', '.odg', '.tbk', '.cpp', '.odp',
    '.tgz', '.crt', '.ods', '.tif', '.cs', '.odt', '.tiff', '.csr', '.onetoc2', '.txt',
    '.csv', '.ost', '.uop', '.db', '.otg', '.uot', '.dbf', '.otp', '.vb', '.dch',
    '.ots', '.vbs', '.der', '.ott', '.vcd', '.dif', '.p12', '.vdi', '.dip', '.PAQ',
    '.vmdk', '.djvu', '.pas', '.vmx', '.docb', '.pdf', '.vob', '.docm', '.pem', '.vsd',
    '.docx', '.pfx', '.vsdx', '.dot', '.php', '.wav', '.dotm', '.pl', '.wb2', '.dotx',
    '.png', '.wk1', '.dwg', '.pot', '.wks', '.edb', '.potm', '.wma', '.eml', '.potx',
    '.wmv', '.fla', '.ppam', '.xlc', '.flv', '.pps', '.xlm', '.frm', '.ppsm', '.xls',
    '.gif', '.ppsx', '.xlsb', '.gpg', '.ppt', '.xlsm', '.gz', '.pptm', '.xlsx', '.h',
    '.pptx', '.xlt', '.hwp', '.ps1', '.xltm', '.ibd', '.psd', '.xltx', '.iso', '.pst',
    '.xlw', '.jar', '.rar', '.zip', '.java', '.raw'
)

def args_parser() ->  argparse.Namespace:
    parser = argparse.ArgumentParser(description="The spider program allow you to extract all the images from a website, recursively, by providing a url as a parameter")
    parser.add_argument("-r", "--reverse", help="to reverse the infection", type=str, )
    parser.add_argument("-v", "--version", help="version of the programe", action="store_true")
    parser.add_argument("-s", "--silent", help="the program will not produce any output.", action="store_true")

    args = parser.parse_args()
    return args


def main():
    args = args_parser()
    if args.version:
        print("version: 1.1")
    else:
        allfiles = []
        for file in os.listdir():
            if file != "stockholm.py" and file != "Makefile" and file != "README.md":
                print(file)
            # if file.endswith(extensions):

if __name__ == '__main__':
    main()