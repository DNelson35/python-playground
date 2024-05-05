import os
import random
import time

class Particle:
    def __init__(self, x, y, velocity, lifetime):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.lifetime = lifetime

    def update(self):
        self.y += self.velocity
        self.lifetime -= 1

    def is_alive(self):
        return self.lifetime > 0

def generate_particles(grid_width, grid_height, num_particles):
    particles = []
    for _ in range(num_particles):
        x = random.randint(0, grid_width - 1)
        y = random.normalvariate(grid_height / 2, grid_height / 4) # Normal distribution around the middle
        velocity = random.uniform(-1, 1) # Example velocity, adjust as needed
        lifetime = random.randint(10, 50) # Example lifetime, adjust as needed
        particles.append(Particle(x, y, velocity, lifetime))
    return particles

def create_grid(grid_width, grid_height, particles):
    grid = [[' ' for _ in range(grid_width)] for _ in range(grid_height)]
    for particle in particles:
        if particle.is_alive():
            # Convert the y position to an integer, rounding to the nearest integer
            y_int = round(particle.y)
            # Ensure the y position is within the grid bounds
            y_int = max(0, min(y_int, grid_height - 1))
            # Ensure the x position is within the grid bounds
            x_int = max(0, min(particle.x, grid_width - 1))
            # Place a character in the grid based on the particle's position and lifetime
            grid[y_int][x_int] = 'S' if particle.lifetime > 10 else ' '
    return grid


def display(grid):
    os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
    for row in grid:
        print(''.join(row))

def main():
    grid_width = 7
    grid_height = 5
    num_particles = 100
    particles = generate_particles(grid_width, grid_height, num_particles)

    max_iterations = 500 # Adjust based on how long you want the simulation to run
    for _ in range(max_iterations):
        for particle in particles:
            particle.update()
        grid = create_grid(grid_width, grid_height, particles)
        display(grid)
        time.sleep(0.1) # Adjust the speed of the simulation

if __name__ == "__main__":
    main()
