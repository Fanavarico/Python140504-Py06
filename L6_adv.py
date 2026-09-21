#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:12:28 2026

@author: apm


L6_ADV


"""


'''

Asan kojaeim --> 200 ta notes yad grfitm -> hameye inaor hefz??
bayad ma yek derakht az kole python too zehnemon bashe
ke vaghty khastim hal konim bedonim aval kodom shakhe hastim
bad berim too oon shakeh riz tr bshim



Human (english) <------interface(python)-----> Machine (binary)
'''


#========================================================
#========================================================
#========================================================
#========================================================



'''
Python --> zaban --> trasnlate mikone age baladeshbashim
vaghty toye editor/IDE mizanim roo run , python --> binary va ejra mishe


python --> yek zabane mesle faransavi , italian, farsi --> vocab , grammar

tooye code toye yek file .py shoma faghat mojazid be zabane python beenvsiid

agar bekhahid be zabane digar benevisid # qutation --> comment, description,....


harchizi gheyr az in b se bakhsh taghsim mishe


1- Python built in functins --> tavabe ye dakhelie python ro darid
ina yek amalkardi daran --> spyder narenji mishan
print() --> in namayesh mide too console
input() --> yek tabe hast ke vorodi migire va khorojio mirize to zarf
        nokat --> 1-khoroji mid emirizi to zarf 2-khorojishj hamishe str
type() , len() , .........

kafie sar titr ro search bezanid --> kole tavabe ro miare 
mohemtarin ha dars dade shode, hamashono dodne done berid yad bgirdi
abs() --> abs(-10) --> +10 absolute -
max([10,20,30,40]) -> 40
min([10,20,30,40]) --> 10
sum([10,20,30,40,50])-->150

zip() , enumerate() --> for ham estefade mishan
isinstance() --> check krdane type hast
format() 

khode type ham --> int , float

'''
print()
input()
type()
len()
abs()
max()
min()
sum()
zip()
enumerate()
format()
isinstance()
int() #adade ashari bezariu olosh --> intsh
#int(input()) 
float()
complex()
bool()
str()
list()
tuple()
set()
dict()


#========================================================
#========================================================
#========================================================
#========================================================

'''

2- keywords --> banafsh mishan
vaghty mikhahhi logice code ro avaz koni

shoma vaghty yek file .py dari --> run --> mifrste ipython ->
shabihe yek ensan az bala be paein az chap be rast shoro mikone be 
run krdn --> in mantegh ro beham bznid --> keywords --> banafshan
and 
or
if
for
while
else:

    
    2.1 Conditional statement (dastoorate sharti)
    
        2.1.1. Just if
        
        
        2.1.2. If else
        
        
        2.1.3. If elif elif else
    
    
    
    
    
    
    
    
    2.2. Loops (halghe ha)
    
    
        2.2.1. For
        
        
        
        
        2.2.2. While
        
        
        
        
'''




#========================================================
#========================================================
#========================================================
#========================================================

'''

3- variables (moteghayer)  zarf

harchizi joz python built in function benevisi ya keywordds 
na narenji mishe na banafsh --> esme yek zarf (moteghayer)


zarf ? ---> yek chizi hast ke dakhelesh yek ya chandin meghdar (value) zakhire mikone


a= 10 

name = 'ali'

sefid -> unknown -> khodet tarif koni

    

    3.1. Numbers --> 
        3.1.1 Int --> sahih 
            a = 10    
            b = 20
            c = 30
        3.1.2. Float --> ashar
            a = 10.223
            a=10.223322332
        
        3.1.3. complex --> riaziati --> i + j
        
        
        ba numbers --> 
            amaliate mohasebati
            c = a + b
            **  , * , / , + , -  , =
            dastoro --> ejra mishe
            
            amaliate moghayese
            == != > >= < <=
            a==b --> true false
            
            
    3.2. Boolean --> True , False
    
    
    3.3. Str --> string --> vaghty mikhahi yek chizi ya chandin chizi az
    keybaordet ro be onvane megdhar too zarf berizi
    
        name = 'ali'
        
        a ='2' -->str 
        a=2  --> int
        
        zarf = 'alipilehvar'
        
        zarf[index]
        
        zarf[0] ->a
        
        zarf[3:11] -->pilehvar
        
        
        str -> str functions() --> tavabe ei ke fght baraye str ha hastand
        
        lower
        
        zarf = 'alipilehvar'
        ####xxx lower(zarf)
        
        zarf.lower()   zarf.upper()
        
        khoroji midan , khdoe zrf taghir nmikone
        
        new_zarf = zarf.upper()
        zarf -->ali
        new_zarf --> ALI
        
        upper() lower() title() .......
        zarf.count('a') --> 3     zarf.find('a') --> 2
        
        islower() isupper() ->true false
        
        ***
        yekbar ham ke shode bayad kolesho bara khdieton benevisid
        in baes mishe vaghty tamrin mikonid
        yeja ke ba str ha kar mikonid, yani zarfi darid vorodi darid
        midoni felan kari ke mikhahid konid (pichidash konid)
        str funbctetsh hast
        
        yek jomle darid -> kalame haro az toosh joda konid -->list
        .split()
        
        space samte chapo  samte rasto hazf konid
        .strip()
        
        bebinid yek kalame hamash az adad hast ya na??
        .isdigit()
        
        https://www.w3schools.com/Python/python_ref_string.asp
        
        
    3.4. Iterables --> chandin meghdar dar yek zarf bezari
    multiple values inside one variable 
    
        --> list() , tuple() , set() ,dictionary()
        --> kole kareshon-->ejaze midahand ke shoma chandin meghdar ro
            dakhele yek zarf berizid
            
            key koja? ---> vaghty chndin megdhar khasi zakhire konid --> iterables estefade koni
            kodom behtre --> darsesh midm
    
    a=10  
    yek zarf , yek meghdar
    name = 'ali'
    
    3.4.1. List() --> marsoom tarin type i hast ke shoma estefade mikonid
    baraye inke chandin meghdar dakhele zarf beirzid
    
    esm = [value1,value2,value3,value4]
    
    a = [1,2,3,4,5]
    a=[10,20,30,40,50]
    b=[10,10.32332 ,True , 10 , 'Ali']
    
    a=[1,2,3,4]
    a=list([1,2,3,4])
    
    b = [10,20,[30,40,50]]
    
    --> marsoom tarine ama yadet bashe hameye inaro ba 3 moalefe misanjan
    -- >  list
            
        ordered (index) , changable hast , allow duplicated
    
    
    
    [val1,val2,val3]
    
    index value
    0     value1   10.3223
    1      value2 'alI'
    2       value2 10
    
    ordered (index)-->dastresi peyd akonam
    
    zarf -chandin meghdar --> 
    
    names = ['ali','vahid','reza']
    
    names[0]
        
        
        
'''

names = ['ali','vahid','reza']

names[0] #Out[1]: 'ali'

names[0:2]#Out[2]: ['ali', 'vahid']

#index -> access 

#dastresi peyda mikonam ke chi?
#1--> read koni ->bekhonish
#2--->changesh koni (changable?)


names[0] = 'hamid'

print(names) #['hamid', 'vahid', 'reza']



names=['ali','ali','ali']



#shoma vaghty chndin chizo khatsti zakhire koni --> list ro dar nazar begir (by default)


#list functions -----> fucntion hae k fgth baray elist ha hast


names.insert(2,'vahid')

#new_name = name.upper() -->tavabe str --> khoroji midan, emal nmishan
#tavbeye list --> emal mishan , khoroji nemidan

print(names) #['ali', 'ali', 'vahid', 'ali']



#---mohem tarin tabe --> append harchi bzri b tahesh ezaf

#for ha --> estfade -> for mizani , ifi , .append() 


names.append('asal')
print(names) #['ali', 'ali', 'vahid', 'ali', 'asal']


#---remove() pop()

names.remove('vahid')
print(names) #['ali', 'ali', 'ali', 'asal']


names.pop(1)
print(names) #['ali', 'ali', 'asal']

names.pop(1)
print(names) #['ali', 'asal']


#vahido be tah
names.append('vahid')
print(names) #['ali', 'asal', 'vahid']


names.insert(0,'reza')
print(names) #['reza', 'ali', 'asal', 'vahid']





names.count('ali') #1


#.sort() --> sortesh

names.sort()
print(names) #['ali', 'asal', 'reza', 'vahid']

#belax ->sorte barax
names.reverse()


#del names


names.clear()
#khode zarfo ba jash hazf koni, tooye zarf ro pak koni

#delete va clear

names = []



#https://www.w3schools.com/Python/python_ref_list.asp



'''
3.4.2. Tuple

hala ke listo darim, tuple ro gozashtan?? ghazie chie?
mage multiple values --> one variable --> iterables, list , chi mishe tuple ??



ordered (index) ,  unchangable  , allow duplicated


index  values
0      val1
1     val2
2     val3


tuple --> yek listi hast ke change nemishe



'''

a=[10,20,30,40]

b = (10,20,30,40)

b= tuple((10,20,30,40))


c =(10,10,20,30) #duplicated

#yek tupel --> yedone 10 bezari
d = (10) 
print(type(d)) #<class 'int'>


d=[10]
print(type(d)) #<class 'list'>


#gar fght tupel --> agar yek ozv bekhahi --> ,
d = (10,) 
#adad nist

print(type(d)) #<class 'tuple'>


#chandin valeus inside one variable

print(type(a)) #<class 'list'>
print(type(b)) #<class 'tuple'>



#access ->index -> order

a[0] #Out[29]: 10
b[0] #Out[30]: 10


#-->chanagblity

a[0]=100

print(a) #[100, 20, 30, 40]



b[0]=100
#TypeError: 'tuple' object does not support item assignment


#Yani shoma nemitavanid taghir dahid ????????




#----------
#tuple -> hamon list hast ke nmishe change shod ???

#vaghty shoma ba databse kar mikonid ya ba chizhaye mortabet ba db --> nemikhahid 
#eshtebahi --> codeton biad yeho , pichide (complex) nmikhahid ina change beshan
#hamoni k az db migirid khate 4 az database (10,20,30,40) toye kahte 400 behehs dastresi peyd amikonid
#4 ta 400 , eshtebahi changi roosh sorat begire

#40 doros hsod --> dataton amadas --> zakhrie koonid databse

#efficiency --> background --> 800 anjam #
#40 ta 800 -->etefaghi in variable --> hesab_ketab --> change nashe --> tuple

#------unpacking--------
a = [10,20,30]
b  , c , d  = a



a = (10,20,30)
b , c , d = a



def jam_tafrigh(numb1,numb2):
    jam = numb1 + numb2
    tafrigh = numb1 - numb2
    return jam , tafrigh 


zarf = jam_tafrigh(10,20)

print(type(zarf)) #<class 'tuple'>

print(zarf) #(30, -10)

#vaghtyy tabe chandin khoroji dahste bashe -> hame khoroji haro 2 ,3,4,-->tupel va pas mide

zarf[0] #Out[45]: 30


zarf1 , zarf2 = jam_tafrigh(10,20)


#accidental changable nist --> tasaodif changesh koni


#python az yek version

b = (10,20,30,40)

b[0]=100 #TypeError: 'tuple' object does not support item assignment

#man inkaro krdm na ke joloto begiram , balke etefaghi in karo nakoni

#casting

a=10
print(type(a)) #int
b = float(a)
print(type(b)) #float 
#b=10.0

c ='10'
d= int(c)
print(type(c)) #str
print(type(d)) #int


#----
b = (10,20,30,40)
b[0]=100 #TypeError: 'tuple' object does not support item assignment

c = list(b)
c[0]=100

print(c) #[100, 20, 30, 40]

b = tuple(c)
print(b) #(100, 20, 30, 40)




#1---> tupel hamonlistie ke unchangable hast
#2--> khob inke man tonesam --> tasadofi chage nmitoni koni 
#rahesh hast




#---------------------


'''
3.4.3.set

no order ( no index) , unchangable , No duplicated


Majmooe haye riaziat --> majmoe
tekrar haye yek list ro hazf koni


'''

a=[10,20,30,40]  #list
b=(10,20,30,40) #tuple
c ={10,20,30,40} #set

print(c) #{40, 10, 20, 30}


#set functions () --> eshterak , ejtema ,....
#search --> dota majmoe riazi -_> ekhtelafe , ejtema 


#--> 
my_names=['ali','vahid','hamid','reza','ali']


b = set(my_names)

my_names = list(b)




'''

list [] --> order , changable, allow duplicated
tuple () -> ordder , unchangabel, allow duplicated -_> listie ke unchanagbel (DB)
set {} --> no order, unchanagbel , no duplicated -_> majmoe riazi, hazfe tekrari


index value
0      val1
1    val2
2     val3

3.4.4. dict

Information --> etelaat

'''

#ensan bashe , product , ....

information =['ali',30,'09190000000','Tehran']

information[0] #Out[57]: 'ali'

information[1]



#infromation = tabe() --> 50 ta khoroji mide 
#nemdioni sene taraf kodom index --> print() ->codet automation

'''
tartib barma mohem nis


index value
0      ali
1     30
2      09199




key   value
esm    ali
sen    30
phoen  0919999



information[2]

information['phone']


infromation_list = [value1 , value2 , value3]

na tanha value ro msiazam , hamzaman kilidvazhe midam (index)


infromation = {key1 : value1    , key2 :value2}


infromation = {key1 : value1    , 
               key2 :value2   ,
               key3 : value3 ,
               key4 : value4}





'''

information_list =['ali',30,'09190000000','Tehran']


information_list[1] #Out[60]: 30

information_dict = {  'esm' : 'ali' , 'sen':30  ,'phone':'0919000' ,'shahr':'Tehran'  }


information_dict['sen'] #Out[61]: 30



#chanagbel


information_dict['sen'] = 31

print(information_dict)

#{'esm': 'ali', 'sen': 31, 'phone': '0919000', 'shahr': 'Tehran'}




information_dict['code_meli'] = '0440....'


'''
more information
https://www.w3schools.com/python/python_ref_dictionary.asp
'''


#sen
information_dict['sen'] #Out[65]: 31

information_dict['salamo aleykom'] #KeyError: 'salamo aleykom




information_dict.get('sen') #Out[66]: 31
zarf = information_dict.get('salamo aleykom')
print(zarf) #None




information_dict = {  'esm' : 'ali' , 'sen':30  ,'phone':'0919000' ,'shahr':'Tehran'  }

sen = information_dict['sen']


#----safe tar

sen = information_dict.get('sen')





#-------
#db,frontend ,.....

information_dict = {  'esm' : 'ali' ,'phone':'0919000' ,'shahr':'Tehran'  }

sen = information_dict['sen']

# KeyError: 'sen'


#----safe tar

sen = information_dict.get('sen')

#if sen:  
    
sen = information_dict.get('sen',18)
#agar dashte ke hamono vardar
#agar nadasht oon kildivazhe ro , ino default bezare




for x in information_dict:
    print(x)


'''
esm
phone
shahr
'''


#kilid vazhe ha


for x in information_dict.values():
    print(x)

'''
ali
0919000
Tehran
'''


#joftys

for x,y in information_dict.items():
    print(x,y)

'''
esm ali
phone 0919000
shahr Tehran
'''


for key,value in information_dict.items():
    print(x,y)
    
    
    

#---------------
products = {
    "laptop": 1200,
    "phone": 800,
    "tablet": 500,
    "mouse": 50
}


for price in products.values():
    if price>400:
        print(price)

'''
1200
800
500
'''

#------
for product,price in products.items():
    if price>400:
        print(product)

'''
laptop
phone
tablet
'''




#in print mikone
for price in products.values():
    if price>400:
        print(price)


best_prices=[]
for price in products.values():
    if price>400:
        #print(price)
        best_prices.append(price)

print(best_prices) #[1200, 800, 500]



best_prices = [price for price in products.values() if price>400]
print(best_prices) #[1200, 800, 500]


dict(best_prices)
#TypeError: cannot convert dictionary update sequence element #0 to a sequence






#bedone print --. for

information_dict.keys() #Out[70]: dict_keys(['esm', 'sen', 'phone', 'shahr', 'code_meli'])

information_dict.values() #Out[71]: dict_values(['ali', 31, '0919000', 'Tehran', '0440....'])


information_dict.pop('sen')



information_dict.clear()

#information_dict={}







#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================
#========================================================


'''
tamine hsomare 1 hal shod
tamrine shomare 2 hal shod
tamrine shomare 3 hal shod

tamrine shomare 4 (jalse 5) --> 2 ,3 soal hal shdoe, hint dade shode

tamrine shomare 5 (jalase 6)



'''

'''
tmrine shomare 5 -- jalase 6

'''


'''
1- yek products az yek foroshgah darim
barname  ie benvisid, geran tarin mahsol, arzan tarin mahsol, maingin ,
mahgsolati ke gheymateshan bish az 500 , majmoe gheymate tamame mahsolat


products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}
'''
products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}

print(type(products)) #<class 'dict'>

#bayad beram toosh --> geron tarino peyda konm

max_price = 0
for price in products.values():
    if price > max_price:
        max_price = price
        
print(max_price) #1200




max_price=0
for product,price in products.items():
    if price > max_price:
        max_price = price
        max_product = product
        
print(max_product, 'bishtarin hast ba gheymate',max_price)  

#laptop bishtarin hast ba gheymate 1200


#-->minimumesho bznid

max([10,20,30,40]) #Out[96]: 40


most_expensive = max(products , key = products.get)

chepeast = min(products,key = products.get )


#jame koleshon total price



#price -> values
total = 0 
for price in products.values():
    total = total + price
    

print(total) #2550



products.values() #Out[100]: dict_values([1200, 800, 500, 50])

total = sum(products.values()) #Out[101]: 2550


#------totalo

#average = total / len


average =  total / len(products)
print(average) #637.5




for product,price in products.items():
    if price>500:
        print(product,price)

'''
laptop 1200
phone 800
'''


best_prices=[]
for product,price in products.items():
    if price>500:
        #print(product,price)
        best_prices.append({product:price})



#------------
'''

inventory = {
“apple”: 20,
“banana”: 5,
“orange”: 0,
“milk”: 12,
“bread”: 0
}


too ye list available ha
unavailable ye lste



'''
inventory = {
    "apple": 20,
    "banana": 5,
    "orange": 0,
    "milk": 12,
    "bread": 0
}

available_products=[]
unavailable_products=[]
for product,stock in inventory.items():
    if stock==0:
        unavailable_products.append(product)
        
    else:
        available_products.append(product)
        
        
    
print(unavailable_products) #['orange', 'bread']
print(available_products) #['apple', 'banana', 'milk']


#yek listi az dictionary ha


available_products=[]
unavailable_products=[]
for product,stock in inventory.items():
    if stock==0:
        unavailable_products.append({  product : price })
        
    else:
        available_products.append({  product : price })
        
print(unavailable_products)  #[{'orange': 50}, {'bread': 50}]
        
        
'''
3

frequency
shoamreshe horof ba fdictionar
        
'''

name='alipilehvar'


#code -->
'''
{
 'a' :2
 'l':2}
'''

my_dict={}
for char in name:
    if char in my_dict :
        my_dict[char] = my_dict[char] + 1

    else:
        my_dict[char]=1
        
    
print(my_dict)

'''
{'a': 2, 'l': 2, 'i': 2, 'p': 1, 'e': 1, 'h': 1, 'v': 1, 'r': 1}
'''


#------4---
employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },

    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}

#balatarin hoghoggh , kamtarin hoghogh , hoghoghe bala 300 , miangine hoghogh



#for key , value in employees.items():
    

highest_salary = 0

highest_salary_employ = None

for employ , information in employees.items():
    if information['salary']>highest_salary:
        highest_salary= information['salary']
        highest_salary_employ= information['name']
        
        
print(highest_salary_employ)    #Sara  
    
    
    
    
    
    
lowest_salary = float('inf')
   
lowest_salary_employ = None
 
for employ , information in employees.items():
    if information['salary'] < lowest_salary:
        lowest_salary= information['salary']
        lowest_salary_employ= information['name']
        

print(lowest_salary_employ) #Reza




#------------
total = 0 
for employ , information in employees.items():
    total = total + information['salary']
    

print(total)   #10300
len(employees)
        


average = total  / len(employees)
print(average) #3433.3333333333335


#khoddeton hal konid --> onaei ke bishtr az 3000 ogh daran namayesh bede 
#--> esmeshono print kon



#--------etelaate danesh amoozan
students = {
    "Ali": [18, 17, 20],
    "Sara": [15, 19, 18],
    "Reza": [12, 14, 10],
    "Mina": [20, 20, 19]
}

#miangineshono , vaziate ghabolishon 
#>=15 -> pass shode


mianging_students = {}


for name,scores in students.items():
    miangin = sum(scores)/len(scores)
    mianging_students[name] = miangin
    
    
print(mianging_students)
'''
{'Ali': 18.333333333333332, 'Sara': 17.333333333333332, 'Reza': 12.0, 'Mina': 19.666666666666668}
'''


#************
#---> pass shdoan ro hesab kone pass shodan -> liste ke esme onaei ke pass hsodan print kone
#---> balatarin miangin ro dare ro peyda kon --> esmesho bege



#--------------------
'''

tuple i az tuple ha darim

har moshtari chegahdr kharid krde
kodam bishtarinkharido , kodom mahsol chnabar forokhte shode, majmoe daramade foroshgah


'''

sales = (
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
)

all_kharid={}
for kharid in sales:
    #kharid[0] , kharid[1] , kharid[2] 
    if kharid[0] in all_kharid:
        all_kharid[kharid[0]] = all_kharid[kharid[0]] + kharid[2]
    
    else:
        all_kharid[kharid[0]] = kharid[2]
        
        
print(all_kharid) #{'Ali': 2050, 'Sara': 2000, 'Reza': 1200}

#--> boro inja maximum ro peyda kon-->
#majmoe daramae foroshgah -->




sales = (
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
)

all_kharid={}
for kharid in sales:
    #kharid[0] , kharid[1] , kharid[2] 
    if kharid[1] in all_kharid:
        all_kharid[kharid[1]] = all_kharid[kharid[1]] + 1
    
    else:
        all_kharid[kharid[1]] = 1
        
    
print(all_kharid)
#{'Laptop': 3, 'Phone': 2, 'Mouse': 1}







#7 , 8 , 9 ----> hal nashdoe


    






