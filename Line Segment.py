import math

point1x = float(input("Point 1 x-value: "))
point1y = float(input("Point 1 y-value: "))
ratio1 = float(input("Enter left side ratio: "))
ratio2 = float(input("Enter right side ratio: "))
point2x = float(input("Point 2 x-value: "))
point2y = float(input("Point 2 y-value: "))
def line_segment_length():
    length = math.sqrt(((point2x - point1x)**2) + ((point2y - point1y)**2))
    return length

def section_point():
    x_value = ((ratio1*point2x) + (ratio2*point1x))/(ratio1 + ratio2)
    y_value = ((ratio1*point2y) + (ratio2*point1y))/(ratio1 + ratio2)
    section_point = (x_value, y_value)
    return section_point

def line_midpoint():
    x_value = ((point1x + point2x)/2)
    y_value = ((point1y + point2y)/2)
    midpoint = (x_value , y_value)
    return midpoint

print("Length: ",line_segment_length(), "Midpoint: ",line_midpoint(), "Section Point: ",section_point())
