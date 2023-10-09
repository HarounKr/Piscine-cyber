from PIL import Image, IptcImagePlugin
from PIL.ExifTags import TAGS
import sys

def main() -> int:

    try:
        for i in range(1, len(sys.argv)):
            image = Image.open(sys.argv[i])
            info_dict = {
                "Filename": image.filename,
                "Image Size": image.size,
                "Image Height": image.height,
                "Image Width": image.width,
                "Image Format": image.format,
                "Image pixels": image.getpixel((0,0)),
                "Image Mode": image.mode,
                "Image is Animated": getattr(image, "is_animated", False),
                "Frames in Image": getattr(image, "n_frames", 1)
            }
            for label,value in info_dict.items():
                print(f"{label:25}: {value}")
            exifdata = image._getexif()
            if exifdata:
                for tagid in exifdata:
                    tag = TAGS.get(tagid, tagid)
                    data = exifdata.get(tagid)
                    if isinstance(data, bytes):
                        data = data.decode()
                    print(f"{tag:25}, {data}")
                if i != len(sys.argv) - 1:
                    print("\n")
            else:
                exif = "Exif"
                print(f"{exif:25}: No exif data")
    except Exception as e:
        print(e)
    
    return 0
    
if __name__ == '__main__':
    main()