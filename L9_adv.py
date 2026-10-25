"""
In The Name of GOD


Created on Sun Oct 25 20:21:59 2026

@author: Ali Pilehvar Meibody



L9 --> online




zabane C --> in zaban paye ye zaban ha , ghabl tar z pytho

in zaban --> tamame karhaei ke ma ba python mikonim mikrd

ama moshkele --> learning curve --> toolmikeshid , sakht bood
afrade kmatari balad bodan, develop sakht bod, etabkhoen ha kamtare

Python --> sade tare, nazdiktre be zabane ensan (english) 
va ... --> rahat tar, develop sari, ketabkhoen haye bsihtr


C --> naghse jedi e dasht --> Class suport nmikrd
yek zabane dige--> updat ehham velsh kon
zaban C -->upgrade --> C++
mohemtarin shakhese ash --> class --> Object oriented programming (OOP)
code zani konid 

hamchin goftn -> optimziation anam bdim , yekseri
code ha avaz she va .. --> avaz shod

C++ -->zabane narm afzar ha , computation, gaming , graphic (sorate bala )

Hooshe masnoei --> Shabake haye asabi masnoei (
    Artificial Neural Network (ANN))
modele payeye tamame hoshe masnoei jahane

yek modeli k saratan pishbini mikone,
yek modeli k khane haye califronai ro pishbini mikone
modele paye eye chat gpt , claude
modele paye e k apple -_> auto correction , predict next word
model haye skahte video ,....

sakhtare paye ash --> ANN (shabake ye asabi masnoei)
sorat --> paye ha --> C++ neveshte shode

python --> zabane hoshe masnoei hast

programmeraye aslishon --> sherkatyaye tensorflow , pytorch
--> c++ core (haste neveshte) , interface -> python mitoni codesh


Ahamiate Class --> c --> C ++ 


class ro yad bgirim

dar kole python b 3 ravesh ma code mzinim

1- Monolothic (script)  .py az bala ta paein run mikoni
--> yek akri --> bere tooye fodlere felan , 100 ta ax
convert kone va tamam

automation , conversion ,.......

do chiz estefade mikoni->function class
2- Function based
3- Object orineted programming



Function --> zamani k yek kari ro
mikhay capsulesh koni --> vroodi -_>box __<khoroji
tekrare ziado migire, chandin khate code ro
mziare flexible , 


Class ---> too delam koli variable(attribute) function(methods)
--> object besaze


object b ch drde ma mikhore??????



class name:
    def __init__(self,name,email,balance):
        self.name = name
        ....
        
"""
#class --> shamele variables va methods 
#azash chi miszim --> objects 

#khob hala object ke sakhte mishe 

#__init__ ro besazi -> b in fekr kon chijori
#object mikhay bsazi


class bank_account:
    def __init__(self,fullname , code_meli , phone_number,age , initial_balance):
        pass


#chia bayad bedam baraye inke yek
#ekante bank skahte bshe
#object1 = bank_account()

#yek nfr mikhay hesabe bank besazi
#nam mikhad, shomare meli mikhad, telephone mikhad 

fard1 = bank_account(fullname='ali pilehvar meibody',
                     code_meli = '044...',
                     phone_number = '0912...',
                     age =20 , 
                     initial_balance =10000)


#bank_account ba in moshakahsat yek object (chiz) barmigrdone

print(type(fard1))
#<class '__main__.bank_account'>

fard1.name #AttributeError: 'bank_account' object has no attribute 'name'
#chenin chizi tarif nshode

#self.fullname #NameError: name 'self' is not defined

#biron mikham b esme trf dastresi peyda konm
fard1.fullname
#AttributeError: 'bank_account' object has no attribute 'fullname'

#yek chizi sakhte shode k hichi too delesh nis




fard1 = bank_account(fullname='ali pilehvar meibody')

#TypeError: bank_account.__init__() missing 4 required positional arguments: 'code_meli', 'phone_number', 'age', and 'initial_balance'


#kole kare tabeye __init__ ine ke bege
#agha ina lazeme baraye sakhte yek object(chiz)

#oon objectam (chizam) dakhelsh moteghayd ha
#vizhegi ha, attribute i dashte bashe

#bayad too delesh zakhire konam

