import math
import matplotlib.pyplot as plt

x = 0.0
y = 0.0
theta = 0.0

trajectory = [(x, y, theta)]

print("Discrete Motion Model")
print("Commands: forward <distance>, left <angle>, right <angle>")
print("Type 'done' when finished.\n")

while True:
    command = input("Enter command: ")

    if command.lower() == "done":
        break

    parts = command.split()

    if len(parts) != 2:
        print("Invalid command. Use: forward <value>, left <value>, or right <value>")
        continue

    action = parts[0].lower()
    value = float(parts[1])

    initial_x = x
    initial_y = y
    initial_theta = theta

    if action == "forward":
        theta_rad = math.radians(theta)

        x = x + value * math.cos(theta_rad)
        y = y + value * math.sin(theta_rad)

    elif action == "left":
        theta = theta + value

    elif action == "right":
        theta = theta - value

    else:
        print("Invalid command. Use forward, left, or right.")
        continue

    theta = theta % 360

    trajectory.append((x, y, theta))

    print(
        f"Initial Pos: ({initial_x:.2f}, {initial_y:.2f}, {initial_theta:.2f}) "
        f"| Executing: {command} "
        f"| Final Pos: ({x:.2f}, {y:.2f}, {theta:.2f})"
    )

xs = [point[0] for point in trajectory]
ys = [point[1] for point in trajectory]
thetas = [point[2] for point in trajectory]

plt.figure(figsize=(8, 6))

plt.plot(xs, ys, marker="o", label="Trajectory")

plt.scatter(xs[0], ys[0], marker="s", s=100, label="Start")
plt.scatter(xs[-1], ys[-1], marker="X", s=100, label="End")

for x_pos, y_pos, angle in trajectory:
    angle_rad = math.radians(angle)

    plt.quiver(
        x_pos,
        y_pos,
        math.cos(angle_rad),
        math.sin(angle_rad),
        angles="xy",
        scale_units="xy",
        scale=1
    )

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Discrete Robot Trajectory")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()