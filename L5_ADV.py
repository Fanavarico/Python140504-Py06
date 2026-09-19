
"""
In The Name of GOD


Created on Sun Sep 13 20:13:50 2026

@author: Ali Pilehvar Meibody

ADV5


"""



'''

Human (english) <----interface --> Machine (0,1 binary)


1- Python built in functions (print(), input() , type() , len())
    karbord --> yek kari (amalkardi)
    
2- Keywords --> (if,else, elif, for, while, def) --> logic ro taghir bedim


        2.1.Dastoorate sharti
        
            2.1.1.Just if --> mikhay chizi ro catch koni gir bendazi--> rahzan
                    if shart:
                        dastooor
                        
                    in dastoor agar shart True bashe ejra mishe age na ejra nmishe
                    
            2.1.2. IF else --> do rahi bood
                agar true shod -->kare 1 age false shod --< kare 2
                
                    if shart:
                        dasdtoor1
                    else:
                        dastoor2
                        
            2.1.3. if elif else -> dorahi haye too dar too
            
                if shart1:
                    dastoor1
                elif shart2:
                    dastoor2
                    
                elif shart3:
                    dasoor3
                    
                    2.1.3.1. Multiple selectoion --> calculator --> jam , tafrigh, zarb --> agar user jam -_> jam kon (kar1)
                    agar dad tafrigh tafrigh kon kar2 --> multiple kar --> 2 rahi nis , chand rahie
                    
                    2.1.3.2. Range dashtid --> score beyne 20 - 15 --> , 15 - 10 --> yechizi va va a...
                    
                chanta shart dashte bashi -> shart 1 o 2
                
                if shart1 and/or shart2:
                    dastoor
                    
                    
                
                and --> hatman ham shart1 ham sharte 2 True bashad --> True True
                
                or --> yani hadegahal yekishon --> True True , True False , False True 
                
        
        2.2. Halghe ha (Loops)






3- Variables (moteghayer) --> yek meghdar ro dar yek zarf zakhire konim
    3.1. numbers (int,float, complex,..)
    3.2. Boolean (True,False)
    3.3. Strin --> name='ali' name[index] name.function() --> emal nmishodan khoroji midadan
    
    
    3.4. Iterables --> multiple values in one variable
        3.4.1. List --> ordered (index) , changable , allow duplicated
            a = [10,20,'Ali',True,1j,10.33]
            a[index]
            list.function() -->emal mishodan khoroji nmidadan
            
            a.append(50)
            
        3.4.2. Tuple --> ordered (index) , unchnagbale , allow duplicated
            b=(10,20,30,40,50)
            b[index]
            b[4]=400 XXX --> Unchangable --> database --> dakhele workflow codeton 
            
            new_variable = list(b)
            taghiro bedid
            new_new_variable = tuple(new_variable)
            
            
        3.4.3. Set --> unordered (no index) , unchnagbale, No duplicated
        
            c = {10,20,30,40}
            
            c[index] XXXX
            
            majmoe haye riazi --> tavabe ei dare baraye eshterako ejtema 
            
            
        3.4.4. Dictionary --> information darim
        
            a=['ali',30,'091900000']
            
            a[2]  shoamrash dar oon index hast
            
            index   value
            0       val1
            1       val2
            
            
            
            key    value
            key1    value1
            key2    value2
            
            a={'name':'ali' ,'sen':30 , 'phone':'0919..' }
            
            instead of a[2]
            
            a['phone'] --> shomare mobile
            
            a['name']

            products={'code':'z12' , 'brand':'zara' ,'price':14 ,'discount':5}
            products['discount']
            
            

'''


#================================================
#================================================
#================================================
#================================================
#================================================


'''

Loops

'''


#che zamani az keywords estefade mikoniM?

#python az bala be paein az chap be rast mesle yek ensan
#mikhone code ro run mikone


sen = 10 
print('salam')

#dar hame halat az bala be paein az chap be rast mikhoen run mikone

#sen =10 abashe print salam msihe, sen = 32293232932 print slaam ejra msihe

#agar shoma bekahhid logic(manteghe) in code khonie kernele ipython ro taghir bedid