#fard1 
#fard2
#fard3,,,.......


#hamashon too deleshon yek chizi dahst ebashan
#k baraye khodeshone


#----> self --> khode chiz --> khode shey -> khode object
#object itself


class bank_account:
    def __init__(self,fullname , code_meli , phone_number,age , initial_balance):
        self.full_name = fullname
        self.code_meli  = code_meli
        #hamaro save konm? -> majbor na
        self.phone_number = phone_number 
        self.age = age 
        self.balance = initial_balance
        self.transactions= []
      
        
      
fard1 = bank_account(fullname='ali pilehvar meibody',
                     code_meli = '044...',
                     phone_number = '0912...',
                     age =20 , 
                     initial_balance =10000)


fard1.age #Out[15]: 20

fard1.fullname #AttributeError: 'bank_account' object has no attribute 'fullname'
fard1.full_name #Out[17]: 'ali pilehvar meibody'



#inja nchzii k paramter migirim ba self. yekie
fard1.code_meli #Out[18]: '044...'


fard1.initial_balance #AttributeError: 'bank_account' object has no attribute 'initial_balance'
fard1.balance #Out[20]: 10000

'''

def __init__(self)  -->ejbari ->
az koja bdonm bad az self chi benevism?
 be in fekr kon ke ghrar hast vghty object akhtebshe
 chia begirim tya ch argument hae too dele clas benevisim ta object c
 crret bshe --> construction
 


self.felan = zarf

zarf haro az __init__ migirim mirizim b nami tooye self.

1--> aya hame chizaye k too __init__ hast bayad too self zakhire sbeh?
majboor nistim , ama mamolan mishe -->chon niazesh dahstim k grftim

2--> aya bayad ham esm bashe chizi k migirimo self
self.full_name = fullname

fulname begir va tooye full_name beriz ->
ama hamishe in do esm shabihe hame

3-> mitonim chiz haye ezaf ya tarkibi??
first_name , last_name

self.fullname = first_name + last_name
self.transactions = []
self.count =0

'''


class bank_account:
    def __init__(self,name_kamel,code_meli , shomare_telephone , sen , mojodi_avalie):
        self.full_name = name_kamel 
        self.national_id = code_meli 
        self.phone_number = shomare_telephone
        self.age = sen
        self.balance = mojodi_avalie
        
        

fard1 = bank_account(name_kamel='ali pm', code_meli='033', shomare_telephone='0919', 
                     sen=50, mojodi_avalie=100000)


fard1.full_name #Out[23]: 'ali pm'

print(fard1.full_name)
        
zarf = fard1.full_name



#b ina --> attributes 

hasattr(fard1,'full_name') #Out[25]: True
hasattr(fard1,'name_kamel') #Out[26]: False



#----------------------------------------

#tabe ya method

#az yek class --> objct haye motefavet besazam
#fard1 ba khososiate khodesh, fard2 ba khososiate khdoesh
#fard3 ,,...

#tabe bashe baraye hamashon ejra bshe
#ama shakhsi beshe

#Man ybar tabe benvism vali abraye har chiz (shakhs) yekjor rftar kone

#---> function inside class --> METHOD



class bank_account:
    def __init__(self,name_kamel,code_meli , shomare_telephone , sen , mojodi_avalie):
        self.full_name = name_kamel 
        self.national_id = code_meli 
        self.phone_number = shomare_telephone
        self.age = sen
        self.balance = mojodi_avalie
    
    #be inke chijori estefade ghrar hast koni
    #fard1.welcome()
    #aksariat self drn
    #vaghty tabart vorodi nadare, bade self
    #chizi nzr
    def welcome(self):
        print('salam moshtariue aziz khsoh omadi')
        




fard1 = bank_account(name_kamel='ali pm', code_meli='033', shomare_telephone='0919', 
                     sen=50, mojodi_avalie=100000)



fard1.full_name


#methode welcome estefade koni -->
#yek tabe ei hast k vorodi ndre
#sedash mzin -> mige khosh omdi moshtarie aziz .......
#vorodi nadare, print mikone , khoroji ham ndre 

fard1.welcome()





fard1 = bank_account(name_kamel='ali pm', code_meli='033', shomare_telephone='0919', 
                     sen=50, mojodi_avalie=100000)

