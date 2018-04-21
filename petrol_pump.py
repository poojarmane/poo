import tkinter
from tkinter import *
from random import randint

start_time=0
service_time=0
simulet_time=0
 
def accept_data1():
	global n
	global vehicle_no
	n=int(input("How many vehicle:"))
	for i in range(n):
		vahicle1=input("Enter In Time of vehicle(Int):"(i+1))
		seconds = int(input("Enter number of seconds: "))
 	
		import sys
import tkinter
from tkinter import *
from random import randint

#start_time=800
#service_time=30
#simulet_time=4


start_time=0
service_time=0
simulet_time=0

#n=5
#cat=['sd', 'df', 'sd', 'as', 'xc']
#time_req=[20, 35, 45, 15, 30]
#no_of_pat=[46, 56, 25, 23, 32]
#randam_no=[25,10,45,30,12,87,66,10,78,48]  #Randome number

n=0
cat=[]
time_req=[]
no_of_pat=[]
randam_no=[]

pro=[]
com=[]
ranges=[]

randam=[]
ran_n=0   # no of randam number 
ran_p=0    # no of random patients

final=[]


def accept_data1():
    global cat
    global time_req
    global no_of_pat
    global n
   
    n=int(input("How many Categories/Services of Work(Int):"))
    for i in range(n):
        cat1=("service""{0:2}".format(i+1)).replace(" ","")
        cat.append(cat1)
        cat2=input("Enter %d Cate/Service time required(Int):" % (i+1))
        time_req.append(int(cat2))
        cat3=input("Enter %d work of no of    Customers(Int):" % (i+1))
        no_of_pat.append(int(cat3))
      
    #print(cat[i],time_req[i],no_of_pat[i])
    
def accept_data2():
    global randam_no
    global ran_no
    global service_time
    global simulet_time
    global start_time
    global ran_p
    
    service_time=int(input("How Much Time Schedule Customers Appointment time(min)(Int):"))
    simulet_time=int(input("How Much Time Simulet Customers in Your Systems(Hours)(Int):"))
    start_time=int(input(  "Enter The  Start Time Of Your    Systems      (Hours) (Int):"))
    #ran_n=int(input(       "How Many Random Number You Want in   Your      System (Int)"))
    ran_p=int((simulet_time*60)/service_time)

    for i in range(ran_p+1):
        randam_no.append(randint(10,99))

def print_time(t):
    time=list(str(t))
    if len(time)==4:
        a=''.join(time[:-2])
        b=''.join(time[2:])
        return (a+':'+b)
    if len(time)==3:
        a=''.join(time[:-2])
        b=''.join(time[1:])
        return (a+':'+b)
        
def print_pro_cumu():
    print("\n\t\tDistribution Table for Probability and Cumulative Probability")
    print('\n'"       Categories" '\t' "Time req/min" '\t' "No Of Pati" '\t' "Prob"  '\t' "Cumu Prob" '\t' "Ranges" '\n')
    for i in range(n):
        print('\t',cat[i] ,'\t',time_req[i],'\t\t',no_of_pat[i],'\t''\t',pro[i],'\t',com[i],'\t\t',ranges[i][0],'-',ranges[i][1])
    print('\n')

def print_randam():
    print("\n\t\tDistribution Table for Waiting Timen and  Service time")
    print('\n'"       Patient no" '\t' "Ari Time" '\t' "Randam No" '\t' "Categories"  '\t'  "Service Time" '\n')
    for i in range(len(randam)):
        tp1=print_time(randam[i][1])
        print('\t',randam[i][0] ,'\t\t',tp1,'\t\t',randam[i][2],'\t''\t',randam[i][3],'\t',randam[i][4])
    print('\n')

def print_service():
    print("\n\t\tDistribution Table for Randam Number Service time")
    print('\n'"       Patient no" '\t' "Ari Time" '\t' "service time" '\t' "service duration"  '\t'  "Service End" '\t', "Waiting Time" '\t' ,"Ideal Time" '\n')
    for i in range(len(randam)):
        tp1=print_time(final[i][1])
        tp2=print_time(final[i][2])
        tp3=print_time(final[i][4])
        print('\t',final[i][0] ,'\t\t',tp1,'\t\t',tp2,'\t''\t',final[i][3],'\t\t\t',tp3,'\t\t',final[i][5],'\t\t',final[i][6])
    print('\n')