#masalan begid --> fght khate 164 dar soorati ejra shavad ke sen >18 bashad
#inaj abayd az keywords etsefade konid

#az yekchize banafsh -->keywords --> logico beham mizane --> badane 
#badane (body ) --> 4 ta space (1 tab) -->yekseri dastoorat miran zir majmoeye oon keyword

#va motefavet khodne mishand



sen = 10 

if sen>18:
    print('salam')



#-----------
'''
Loopp --> yek kari ro tekrar anjam bedim 
miaym --> for , while mizanim


'''

print('salam')

#10 bar benevisam
#chiakr konm?

print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')


'''
repeat(10):
    print('salam')

'''

#repeat--> keywords -->

#az yek manteghhi k gahdim too code haye paye e tar -> C


#az yek raveshe dige kari krdn na tanha repeat balke har kari ro betoni anajm bdi --> loop


'''

shomarande --> zarfe -> i , j , k , esm , .. --> esm dare

yek baze --> list bashe, yek chizi bashe k iterable --> list,tuple,.. baze bashe


shomarande ro done done mizare jaye element haye iterable (azaye oon list,)
bad codi k too badane hast ro be ezaye oon ejra mikone

'''

'''
repeat(5):
    print('salam')
'''



for i in [1,2,3,4,5]:
    print('salam')
    
    
'''
i->[1,2,3,4,5] be ezash dastore paein ro ejra kon

in dastoro-->print('salam') yek chize complex --> run krdne LLM (large lamnguage model)


i=1 --> dastoro ejra mikone --> print(salam)-->salam
i=2 -->dastoro ejra mikone -->print(salam) -->salamn
...
i=5 -->dastoro ejra mikone -->print(salam) -->salam

5 bar salam




'''






for i in [1,2,3,4,5]:
    print(i)


'''
be ezaye i haei ke dar [1,2,3,4,5] hastand dastore zir ra ejra kon

i=1 --> dastor ejra kon-->pritn(i)-->print(1)-->1
i=2 -->dastoro ejra kon-->print(i)-->print(2)-->2
i=3 -->sdastoro ejra kon-->priont(i)-->pritn(3)-->3

1
2
3
4
5



'''
    

for i in ['ali','vahid','hamid','reza']:
    print('salam')


'''
i=ali -->dastoro --> print(salam) -->salam
i=vahiud -->dastoro --> print(salam) -->salam
i=hamid --> dastoro --> print(salam) -->salam
i=reza --> dastoro --> print(salam) -->salam





'''

for i in [1,2,3,4,5]:
    print(i)



#az 1 ta 100 

#for i in [1,2,3,4,,,,,,,,,]

#tabeye dakheli -_> range --> mitone tolid kone in list

for i in range(0,100):
    print('salam')


'''
be ezaye i haei ke dar range(0,100 ) hast
be ezaye i haei k [0,1,2,3.....,99] hast

i=0 -->dastor -->print('salam')-->salam
i=1 ...dastor -->print('salam')-->salam

i=99 -->dastor -->print('salam')-->salam


range(start,end,step)


range(start=0,end,step=1) -->default


range(100) ---> 0 ta 100 1 i 1 kie

range(10,100) --> 10 ta 100 1 ki ki

range(10,100,2) --> 10 ta 100 --> 2 ta 2 ta




'''

for i in range(10,100,2):
    print(i)
    
    
'''
be ezaye i haei ke dar 10 at 100 hst 2 ta 2 ta boro

i -->[10,12,14,16,18,......,98]



i=10 -->print(i) -->print(10) -->10
i=12 -->print(i) -->print(10) -->10



'''




for i in [1,2,3,4,5]:
    print(i)
    
    
    
    
my_users = ['ali','vahid','hamid','reza']


for i in my_users:
    print(i)
    
'''
i=ali -->print(i)-->print(ali)-->ali

....
ali
vahid
hamid
reza



iterable -->listo.

varede done doen elemnt --> iteration



'''
    
    
    
my_users = ['ali','vahid','hamid','reza']


for i in my_users:
    if i[0]=='a':
        print(i)

