import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

import random

class drive_control_publisher(Node):

    def __init__(self):

        rclpy.init()
        super().__init__('drive_control_publisher')

        self.drive_control_period = 1/30      # Period for 30Hz
        self.drive_control_timer = self.create_timer(self.drive_control_period, self.drive_control_publish_callback)

        qos_profile = QoSProfile(depth=10)
        self.drive_control_publisher = self.create_publisher(Twist, '/cmd_vel', qos_profile)
        self.drive_control = Twist()

        self.NodeName = self.get_name()
        self.get_logger().info('{0} started'.format(self.NodeName))

    def drive_control_publish_callback(self):

        try:

            if rclpy.ok():

                self.drive_control.linear = Vector3(x=random.uniform(0, 3))
                self.drive_control.angular = Vector3(z=random.uniform(0, 3))

                self.drive_control_publisher.publish(self.drive_control)

                self.get_logger().info('Publish : {}'.format(self.drive_control))

        except KeyboardInterrupt:
            pass

def main(args=None):

    drive_control_pub_node = drive_control_publisher()

    rclpy.spin(drive_control_pub_node)

if __name__ == '__main__':

    main()