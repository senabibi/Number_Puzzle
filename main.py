def div():
    is_ok=True
    while is_ok:
        number=input("Input a large whole number:")
        while not number.isdigit():
            print("Input a large whole number.Try again.")
            number=input("Input a large whole number:")
        div=input("Input the div (whole number):")
        while not(div.isdigit()): 

            print("Input must be whole number.Try again.")
            div=input("Input the div (whole number):")
        if int(div)>=0:    
            if len(number)%int(div)==0:
               number=str(number)
               div=int(div)
               my=[]
               
               sub=len(number)/int(div)
               for i in range(0,len(str(number)),int(sub)):
                   
                   my.append(number[i:i+int(sub)])
               print(*my,sep=",")        
            else:
                print(f"{number} must be evenly divisible by {div}\nTry again.")
div()