def print_all():
    print_pro_cumu()
    print_randam()
    print_service()
    
def find_pro_cumu():
    global cat
    global time_req
    global no_of_pat
    global n
    total=sum(no_of_pat)


    for i in range(0,n):
        temp=float("{0:.2f}".format(no_of_pat[i]/total))
        pro.append(temp)
    #print(pro)

    s0=0
    for i in range(n):
        s0+=pro[i]
        com.append(float("{0:.2f}".format(s0)))
    #print(com)

    s1=0
    s2=0
    p0=[]
    for i in range(n):
        p0.append(int(s1))
        s1=(com[i]*100)
        s2=(com[i]*100)-1
        p0.append(int(s2))
        ranges.append(p0)
        p0=[]
    #print(pro,com,ranges)
    #print(cat,time_req,no_of_pat)
    
    #print_pro_cumu()
    
    
def cal_pat(start,x):
    
    end=start%100
    start+=x
    end+=x
    
    if end>60:
        end-=60
        start-=60
        start+=100
    if end==60:
        return start-60+100
    return start

    
def find_cat(no):
    for i in range(n):
        a=ranges[i][0]
        b=ranges[i][1]

        if no in range(a,b+1):
            return cat[i],time_req[i]

def find_randam_no():
    global randam
    global start_time
    global service_time
    global simulet_time
    global randam_no
    
    pno=[]     # patient number
    pat=[]     # patient arival time
    cat_p=[]   # patient categories
    ser_t=[]   # service time needed 
    ran=[]     #Randome number
    
    ran_p=int((simulet_time*60)/service_time)

    start=start_time
    for i in range(ran_p):
        pno.append(i)
        pat.append(start)
        x=cal_pat(start,30)
        start=x
        ran.append(randam_no[i])
        c,t=find_cat(randam_no[i])
        cat_p.append(c)
        ser_t.append(t)
        randam.append(pno+pat+ran+cat_p+ser_t)
        pno=[]
        pat=[]
        cat_p=[]
        ser_t=[]
        ran=[]
        
    #print(pno,pat,ran,cat,ser_t)
    #print_randam()

def cal_time(w):
    if w>=0:
        if w>60:
            w-=40
            return w,0
        else:
            return w,0
    if w<0:
        t=abs(w)
        if t>=40:
            t-=40
            return 0,t
        else:
            return 0,t
       
            
def find_serive_time():
    global randam
    global final
    
    pn=[]
    at=[]
    st=[]
    sd=[]
    se=[]
    wt=[]
    it=[]

    start=start_time
    for i in range(len(randam)):
        pn.append(i)
        at.append(randam[i][1])
        s1=randam[i][1]
        s2=start
        st.append(start)
        s=(randam[i][4])
        x=cal_pat(start,s)
        start=x
        sd.append(s)
        se.append(x)
        w=s2-s1
        t1,t2=cal_time(w)
        wt.append(t1)
        it.append(t2)
        final.append(pn+at+st+sd+se+wt+it)
        pn=[]
        at=[]
        st=[]
        sd=[]
        se=[]
        wt=[]
        it=[]
        
    #print(pn,at,st,sd,se,it)
    #print_service()

