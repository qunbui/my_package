import launch import LaunchDescription 
import launch_ros.actions import Node 

def generate_launch_description(): 
    return LaunchDescription([ 
        Node( 
            package='demo_node_py', 
            executable='listener' 
        ) 
    ]) 