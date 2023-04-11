import numpy as np
import open3d as o3d

def create_cylinder(radius, height, resolution=20):
    cylinder = o3d.geometry.TriangleMesh.create_cylinder(radius, height, resolution)
    return cylinder

def create_sphere(radius):
    sphere = o3d.geometry.TriangleMesh.create_sphere(radius)
    return sphere

# Robot arm parameters
link1_length = 1
link2_length = 0.8
joint_radius = 0.1
link_radius = 0.05

# Create robot arm links
link1 = create_cylinder(link_radius, link1_length)
link2 = create_cylinder(link_radius, link2_length)

# Position robot arm links
link1.translate((0, link1_length / 2, 0))
link2.translate((0, link1_length + link2_length / 2, 0))

# Create joints
joint1 = create_sphere(joint_radius)
joint2 = create_sphere(joint_radius)
joint2.translate((0, link1_length, 0))

# Combine geometry for visualization
robot_arm = [link1, link2, joint1, joint2]

# Visualize the robot arm
o3d.visualization.draw_geometries(robot_arm)