#ali


'''
i-->ali,vahid,hamid,reza hast

i=ali --> dastoro ejra mikone
if i[0]=='a':
    print(i)


i[0] -->ali[0] --> a    a=='a' ->true --> print(i) -->print(ali) -->ali



i=vahid --> 


'''
  

#-----se no iteration darim
#access mitone motefgavet bashe


#esme aval a bashe
my_users = ['ali','vahid','hamid','reza']

for i in my_users: #Itersation
    if i[0]=='a': #access --> shart 
        print(i)  #action --> chiak rkoni





#andaze esm bsiha z 3 baahe

my_users = ['ali','vahid','hamid','reza']

for i in my_users: #Itersation
    if len(i)>3: #access --> shart 
        print(i)  #action --> chiak rkoni



#agar harfe b dar esm bashe

my_users = ['ali','vahid','hamid','reza']

for i in my_users: #Itersation
    if 'a' in i: #access --> shart 
        print(i)  #action --> chiak rkoni


#-----------action-----------------
#BOTRO TOO LISTE User ham oon haei k a dare avaleshon (shart, access) peydashon (if)
#chika rkonm?? --> action

#-----action1: print---------------

#mige boro tooye list , onaei ke a dare avale esmeshon ro print kon

my_users = ['ali','vahid','hamid','reza']

for i in my_users: #Itersation
    if i[0]=='a': #access --> shart 
        print(i)  #action --> chiak rkoni

    

#-----action2: count(beshmor)---------------

my_users = ['ali','vahid','hamid','amir','reza']

count = 0 

for i in my_users: #Itersation
    if i[0]=='a': #access --> shart 
        #print(i)  #print nakon beshmor
        count = count + 1
        
#dar soorati in count ezafre mishavad ke shart true she
#che zamabi sahrt tru emsihe --> i[0]==a --> kasani ke avale esm =a
#kasani k dar list avaleshon a bashe --L> count = count + 1
#shomaresh misahn

'''
i=ali --> true --> count = cpunt +1  --> count = 0 + 1 = 1
i=vahid --> false --<ejra nmsiehg --> count =1 mimone
i=hamdi --> false --<ejra nmsiehg --> count =1 mimone
i=amir --> True --> ejra mishe ->count = count +1 = 1 + 1 = 2 --> update
i=reza --> false

'''
    
print(count) #2
    
    
#-----action3: jodash kon---------------


my_users = ['ali','vahid','hamid','amir','reza']

#count = 0 
new_list=[]


for i in my_users: #Itersation
    if i[0]=='a': #access --> shart 
        #print(i)  #print nakon beshmor
        #count = count + 1 nmikham beshmorm
        new_list.append(i)
        
        
        

print(new_list) #['ali', 'amir']


#-----action4: hazfesh kon---------------

my_users = ['ali','vahid','hamid','amir','reza']

#count = 0 
#new_list=[]
new_list=[]

for i in my_users: #Itersation
    if i[0]=='a': #access --> shart 
        #print(i)  #print nakon beshmor
        #count = count + 1 nmikham beshmorm
        #new_list.append(i)
        pass
    else:
        new_list.append(i)
        
        
        
        
my_users = ['ali','vahid','hamid','amir','reza']

#count = 0 
#new_list=[]
new_list=[]

for i in my_users: #Itersation
    if i[0]!='a': #access --> shart 
        #print(i)  #print nakon beshmor
        #count = count + 1 nmikham beshmorm
        #new_list.append(i)
        new_list.append(i)

     

    
#for --->
#static repeat --. tekrari k sabete
#dynamic repeat --> shoamrande print(i) 
#iteration --> done done toye yek list hey shart bezani (print,beshmori,list)






#ta zamani ke --> while
# az user password begir , ta zamani k zire 8 ragham hast hey password begir




#-------zamani hast ke --> yek baze darid
#start malome , enteha maloem --> for miay estefade


#mikhay baze nadashte bashi -_> loop bezani ta zamani k (shart bezari)

#while -> Ta zamani ke --> kildivazhe --> while 


