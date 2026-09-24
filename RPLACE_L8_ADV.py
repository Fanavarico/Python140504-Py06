
"""
In The name of GOD

Created on Thu Sep 24 14:07:16 2026

@author: Ali Pilehvar Meibody


Panjshanbe 2 mehr mah
"""



'''
Tabe --. Function ---> BOX


vorodi 1,... -----> BOX ---> Khoroji1,khoroji2 
begirim



be che dard mikhore? --> vaghty ikhahid yek app besazid
masalan apply_discount --> emale takhfif
mohasebeye mojodie sabad -->

in khodesh 7,8 khat code --> ino bayad 15 bar too kol app benevisid

bejaye inke hey ino benevisid --> mitoni oon chandin khat roi besorate yek capsule --> BOX
yekbar benevisid yek esm behesh bedid --> apply_discount() 

hardafe lazem dashtid bejaye neveshtan --> esmeshoo seda bznid (call)


Hadaf haye motefaveti baraye tabe vojod dare

- efficiency -> bazdehie
- dedup --> tekrar nakonim hey
- madular , micro services --> hame chio khob
    calcualtion.py --> tamame tavabe calculation inja bashe 
    accounts.py --> tavabe marbot -> innja bashe
    main.py --> appemon --> inja hamro hey seda miznim
    
    
    khanaei behtr mishe
    baes mishe microservcioe --> harjaei khast
    scalable -> harjaei khsti feature ezafe konid, tose e bedi -> koja 10000 donbalesh bgrdi
    debugging --> bejaye inke 7 ta karo tooye 100 khat anjam bdi --> 7 khat
    seda zdn 7 tabe -> shikonid, error migiri majbor nisi beri 00 khato bkhoni
    mifhmi erroret --> too tabe 2vomet --> debugging
    




tabe sakhtari

do halate -> 1-defintion (besazish -> yekbar ) python mifhme felan esm --> felan tabas (ejra nmishe)result n
            step2 - call -> seda zadan -> har tedadi ke bekhahi, harj aniazesh dari
            
            


sakhtar (structure)


def name(vorodo1,v2,v3,):
    logic 
    #1kht
    #100000 khat bashe
    
    
    
    
#tab (4 space) -->yani ta madami k darinja code bzni --> badaneye tabast (body) otealegh b tabe hast
biay biron dige jozve tab enis 




nokte aval --> esm gozarie tabe -> hamon ghavanini hast ke esm gozari variabl dare
nmitoni ba adad shoro koni 2open  nemishe
nmitoni sm haye reserv shdoe estefade (print , open ,...)
nemitoni az charactri joz _ estefade okoni, $@ space 
case sensetive --> apply ba Apply motefavete

do harf dare --> apply discount --> esm bezari
def apply discount()

charactere space estefade mikone --> error mide


bish az yek kalame ha
apply_discount()
ApplyDiscount()
Apply_Discount()


esme reserv dre , open , print
Print()
Open()
print2()
print_()
my_print()
customized_print()
special_Print()
internal_Print()


na tanha esme tabe , balke esme vorodi ha ham hmintor
'''

#eshtebah
#def open(list,tuple,2data,data@,my data):
    
#dorost  
#def Open(my_list,my_tuple,data2,data_atsan,my_data):



#======================================================
#======================================================
#======================================================
#======================================================
#======================================================
#======================================================
#======================================================
#======================================================

#------ Date bandi tavabe bar asase vorodi khoroji ----

#======================================================
#======================================================
#======================================================
#======================================================
#======================================================
#======================================================
#======================================================
#======================================================

