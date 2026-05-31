import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleSubscriber(Node):
    def __init__(self):
        super().__init__('turtle_subscriber_node')
        # Create a subscriber listening to the '/turtle1/cmd_vel' topic
        self.subscription = self.create_subscription(
            Twist,
            '/turtle1/cmd_vel',
            self.listener_callback,
            10)
        self.get_logger().info('Turtle Subscriber Node has started!')

    def listener_callback(self, msg):
        # Print out the velocities whenever a message is received
        self.get_logger().info(f'Received Command -> Linear X: {msg.linear.x}, Angular Z: {msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