'''


while shart:
    dastooor
    
    
    
aval az baal --> shart True bod varede loop mishe age nabod vared nmishe


'''   



for i in range(0,100,1):
    print('salam')
    
    
   
    
   
    
i=0
while i<100:
    print('salam')
    i = i + 1
    
    
    
#---------error haye rayej
#error -> i is not defined--> i ro besazi
#oon for hast ke naizi nist k i ro tarif koni
#NameError: name 'i' is not defined

while i<100:
    print('salam')
    i=i+1
  
    
  
    
  
#-----

i=200
while i<100:
    print('salam')
    i=i+1
  
  
#errro nmikhori chizi erja nmishe

#aval nemire to lop --> aval yek darvazas

#aya i<100 -->fALSE
    
        
#-----


'''

i=0
while i<10:
    print('salam')


i=0 --> i<10 --> True -->print(salam)  barmigarde
i=0 --> i<10 -->true -->pritn(salam) 
i=0 -->

ta abad i=09 i<10 -->treu -->too loop gir mikone

endless loop


sharte payan bezarid

'''




i=0
while i<10:
    print('salam')
    i = i +1
    
    
'''
i=0 -->io<10 -->avred hsod --> print('salam') i = 0 + 1 -->1
i=1 -> i<10 --> print('salam') i=1+1 =2
....
i=9 -->i<10 -->pritn('salam') i=9+1 = 10
i=10 -->i<10 -->10<10 --> maid biron az halghe

'''



#while true hast

if sen>10:
    pass




while True:
    #yek kari kon
    pass





#--------
#passwordo az user begir--> ta zamni k password bala tar az 8 ragham nazade hey azash begire


#mikhay bendazish too ye loop hey azash kar beekshi gta ye shaertoio

while True:
    password = input('password ra vared konid:')
    
    if len(password)>8:#sharti bezar baraye kasani k farar konan az loop
        break
   
#che kasani _->len()>8   
print('password ba moafaghiat sabt shod')
    
'''
whiel True --:> vared mishe --> password migire --> 333 --> False -->break ejra nmsihe

barmigrde -->shartTrue --> passwordo migire --> inghd inakro anjam mide

ta key --> len(password)>8 -->treu beshe -> brak


'''


password = input('password ra vared konid:')

while len(password)<8:
    password = input('password ra vared konid:')

#che kasani _->len()>8   
print('password ba moafaghiat sabt shod')
    


#==============================
#==============================
#==============================
#==============================
'''
Tamrine shomare 2

'''
#==============================
#==============================
#==============================
#==============================



'''
 ۱ 

بزرگ‌ترین عدد لیست
بزرگ‌ترین عدد لیست زیر را پیدا کنید:

[15,50,70,1,90,20,4,108,6]

'''
#aval bezar to yek listi berizamesh


my_list=[15,50,70,1,90,20,4,108,6]

max(my_list) #108


#dakhele tabeye max --> in chizi k inja minevisam 

#bebin boro tooye ina done done begard bebin bozorgtrin kodome???

#beri begardi --> iteration -> bazresi  , varresi


#for i in my_list:

    
#codemon clean bashe va motvaje beshe
#yeki az rah ha --> bejaye i --> yek variable ghabele fahm bezarim

#max , min ,frequency --> zarf ghabla z for misazan
my_list=[15,50,70,1,90,20,4,108,6]
max_number = 0
#min_number = 1000000000000000000

for number in my_list:
    if number > max_number:
        max_number = number

'''
number = 15 --> ejra moikone kolo -->if number > max_number:
    --> 15 > 0 --> True -> max_number = 15 
    

number = 50 --> ejra mikone if number>max_number
    50 > 15 --> true --> max_number = number = 50 
    

number = 70 --> ejra mikone if number>max_number
    70 > 50 --> true --> max_number = number = 70
    

number = 1 --> ejra mikone if number>max_Number
    1 > 70 -->false --> max_number=number ejra nmishe -> max_number =70
    
ta koja??? ta key??

be ezaye numbwer haei k dar lost hast done done mire
ta zamani ke shart number>max_number -->true 

dafr oonsorat max number update mishe



'''
   