'''
Tabe --> BOx

vorodi1,vorodi2,.. -> BOX --> khroji1 , khrooji2



baraye tabe --> aya elzami hast ke ma vorodi ya khoroji behsh bdim?

aya lazeme yek tabe , vorodishe? ya khroojishe? ya logiceshe?
ya vorodio logice, ya khorojio logice?


def name(v):
    l
    kh
    
v? l? kh? dotashon , setashon




ma be chahar daste taghsim mikonim


1- vorodi dare , khoroji nadare
2- vorodi dare , khoroji ham dare
3- vorodi nadare,  khoroji dare
4- na vorodi dare , na khoorji dare



Vorodi  |  khoroji
yes          no
yes        yes
no          yes
no         no     



tabe be vorodiu vca khoroji bastegi ndre, logice mohem




terminology --> be vorodi haye tabe migan parameter
vaghty seda mzine --> argument

jam(numb1=10,numb2=20) --> keyword argument
jam(10,20) --> positional argument



vaghty ejra mikonm def jam --> chizi anjam nmishe --> tabeye jam va structuresh 
tooye RAM --> skahte mishe -> python mishnase
harvght bnvisam jam() dg nmige jam is not defined


vaghty mziani jam --> mire negah mikoe, mibine tabe chanta parameter dre
va miad mige be hamon andaze shoma bay argument bedi

'''



def jam(numb1,numb2):
    result = numb1 + numb2
    print(result)
    
    
#tafrigh()
jam(10) #ghbl az ejra --> mire parmatero mibine 2 tas , argument yekie
#TypeError: jam() missing 1 required positional argument: 'numb2'


jam(10,20,30)
#TypeError: jam() takes 2 positional arguments but 3 were given


#hameye inaro migm ?-->oon zir too python chi dare mishe

#ya keywordi ya positioali-->mohem nis
jam(numb1=10,numb2=20)
jam(10,20)


#numb1 ye zarf msiaze = vorodi = 10 
#numb2 ye zarfr -. vorodi 20 

#numb1=10 , numb2=20 
#va body ro ejra mikone --> ye fiel run 
'''
result = numb1 + numb2
print(result)


'''

#in mige ye zarf besaz bename resykt = 10 + 20 = 30
#print(rresult) -->print(30  ) --> 30


'''
jam(10,20)
30

'''



#1----- Vorodi dare , khoroji nadare

def jam(numb1,numb2):
    result = numb1 + numb2
    print(result)
    
    
jam(10,20)


#print --> yek dastoore --> print kon felan chizo tooye console --> nemigan khoroji
#khoroji --> betonam joloh yek zarf bzrm (variable) moteghayer

zarf = jam(10,20)

print(zarf) #None


#hameye tavabe ta zamani ke ma msohakahs nakonim (return) --> by default -- None pas midan
#agr joloye tabe ei zarf  gzoshtim va none pas dad ->in tabe khorojie man dar nmide
#khoroji mana ar nmdie--> khoroji ndre

#print khoroji motefavete
#Khoroji yani btoni toye yek zarf zzakhirash koni


#2----- Vorodi dare , khoroji dare

def jam(numb1,numb2):
    result = numb1 + numb2
    #print(result)
    return result


zarf = jam(10,20)

print(zarf) #30


#vorodi dare, khoroji hm dare XXXXX STANDARD XXXXXXX


#print asan chize mohemi nis
def jam(numb1,numb2):
    result = numb1 + numb2
    print(result)
    return result


zarf = jam(10,20)

print(zarf) #30


#noketey khobi

def jam(numb1,numb2):
    result = numb1 + numb2
    return result
    print(result)



zarf = jam(10,20)

#harchizi bad az return inja bashe -> ejrsa nmishe 
#vaghty tabe be return berese , vaghty migim barmigde , tabe ro left mide



def jam(numb):
    for i in range(0,numb):
        print(i)
        return i 
    
    
zarf = jam(10)






#-----------------------------------
#3- vorodi nadare, khoroji dare

def pi():
    return 3.14


zarf = pi()
print(zarf) #3.14





pi = 3.14
zarf = pi



#-----------------------------------
#4- na vorodi dare na khoroji


def welcome():
    print('salam khedmate dostane aziz')


welcome() #dastoor , vorodi nmigire, khoroji mdie (zarf)


