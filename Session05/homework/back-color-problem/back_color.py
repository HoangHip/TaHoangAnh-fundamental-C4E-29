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


def get_shapes():
    return shapes


def generate_quiz():
    text_set = []
    color_set = []
    for item in shapes:
        text_set.append(item['text'].upper())
        color_set.append(item['color'])

    text = choice(text_set)
    color = choice(color_set)
    quiz_type = randint(0, 1)

    return text, color, quiz_type
generate_quiz()
def mouse_press(x, y, text, color, quiz_type):
    x = pos
    
    return True