#vaghty ejra konm chizi print nmishe

my_list=[15,50,70,1,90,20,4,108,6]
max_number = 0
#min_number = 1000000000000000000

for number in my_list:
    if number > max_number:
        max_number = number



print(max_number) #108


#taklif --> min ro peyda konid

'''

input ---> BOX ---> output



list --> BOX --> number(max)




'''

#def max(list):
    
def my_max(my_list):
    max_number = 0 #my_list[0]
    for number in my_list:
        if number > max_number:
            max_number = number
            
    return max_number




my_list=[15,50,70,1,90,20,4,108,6]


my_max(my_list) #108

max(my_list) #108



min(my_list) #1

    
    
def my_min(my_list):
    min_number = my_list[0]
    
    for number in my_list:
        if number <= min_number:
            min_number = number
            
    return min_number


my_min(my_list) #Out[11]: 1
min(my_list) #Out[12]: 1






'''

 ۲ 

ثبت رکورد پرش
برنامه‌ای بنویسید که 10 بار ارتفاع پرش ورزشکار را دریافت کند.

اگر رکورد جدید بود، پیام «بیشترین پرش ثبت شد» نمایش داده شود.
اگر قبلاً ثبت شده بود، پیام مناسب چاپ شود.




'''


#tekrar --:> for mikham 
#begirad daryaft kon--> input

max_ertefa=0

for i in range(0,10):
    ertefa = float(input('ertefae paresh bede:'))
    
    if ertefa>max_ertefa:
        max_ertefa=ertefa
        print('shoma bishtarin record ro zadi')
    else:
        print('bishtarin ertefae sabt shode ta alan:',max_ertefa)
        

    
    

'''




 ۳ 

اعداد 1 تا 10
بین اعداد 1 تا 10 حرکت کنید:
اگر عدد فرد بود، در ۵ ضرب شود.
اگر عدد زوج بود، ۵ واحد به آن اضافه شود.
در انتها مجموع کل را نمایش دهید.
 


'''

#harekat konid --> iterate --> varesi konid

#range --> akahri exclude

#name='alipilehvar'   name[1:5]  --> 1,2,3,4  

#for i in [1,2,3,4,5,6,7,8,9,10]:
  
#yek if bezari befahme zoje ya fard

#number%2==0 --> zoj , fard
number=60

print(number%7) #4

print(number%2) #0




for i in range(1,11): #1 ,2,3,4,5,6,7,8,9,10
    if i%2==0:
        #zoj
        #i = i+5 #hshomarando taghir bed
        #zarf
        zarf= i + 5
        print(zarf)
        
        #print(i*5)
        
    else:
        #fard
        zarf = i*5
        print(zarf)
        

'''
5
7
15
9
25
11
35
13
45
15
'''





 


'''
۴ 

بررسی طول رشته
یک رشته دریافت کنید.

اگر طول رشته زوج بود، نیمه اول را چاپ کنید.
اگر فرد بود، نیمه دوم را چاپ کنید.
 

'''

#toole reshte

reshte = input('yek reshte vbedahid')

if len(reshte)%2==0:
    #zoje
    #len(reshte)/2 --> 
    #[0:len(reshte)/2]
    print(reshte[:len(reshte)/2])
    
else:
    #fard
    print(reshte[len(reshte)/2:])






'''


۵ 

ماشین حساب
دو عدد و یک عملگر (+ – * /) دریافت کنید و نتیجه را نمایش دهید.



'''
'''

 ۶ 

میانگین
از کاربر ۱۰ عدد دریافت کرده و میانگین آن‌ها را محاسبه کنید.


'''

#yek list daram mianginesho bde

my_list=[15,50,70,1,90,20,4,108,6,20]


sum(my_list)/len(my_list) # 38.4


total = 0 

for number in my_list:
    total = total  + number
    
    
print(total) #384


total/len(my_list) #Out[19]: 38.4



#-------

total = 0 

for i in range(0,10):
    number = float(input('number bede:'))
    
    total = total  + number
    
    
miangin = total/10