#maalan --> save tooye db , chizaro 100 khat print mikone
#tooye db -> 
'''
def send_message_to_all_telgram_subscribers():
    #vcasl msihe b db
    #hame users haro migire -->users()
    #user_ids()
    for user in users:
        send_telegram()
        
    print('finish')



timer(send_message_to_all_telgram_subscribers() , 3:14)
'''





#------Vorodi darim , input chi mishe? input chie?



#tabe vorodi dare , 


def jam(numb1,numb2):
    result = numb1 + numb2
    return result





jam(10,20)





a=float(input('adade 1to bede:'))
b=float(input('adade 2to bede:'))

jam(a,b)



#tooo halate aval -->khdoemon mostaghim be tabe 2 ta viorodi dadim
#too halate dovom-> ma aval az user 2 adad grftim badesh 2 ta vorodi dadim

#yani barye tabe mohem nis in vorodi ha khodetmidi, input miad (frontend miad (website, safe web mid-->backend))

#tabe dota vorodi migire



#---tavabe ei k vorodi ndre --> mitonid oinput dakhele tabe bezarid -> masaleo tamrin (vaghei)

#yek tabe besaz  , az user adade 1 va 2 ro begire , jam kon, jameshono pas bede (khoroji bede)
#az user begire -> tabamon vorodi ndre

#yek tabe bessaz 2 ta vorodi bgrie jam kone pas bede . 2 vorodi --> box --> khoroji

#to in bala ye tab ebesaz az user 2 vorodi begire   no vord --> box (2 vorodi bgire az user) -> khoroji

'''
def get_values(numb1,numb2):
    result = numb1 + numb2
    return result
'''

def get_values():
    numb1 = float(input('adade aval ro bego:')) 
    numb2 = float(input('adade dovom ro bego:'))
    result = numb1 + numb2
    return result




get_values()  #vorodi e nemigire az input migir, na khdoet mdii

#run mishe --> kole body run mishe
#body --> aval input dastore inptu run mishe -> console --> 


zarf = get_values() 

print(zarf) #30.0



#====================================================
#====================================================
#====================================================
#              LOCAL VS GLOBAL      
#====================================================
#====================================================
#====================================================

def jam(numb1,numb2):
    result = numb1 + numb2
    return result



zarf = jam(numb1=10,numb2=20)

print(zarf) #30.0
#print(numb1) --> chi mide
#print(result) --> 

#print(numb1) #NameError: name 'numb1' is not defined
#print(numb2) #NameError: name 'numb2' is not defined
#print(result) #NameError: name 'result' is not defined


#yek bahsi hast bename Local variables -> moteghayer haye mahali



def jam(numb1,numb2):
    result = numb1 + numb2
    return result



zarf = jam(numb1=10,numb2=20)

#aval se khato ejra krdm --> tabe ei bename JAM -- toye RAM sakhte shdoe
#zarf = --> yani yek zarf besaz mosaviee ...

#jam(  --> mibine bale in tabe ro mishanse, age nmsihankht --> jam is not defined
#mibine dota parametr numb1,numb2 --> barmigrde mibine dota argument (2 vorodi) doroste
#age bishtr bod --> 2 requrie , 3 given   || 1 done -> miss 1 done --> daghigh doros
#numb1 = 10 , numb2 = 20 ---> har moteghayer

#********** --> har moteghayeri ke dakhele tabe sakhte beshe -> locale
#yani miad zarf haye movaghat misaze --> zarfe movaghat numb1=10 , zarfe movagahat numb2=20
#zarf movaghat result = zarfe movagahat numb1 + zarfe movaghat numb2 = 10 + 20 =30

#ghable retunr -> se ta zarfe movaghat 

#return result --> return bede zarfe movaghate result --> return bede megdhar dakhele zarfe movaghate resulto
#return bede 30 ro koa? jaei k seda khorde
#zarf = --> yani yek zarf besaz mosaviee ...

#zarf = return dakhele resylt = 30 

