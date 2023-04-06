import math

#15°ごとのsin, cos, tanの値
angle = 0
while angle <= 360:
    print("sin"+ str(angle) + "°：")
    print(round(math.sin(math.radians(angle)), 4))
    print("cos"+ str(angle) + "°：")
    print(round(math.cos(math.radians(angle)), 4))
    print("tan"+ str(angle) + "°：")
    print(round(math.tan(math.radians(angle)), 4))
    angle += 15