'''

 ۷

بررسی رنگ‌ها
سه رنگ از کاربر دریافت کنید.

اگر دو رنگ برابر بودند، پیام مناسب نمایش داده شود.
اگر سه رنگ برابر بودند، پیام جداگانه نمایش داده شود.
در غیر این صورت اعلام شود که رنگ‌ها یکسان نیستند.
 

'''




'''


۸ 

برداشت از حساب
موجودی حساب و مبلغ برداشت را دریافت کنید.

اگر موجودی کافی بود، عملیات انجام شود.
اگر موجودی کافی نبود، پیام خطا نمایش داده شود.
اگر مبلغ منفی یا صفر بود، پیام خطا چاپ شود.
  
'''





'''


۹  

چاپ اعداد منفی
روی یک لیست حرکت کنید و فقط اعداد منفی را چاپ نمایید.

'''

  
  

     
#==============================
#==============================
#==============================
#==============================
'''
Tamrine shomare 3

'''
#==============================
#==============================
#==============================
#==============================



'''
  ۱  

بازی حدس عدد
برنامه‌ای بنویسید که کامپیوتر یک عدد تصادفی تولید کند و کاربر آن عدد را حدس بزند.

اگر عدد واردشده توسط کاربر بزرگ‌تر از عدد تولیدی کامپیوتر بود، پیام دهد که عدد را کوچک‌تر کند.
اگر عدد واردشده توسط کاربر کوچک‌تر از عدد تولیدی کامپیوتر بود، پیام دهد که عدد را بزرگ‌تر کند.
اگر دو عدد برابر بودند، پیام تبریک نمایش داده شود.
پس از حدس صحیح، اجرای بازی متوقف شود.
 
'''


#ketabkhane haro bedonid

#yek tabe --> yek adade tasadofi mide

import random 

computer_generated_number = random.randint(0,100)

user_guess = int(input('yek adad az 0 ta 100 pishbini kon:'))


if computer_generated_number==user_guess:
    print('mobarake barande shodi')
elif computer_generated_number>user_guess:
    print('adad ro bozrogtar kon')
else:#in hamon computer_generated_number<user_guess
    print('adad ro kochiktar kon')
    

#in yekbar run mishe --> in barname mikhad
#ta zamani k doros nagoftm hey komak kone

#ta zamani --> while



#---

import random 
computer_generated_number = random.randint(0,100)

while True:

    user_guess = int(input('yek adad az 0 ta 100 pishbini kon:'))

    if computer_generated_number==user_guess:
        print('mobarake barande shodi')
        break
    elif computer_generated_number>user_guess:
        print('adad ro bozrogtar kon')
    else:#in hamon computer_generated_number<user_guess
        print('adad ro kochiktar kon')
        
        
    
    
    
    
    




while True:

    user_guess = int(input('yek adad az 0 ta 100 pishbini kon:'))

    if computer_generated_number==user_guess:
        print('mobarake barande shodi')
        break
    elif computer_generated_number>user_guess:
        print('adad ro bozrogtar kon')
    else:#in hamon computer_generated_number<user_guess
        print('adad ro kochiktar kon')
        
        
    
        

#-----------

import random 
computer_generated_number = random.randint(0,100)

user_guess = int(input('yek adad az 0 ta 100 pishbini kon:'))


while user_guess!=computer_generated_number:
    if computer_generated_number>user_guess:
        print('adad ro bozrogtar kon')
    else:#in hamon computer_generated_number<user_guess
        print('adad ro kochiktar kon')
        
    user_guess = int(input('yek adad az 0 ta 100 pishbini kon:'))


print('mobarake barande shodi')     
    



'''




 ۲  

بازی سنگ، کاغذ، قیچی
برنامه‌ای بنویسید که از کاربر بخواهد یکی از گزینه‌های سنگ، کاغذ یا قیچی را وارد کند. کامپیوتر نیز باید یکی از این گزینه‌ها را به‌صورت تصادفی انتخاب کند و برنامه برنده را اعلام نماید.

اگر کاربر ورودی غیر از سنگ، کاغذ یا قیچی وارد کرد، پیام مناسب نمایش داده شود و از کاربر خواسته شود مجدداً مقدار وارد کند.
اگر کاربر exit را وارد کرد، اجرای بازی خاتمه یابد.
  
'''
import random
computer_selection = random.choice(['sang','kaghaz','gheichi'])