#**yadet nre tooye python--> ye tefagh -> tamame zarf haye movaghat ro mishkone -> pak mikone
#Numb1numb2,result vopjode khareji ndre !!!!!!!!
#inaro movaghatt sakht kareto anjam bde tamam 

#vorodi --> box --> khoroji 
#kari b box ndri k koli varibale negah dare too RAM .oona hastan mese vasile karto mikonen
#to khoroji mohem --> khroojito to zarf mirizi



numb1=100

def jam(numb1,numb2):
    result = numb1 + numb2
    return result



zarf = jam(numb1=10,numb2=20)

print(zarf) #30
print(numb2) #NameError: name 'numb2' is not defined
print(result) #NameError: name 'result' is not defined
print(numb1) #100


#tmam zarf hga movaghate -->
#age oon zarf az ghabl vojod nadasht --> misaze movaghat ->kresho mikone -> pakesh mikone --> not define
#age oon zarf az ghabl vojod dasht (numb1=100) --> mojadsad khalish mikoen numb1=vorodi =10 -->karesho mikone

#hala k return 30 --> miad zardfaro beshkone
#numb2 , result --> vojode khareji ndshtn -> pak mikone
#numb1 -> vojod dashte , beja inke pakesh kone , baresh migrdone b chizi k bod --> 100


#yek zarfo bejaye inke movaghat dahste bashim , hamishegi bashe
#vahghy ke sakht (ch vojod ndsht, ya ye adade dige bod)
#vaghtytabe seda bokhore, har adadi onaj bashe ,dige in bemone 

#local --> global

def jam(numb1,numb2):
    global numb1
    result = numb1 + numb2
    return result

#zarfe numb1 ro dg movaghat nasaz -> bad az retun , harchi k inja hast -- meyare





#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------

def jam(numb1,numb2):
    result = numb1 + numb2
    return result



jam(10,20) #Out[58]: 30

#chon bayad zarf mizashti nazashri --> endakhte tooye consoel
#zarf bzari -> 30 ro nmibini --> 30 mire too zarfet





def jam(numb1,numb2):
    result = numb1 + numb2
    print(result)

jam(10,20) #30
#30 print bode 
#zarf bzare --> zarf = None
zarf = jam(10,20) #30 ro mibini
print(zarf) #None








#-------------------------------------------------------

def jam(numb1,numb2):
    result = numb1 + numb2
    return result


zarf = jam(10,20) #positional arguments
zarf = jam(numb1=10,numb2=20)  #keyword arguments



zarf = jam(10) #error mide --> numb2 
#TypeError: jam() missing 1 required positional argument: 'numb2'
#aval ngah mikone tabe chanta vorodi dre
#error mide

#error nmdiad ???
#numb1 + numb2 kone 10 + chi kone???



#migan bai yekar kon-->default bzar
#yani bgoo-->felan parametre man --> age dadiu --> ke ooni k to midi ok=laviat (overwrite)
#age nadadi--> natanah error nmidm behet , balke default felan adado

def jam(numb1,numb2=100):
    result = numb1 + numb2
    return result



zarf = jam(10,20)

#numb1=10 , numb2=20 (100 mohem nis) oni k to vorodi midi --> overwrite mikoen
#result = 10 + 20 --> zarf = 30




zarf = jam(10)

#etefaghe 1 --> error nmudi error nmide
#etefaghe 2 --> rsult = 10 + numb2 ??? (100) = 10 + 100 = 110



#hamishe default ro bayad tahe paramter
'''
def jam(numb1=100,numb2):
    result = numb1 + numb2
    return result
'''


def jam(numb2,numb1=0):
    pass


#too tarife tabe --> aval non default parmater badesh default parameters



def jam(numb1,numb2):
    result = numb1 + numb2
    return result



zarf = jam(10,20) #positional argument
zarf = jam(numb1 = 10,numb2 = 20) #keyword argument

#joftesho besorate defaulrt --> tabe ha ejaze midan


#shoma mitonid yekar konid ke ejaze nadan

