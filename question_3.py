"""Question 3 
Create a program that uses a recursive function to generate a geometric pattern using 
Python's turtle graphics. The pattern starts with a regular polygon and recursively 
modifies each edge to create intricate designs. 
Pattern Generation Rules: 
For each edge of the shape: 
1. Divide the edge into three equal segments 
2. Replace the middle segment with two sides of an equilateral triangle pointing 
inward (creating an indentation) 
3. This transforms one straight edge into four smaller edges, each 1/3 the length of 
the original edge 
4. Apply this same process recursively to each of the four new edges based on the 
specified depth 
Visual Example: 
Depth 0: Draw a straight line (no modification) 
Depth 1: Line becomes: ——\⁄—— (indentation pointing inward) 
Depth 2: Each of the 4 segments from depth 1 gets its own indentation 
User Input Parameters: 
The program should prompt the user for: 
Number of sides: Determines the starting shape 
Side length: The length of each edge of the initial polygon in pixels 
Recursion depth: How many times to apply the pattern rules 
Example Execution: 
Enter the number of sides: 4 
Enter the side length: 300 
Enter the recursion depth: 3 """


import turtle
def draw_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_edge(t, length, depth - 1)
        t.left(60)
        draw_edge(t, length, depth - 1)
        t.right(120)
        draw_edge(t, length, depth - 1)
        t.left(60)
        draw_edge(t, length, depth - 1)
def draw_polygon(t, sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        draw_edge(t, length, depth)
        t.right(angle)



def main():
    #inputs from user
    sides = int(input("enter the number of sides: "))
    length = int(input("enter the side length: "))
    depth = int(input("enter the recursion depth: "))

    #settingup turtle
    screen = turtle.Screen()
    screen.title("recursive geometric pattern")
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed

    # it draws the polygon with recursive pattern
    draw_polygon(t, sides, length, depth)

    turtle.done()

if __name__ == "__main__":
    main()

            