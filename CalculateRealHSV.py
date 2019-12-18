import math

def rgb_to_hsv(r, g, b):
    #Convert rgb 0-255 to 0-1
    r, g, b = r/255.0, g/255.0, b/255.0

    #Find max and min of r,g,b
    mx = max(r, g, b)
    mn = min(r, g, b)

    #Calculate the difference of max and min
    df = mx-mn

    #4 different posibilities to find h
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360

    #2 different posibiliies to find s
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100

    v = mx*100
    return h, s, v