def jam(*,numb1,numb2):
    result = numb1 + numb2
    return result


#3 vorodi nmishe -> hamon do vodi

jam(10,20) #TypeError: jam() takes 0 positional arguments but 2 were given
jam(numb1=10,numb2=20) #Out[69]: 30
    
#baz az *,  harchi omd bayad keywordi vared she



#------------------------------


def jam(numb1,numb2,/):
    result = numb1 + numb2
    return result


#3 vorodi --> 2 vorodi migire

jam(10,20) #Out[70]: 30
jam(numb1=10,numb2=20) #TypeError: jam() got some positional-only arguments passed as keyword arguments: 'numb1, numb2'=
 

#har parametri ke pohte ,/ biad fght positionalmitone vared she (adadi)




#ya mitonam tarkibkonm???


def alaki(a,b,/,*,c,d):
    pass



#yani a, b ghabl az / --> mitonan positionali --> 10 , 20 nmitoni bnvisi a= b= 
#bad az *, --> c , d -- fght bayad keywordesho c= , d=    , 

alaki(10,20,30,40) #error
alaki(a=10,b=20,c=30,d=40) #error
alaki(10,20,c=30,d=40)

alaki(10,20,d=40,c=30) #yani keywordi haro mitoni taghir bdi chon dari keyword


def alaki(a,b,/,*,c,d,e='default'):
    pass






#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------
#----------------------------------------------------
#mutliple inputs (chandin input)
#chandin khroji darim?

def jam_tafrigh(numb1,numb2):
    jam = numb1 + numb2
    tafrigh = numb1 - numb2
    return jam ,tafrigh


#jam_tafrigh(numb1=10,numb2=20)
zarf = jam_tafrigh(10,20)
 
print(zarf) #(30, -10)
print(type(zarf)) #<class 'tuple'>

#agar tabe at chandin khroji dashte bashe -> mohem nis
#hamasho mziare tooye yek tuple behet pas mide

#(30,-10)
zarf[0] #Out[77]: 30
zarf[1] #Out[78]: -10



#unpacking

zarf1 , zarf2 = jam_tafrigh(10,20)

#agr joloye tupel be ezaye elementash zarf bzari -> unpack mishe





#----------------------------------------------------
#tavabeton ro khana va tamiz benevisid-------------

#chera? --> 1-vaghty ziba benevsiid doros benevsiid -> bad az sad salam bargrdid beebinid --> mifhmiod chsihode
#debugging, rafe khata , moshkel yabi , tose e scale ,..-_> sade tare

#reviewer --> company, resumatono projato , project --> ghabele fhm tre mifhme chikar krdi 
#group --> 10 nfr kar koni


#agent -> agent ham donyaye emrozi vaghty code ro midi behesh kari kone, debugg 




#1--> esm haye mani dar baraye tabe va moteghayer ha bzrid
#a , b , c my ,... naza
#def jm(a,b):

def addition(number1,number2):
    addition_result = number1 + number2
    return addition_result
    
#for i in ....


#for user in users:



#2---> type hint bzar --> yni
#Hint bede-->komak kon ke type malom she

def addition(number1:int,number2:int)-> int:
    addition_result = number1 + number2
    return addition_result

addition() #inja hint mikone ke ch vorodi haei bede

addition(number1=10.1 , number2=20.344334) #Out[82]: 30.444333999999998

#errro nmide --> hint mide 
#mitoni ha mhint bzri ham nzri

def addition(number1:int,number2:int)-> int:
    if type(number1)!=int or type(number2)!=int:
        print('ghalat ast ')
        return None
    addition_result = number1 + number2
    return addition_result


zarf = addition(number1=10.1 , number2=20.344334) #ghalat ast 
print(zarf) #None



def addition(number1:int,number2:int)-> int:
    if isinstance(number1,int) and isinstance(number1,int):
        addition_result = number1 + number2
        return addition_result
    else:   
        print('ghalat ast ')
        return None



#---docstring darim
#yek chize baze


