import sys
import rospy
from geometry_msgs.msg import Twist


'''
TODOS AS FUNÇÕES SERÃO ALTERADAS QUANDO ESTIVER 
FEITO A PARTE DE ENVIO E LEITURA PELA SERIAL.
'''

class getValue():
    def readMotorAmps():
        #RECEBER OS DADOS E RETORNAR UM VETOR COM O VALOR DOS DOIS DADOS
        return '?A '

    def readBatteryAmps():
        return '?BA R:'

    def readEncoderCounteAbsolute(motorch)
        return '?C ' + str(motorch)

    def readEncoderCountRelative(motorch):
        return '?CR '+str(motorch)

    def readClosedLoopError(motorch):
        return '?E ' + str(motorch)    
    
    def readFeedback(motorch):
        return '?F ' +str(motorch)

    def readMotorPowerOutputApplied(motorch):
        return '?P '+str(motorch)

    def readEncoderMotorSpeedinRPM(motorch):
        return '?S ' +str(motorch)

    def readEncoderSpeedRelative(motorch):
        return '?SR ' +str(motorch)

    def readTemperature(channel)
    '''channel 1: MCU
        channel 2: channel1 side
        channel 3: channel2 side'''
        return '?T ' str(channel)

     def readPositionRelativeTracking(motorch)
        return '?TR ' +str(motorch)

class setCommand():
    def setAceleration(motorch, acel):
    #Acceleration value is in 0.1 * RPM per second.    
        return '!AC ' + str(motorch) +' '+ str(acel)

    def setEncoderCounters(motorch, conter):
        return '!C '+str(motorch)+' '+str(conter)
        
    def setDeceleration(motorch, deccel):
    #Decceleration value is in 0.1 * RPM per second    
        return '!DC '+str(motorch)+' '+str(deccel)

    def goToSpeed(motorch, vel):
        return '!G '+str(motorch)+' '+str(vel)

    def setMotorSpeed(motorch, speed):
        return '!S '+ str(motorch)+' '+str(speed)

    def readVolts(sensor):
    ''' 1 : Internal volts
        2 : Battery volts
        3 : 5V output'''  
        return '?V '+str(sensor)

    



class hdc2450(object):
    """docstring for hdc245."""
    getValue   getValue
    setCommand setCommand
    SAFETYKEY = '321654987'

    def __init__(self):
        super(hdc245, self).__init__()
        
    def reset():
        cmd = '%RESET' + SAFETYKEY

    def emergencyStop():
        return '!ES'

    def emergencyStopReleased():
        return '!MG'