speed = float(input('შეიყვანეთ მანქანის სიჩქარე (კმ/სთ): '))

if speed<30:
    print("Slow")
elif speed < 60:
    print("Moderate")
elif speed < 120:
    print("Fast")
else:
    print("Very fast")