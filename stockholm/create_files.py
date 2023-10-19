import xml.etree.ElementTree as gfg  
import sys
import csv
from faker import Faker
import requests

def GenerateXML(fileName) : 
    root = gfg.Element("Catalog") 
      
    m1 = gfg.Element("mobile") 
    root.append(m1) 
      
    b1 = gfg.SubElement(m1, "brand") 
    b1.text = "Redmi"
    b2 = gfg.SubElement(m1, "price") 
    b2.text = "6999"
      
    m2 = gfg.Element("mobile") 
    root.append (m2) 
      
    c1 = gfg.SubElement(m2, "brand") 
    c1.text = "Samsung"
    c2 = gfg.SubElement(m2, "price") 
    c2.text = "9999"
      
    m3 = gfg.Element("mobile") 
    root.append (m3) 
      
    d1 = gfg.SubElement(m3, "brand") 
    d1.text = "RealMe"
    d2 = gfg.SubElement(m3, "price") 
    d2.text = "11999"
      
    tree = gfg.ElementTree(root) 
      
    with open (fileName, "wb") as files : 
        tree.write(files) 
  
def GenerateCSV():
    fake = Faker()
    number_of_records = 50

    with open('random-person.csv', mode='w') as file:
        file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(['first_name', 'last_name', 'age', 'adress'])

        for _ in range(number_of_records):
            file_writer.writerow([fake.first_name(), fake.last_name(), fake.numerify("@#"), fake.address()])

def GenerateCfile():
    C_code = '#include <stdio.h>\n#include <string.h>\n\nint main() { \n\n  const char *src = "Hello world";\n  char dest[100];\n  strcpy(dest, src);  printf("%s\\n", dest);\n  return 0;\n}'
    with open("str_copy.c", mode='w') as file:
        file.write(C_code)

def GenerateTXT():
    with open("lorem_ipsum.txt", mode='w') as file:
        file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nMorbi in ante fringilla, fermentum urna ac, fermentum dolor. \nCurabitur non auctor erat. Nullam tempor metus sed placerat eleifend. \nFusce sagittis venenatis diam, a porttitor augue posuere vel. \nVestibulum elit massa, viverra ac elit id, sagittis euismod erat. Quisque eget euismod purus. In nec nunc sed sem lacinia dignissim. \nUt eu urna in nibh scelerisque vulputate a quis nulla. \nSed ligula nulla, vulputate at enim a, porttitor maximus lorem. Curabitur vestibulum viverra lorem non placerat.")

def GenerateJPG():
    url = "https://www.shutterstock.com/image-vector/motor-scrapper-truck-dual-tone-260nw-2246737611.jpg"
    data = requests.get(url).content
    with open("image.jpg", mode = 'wb') as file:
        file.write(data)

if __name__ == "__main__":  
    GenerateXML("Catalog.xml")
    GenerateCSV()
    GenerateCfile()
    GenerateTXT()
    GenerateJPG()