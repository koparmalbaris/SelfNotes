import xml.etree.ElementTree as ET
import sys


tree = ET.parse(sys.argv[1])
root = tree.getroot()

readonly = []
writable = []
password = []
printer = []

def print_list(lists):
    for item in lists:
        print("\t" + item)

for items in root.findall("items"):
    item = items.findall("item")
    for itemler in item:
        ip = itemler.find("ip-address")
        folders = itemler.find("folders")
        for folder in folders:
            if(folder.attrib['attributes'] == "readonly"):
                readonly.append("\\\\"+ip.text+"\\"+folder.text)
            if(folder.attrib['attributes'] == "writable"):
                writable.append("\\\\"+ip.text+"\\"+folder.text)
            if(folder.attrib['attributes'] == "password"):
                password.append("\\\\"+ip.text+"\\"+folder.text)
            if(folder.attrib['attributes'] == "printer"):
                printer.append("\\\\"+ip.text+"\\"+folder.text)
print("Writable Shares:\n")
print_list(writable)
print("\nReadonly Shares:\n")
print_list(readonly)
print("\nPrinter Shares:\n")
print_list(printer)
print("\nWith Password Shares:\n")
print_list(password)