def addition(number1:int,number2:int)-> int:
    '''
    tozih --> addition : ch etabei .....
    number1--> int 
        tozih 
    number2--> int
        tozi
        
    khroji -> int
        tozih bedi
        
    error hae begire
    chikar kone
     default ga
    
    '''
    
    addition_result = number1 + number2
    return addition_result


addition()


help(addition)

'''
Help on function addition in module __main__:

addition(number1: int, number2: int) -> int
    tozih --> addition : ch etabei .....
    number1--> int 
        tozih 
    number2--> int
        tozi
    
    khroji -> int
        tozih bedi
    
    error hae begire
    chikar kone
     default ga
     
'''



def addition(numb1,numb2):
    '''
    

    Parameters
    ----------
    numb1 : int
        cffd.
    numb2 : int
        DESCRIfdfdfdfddsPTION.

    Returns
    -------
    None.

    '''
    pass





#tabe mitone list begire??



def my_sum(my_list):
    total=0
    for i in my_list:
        total = total + i 
        
    return total


#list ---> box --> adad

#yek list, tupel,-->yek vorodi

my_sum([10,20,30,40]) #Out[93]: 100




def information_processor(a:dict):
    b = a['sen'] + 10 
    return b



#dictionary --> BOX --> adad

information_processor({'esm':'ali','sen':30}) #Out[94]: 40



#yek vorodi list migir, yek vorodi dictionary


#mitoni -- chandin parametr begiri --> namahdood-->ama behet list pas bede


def my_sum(my_list):
    total=0
    for i in my_list:
        total = total + i 
        
    return total


my_list=[10,20,30,40,50]
my_sum(my_list) #Out[95]: 150


#my_sum(10,20,30,40,50,60,70,80,90,100)


#def my_sum(a1,a2,a3,a4,..........)

#*args


def my_sum(*a):
    print(type(a))
    
    for i in a :
        print(i)
    
    
my_sum(10,20,30,40,50,60,70) #<class 'tuple'>


#agr kenare yekparametr behsh chasbide

#namahdoodd positional argument mitoni bedi-->hamro migire ->mirize to yek tupel bename a

#*har zarfi

def my_sum(*a):
    total = 0 
    for i in a :
        total = total + i
        
    return total


my_sum(10,20) #Out[99]: 30
my_sum(10,20,30,40,50,60,70,80) #Out[100]: 360


#chera haro list nakonm besorate yek vorodi begiram?--> bastebe karbordet





#-------
#**kwrgs


def my_sum(**a):
    print(type(a))




my_sum(a=10,b=20,c=30) #<class 'dict'>



def my_sum(**a):
    print(a)

my_sum(a=10,b=20,c=30)

#{'a': 10, 'b': 20, 'c': 30}


#vroodi keyword argument



def my_sum(**information):
    
    new_age = information['sen'] +20
    
    if new_age >40:
        return True
    else:
        return False
    
    
    
my_sum(esm = 'ali' , sen = 40 , phone = '0919...') #Out[103]: True



#*args --> chandin vorodi namahdood--> tuple
#**kwrgs--> chandn vorodi keywordi --> dictionry


#----------------------
#----------------------
#----------------------

#tyabe   numb1,numb2,operation --> box --> result



def calculator(numb1,numb2,operation):
    if operation=='jam':
        result = numb1 + numb2
        return result
    elif operation=='tafrigh':
        result = numb1 - numb2
        return result
    elif operation=='taghsim':
        result = numb1 / numb2
        return result
    elif operation=='zarb':
        result = numb1 * numb2
        return result
    else:
        print('Bayad az yeki az gozine haye (jam,tafrigh,taghsim,zarb) estefade konid')
        return None #Mitoni inm nnvisi ,by default None pas mdie
    
    
    
    
zarf = calculator(numb1=10,numb2=20,operation='jam')
    
    
print(zarf) #30



zarf = calculator(numb1=10,numb2=20,operation='tavan')

#Bayad az yeki az gozine haye (jam,tafrigh,taghsim,zarb) estefade konid
#zarfo --> None