'''

۳  

بررسی اعتبار رمز عبور
برنامه‌ای بنویسید که از کاربر رمز عبور دریافت کرده و آن را بر اساس معیارهای زیر بررسی کند:

طول رمز عبور باید دقیقاً ۸ کاراکتر باشد.
چهار کاراکتر اول رمز عبور باید حروف الفبا باشند.
چهار کاراکتر آخر رمز عبور باید عدد باشند.
اگر رمز عبور تمام معیارها را داشت، عبارت «معتبر» نمایش داده شود.
در غیر این صورت، عبارت «نامعتبر» نمایش داده شود.
 
'''



#hal shdoe





'''
 
 ۴  

محاسبه مجموع اعداد
برنامه‌ای بنویسید که از کاربر عدد دریافت کند و تا زمانی که کاربر عدد 0 وارد نکرده است، اگر کاربر 0 وارد کرد جمع اعداد را نمایش دهد.

'''


total = 0 

while True:
    
    number = float(input('adad vared kon:'))
    
    if number==0:
        break
    
    total = total + number
    
    
print(total)
    



#-----



total = 0 


number = float(input('adad vared kon:'))


while number!=0:
    total = total + number
    
print(total)
  
    

'''
۵  

چاپ الگوی ستاره‌ای
برنامه‌ای بنویسید که خروجی را به‌صورت زیر چاپ کند:

*
**
***
****
*****
'''  
print('*'*1)
print('*'*2)





print('*'*1)
print('*'*2)
print('*'*3)
print('*'*4)
print('*'*5)




#for i in range(1,6):
    
for i in [1,2,3,4,5]:
    print('*'*i)


for i in range(1,6):
    print('*'*i)
        
    
    


#==============================
#==============================
#==============================
#==============================
'''
Tamrine shomare 3

'''
#==============================
#==============================
#==============================
#==============================


#1-->jalse ghabl


#---2--

'''
۲

برنامه‌ای بنویسید که یک رشته دریافت کند و تمام کاراکترهایی که بیشتر از یک بار تکرار شده‌اند را حذف نماید؛
به‌طوری که فقط اولین مقدار باقی بماند.

Input: programming
Output: progamin

'''


reshte = input('yek reshte bede:')

hamechiz=[]
nahaei= []

for ch in reshte:
    if ch not in hamechiz:
        nahaei.append(ch)
    
    hamechiz.append(ch)
    

print(hamechiz)   #['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
print(nahaei) #['p', 'r', 'o', 'g', 'a', 'm', 'i', 'n']


reshte_nahaei = ''.join(nahaei)
print(reshte_nahaei) #progamin


        
        
        
#-------------------------------
    
reshte = input('yek reshte bede:')

hamechiz=[]
nahaei= ''

for ch in reshte:
    if ch not in hamechiz:
        nahaei = nahaei + ch
    
    hamechiz.append(ch)
    
print(nahaei)


#-------

#set --> yek karbord --> mikhay too yek list 
#chikar koni --> biay tekrari gharo hazf koni --> set(list)


numbers=[10,20,30,40,10]

set(numbers) #{10, 20, 30, 40}




reshte='programming' #b yek list
#reshte.split(' ')
my_list=[]
for resh in reshte:
    my_list.append(resh)
    
print(my_list) #['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']


set(my_list)
#Out[60]: {'a', 'g', 'i', 'm', 'n', 'o', 'p', 'r'}




my_list = list(reshte)
print(my_list)
'''
['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
'''





'''
۳

برنامه‌ای بنویسید که رشته ای از کاربر دریافت کرده و تعداد موارد زیر را محاسبه نماید:

حروف انگلیسی
حروف بزرگ
حروف کوچک
اعداد
فاصله‌ها
کاراکترهای خاص

'''

#reshte --> input()

#for ---> if haei bezani c

#chanta count varibale 

