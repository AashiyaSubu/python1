class assignment1():
    def subfieldsinAI():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processin")
    def oddeven():
        num1=int(input("Enter the number"))
        if (num1%2==0):
            print("Even")
            message="Even"
            return message
        else:
            print("Odd")
            message="Odd"
            return message


    def avrg ():
        eng=int(input("Enter the English mark"))
        tam=int(input("Enter the Tamil mark"))
        mat=int(input("Enter the Maths mark"))
        sci=int(input("Enter the Science mark"))
        sst=int(input("Enter the SST mark"))
           
        total=eng+tam+mat+sci+sst
        percent=total/5
        return(percent)
    def triangle():
        a=int(input("Enter the side1 width"))
        b=int(input("Enter the side2 width"))
        c=int(input("Enter the side3 width"))
        area=(a*b)/2
        perimeter=a+b+c
        print("Area of a triangle is")
        print(area)
        print("Perimeter of a triangle is")
        print(perimeter)
        return(area,perimeter)
       
    def bmi1():
        bmi=int(input("Enter the bmi:  "))
        if(bmi < 18.5):
            print("Underweight")
            res="Underweight"        
        elif(18.5 <= bmi <=25):
            print("Normal")
            res="Normal"
        elif(25 <= bmi <= 35):
            print("Overweight")
            res="Overweight"
        else:
            print("Obesity")
            res="Obesity"
        return res