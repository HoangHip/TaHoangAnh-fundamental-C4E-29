from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]
color = '#4CAF50'
x = 100
y = 140

text_set = []
for item in shapes:
    text_set.append(item['text'].upper())
    text = choice(text_set)
print(text)
for item in shapes:
    if item['text'] == text.lower:
        rect = item['rect']
        print(rect)
        print(rect[0])
        print(rect[0]+rect[2])
        print(rect[1]+rect[3])
        if x in range(rect[0], rect[0]+rect[2]):
            if y in range(rect[1], rect[1]+rect[3]):
                print("T")


            else:
                print(1)
        else:
            print(2)