def display_all():
    global n
    global cat
    global pro
    global com
    global randam
    global final
    global ranges
    global time_req
    global no_of_pat

    roop = Tk()
    roos = Tk()

    roop.title("Single Service Queuing System")
    roop.geometry("750x750")

    roos.title("Single Service Queuing System")
    roos.geometry("750x750")

    
    lh1 = Label(roop, text="Distribution Table for Probability and Cumulative Probability",)
    lh1.pack()
    lh1.config(font=('times', 14, 'bold underline'))
    lb1 = Label(roop, text="Categories    Time req/min    No Of Pati    Prob    Cumu Prob    Ranges",)
    lb1.place(x=85,y=30)
    lb1.config(font=('times', 13, 'bold'))

    j=0
    for i in range(n):
        X=85
        Y=55+j
        lb11 = Label(roop, text=cat[i],height=1)
        lb11.config(font=('times', 13))
        lb11.place(x=X,y=Y)
        X+=120

        lb12 = Label(roop, text=time_req[i],height=1)
        lb12.config(font=('times', 13))
        lb12.place(x=X,y=Y)
        X+=120

        lb13 = Label(roop, text=no_of_pat[i],height=1)
        lb13.config(font=('times', 13))
        lb13.place(x=X,y=Y)
        X+=80

        lb14 = Label(roop, text=pro[i],height=1)
        lb14.config(font=('times', 13))
        lb14.place(x=X,y=Y)
        X+=80

        lb15 = Label(roop, text=com[i],height=1)
        lb15.config(font=('times', 13))
        lb15.place(x=X,y=Y)
        X+=80

        p=(str(ranges[i][0]))+"-"+(str(ranges[i][1]))
        lb16 = Label(roop, text=p,height=1)
        lb16.config(font=('times', 13))
        lb16.place(x=X,y=Y)
        j+=30

    Y1=n*30+60
        
    lh2 = Label(roop, text="Distribution Table for Waiting Timen and  Service time",)
    lh2.place(x=100,y=Y1)
    lh2.config(font=('times', 14, 'bold underline'))
    lb2 = Label(roop, text="Cust no   Ari Time    Randam No    Categories    Service Time",)
    lb2.place(x=85,y=Y1+30)
    lb2.config(font=('times', 13, 'bold'))

    j=60
    for i in range(len(randam)):
        X=90
        Y=Y1+j
        lb21 = Label(roop, text=randam[i][0],height=1)
        lb21.config(font=('times', 13))
        lb21.place(x=X,y=Y)
        X+=100
        
        tp1=print_time(randam[i][1])
        lb22 = Label(roop, text=tp1,height=1)
        lb22.config(font=('times', 13))
        lb22.place(x=X,y=Y)
        X+=100

        lb23 = Label(roop, text=randam[i][2],height=1)
        lb23.config(font=('times', 13))
        lb23.place(x=X,y=Y)
        X+=80

        lb24 = Label(roop, text=randam[i][3],height=1)
        lb24.config(font=('times', 13))
        lb24.place(x=X,y=Y)
        X+=120

        lb25 = Label(roop, text=randam[i][4],height=1)
        lb25.config(font=('times', 13))
        lb25.place(x=X,y=Y)
        j+=30

        
        
    lh3 = Label(roos, text="Distribution Table for Randam Number Service time",)
    lh3.pack()
    lh3.config(font=('times', 14, 'bold underline'))
    lb3 = Label(roos, text="Cust no    Arri Time    Service(t)    Service Dur    Service End    Waiting(t)    Ideal(t)",)
    lb3.place(x=70,y=35)
    lb3.config(font=('times', 13, 'bold'))

    j=0
    for i in range(n):
        X=85
        Y=55+j
        lb31 = Label(roos, text=final[i][0],height=1)
        lb31.config(font=('times', 13))
        lb31.place(x=X,y=Y)
        X+=80
        
        tp1=print_time(final[i][1])
        lb32 = Label(roos, text=tp1,height=1)
        lb32.config(font=('times', 13))
        lb32.place(x=X,y=Y)
        X+=90

        tp2=print_time(final[i][2])
        lb33 = Label(roos, text=tp2,height=1)
        lb33.config(font=('times', 13))
        lb33.place(x=X,y=Y)
        X+=100

        lb34 = Label(roos, text=final[i][3],height=1)
        lb34.config(font=('times', 13))
        lb34.place(x=X,y=Y)
        X+=120

        tp3=print_time(final[i][4])
        lb35 = Label(roos, text=tp3,height=1)
        lb35.config(font=('times', 13))
        lb35.place(x=X,y=Y)
        X+=100

        lb36 = Label(roos, text=final[i][5],height=1)
        lb36.config(font=('times', 13))
        lb36.place(x=X,y=Y)
        X+=80

        
        lb37 = Label(roos, text=final[i][6],height=1)
        lb37.config(font=('times', 13))
        lb37.place(x=X,y=Y)
        j+=30


    
