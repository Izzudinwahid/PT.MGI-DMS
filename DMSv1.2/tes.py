# import RPi.GPIO as GPIO
# 
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# 
# GPIO.setup(17,GPIO.OUT)
# GPIO.setup(27,GPIO.OUT)
# # GPIO.setwarnings(False)
# 
# 
# GPIO.output(17,1)
# GPIO.output(27,1)

tes = [0,1]


for i in range(0,2):
    tes.pop(i)
    print(tes)