fard2 = bank_account(name_kamel='vahid pm', code_meli='033', shomare_telephone='0919', 
                     sen=50, mojodi_avalie=100000)


fard1.age #50

fard2.full_name #vahid pm


#() --> parantez moshakahseye tabe ast


#.welcome() -->vrodoi nmgiird


fard1.welcome()
#salam moshtariue aziz khsoh omadi


fard2.welcome()
#salam moshtariue aziz khsoh omadi


def welcome():
    print('salam msohatrie aziz')
    
    
    
    
class bank_account:
    def __init__(self,name_kamel,code_meli , shomare_telephone , sen , mojodi_avalie):
        self.full_name = name_kamel 
        self.national_id = code_meli 
        self.phone_number = shomare_telephone
        self.age = sen
        self.balance = mojodi_avalie
    
    #be inke chijori estefade ghrar hast koni
    #fard1.welcome()
    #aksariat self drn
    #vaghty tabart vorodi nadare, bade self
    #chizi nzr
    
    #shakhsi mikonie
    #esmesho bgi
    def welcome(self):
        print('salam moshtariue aziz',self.full_name  ,'khosh amadi')
        
        
fard1 = bank_account(name_kamel='ali pm', code_meli='033', shomare_telephone='0919', 
                     sen=50, mojodi_avalie=100000)

fard2 = bank_account(name_kamel='vahid pm', code_meli='033', shomare_telephone='0919', 
                     sen=50, mojodi_avalie=100000)
     
        
fard1.welcome()
#salam moshtariue aziz ali pm khosh amadi


fard2.welcome()
#salam moshtariue aziz vahid pm khosh amadi



zarf = fard2.welcome()

#salam moshtariue aziz vahid pm khosh amadi

print(zarf) #None







class bank_account:
    def __init__(self,name_kamel,code_meli , shomare_telephone , sen , mojodi_avalie):
        self.full_name = name_kamel 
        self.national_id = code_meli 
        self.phone_number = shomare_telephone
        self.age = sen
        self.balance = mojodi_avalie
    
    #be inke chijori estefade ghrar hast koni
    #fard1.welcome()
    #aksariat self drn
    #vaghty tabart vorodi nadare, bade self
    #chizi nzr
    
    #shakhsi mikonie
    #esmesho bgi
    def welcome(self):
        zarf = 'salam moshtariue aziz',self.full_name  ,'khosh amadi'
        return zarf
        
        
        
        
fard1 = bank_account(name_kamel='ali pm', code_meli='033', shomare_telephone='0919', 
                     sen=50, mojodi_avalie=100000)

fard2 = bank_account(name_kamel='vahid pm', code_meli='033', shomare_telephone='0919', 
                     sen=50, mojodi_avalie=100000)
   


zarf = fard1.welcome() 

#chizi print nmishe

print(zarf)

#dige none nist
#('salam moshtariue aziz', 'ali pm', 'khosh amadi')


'''
vaghty bekhahhi yek tabe (method) dar dele class besazi

nefgah kon chijori esteafde mishe

1--> chandta vorodi dr

age nadare

def function(self)

age dare

def fucntion(self,voro1,voro2,...)

obj1 = class(.....)
obj1.function()
obj1.function(......)

2-->toosh b shakhsi sazi niaz dri?

self mitoni komak begiri too dele tabe

3-->aya khoroji dre?

zarf = obj1.function()

def :
    return .......




'''

class STR:
    def __init__(self,value):
        self.value = value
    
    #zarf.upper()
    def upper(self):
        #
        #return
        pass
    
    #zarf.count('a')
    def count(self,character):
        countint = 0
        for char in self.value:
            if char==character:
                countint = countint + 1
                
        return countint
    
    
    def find(self,character):
        for i in range(0,len(self.value)):
            if self.value[i]==character:
                return i
        return -1
        
        
        
        
        

name = 'ali'

name1 = str('ali')

name2 = STR('ali')

#hardafi shoma yekchizi str misazid
#yek object az clase str misazid

print(type(name1)) #<class 'str'>
print(type(name2)) #<class '__main__.STR'>


name1.upper() #Out[52]: 'ALI'