#gahan mikhay --> doros error bede be trf asan jolosho bgire, pas nade


#--> raise estefade mikoni



def calculator(numb1,numb2,operation):
    if operation=='jam':
        result = numb1 + numb2
        return result
    elif operation=='tafrigh':
        result = numb1 - numb2
        return result
    elif operation=='taghsim':
        result = numb1 / numb2
        return result
    elif operation=='zarb':
        result = numb1 * numb2
        return result
    else:
        #print('Bayad az yeki az gozine haye (jam,tafrigh,taghsim,zarb) estefade konid')
        #return None #Mitoni inm nnvisi ,by default None pas mdie
        raise ValueError('Bayad az yeki az gozine haye (jam,tafrigh,taghsim,zarb) estefade konid')
        
      
        
zarf = calculator(numb1=10,numb2=20,operation='tavan')

#ValueError: Bayad az yeki az gozine haye (jam,tafrigh,taghsim,zarb) estefade konid




#-------------def in def
def jam(numb1,numb2):
    result = numb1 + numb2
    return result

jam(10,20) #Out[153]: 30

#koja return==?onjaei k seda shode


def tafrigh(numb1,numb2):
    result = numb1 - numb2
    return result


zarf = tafrigh(20,10)





#dakhele calculator


def calculator(numb1,numb2,operation):
    if operation=='jam':
        result = jam(numb1,numb2)
        return result
        
    elif operation=='tafrigh':
        result = numb1 - numb2
        return result
    elif operation=='taghsim':
        result = numb1 / numb2
        return result
    elif operation=='zarb':
        result = numb1 * numb2
        return result
    else:
        #print('Bayad az yeki az gozine haye (jam,tafrigh,taghsim,zarb) estefade konid')
        #return None #Mitoni inm nnvisi ,by default None pas mdie
        raise ValueError('Bayad az yeki az gozine haye (jam,tafrigh,taghsim,zarb) estefade konid')
    
    
calculator(numb1=10,numb2=20,operation='jam')
        




















SyntaxError #* , .
TypeError #type eshtebahi vorodi dare, anjam shode
ValueError #adade ehstebahi  , manfi nmiotonese 
FileExistsError()
FileNotFoundError()
ZeroDivisionError() #/0 -->

#list --> https://docs.python.org/3/builtins/exceptions.html




def withdraw(balance,amount):
    balance = balance - amount
    return balance


withdraw(100,10) #Out[109]: 90







def withdraw(balance,amount):
    if balance<0:
        raise ValueError('balance nemitone manfi bashe')
        
    if balance < amount :
        raise ValueError('mojodi kafi nemibashad')
        
    #assert balance<amount,'mojodi kafi nemibashad'   
        
    balance = balance - amount
    
    
    assert balance<0 #proirgamming, usereto ina ehstebah nkrdn ama momkene to logical yejaye coddet eshtebah bashe
    #programmer , entezar dare baalnce >0

    
    #baalnce<0 -> true shdo --> abalnce <0 --->
    
    return balance



withdraw(100,10) #Out[111]: 90

withdraw(-10,10)  #ValueError: balance nemitone manfi bashe

withdraw(100,500) #ValueError: mojodi kafi nemibashad




#assert balance<0 



#if balance<0:
#    raise AssertionError('')

def withdraw(balance,amount):
    if balance<0:
        raise ValueError('balance nemitone manfi bashe')
        
    if balance < amount :
        raise ValueError('mojodi kafi nemibashad')
        
    #assert balance<amount,'mojodi kafi nemibashad'   
        
    balance = balance - amount
    
    return balance




#main.py 
#ejra msieh--> khod pardaz
while True:
    db  = 100000
    balance = db
    
    amount= float(input('chegahdr mikahhid bardasht konid:'))
    
    try:
        mojodi_baghimonde = withdraw(balance,amount)
    except ValueError:
        print('ba khata movaje shod')
    
    
