sub_1 = int(input("enter the marks in c++ : "))
sub_2 = int(input("enter the marks in python : "))
sub_3 = int(input("enter the marks in data structure : "))


total = (sub_1+sub_2+sub_3)/3

if(total>79):
    print("you got first division ")
elif(total>59 and total<=79):
    print("you got second division ")
elif(total>49 and total<=59):
    print("you got third division ")
elif(total>=33 and total<=49):
    print("you got fourth division ")
else:
    print("failed!")