zarf = name1.upper()

print(name1) #ali
print(zarf) #ALI

#tabe ye upper() -> khoroji mdiad, emal nmishod

name1.count('a') #Out[60]: 1

name2.count('a') #Out[64]: 1






class LIST:
    def __init__(self,value):
        self.value = value
    
    #zarf.append(adad)
    def append(self,element):
        self.value.append(element)
        #chizi return nmidadddd
        #rooye self.value ejra mishdo
        

a=[10,20,30]

a=list([10,20,30,40])

b= LIST([10,20,30,40])


a.append(50)
print(a) #[10, 20, 30, 40, 50]

b.append(50)
print(b.value) #[10, 20, 30, 40, 50]






#========================================



class bank_account:
    def __init__(self,name_kamel,code_meli , shomare_telephone , sen , mojodi_avalie):
        self.full_name = name_kamel 
        self.national_id = code_meli 
        self.phone_number = shomare_telephone
        self.age = sen
        self.balance = mojodi_avalie
        #self._balance
    
    #be inke chijori estefade ghrar hast koni
    #fard1.welcome()
    #aksariat self drn
    #vaghty tabart vorodi nadare, bade self
    #chizi nzr
    
    #shakhsi mikonie
    #esmesho bgi
    def welcome(self):
        
        print('salam moshtariue aziz',self.full_name  ,'khosh amadi')
    
    
    #fard1= bank_account(.....)
    #fard1.welcome()
    #fard.show_balance() #khoroji bir
    def show_balance(self):
        print('mojodie shoma hast:',self.balance)
        
        
    #mojodi = fard.get_balance()
    def get_balance(self):
        return self.balance

fard1 = bank_account(name_kamel='ali pm', code_meli='033', shomare_telephone='0919', 
                     sen=50, mojodi_avalie=100000)

fard2 = bank_account(name_kamel='vahid pm', code_meli='033', shomare_telephone='0919', 
                     sen=50, mojodi_avalie=200000)
   

fard1.show_balance() #mojodie shoma hast: 100000
fard2.show_balance() #mojodie shoma hast: 200000

zarf = fard1.show_balance()
print(zarf) #None



zarf = fard1.get_balance()
print(zarf) #100000

zarf2= fard2.get_balance()
print(zarf2) #200000



fard1.balance #Out[80]: 100000


fard1.balance = 50000

print(fard1.balance) #50000
fard1.show_balance() #mojodie shoma hast: 50000
fard1.get_balance() #Out[84]: 50000
#self.balance --> aaz mishe

setattr(fard1,'balance',6000)

print(fard1.balance) #6000
fard1.show_balance() #mojodie shoma hast: 6000
fard1.get_balance() #Out[88]: 6000


fard1.balance=-10000


#._ -->private attribute --> ino behesh dast anzan





class bank_account:
    def __init__(self,name_kamel,code_meli , shomare_telephone , sen , mojodi_avalie):
        self.full_name = name_kamel 
        self.national_id = code_meli 
        self.phone_number = shomare_telephone
        self.age = sen
        self._balance = mojodi_avalie


    def welcome(self):
        print('salam moshtariue aziz',self.full_name  ,'khosh amadi')
    

    def show_balance(self):
        print('mojodie shoma hast:',self._balance)
        
        
    #mojodi = fard.get_balance()
    def get_balance(self):
        return self._balance
    
    #fard1.balance = 20000
    #fard1.set_balance(20000)
    def set_balance(self,new_value):
        if new_value<0:
            raise ValueError('nemitavanid  adade manfi bezarid')
            
        self._balance = new_value
      
        
     #ezaf konim balan
     #fard1.deposit(5000) #-->print(anajm shod)
    def deposit(self,amount):
        self._balance = self._balance + amount
        print('ba moafahiat anjam shod')
        
    #new mojodi
    #zarf = fard1.deposit(5000)
   # def deposit(self,amount):
    #    self._balance = self._balance + amount
    #    return self._balance 
    
    def withdraw(self,amount):
        self._balance = self._balance - amount 
        print('ba moafaghiat najam shod')

#fard1.set_balance(10000)

#------------------advanced------------------
#attributes --> instance attributes --> fard1.fullname ,...
#class attributs ->baraye hameye fard ha yekie --> balaye __init__


