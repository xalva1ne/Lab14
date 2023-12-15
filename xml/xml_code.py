import xml.etree.ElementTree as ET

number_tuple = (1,2,3,4,5,6,7,8,9,0)

counter = 0

for num in number_tuple:
    if num % 2 == 0:
        counter += 1

root = ET.Element("counter")

counter_element = ET.SubElement(root, "value")
counter_element.text = str(counter)

tree = ET.ElementTree(root)

with open("Lab14.xml", "wb") as file:
    tree.write(file)

with open("Lab14.xml", "r", encoding="utf-8") as file:
    result = file.read()
    print(result)