print("--------------------------")
print("| BIRTHDATE MAGIC SQUARE |")
print("--------------------------")
print("UNLIKE RAMANUJAN'S MAGIC SQUARE WHICH ONLY CONTAINS 24 COMBINATIONS")
print("THE MAGIC SQUARE CONTAINS 26 POSSIBLE COMBINATIONS.")

while True :
    choose = input("TRY WITH YOUR BIRTHDATE NUMBER(i) OR GENERATE WITH RANDOM NUMBERS(o) or QUIT(q) :: ") 
    if choose=="i" :
        print("AVOID GIVING SAME NUMBERS OR ELSE THE MAGIC SQUARE CONTAINS SAME NUMBER")
        a = -1
        while a<0 or a>32 :
             a = int(input("Enter birth date number : "))
        b = -1
        while b<0 or b>13 :
             b =int(input("Enter birth month number : "))
        z = 0
        while z < 1000:
             z =int(input("Enter your birth year : "))
        c = int(z/100)
        d = z-c*100

    elif choose=="o" :
        import random
        a = random.randint(0,100)
        b = random.randint(0,100)
        z = random.randint(999,10000)
        c = int(z/100)
        d = z-c*100
        if a==b==c==d :
            a = random.randint(0,100)
            b = random.randint(0,100)
            z = random.randint(999,10000)
            c = int(z/100)
            d = z-c*100
    elif choose == 'q':
        break
    else :
        print("type 'i','o' or 'q'")
        continue

    s = a+b+c+d
    row = [a,b,c,d]
    
    n = "|      "*4 
    if (s/2)*10-(s//2)*10==0 :
        x =[2*b+c, s//2, a-d]
        row1 =[x[0]-a, a+d-2*b, 2*b, a-b]
        row2 =[x[1]-c, x[1]-d, x[1]-a, x[1]-b ]
        row3 =[x[1]-2*b, x[1]+(b-a), x[1]+a-(x[0]), x[1]+2*b-x[2]]
    else :
        x =[2*b+c, s//2, a+d]
        row1 =[x[0]-a, a+d-2*b, 2*b, a-b]
        row2 =[x[1]-c+1, x[1]-d, x[1]-a+1, x[1]-b ]
        row3 =[x[1]-2*b, x[1]+(b-a)+1, x[1]+a-(x[0]), x[1]+2*b+1-x[2]]
        '''
        if row==row1 or row==row2 and r:
            row1 =[x[0]-a, a+d-2*b, 2*b, a-b]
            row2 =[x[1]-c, x[1]-d+1, x[1]-a, x[1]-b+1 ]
            row3 =[x[1]-2*b+1, x[1]+(b-a), x[1]+a-(x[0])+1, b+x[0]-x[1]]
        else :
            row1 =[x[0]-a, a+d-2*b, 2*b, a-b]
            row2 =[x[1]-c+1, x[1]-d, x[1]-a+1, x[1]-b ]
            row3 =[x[1]-2*b, x[1]+(b-a)+1, x[1]+a-(x[0]), b+x[0]-x[1]+1]
    '''
    #------------------------------1
    if int(a/10)==0 :
        l1 = " "
        box1 = "|  "+l1+str(a)+"  "
    else :
        l1 = ""
        box1 = "|  "+l1+str(a)+"  "
    
    if int(b/10)==0 :
        k1 = "   "
        box2 = "|"+k1+str(b)+"  "
    else :
        k1 = "  "
        box2 = "|"+k1+str(b)+"  "
    
    if int(c/10)==0 :
        k2 = "   "
        box3 = "|"+k2+str(c)+"  "
    else :
        k2 = "  "
        box3 = "|"+k2+str(c)+"  "
    
    if int(d/10)==0 :
        k3 = "   "
        box4 = "|"+k3+str(d)+"  |"
    else :
        k3 = "  "
        box4 = "|"+k3+str(d)+"  |"
     
    #--------------------------------2
    
    if int(row1[0]/10)==0 and row1[0]>=0 and row1[0]<100:
        l2 = " "
        box5 = "|  "+l2+str(row1[0])+"  "
    else :
        if int(-row1[0])<10 and row1[0]<100:
            l2 = ""
            box5 = "|  "+l2+str(row1[0])+"  "
        else :
            l2 = ""
            box5 = "| "+l2+str(row1[0])+"  "
    
    if int(row1[1]/10)==0 and row1[1]>=0 and row1[1]<100:
        k4 = "   "
        box6 = "|"+k4+str(row1[1])+"  "
    else :
        if int(-row1[1])<10 and row1[1]<100:
            k4 = "  "
            box6 = "|"+k4+str(row1[1])+"  "
        else :
            k4 = " "
            box6 = "|"+k4+str(row1[1])+"  "
                
    
    
    if int(row1[2]/10)==0 and row1[2]>=0 and row1[2]<100:
        k5 = "   "
        box7 = "|"+k5+str(row1[2])+"  "
    else :
        if int(-row1[2])<10 and row1[2]<100:
            k5 = "  "
            box7 = "|"+k5+str(row1[2])+"  "
        else :
            k5 = " "
            box7 = "|"+k5+str(row1[2])+"  "
    
    if int(row1[3]/10)==0 and row1[3]>=0 and row1[3]<100:
        k6 = "   "
        box8 = "|"+k6+str(row1[3])+"  |"
    else :
        if int(-row1[3])<10 and row1[3]<100:
            k6 = "  "
            box8 = "|"+k6+str(row1[3])+"  |"
        else :
            k6 = " "
            box8 = "|"+k6+str(row1[3])+"  |"
    #-----------------------------------3
    
    if int(row2[0]/10)==0 and row2[0]>=0 and row2[0]<100:
        l3 = " "
        box9 = "|  "+l3+str(row2[0])+"  "
    else :
        if int(-row2[0])<10 and row2[0]<100:
            l3 = ""
            box9 = "|  "+l3+str(row2[0])+"  "
        else:
            l3 = ""
            box9 = "| "+l3+str(row2[0])+"  "
                
    
    
    if int(row2[1]/10)==0 and row2[1]>=0 and row2[1]<100:
        k7 = "   "
        box10 = "|"+k7+str(row2[1])+"  "
    else :
        if int(-row2[1])<10 and row2[1]<100:
            k7 = "  "
            box10 = "|"+k7+str(row2[1])+"  "
        else :
            k7 = " "
            box10 = "|"+k7+str(row2[1])+"  "
    
    if int(row2[2]/10)==0 and row2[2]>=0 and row2[2]<100:
        k8 = "   "
        box11 = "|"+k8+str(row2[2])+"  "
    else :
        if int(-row2[2])<10 and row2[2]<100:
            k8 = "  "
            box11 = "|"+k8+str(row2[2])+"  "
        else :
            k8 = " "
            box11 = "|"+k8+str(row2[2])+"  "    
    
    
    if int(row2[3]/10)==0 and row2[3]>=0 and row2[3]<100:
        k9 = "   "
        box12 = "|"+k9+str(row2[3])+"  |"
    else :
        if int(-row2[3])<10 and row2[3]<100:
            k9 = "  "
            box12 = "|"+k9+str(row2[3])+"  |"
        else :
            k9 = " "
            box12 = "|"+k9+str(row2[3])+"  |"    
    
    
    #-----------------------------------4
    
    if int(row3[0]/10)==0 and row3[0]>=0 and row3[0]<100:
        l4 = " "
        box13 = "|  "+l4+str(row3[0])+"  "
    else :
        if int(-row3[0])<10 and row3[0]<100:
            l4 = ""
            box13 = "|  "+l4+str(row3[0])+"  "
        else :
            l4 = ""
            box13 = "| "+l4+str(row3[0])+"  "
    
    if int(row3[1]/10)==0 and row3[1]>=0 and row3[1]<100:
        k10 = "   "
        box14 = "|"+k10+str(row3[1])+"  "
    else :
        if int(-row3[1])<10 and row3[1]<100:
            k10 = "  "
            box14 = "|"+k10+str(row3[1])+"  "
        else :
            k10 = " "
            box14 = "|"+k10+str(row3[1])+"  "
    
    
    if int(row3[2]/10)==0 and row3[2]>=0 and row3[2]<100:
        k11 = "   "
        box15 = "|"+k11+str(row3[2])+"  "
    else :
        if int(-row3[2])<10 and row3[2]<100:
            k11 = "  "
            box15 = "|"+k11+str(row3[2])+"  "
        else :
            k11 = " "
            box15 = "|"+k11+str(row3[2])+"  "
    
    if int(row3[3]/10)==0 and row3[3]>=0 and row3[3]<100:
        k12 = "   "
        box16 = "|"+k12+str(row3[3])+"  |" 
    else :
        if int(-row3[3])<10 and row3[3]<100:
            k12 = "  "
            box16 = "|"+k12+str(row3[3])+"  |"
        else :
            k12 = " "
            box16 = "|"+k12+str(row3[3])+"  |"
    
    #-------------------------------------
    
    print("*"*30)
    print("^"*30)
    print("^"*30)
    print("*"*30)
    
    #--------------------------------------
    print(" ------"*4+" ")
    print(n+"|")
    
    print(box1+box2+box3+box4)
    
    print(n+"|")
    print(" ------"*4+" ")
    print(n+"|")
    
    print(box5+box6+box7+box8)
    
    print(n+"|")
    print(" ------"*4+" ")
    print(n+"|")
    
    print(box9+box10+box11+box12)
    
    print(n+"|")
    print(" ------"*4+" ")
    print(n+"|")
    
    print(box13+box14+box15+box16)
    
    print(n+"|")
    print(" ------"*4+" ")
    #------------------------------
    print("*"*30)
    print("^"*30)
    print("^"*30)
    print("*"*30)
    print("_"*30)
    print("THE SUM OF ALL -26- POSSIBLE COMBINATIONS IN THE MAGIC SQUARE WILL BE "+str(s))
    print("------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------")
    #-----------------
    print("vertical combination-4 ,horizontal combination-4 ,diagonal combination -2")
    
    print("+===+===+===+===+                      +===+===+===+===+                      +===+===+===+===+")
    print("+ 1 + 2 + 3 + 4 +                      + 1 + 1 + 1 + 1 +                      + 1 +   +   + 2 +")
    print("+===+===+===+===+                      +===+===+===+===+                      +===+===+===+===+")
    print("+ 1 + 2 + 3 + 4 +                      + 2 + 2 + 2 + 2 +                      +   + 1 + 2 +   +")
    print("+===+===+===+===+                      +===+===+===+===+                      +===+===+===+===+")
    print("+ 1 + 2 + 3 + 4 +                      + 3 + 3 + 3 + 3 +                      +   + 2 + 1 +   +")
    print("+===+===+===+===+                      +===+===+===+===+                      +===+===+===+===+")
    print("+ 1 + 2 + 3 + 4 +                      + 4 + 4 + 4 + 4 +                      + 2 +   +   + 1 +")
    print("+===+===+===+===+                      +===+===+===+===+                      +===+===+===+===+")
    print("V")
    print("{0}+{1}+{2}+{3}={4}".format(a,row1[0],row2[0],row3[0],s))
    print("{0}+{1}+{2}+{3}={4}".format(b,row1[1],row2[1],row3[1],s))
    print("{0}+{1}+{2}+{3}={4}".format(c,row1[2],row2[2],row3[2],s))
    print("{0}+{1}+{2}+{3}={4}".format(d,row1[3],row2[3],row3[3],s))
    print("H")
    print("{0}+{1}+{2}+{3}={4}".format(a,b,c,d,s))
    print("{0}+{1}+{2}+{3}={4}".format(row1[0],row1[1],row1[2],row1[3],s))
    print("{0}+{1}+{2}+{3}={4}".format(row2[0],row2[1],row2[2],row2[3],s))
    print("{0}+{1}+{2}+{3}={4}".format(row3[0],row3[1],row3[2],row3[3],s))
    print("D")
    print("{0}+{1}+{2}+{3}={4}".format(a,row1[1],row2[2],row3[3],s))
    print("{0}+{1}+{2}+{3}={4}".format(d,row1[2],row2[1],row3[0],s))
    #---------------------
    print("------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------")
    #-----------------------------
    print("centre and corner-2")
    
    print("+===+===+===+===+                      +===+===+===+===+")
    print("+   +   +   +   +                      + 2 +   +   + 2 +")
    print("+===+===+===+===+                      +===+===+===+===+")
    print("+   + 1 + 1 +   +                      +   +   +   +   +")
    print("+===+===+===+===+                      +===+===+===+===+")
    print("+   + 1 + 1 +   +                      +   +   +   +   +")
    print("+===+===+===+===+                      +===+===+===+===+")
    print("+   +   +   +   +                      + 2 +   +   + 2 +")
    print("+===+===+===+===+                      +===+===+===+===+")
    print("centre")
    print("{0}+{1}+{2}+{3}={4}".format(row1[1],row1[2],row2[1],row2[2],s))
    print("corner")
    print("{0}+{1}+{2}+{3}={4}".format(a,d,row3[0],row3[3],s))
    print("------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------")
    #------------------------------
    print("inner squares-8")
    
    print("+===+===+===+===+                      +===+===+===+===+                      +===+===+===+===+")
    print("+ 1 + 1 + 2 + 2 +                      +   + 5 + 5 +   +                      +   +   +   +   +")
    print("+===+===+===+===+                      +===+===+===+===+                      +===+===+===+===+")
    print("+ 1 + 1 + 2 + 2 +                      +   + 5 + 5 +   +                      + 7 + 7 + 8 + 8 +")                      
    print("+===+===+===+===+                      +===+===+===+===+                      +===+===+===+===+")
    print("+ 4 + 4 + 3 + 3 +                      +   + 6 + 6 +   +                      + 7 + 7 + 8 + 8 +")
    print("+===+===+===+===+                      +===+===+===+===+                      +===+===+===+===+")
    print("+ 4 + 4 + 3 + 3 +                      +   + 6 + 6 +   +                      +   +   +   +   +")
    print("+===+===+===+===+                      +===+===+===+===+                      +===+===+===+===+")
    print("1^^{0}+{1}+{2}+{3}={4}".format(a,b,row1[0],row1[1],s))
    print("2^^{0}+{1}+{2}+{3}={4}".format(c,d,row1[2],row1[3],s))
    print("3^^{0}+{1}+{2}+{3}={4}".format(row2[2],row2[3],row3[2],row3[3],s))
    print("4^^{0}+{1}+{2}+{3}={4}".format(row2[0],row2[1],row3[0],row3[1],s))
    print("5^^{0}+{1}+{2}+{3}={4}".format(b,c,row1[1],row1[2],s))
    print("6^^{0}+{1}+{2}+{3}={4}".format(row2[1],row2[2],row3[1],row3[2],s))
    print("7^^{0}+{1}+{2}+{3}={4}".format(row1[0],row1[1],row2[0],row2[1],s))
    print("8^^{0}+{1}+{2}+{3}={4}".format(row1[2],row1[3],row2[2],row2[3],s))
    print("------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------")
    #-----------------------------
    print("others-6")
    
    print("+===+===+===+===+                      +===+===+===+===+")
    print("+ 1 + 1 + 2 + 2 +                      +   + 3 + 3 +   +")
    print("+===+===+===+===+                      +===+===+===+===+")
    print("+   +   +   +   +                      +   +   +   +   +")
    print("+===+===+===+===+                      +===+===+===+===+")
    print("+   +   +   +   +                      +   +   +   +   +")
    print("+===+===+===+===+                      +===+===+===+===+")
    print("+ 1 + 1 + 2 + 2 +                      +   + 3 + 3 +   +")
    print("+===+===+===+===+                      +===+===+===+===+")
    print("1^^{0}+{1}+{2}+{3}={4}".format(a,b,row3[0],row3[1],s))
    print("2^^{0}+{1}+{2}+{3}={4}".format(c,d,row3[2],row3[3],s))
    print("3^^{0}+{1}+{2}+{3}={4}".format(b,c,row3[1],row3[2],s))
    
    print("------------------------------------------------------------------------------------------------")
    print("+===+===+===+===+                      +===+===+===+===+")
    print("+ 4 +   +   + 4 +                      +   +   +   +   +")
    print("+===+===+===+===+                      +===+===+===+===+")
    print("+ 4 +   +   + 4 +                      + 6 +   +   + 6 +")
    print("+===+===+===+===+                      +===+===+===+===+")
    print("+ 5 +   +   + 5 +                      + 6 +   +   + 6 +")
    print("+===+===+===+===+                      +===+===+===+===+")
    print("+ 5 +   +   + 5 +                      +   +   +   +   +")
    print("+===+===+===+===+                      +===+===+===+===+")
    print("4^^{0}+{1}+{2}+{3}={4}".format(a,d,row1[0],row1[3],s))
    print("5^^{0}+{1}+{2}+{3}={4}".format(row2[0],row2[3],row3[0],row3[3],s))
    print("6^^{0}+{1}+{2}+{3}={4}".format(row1[0],row2[0],row1[3],row2[3],s))
    print("------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------------------")
    
    
    
    
    if input("want to check(yes/no) :: ") =="yes" :
            #--------------------------------------
        print(" ------"*4+" ")
        print(n+"|")
        
        print(box1+box2+box3+box4)
        
        print(n+"|")
        print(" ------"*4+" ")
        print(n+"|")
        
        print(box5+box6+box7+box8)
        
        print(n+"|")
        print(" ------"*4+" ")
        print(n+"|")
        
        print(box9+box10+box11+box12)
        
        print(n+"|")
        print(" ------"*4+" ")
        print(n+"|")
        
        print(box13+box14+box15+box16)
        print(n+"|")
        print(" ------"*4+" ")
    
    
        while True :
            check1 = int(input("input(1) : "))
            check2 = int(input("input(2) : "))
            check3 = int(input("input(3) : "))
            check4 = int(input("input(4) : "))
            sm = check1+check2+check3+check4
            print("{0}+{1}+{2}+{3}= {4}".format(check1,check2,check3,check4,sm))
            if input("want to check again(y/n) :") =="n":
                break
        
    

              


        



        
                
                            
    


