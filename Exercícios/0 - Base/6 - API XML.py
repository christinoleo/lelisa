import xml.etree.ElementTree as ET
tree = ET.parse('casa.xml')
root = tree.getroot()

# imprime o dono
print(root[0].text)

#imprime os adjuntos
for pessoa in root.iter('pessoa'):
    print(pessoa.text)

#imprime os nomes dos animais
for animal in root.iter('animal'):
    print(animal.find('nome').text)

# imprime os tipos de animais (sem repetir)
tipos = []
for animal in root.iter('animal'):
    if animal.find('tipo').text not in tipos:
        tipos = tipos + [animal.find('tipo').text]
print (tipos)

#imprime quantas pessoas & animais tem na casa
num = 0
for child in root:
    if child.tag != 'adjuntos':
        num = num + 1

for pessoa in root.iter('pessoa'):
            num = num + 1

print(num)

