temp = -5
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("Outdoor event is cancelled😭😭😭")
else:
    print("The outdoor event is on!!")

temp = 50
is_sunny = False
if temp > 45 and is_sunny:
    print("Its hot outsideho🥵🥵")
    print("Its sunny🌞🌞")
elif temp < 0 and is_sunny:
    print("Its cold outside")
    print("Its still sunny")
elif not is_sunny:
    print("Its cloudy outside☁️☁️")
