import tkinter as tk

# Define the colors for each face of the cube
COLORS = {
    'white': 'white',
    'yellow': 'yellow',
    'red': 'red',
    'orange': 'orange',
    'blue': 'blue',
    'green': 'green',
}

class CubeVisualizer(tk.Tk):
    def __init__(self, cube):
        super().__init__()

        self.cube = cube

        # Create a canvas to draw the cube
        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.pack()

        # Draw the cube on the canvas
        self.draw_cube()

    def draw_cube(self):
        side_size = 100
        gap = 10
        x_offset = 100
        y_offset = 100

        for row in range(3):
            for col in range(3):
                x0 = col * (side_size + gap) + x_offset
                y0 = row * (side_size + gap) + y_offset
                x1 = x0 + side_size
                y1 = y0 + side_size

                # Get the color of the current cell in the green side
                color = self.cube.sides[GREEN_SIDE][row][col]

                # Draw a rectangle with the corresponding color
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=COLORS[color])