#yani migi man asan raise nmzirm
#hamishe khata daste to nsi --> to baya dmanage koni
  
    
    
#-----------------------------------------------
#bdone try 

while True:

    a= float(input('yek adad bede:'))
    
    
    b = 100/a
    
    
    print(b)
        







while True:
    try:
        a= float(input('yek adad bede:'))
        
        
        b = 100/a
        
        
        print(b)
        
    except ValueError:
        print('shoma adad vared nakardid ')
    except ZeroDivisionError:
        print('shoma nmeitavanid 0 ra vared konid')
    except Exception as e: #unexcpected error -> psihbini nakrdi
        print('khataye pish bini nashode')
        #e --> databas, telegram notif, error hanamayeshesh b khodet (admin)
        
        
        
        
        


#error --> erro rune barname ro mtoevaghef mikone 

#try kon ta zamani k errro ndsht k besmlea
#age dasht, error nde, moefaveghef nkon--> balke inkaro estesnaan boko -- exception

    
    



#-----------------------------------------
#-----------------------------------------
#-----------------------------------------
#try ro ba except mizanan
#aval exception haei k mishnasi va hads mzini
#exception haei k nmidonui (unexcpected)






while True:
    try:
        a= float(input('yek adad bede:'))
        
        
        b = 100/a
        
        print(b)
        
    except ValueError:
        print('shoma adad vared nakardid ')
    except ZeroDivisionError:
        print('shoma nmeitavanid 0 ra vared konid')
    except Exception as e: #unexcpected error -> psihbini nakrdi
        print('khataye pish bini nashode')
        #e --> databas, telegram notif, error hanamayeshesh b khodet (admin)
    
    #Mitoni beznai mitoni nazani
    else:
        #gar error nakhord in ejra she
        print('moafagh bood')
        








try:
    a= float(input('yek adad bede:'))
    
    
    b = 100/a
    
    print(b)
    
except ValueError:
    print('shoma adad vared nakardid ')
except ZeroDivisionError:
    print('shoma nmeitavanid 0 ra vared konid')
except Exception as e: #unexcpected error -> psihbini nakrdi
    print('khataye pish bini nashode')
    #e --> databas, telegram notif, error hanamayeshesh b khodet (admin)

#Mitoni beznai mitoni nazani
else:
    #gar error nakhord in ejra she
    print('moafagh bood')

finally:
    #ch khata khod ch nakhor in beshe
    print('payane barname')
    #cleanup()
    
    
    
    
#-----------------------------------------
#-----------------------------------------

#iter()
#next()
#yield


a=[10,20,30]

for i in a:
    print(i)

#a --> iterables
#iteration mikoni ba for

#list,tupke,set , diction --> dakhele iter


b= iter(a) #iterator --> genrator

print(type(b)) #<class 'list_iterator'>

next(b) #Out[138]: 10

next(b) #Out[139]: 20

next(b) #Out[140]: 30
next(b) #StopIteration







for i in a:
    print(i)


#-----------------------------
i=0
while True:
    if i==len(a):
        break
    next(b)
    i=i+1
    

#_---

def my_list_something(my_list):
    for i in my_list:
        return i
    
    
my_list_something([10,20,30,40]) #Out[141]: 10

#return resid --> edmey code ro ejra nmidkon


my_list_something([10,20,30,40])  #Out[141]: 10





def my_list_something(my_list):
    for i in my_list:
        yield i



g = my_list_something([10,20,30,40])

print(type(g)) #<class 'generator'>


next(g) #Out[145]: 10

next(g) #Out[146]: 20

zarf = next(g)
print(zarf) #30



#yek million adad toolid konid


def generate_1million():
    my_list=[]
    for i in range(0,1000000):
        my_list.append(i)
        
    return my_list




def generate_1million():
    my_list=[]
    for i in range(0,1000000):
        yield i



gen = generate_1million()


next(gen) #Out[150]: 0
 
next(gen) #Out[151]: 1

#1 miliar, 1 billlion








