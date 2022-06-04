# -*- coding: utf-8 -*-

# checks if 3 given points are on one linear function


def handle_input(axis, point_number):
    entry = input(f"{axis}-Koordinate {point_number}. Punkt: ")
    return entry

def calculate_gradient(point_one, point_two):
    if point_one[0] > point_two[0]:
        y = point_one[1] - point_two[1]
        x = point_one[0] - point_two[0]
    else:
        y = point_two[1] - point_one[1]
        x = point_two[0] - point_one[0]
    return y / x


def main():
    nr_points = int(input("Wie viele Punkte sollen berechnet werden: "))
    points = []
    # collect coordinates of the points
    for i in range(1, nr_points+1):
        entry_x = handle_input("x", str(i))
        entry_y = handle_input("y", str(i))
        points.append([float(entry_x), float(entry_y)])
    print(points)
    
    # calculate the gradient
    j=0
    z=1
    gradient_list = []
    for i in points:
        if j < len(points)-1:
            gradient = calculate_gradient(points[j], points[z])
            gradient_list.append(gradient)
            j=j+1
            z=z+1
        else:
            pass
    print(gradient_list)

    # compare all gradients
    j=0
    z=1
    result = True
    for i in gradient_list:
        if j < len(gradient_list)-1:
            if gradient_list[j] != gradient_list[z]:
                result = False
                break
            j=j+1
            z=z+1       
        else:
            pass

    if result == True:
        print("Die Punkte liegen auf einer linearen Funktion")
    else:
        print("Die Punkte liegen nicht auf einer linearen Funktion")



if __name__ == "__main__":
    main()