def next_step():
    global randam_no
    global ran_no
    global service_time
    global simulet_time
    global start_time
    global ran_p

    service_time=int(v1.get())
    simulet_time=int(v2.get())
    start_time=int(v3.get())
    ran_p=int((simulet_time*60)/service_time)

for i in range(ran_p+1):
        randam_no.append(randint(10,99))

    find_pro_cumu()
    find_randam_no()
    find_serive_time()
    display_all()
    #print_all()
    
def acept_val2():
    global v1
    global v2
    global v3
    
    global n
    global time_req
    global no_of_pat
    
    X1=n*30+100
    
    for i in range(n):
        time_req.append(int(entry1[i].get()))
        no_of_pat.append(int(entry2[i].get()))
        
    lb1 = Label(root, text="How Much Time Schedule Customers  (min)(Int):",height=1)
    lb1.config(font=('times', 13))
    lb1.place(x=10,y=X1)
    lb2 = Label(root, text="How Much Time Simulet the System (Hours)(Int):",height=1)
    lb2.config(font=('times', 13))
    lb2.place(x=10,y=X1+30)
    lb3 = Label(root, text="Enter Start Time Of Your Systems (Hours) (Int):",height=1)
    lb3.config(font=('times', 13))
    lb3.place(x=10,y=X1+60)
    
    
    e1=Entry(root,textvariable=v1,width=10)
    e1.place(x=400,y=X1)
    e2=Entry(root,textvariable=v2,width=10)
    e2.place(x=400,y=X1+30)
    e3=Entry(root,textvariable=v3,width=10)
    e3.place(x=400,y=X1+60)

    
    b2 = Button(root, text='OK', command=next_step)
    b2.place(x=100,y=X1+90)
        
def acept_val1():
    global n
    global cat
        
    global entry1
    global entry2
    
    n=int(v.get())
    i=70

    lb1 = Label(root, text="Services",height=1)
    lb1.config(font=('times', 13))
    lb1.place(x=10,y=40)
    lb2 = Label(root, text="Duration",height=1)
    lb2.config(font=('times', 13))
    lb2.place(x=100,y=40)
    lb3 = Label(root, text="Customer",height=1)
    lb3.config(font=('times', 13))
    lb3.place(x=200,y=40)
    
    
    for j in range(n):
        p=("service""{0:2}".format(j+1)).replace(" ","")
        cat.append(p)
        lb = Label(root, text=p,height=1)
        lb.config(font=('times', 13))
        lb.place(x=20,y=i)
        
        e1 = Entry(root,width=10)
        e1.place(x=100,y=i)
        entry1[j] = e1


        e2 = Entry(root,width=10)
        e2.place(x=200,y=i)
        entry2[j] = e2
    
        i+=30
        
    X1=n*30+70
    b1 = Button(root, text="OK", command=acept_val2)
    b1.place(x=100,y=X1)

    
if __name__ == "__main__":
    Tk = tkinter.Tk
    root = Tk()

    entry1 = {}
    entry2 = {}
    
    root.title("Single Server Queuing System - Solutions")
    root.geometry("600x600")


    v = StringVar()
    v1 = StringVar()
 v2 = StringVar()
    v3 = StringVar()


    lb=Label(root,text="How many Categories/Services of Work(Int):",height=1)
    lb.config(font=('times', 13))
    lb.place(x=10,y=10)

    entry=Entry(root,textvariable=v,width=10)
    entry.place(x=350,y=10)
    
    button = Button(root, text='OK', command=acept_val1)
    button.place(x=450,y=10)
    
    root.mainloop()


    #accept_data1()
    #accept_data2()
    #find_pro_cumu()
    #find_randam_no()
    #find_serive_time()
    #print_all()

