import argparse
from robot import  Robot


parser = argparse.ArgumentParser(description='Calculate the area that a Robot avoid EMP Mines would go to')

parser.add_argument('--c','-c', metavar='condition', type=int, nargs='+',
                   help='an integer to show the condition or danger zone for the Robot',required=True)
args = parser.parse_args()
condition = args.c[0]

robot = Robot(condition)
print("The area that can be travelled by the Robot, given the condition of {} is ......".format(condition))
print("*"*condition*2)
print(robot.get_access_area())
print("*"*condition*2)