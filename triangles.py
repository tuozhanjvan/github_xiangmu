import math
while True:
    a=float(input("a="))
    b=float(input("b="))
    c=float(input("c="))
    if a<=0 or b<=0 or c<=0:
        print("真是人才")
    elif a+b<=c or a+c<=b or b+c<=a:
        print("《三角形》")
    else:
        print("python:triangle, geometry, mathematics")
        print("结果：")
        def calculate_angles(a, b, c):
            angle_A=math.acos((b**2+c**2-a**2)/(2*b*c))
            angle_B=math.acos((a**2+c**2-b**2)/(2*a*c))
            angle_C=math.acos((a**2+b**2-c**2)/(2*a*b))
            return math.degrees(
            angle_A), math.degrees(angle_B), math.degrees(angle_C)
        angles = calculate_angles(a, b, c)
        print(f"  ∠ A = {angles[0]:.2f}°")
        print(f"  ∠ B = {angles[1]:.2f}°")
        print(f"  ∠ C = {angles[2]:.2f}°")
        print("  ∠ A的余弦值为", (b**2+c**2-a**2)/(2*b*c))
        print("  ∠ B的余弦值为", (a**2+c**2-b**2)/(2*a*c))
        print("  ∠ C的余弦值为", (a**2+b**2-c**2)/(2*a*b))
        if (angles[0]<90 and angles[1]<90 and angles[2]<90):
            print("    锐角三角形")
        elif (angles[0]==90 or angles[1]==90 or angles[2]==90):
            print("    直角三角形")
        else:
            print("    钝角三角形")
        if a==b==c:
            print("    等边三角形")
        elif a==b or a==c or b==c:
            print("    等腰三角形")
        print("   周长为", a+b+c)
        print("   面积为:", pow((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c),0.5), "   by hailungongshi")
    print("")
    print("")