class bank_account:
    bank_name = 'Melat'
    #show_balance_fee = 1000
    
    def __init__(self,name_kamel,code_meli , shomare_telephone , sen , mojodi_avalie):
        self.full_name = name_kamel 
        self.national_id = code_meli 
        self.phone_number = shomare_telephone
        self.age = sen
        self._balance = mojodi_avalie
        
        self.show_balance_fee = 1000
        self.deposit_balance_fee= 2000
        self.maximum_amount_withdraw = 2000000
        self.maximum_amount_deposit = 10000000
        self.minimum_balance = 1000
        


    def welcome(self):
        print('salam moshtariue aziz',self.full_name  ,'khosh amadi')
    

    def show_balance(self):
        if self._balance < self.show_balance_fee:
            raise ValueError('mojodie shoam baraye msohahedeye mojodi kafi nist')

        self._balance = self._balance - self.show_balance_fee
        print('mojodie shoma hast:',self._balance)
        
        
    #mojodi = fard.get_balance()
    def get_balance(self):
        if self._balance < self.show_balance_fee:
            raise ValueError('mojodie shoam baraye msohahedeye mojodi kafi nist')


        return self._balance
    
    #fard1.balance = 20000
    #fard1.set_balance(20000)
    def set_balance(self,new_value):
        if new_value<0:
            raise ValueError('nemitavanid  adade manfi bezarid')
            
        self._balance = new_value
      
        
    def deposit(self,amount):
        self._balance = self._balance + amount
        print('ba moafahiat anjam shod')

    def withdraw(self,amount):
        self._balance = self._balance - amount 
        print('ba moafaghiat najam shod')


fard1 = bank_account(name_kamel='ali pm', code_meli='033', shomare_telephone='0919', 
                     sen=50, mojodi_avalie=100000)

fard2 = bank_account(name_kamel='vahid pm', code_meli='033', shomare_telephone='0919', 
                     sen=50, mojodi_avalie=200000)
   
fard1.full_name #Out[92]: 'ali pm'

fard1.bank_name #Out[93]: 'Melat'
fard2.bank_name #Out[94]: 'Melat'

fard2.bank_name = 'blue bank'


fard2.bank_name #blue bank
fard1.bank_name #melat 



fard1.show_balance()






class bank_account:
    bank_name = 'Melat'
    #show_balance_fee = 1000
    
    def __init__(self,name_kamel,code_meli , shomare_telephone , sen , mojodi_avalie):
        self.full_name = name_kamel 
        self.national_id = code_meli 
        self.phone_number = shomare_telephone
        self.age = sen
        self._balance = mojodi_avalie
        
        self.show_balance_fee = 1000
        self.deposit_balance_fee= 2000
        self.maximum_amount_withdraw = 2000000
        self.maximum_amount_deposit = 10000000
        self.minimum_balance = 1000
        
        self._transactions=[]
        


    def welcome(self):
        print('salam moshtariue aziz',self.full_name  ,'khosh amadi')
    

    def _check_fee_balance(self):
        if self._balance < self.show_balance_fee:
            raise ValueError('mojodie shoam baraye msohahedeye mojodi kafi nist')

    def show_balance(self):
        self._check_fee_balance()
        
        self._balance = self._balance - self.show_balance_fee
        self._transactions.append(-1*self.show_balance_fee)
        print('mojodie shoma hast:',self._balance)
        
        
    #mojodi = fard.get_balance()
    def get_balance(self):
        self._check_fee_balance()
        self._balance = self._balance - self.show_balance_fee
        self._transactions.append(-1*self.show_balance_fee)
        return self._balance
    
    #fard1.balance = 20000
    #fard1.set_balance(20000)
    def set_balance(self,new_value):
        if new_value<0:
            raise ValueError('nemitavanid  adade manfi bezarid')
            
        self._balance = new_value
      
        
    def deposit(self,amount):
        if amount> self.maximum_amount_deposit:
            raise ValueError('hade aksar mitavan.. bardasht')
            
        
        self._balance = self._balance + amount
        self._transactions.append(amount)
        print('ba moafahiat anjam shod')

    def withdraw(self,amount):
        if amount > self.maximum_amount_withdraw:
            raise ValueError('hade aksar ....')
        
        if amount > self._balance:
            raise ValueError('mojodi kafi nemibshad')
            
        self._balance = self._balance - amount 
        self._transactions.append(-1 * amount)
        print('ba moafaghiat najam shod')
    
    def get_transactions(self):
        return self._transactions
    
    def show_transactions(self):
        for transact in self._transactions:
            print(transact)





