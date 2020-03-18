import sys
import rospy
from geometry_msgs.msg import Twist
from gpar_hulk_HDC2450 import *
import math

max_vel = 25000 #rpm
dist_hulk = -1  #averiguar
raio_hulk = -1  #averiguar

def recieveData(vel):

    v = vel.linear.x * max_vel
    w = vel.angular.z * max_vel

    vd_rad = (v+w*dist_hulk)
    ve_rad = (v-w*dist_hulk)

    vd = vd_rad/max_vel *1000
    ve = ve_rad/max_vel *1000

    vd_linear = (vd_rad*60/(2*math.pi*raio_hulk))
    ve_linear = (ve_rad*60/(2*math.pi*raio_hulk))

    #ESCREVE NA SERIAL VD E VE


def main():
    rospy.init_node('gpar_hulk_controll', anonymous=True)
    rospy.Subscriber('/hulk_move', String, recieveData())

    '''SCRIPT PARA INICIALIZAÇÃO DO DRIVER
       ENTRADA DA VELOCIDADE MAXIMA,
       ACELERAÇÃO E DESACELERAÇÃO,
       ETC... 
    '''


    rospy.spin()

if __init__ == '__main__':
    try:
        main()
    except:
        rospy.ROSInterruptException:
            pass