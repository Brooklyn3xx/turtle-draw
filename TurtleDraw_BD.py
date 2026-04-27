import turtle
import math

# Set up the turtle window
screen = turtle.Screen()
screen.setup(450, 450)
screen.title("TurtleDraw")
screen.setworldcoordinates(-200, -200, 200, 200)

# Create turtle
t = turtle.Turtle()
t.hideturtle()
t.pensize(2)
t.speed(0) # maximum speed

# Ask for file
filename = input("Enter the file name: ")
file = open(filename, "r")

# Setup variables
t.penup()
first_point = True
total_distance = 0
previous_x = 0
previous_y = 0

# Read file
for line in file:
    line = line.strip()
    parts = line.split()

    if line == "stop":
        t.penup()
        first_point = True
    else:
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        t.color(color)

        if first_point:
            t.goto(x, y)
            t.pendown()
            first_point = False
        else:
            distance = math.sqrt((x - previous_x) ** 2 + (y - previous_y) ** 2)
            total_distance += distance
            t.goto(x, y)

        previous_x = x
        previous_y = y   

file.close()

t.penup()
t.goto(60, -190)
t.color("black")
t.write("Total distance: " + str(round(total_distance, 2)), font=("Arial", 10, "normal"))

input("Press Enter to close the window...")
   
# Keep window open
screen.bye()