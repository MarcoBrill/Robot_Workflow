import numpy as np
from robot_workflow import RobotPerceptionModule, PlanningControlModule

def generate_sensor_data():
    """
    Generate simulated sensor data (e.g., LiDAR or camera data).
    Output: Simulated sensor data as a 2D numpy array.
    """
    return np.random.rand(100, 100)  # Simulated 100x100 grid

def main():
    # Initialize modules
    perception_module = RobotPerceptionModule()
    control_module = PlanningControlModule()

    # Generate simulated sensor data
    sensor_data = generate_sensor_data()

    # Perception workflow
    print("Running SLAM...")
    map, robot_position = perception_module.slam(sensor_data)
    print(f"Map shape: {map.shape}, Robot Position: {robot_position}")

    print("Partitioning environment...")
    partitions = perception_module.partition_environment(map)
    print(f"Number of partitions: {len(partitions.vertices)}")

    print("Detecting obstacles...")
    obstacles = perception_module.detect_obstacles(sensor_data)
    print(f"Obstacles detected at: {obstacles}")

    # Planning & Control workflow
    goal = (90, 90)  # Example goal position
    print(f"Navigating from {robot_position} to {goal}...")
    path = control_module.navigate(map, robot_position, goal)
    print(f"Planned path: {path}")

    print("Generating motion commands...")
    commands = control_module.control_motion(path)
    print(f"Robot Commands: {commands}")

    print("Returning to charge...")
    charge_path = control_module.return_to_charge(map, robot_position)
    print(f"Path to charging station: {charge_path}")

    print("Avoiding obstacles...")
    safe_path = control_module.avoid_obstacles(map, obstacles)
    print(f"Safe path: {safe_path}")

if __name__ == "__main__":
    main()
