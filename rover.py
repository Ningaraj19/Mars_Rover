class Command:
    def execute(self):
        pass

class MoveCommand(Command):
    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        self.rover.move()

class LeftCommand(Command):
    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        self.rover.turn_left()

class RightCommand(Command):
    def __init__(self, rover):
        self.rover = rover

    def execute(self):
        self.rover.turn_right()

class Rover:
    def __init__(self, x, y, direction, grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid

    def move(self):
        new_x, new_y = self.x, self.y

        if self.direction == 'N':
            new_y += 1
        elif self.direction == 'S':
            new_y -= 1
        elif self.direction == 'E':
            new_x += 1
        elif self.direction == 'W':
            new_x -= 1

        if not self.grid.has_obstacle(new_x, new_y) and self._is_within_bounds(new_x, new_y):
            self.x, self.y = new_x, new_y

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def _is_within_bounds(self, x, y):
        return 0 <= x < self.grid.size and 0 <= y < self.grid.size

class Grid:
    def __init__(self, size, obstacles=[]):
        self.size = size
        self.obstacles = obstacles

    def has_obstacle(self, x, y):
        return any(obstacle.x == x and obstacle.y == y for obstacle in self.obstacles)

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class StatusReport:
    def generate_report(self, rover):
        obstacle_detected = rover.grid.has_obstacle(rover.x, rover.y)
        report = f"Rover is at ({rover.x}, {rover.y}) facing {rover.direction}."

        if obstacle_detected:
            report += " Obstacle detected."
        else:
            report += " No obstacles detected."

        return report

grid = Grid(10, [Obstacle(2, 2), Obstacle(3, 5)])
rover = Rover(0, 0, 'N', grid)
commands = [MoveCommand(rover), MoveCommand(rover), RightCommand(rover), MoveCommand(rover), LeftCommand(rover), MoveCommand(rover)]

# Execute the commands
for command in commands:
    command.execute()
# Generate status report
report_generator = StatusReport()
report = report_generator.generate_report(rover)

# Print the report
print(report)



#output: Rover is at (1, 3) facing N. No Obstacles detected.
