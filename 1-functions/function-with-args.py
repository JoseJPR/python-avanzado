def calcule_perimeter(side_1, side_2, side_3, side_4):
    perimeter = side_1 + side_2 + side_3 + side_4
    return perimeter

perimeter = calcule_perimeter(1, 2, 1, 2)
print(perimeter)
 
def calcule_perimeter_with_args(*args):
    print(args)
    perimeter = 0
    for side in args:
        perimeter += side
    return perimeter

perimeter_with_args = calcule_perimeter_with_args(1, 2, 1, 2, 5)
print(perimeter_with_args)