#harkodom az in if ha agar true bod --> oon countesho + 1 mikoni

#character.islower() ---> lower_count = lower_count +1

#toye for anjam midi






'''
۴

برنامه‌ای بنویسید که یک جمله دریافت کند و مشخص نماید کدام کلمه بیشترین تعداد تکرار را دارد.

ﻣﺜﺎل :

Input:
python is easy and python is powerful and python is popular
python -> 3
'''
#reshte --> input()

# yek dictionary msiazi ke key misazi 

#key = pytho

#reshte --> split)(' ')  -->[word1,word2] -> for mizani

#dictionary kamel besaz --> 'key1' 

#dict={}

#dict[i] = 1

#if i in dict.keys():
    #dict[i] = dict[i]+1


'''

dcitionary:{'python':1  , 'is': 2 , ''}


if i in my_dict.keys():
    my_dict[i]= my_dict[i] + 1
else:
    my_dict[i]=1
    
    
    
toosh for bzni max ro peyda koni
    


'''






'''
۵

برنامه‌ای بنویسید که یک جمله دریافت کند و طولانی‌ترین کلمه را پیدا نماید. اگر چند کلمه طول یکسان داشتند، اولین کلمه نمایش داده شود.

مثال:

:Input
Python programming is extremely interesting

:Output
extremely
Length: 9

'''


#jomle --> split(' ') -->[word1,word2] -->for bezani

#len()    max_len = 0 

#if len() > max_len --> max_len 
#max_len_word = ''
#too on ife --> agr len (kalamat) > max_len  
#ham max_)len ro update kon , kalameye max_len_word ro varesh dar

'''
۶

برنامه‌ای بنویسید که یک متن دریافت نماید. اگر متن شامل هرکدام از کلمات زیر بود، آن کلمه را پیدا کرده و تعداد تکرار آن را نمایش دهد:

[“hack”, “fraud”, “scam”, “password”, “atack”]
ﻣﺜﺎل :

: Input
This is a password atack and another password atack

: Output
password -> 2
atack -> 2

'''


#matne ro split mizani , for mizani

#if --> word in [“hack”, “fraud”, “scam”, “password”, “atack”]

#countesh mikoni --> printeshmikoni 

#?????!!!!!!





'''
۹

برنامه‌ای بنویسید و یک سیستم Login طراحی کنید که user و password را از کاربر دریافت کند.

کاربر حداکثر ۳ بار فرصت ورود داشته باشد.
اگر نام کاربری یا رمز عبور اشتباه بود، ﭘﯿﺎم زﯾﺮ را ﻣﻄﺎﺑﻖ ﻣﺜﺎل زﯾﺮ ﺑﺪﻫﺪ ﺑﻪ ﻫﻤﺮاه ﺗﻌﺪاد ﺗﻼش ﻧﺎﻣﻮﻓﻖ نمایش داده شود.
Wrong username or password
Atempts remaining: 2

اگر اطلاعات درست بود، پیام Login successful نمایش داده شو

'''





failed_count = 0 
while True:
    user = input('useername:')
    password = input('password')
    
    
    if user=='admin' and password=='1234':
        print('login successfuly')
        break
    
    #else:
        
    print('username ya password eshtebah mibashad')
    
    if failed_count>=3:
        print('shoma bish az hade mojaz ghalat vared krdid')
        break
    
    failed_count = failed_count + 1
    
    print('talashe namovaafagh:',failed_count)
    
    
    


#set interaction-->eshterak migire

#2 for anjam bedid

'''
۱۰

برنامه‌ای بنویسید که دو جمله از کاربر دریافت کرده و مشخص کند چه کلماتی در هر دو جمله وجود دارند.

Sentence 1:
I love Python programmingSentence 2:
Python is a powerful programming language
Common words:
Python
Programming

'''









#===================================
#===================================
#===================================
#===================================
# Javab ----------------------------
#===================================
#===================================
#===================================
#===================================
#injaro9 kasani k hal kardan bebinand (ke motmaen shan)
#onaei k hal nakrdan , hint haye balaro bebinan hal konan

#tozihate takmili -> jalse bad













