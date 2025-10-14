import colorgram

rgb = []
colors = colorgram.extract('Color.jpeg', 7)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r,g,b)
    rgb.append(new_color)
print(rgb)