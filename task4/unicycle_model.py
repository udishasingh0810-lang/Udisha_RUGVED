import math
import matplotlib.pyplot as plt

# Initial robot pose
x = 0.0
y = 0.0
theta = 0.0

dt = 0.01

trajectory = [(x, y, theta)]

print("Continuous Unicycle Model")
print("Enter: linear_velocity angular_velocity duration")
print("Example: 1.0 0.5 5")
print("Angular velocity is in rad/s")
print("Type 'done' when finished.\n")

while True:
    command = input("Enter velocity command: ")

    if command.lower() == "done":
        break

    parts = command.split()

    if len(parts) != 3:
        print("Invalid command. Use: v omega duration")
        continue

    v = float(parts[0])
    omega = float(parts[1])
    duration = float(parts[2])

    initial_x = x
    initial_y = y
    initial_theta = theta

    print(
        f"Initial State: "
        f"(x={initial_x:.2f}, y={initial_y:.2f}, "
        f"theta={math.degrees(initial_theta):.2f}°)"
    )

    steps = int(duration / dt)

    for _ in range(steps):

        x = x + v * math.cos(theta) * dt
        y = y + v * math.sin(theta) * dt
        theta = theta + omega * dt

        trajectory.append((x, y, theta))

    theta = theta % (2 * math.pi)

    print(
        f"Final State: "
        f"(x={x:.2f}, y={y:.2f}, "
        f"theta={math.degrees(theta):.2f}°)\n"
    )

xs = [point[0] for point in trajectory]
ys = [point[1] for point in trajectory]

plt.figure(figsize=(8, 6))

plt.plot(xs, ys, label="Continuous Trajectory")

plt.scatter(
    xs[0],
    ys[0],
    marker="s",
    s=100,
    label="Start"
)

plt.scatter(
    xs[-1],
    ys[-1],
    marker="X",
    s=100,
    label="End"
)

plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.title("Continuous Unicycle Model Trajectory")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()