#------------------------------------------
#------------------------------------------
#------------------------------------------
#------------------------------------------

'''
Karborde aslie class ha --> vaghty shoma mikhahi
chizi besazi

chiz (shey)


online shop darid --> shop darid -->
ketab mifrosham, ......

Product daram -> 


'''

#product1 = product(name , code , price, quantity)

class product:
    def __init__(self,name,code,price,quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity= quantity
        
    def show_price(self):
        print('mahsole shoma hast',self.price)
        
    def is_available(self):
        if self.quantity>0:
            return True
        else:
            return False
    
    #p1.sell(2)
    def sell(self,amount):
        if self.quantity<amount:
            raise ValueError('Mojodie mahsol kafi nsit')
            
        self.quantity = self.quantity - amount
        
    def recharge(self,amount):
        self.quantity = self.quantity + amount
        
        
        
        
        
    

p1  = product('book1','b10',1000,10)


p1.code #Out[102]: 'b10'

p1.show_price()
#mahsole shoma hast 1000

p1.is_available() #Out[107]: True



p1.is_available() #Out[110]: True

p1.sell(9)

p1.is_available() #Out[112]: True

p1.sell(1)

p1.is_available() #Out[114]: False

p1.recharge(5)

p1.is_available() #Out[116]: True

p2  = product('book2','b10',1000,10)



#migam agha man yek physical product (mahsoel phiziki)
#yek mahsol drm bename digital product --> nlinan

#p1 = physicalproduct=(book2,b10,1000,10,'shobe1')
#mohasebe gheyat -->mohasebe shobe o addrese moshtari




class physical_product:
    def __init__(self,name,code,price,quantity,address):
        self.name = name
        self.code = code
        self.price = price
        self.quantity= quantity
        self.address = address
        
    def show_price(self):
        print('mahsole shoma hast',self.price)
        
    def is_available(self):
        if self.quantity>0:
            return True
        else:
            return False
    
    #p1.sell(2)
    def sell(self,amount):
        if self.quantity<amount:
            raise ValueError('Mojodie mahsol kafi nsit')
            
        self.quantity = self.quantity - amount
        
    def recharge(self,amount):
        self.quantity = self.quantity + amount
        
    def calculate_distance(self,address):
        #hesabe
        #return 
        pass
    
    
    




#p2 = digitalproduct = (book3,b10,100,10,link_download)
#ersale link bashe --> tabeye

#az classse Product estefade konmbraye har jofte ina?

class digital_product:
    def __init__(self,name,code,price,quantity,download_link):
        self.name = name
        self.code = code
        self.price = price
        self.quantity= quantity
        self.download_link = download_link
        
    def show_price(self):
        print('mahsole shoma hast',self.price)
        
    def is_available(self):
        if self.quantity>0:
            return True
        else:
            return False
    
    #p1.sell(2)
    def sell(self,amount):
        if self.quantity<amount:
            raise ValueError('Mojodie mahsol kafi nsit')
            
        self.quantity = self.quantity - amount
        
    def recharge(self,amount):
        self.quantity = self.quantity + amount
        
        
    def get_download_link(self):
        return self.download_link
    
'''
phsyical product va digital product
hamon productan fght ya vorodi jadid mgiiran
ya tavabashon ezafe bar product hast

chra man bayad digitalprodutc ya physcialproduct
dobvare product ro benevisam????

nemitonm hamon producto besazam ono tahir bdm??
bale --> ers bebar az product

physicalproduct, digitalproduct --> ers bebaran az prodict
inheritance --> ers bari


'''


#yek chiz dari

#Product()
#bank_account()

#Paye tarin , base tarin class 

#physicalprodyct


#dollar_bank_account()


#-----classs BASE azash ers mibaran --> pedar, madar

class product:
    def __init__(self,name,code,price,quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity= quantity
        
    def show_price(self):
        print('mahsole shoma hast',self.price)
        
    def is_available(self):
        if self.quantity>0:
            return True
        else:
            return False
    
    #p1.sell(2)
    def sell(self,amount):
        if self.quantity<amount:
            raise ValueError('Mojodie mahsol kafi nsit')
            
        self.quantity = self.quantity - amount
        
    def recharge(self,amount):
        self.quantity = self.quantity + amount
        
        
        
#class PhysicalProduct: yek classe joda
class PhysicalProduct(product):
    def __init__(self,name,code,price,quantity,address):
        super().__init__(name,code,price,quantity)
        self.address = address
        
    def calculate_distance(self,shobe):
        if shobe==1:
            return 1000
        elif shobe==2:
            return 10000
        else:
            return 'Not Number'
        

#pp1 = PhysicalProduct(name,code,price,quantity,address)
        
        
p1 = product('book1','b1',1000,10)
p1.name #Out[120]: 'book1'
p1.show_price() #mahsole shoma hast 1000

p1.address #AttributeError: 'product' object has no attribute 'address'

p1.calculate_distance() #nADARAD



p2 = PhysicalProduct('book2', 'pb1', 4000, 5, 'shobe zaferanie')
p2.name #Out[123]: 'book2'

p2.address #Out[124]: 'shobe zaferanie'

p2.is_available() #Out[126]: True
p2.show_price() #mahsole shoma hast 4000
p2.sell(5)


p2.calculate_distance(1) #Out[134]: 1000


class DigitalProduct(product):
    def __init__(self,name,code,price,quantity,download_link):
        super().__init__(name,code,price,quantity)
        self.download_link = download_link 
    
    def get_download_links(self):
        print('linke downloade shoma :')
        print(self.download_link)
    

p1 = product('book1','b1',1000,5)

print(type(p1)) #<class '__main__.product'>

p1.name #Out[138]: 'book1'

p1.show_price()
p1.is_available()


p2 = PhysicalProduct('book2', 'b2', 20000, 3, 'shobe 2')
print(type(p2)) #<class '__main__.PhysicalProduct'>
p2.name #Out[142]: 'book2'

p2.address #Out[143]: 'shobe 2'
p1.address #AttributeError: 'product' object has no attribute 'address'

#tavabey product? ers bore
p2.show_price() #mahsole shoma hast 20000

p2.calculate_distance(2) #Out[148]: 10000



p3 = DigitalProduct('book3', 'b3', 2400, 5000, 'https://getplutus.solution')
print(type(p3)) #<class '__main__.DigitalProduct'>

p3.name #Out[151]: 'book3'

p3.download_link #Out[152]: 'https://getplutus.solution'

p3.show_price()


p3.calculate_distance()
#AttributeError: 'DigitalProduct' object has no attribute 'calculate_distance'

p3.get_download_links()
'''
linke downloade shoma :
https://getplutus.solution
'''



'''
shabake haye asabi masnoei


NeuralNetwork




Convolutional neural network -> shabake haye asabi
picheshi hastan


ConvolutionalNeuralNetwork(NeuralNetwork)



Recurrentneuralnetwork(NeuralNetwork)

LongShortTermMemory_LSTM(Recurrentneuralnetwork)


'''





#=====================================
#=====================================
#=====================================
#=====================================
#=====================================
#=====================================
#=====================================

'''
Taki anjam bdn --> project amade hast --> dasteshon garm msieh

emaile man ba subject

P_Project_esmetoon email bznid

jome in hafte 8 aban


Yek project-_> real - mini project
shoro mikoni -_> service layer msiazim
3,4 nafar bahm dige team beshan va in prozhe
zamne bsihtri mibr

mentoring ro anajm midm . 

dostani k dakhele class haye online aksareesho bodn
takalif ro ersal krde bshn 






M_Project_esmetton

matne kamel vavazeh --> moarefie kamelkhodeton
afradi ro agar mishansid too dore --> mirtonid team
nemishansam , 
agar (seni , jensi)
dar ch fieldi kolan alaghe mand hastid 

deadline --> fardashab --> doshanbe 12 shab



ai.course22.alipilehvar@gmail.com

'''












