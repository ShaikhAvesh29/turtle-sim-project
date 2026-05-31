import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtlePublisher(Node):
    def __init__(self):
        super().__init__('turtle_publisher_node')
        # Create a publisher that sends Twist messages to the '/turtle1/cmd_vel' topic
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        # Set a timer to publish a command every 0.5 seconds
        self.timer = self.create_timer(0.5, self.send_velocity)
        self.get_logger().info('Turtle Publisher Node has started!')

    def send_velocity(self):
        msg = Twist()
        msg.linear.x = 2.0   # Speed (Move forward at 2.0 m/s)
        msg.angular.z = 1.0  # Turn rate (Turn left at 1.0 rad/s)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtlePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
