'''
In The Name of GOD

Ali Pilehvar Meibody


L2_Adv.py

Jalase Dovom, class advanced python


'''





'''

Review----------------------

Python ro az bala migam chie


Human (En) <-------(interface)-----> Machine (0,1 Binary)



dastoor bedam ensan b machine --> programming (barname nevisi)

interface --> programming language . En -> Zabon . zabon-->translate --> 00101001010 -> ejra


Python --> interface --> Programming language (zaban) faransavi, italiae,....Farsi


Computer --> do ta lazeme 1-Ipython kernel 2-IDE (spyder ,...)/Editor(vs code)

Anaconda --> laptobet mohit (environment) haye mtoefavet besazi , baraye har env
yek python, baraye har env yek ide (spyder) --> yesal dg porozhe


python + spyder (raveshe1)
anaconda-->mohit --> spyder (raveshe2) --> herfe ei , project hast



vaghty shoma yek file .py misazi --> yani mikhay toosh pythonic benvisid


run mizani --> Spyder (IDE/Editor) kole oon file .py --> python kernel () az
bala be paein, az chap be rast mikhone

# ''  ""  --> comment mibine o ignore mikone 

harchizi k minevisi ro bayad befahme, barash tarif shode bashe


faransavi balade, app i minevsiam --> oon ag man italiae, englisi nmifhme error mide

python ag gheyre pythonic benevisi -> error



----------defined --------------
1-Python Built in functions (tavabeye dakhelie python) --> narenji 
print()    --> harchi toosh bexari namayesh mide
input() ---L> chizi migire 
len() --> andaze mide
type() ---> typesho behet mide



yek amalkardi, kari anjam mide

https://docs.python.org/3/library/functions.html





2- Keywords --> logice va mnategho avaz koni --> print('salam') ejra bshe ejra --> if else 
chanbar ejra --> for ,.--->banafsh


----------undefined --------------
rangesho sefid mikone nemishansam

3- Variables -- moteghayer bashan
yekj zarf bashan chizi toosh berizi

a=10
b=40

yek shoroti dare baraye esm gzoari , characteri _ , case sensetive


3.1. Numbers (int,float, complex) --> () ** * / + - , == != > < >= <=
3.2. Bool (True,False) --> 
3.3. String --> yek character, yek kalame, yek jomle --> qutation --> str shenakhte mishod



'''


print('salam')


#---------Strings------------

a='salam'


#dastresi --> index
#az 0 shoro mishe

#s a l a m
#0 1 2 3 4 

a[0] #Out[1]: 's'


#yek manteghi hast --> range -->oon tahi ro exclude mikone

#0 1 2 
a[0:3]   # 'sal'



#for --> range(0,101) #0  


a[0]='b'

'''
runfile('/Users/apm/Desktop/L2_adv.py', wdir='/Users/apm/Desktop')
salam
Traceback (most recent call last):

  File ~/anaconda3/envs/DL/lib/python3.10/site-packages/spyder_kernels/py3compat.py:356 in compat_exec
    exec(code, globals, locals)

  File ~/Desktop/L2_adv.py:134
    a[0]='b'

TypeError: 'str' object does not support item assignment


Yek fiel ersal mikonam (yadavari)

'''


#----str functions--------
#tavabe ei k roye str ha hastan

#lower()
#upper()


a='name'

lower(a)


#NameError: name 'lower' is not defined

#tavabe dakhelie python-->shenakshte shode --> naranji 

#tavabeye dakhelie str --> str function --> tabe haei hastan
#k fght baraye str ha hastan

#zarf.function()

a.upper() #Out[7]: 'NAME'

print(a) #name

#tavabeye str --> emal nemikonan, khoroji midahand

#1 -> oon variable taghir nmikone , zarfe jadid mikhay 



b = a.upper()


print(a) #name

print(b) #NAME



#----------
'''

1- Taghirati hastan 

.upper()
.lower()
.title() har kalame ro horofe avalesho bozorg mikone
.capitalize()  horofe aval bozorg mikone
.replace()  #horofi ro taghir mide




2- Adad pas mide
.count()
.find()


3-True False pas midan

is daran

isdigit()

isalnum()





'''


name = 'ali'


#lower(name)  --> tavabe ye dakheli , print() ,.....

#zarf.function() --> emal nmishe, khoroji mide
#zarf_jadid = zarf.function()   


new_name = name.lower()

print(new_name) #ali



new_name = name.upper()

print(new_name) #ALI



new_name = name.capitalize()

print(new_name) #Ali


name2= 'in the name of god'

name3 = name2.title()
print(name3) #In The Name Of God



name = 'ali'
new_name = name.replace('a','b')

print(name) #ali

print(new_name) #bli



#lower() --> save koni information moshtariato hamaro bayad koochik koni
#lower() --> database --> normalziation



#namayesh bedi esmesho , ATM , --> title() capitalize()






#vorodit az msohtari biad, moshtarit , esmesho space aval tahesh
#bayad space samte chapo raste yek kalame ro hazf koni

name1 = 'ali'
name2 = 'ali '

print(name1==name2) #False


print(len(name1)) #3 --> a  l i
print(len(name2)) #4 --> a l i [space]


#az chap va rast space ro hazf mikone
name3 = name2.strip()
print(len(name3)) #3


#rstrip() az right (rast faghat hazf kon)
#lstrip() az left (az chap fght hazf kon)

#strip() --> az do tarqaf

full_name = ' ali pilehvar meibody '


print(len(full_name)) #22



new_full_name = full_name.strip()

print(new_full_name) #ali pilehvar meibody

print(len(new_full_name)) #20



full_name = ' ali pilehvar meibody '

name10 = full_name.replace('a','b')  #harja a bbine b
print(name10) #bli pilehvbr meibody 


full_name = ' ali pilehvar meibody '

name11 = full_name.replace(' ','')

print(name11) #alipilehvarmeibody



#--------- yek kalame --> kalame pas midad



full_name.count('a') # 2

#broo too full name beshmor chnata  a 

full_name.find('a') #Out[34]: 1

#a ro peyda kon --> avalin a ro k peyda kone indexesho barmigrdon



#------is --> True False

a = 'salam'

a.isdigit() #Out[35]: False

b='3223223'

b.isdigit() #Out[36]: True



a='salam'
a.isupper() #Out[37]: False

b='SALAM'
b.isupper() #Out[38]: True

'''
str fucntions--->
1- tavabe ei hastan k fght baraye str ha hastan , na kol 

2- zarf.function() -->injori estefade mikone

3- ina emal nmishe (zarf taghir) ->khrooji mide --> khrooji ro mirizi to zarfe jadid

4- 3 no tabe darim 1-taghirato pas mide (lower(),upper(),) ,2-adad (find, count) 3-is ->true false


5- Liste kameli az hameye tavabe --> niazi b hefz nist , aslia agar hey estefade (moror )




Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values from a dictionary in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Converts the elements of an iterable into a string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning


'''





#---------------
#1-Python built in fucntion
#2-Keywords
#3-Variables (3.1.numbers 3.2.bool 3.3.Str)

#yek value -->mirikhtim dar yek zarf --> chanta value ro dar yek zarf brizam


#--> Iterable --> yani chzi k mishs toosh iteration
#list  --->  Index (ordered) , Changable, Allow duplicated
#tuple
#set
#dictioanry

#->list 

b = [10,20,30,40,50,60,70]


b = [10 ,10.433 , 'Ali', True , [10,20,30]]



#dastrsii --> string index

#string -- >listi az charactefr ha hast

#0 1 2 3 4 5
b[0] #Out[39]: 10

b[0]=200

print(b) #[200, 10.433, 'Ali', True, [10, 20, 30]]



#list fucntions --> 


#function ahe k fgth baraye list hast

#append()

#append(a)


#zarf.append()



#in tavabe emal mishan , khorohji nemidan

#yani chi? ---> yani zarf.fucntion()  , niazi b zarfe jadid . emal mikone roye zarf

#insert
a = [10,20,30,40]

a.insert(1,100)  #b= XXXX , a

print(a) #[10, 100, 20, 30, 40]


a = [10,20,30,40]

a.insert(4,100)

print(a) #[10, 20, 30, 40, 100]

#sakhtame



#append->harchi ezafe koni b tahet ezafe mikonm
a = [10,20,30,40]

a.append(100)

print(a) #[10, 20, 30, 40, 100]


a.remove(10)
print(a) #[20, 30, 40, 100]


#a.pop --> ham emal mikone ham khorji

#a.remove(khode element) hjazf kone
#pop-->indexo midi va hazf mikone
a = [10,20,30,40]
a.pop(0) #Out[49]: 10

print(a) #[20, 30, 40]

a = [10,20,30,40]
a.pop() #Out[54]: 40
print(a) #[10, 20, 30]



#na tanha hazf mikone balke elemente hazf shode ro ham pas mide va shoma agar niaz dahste bashid
#Mitavanid dar yek zarf berizidesh


#farghe clear ba delet chie?

#clear -->khali koon dakehelsho
a.clear()
print(a) #[]


#-->keyworde --> kole zarfo ba jasho 
del a

print(a) #NameError: name 'a' is not defined


#--------
a = [10,20,30]
b = a 


a[0]=200

print(a) #[200, 20, 30]

print(b) #[200, 20, 30]


'''
b = a --> python miad ta abad in dotaro abrabar gahrar

har taghiri rooye a bedi , rooye b ejra mishe



b = a ?? --> backup begiri , copy bgiri 

b = a


'''

#ag bkhay ba a sync nabashe , har taghiri roye a , b 
a=[10,20,30]
b = a.copy()


a[0]=200

print(a) #[200, 20, 30]

print(b) #[10, 20, 30]



#.sort() --> horof Capital a-z , kochik a-z , number az 
#.reverted()

'''
List fucntions
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

'''



#---Iterabels --------
#List --> [] Ordered (index) ,changable , allow duplicated
#tuple--->() ordered (index) , unchanagable (db) , allow duplicated
#set--->{}  unordered(index nadare) , unchangable ,No duplicated -->majmoe haye riazi
#dictionary --> {key1:value2 , key2:value2} Index value --> Key value --> infomration, etelaati


a=['ali',190, 30,'09191111111']



a[0]



a[1]

'''
list
index value
0      val1
1      val2
2 

list[index] -->dastresi





dictioanry
key     value
key1    value1
key2    value2

dict[key] -->dastresiii




'''



a={'name': 'ali' , 'ghad':180 , 'sen':40 , 'phone':'091911111111'}


a['name'] #Out[62]: 'ali'

a['ghad'] #Out[63]: 180




#----------------------------------
#1-puython built in functions ()+++
#2-Keywords (if,else,elif,for , while)
#3-Variables (numbers(int,float,complex),bool, str([],[index],slicing,str functions),list(list fucntins),tuple,set,dictionary)



#---keywords -->zamani k mikhahim logice barname ro taghirbedim az in keywords ha estefadde mikonim





a=100

print('salam')


#a=10 --> salam
#a=100  #salam

#khate 683 hamishe eye khoda ejra mishe -->logice python
#az bala b paein chap b rast mikhonam


#gahi mikhahid in khat , ye khat (yek section)

#hamishe ejra nashe --> vabastash konid b chizi , b sharti

#mikham ejraye codam ro shartish konm



#print('salam') --.dar soorati k a=10, dar gheyre insorat nashe

#2D -->monitro 
#3D --> mikeshidamesh brion



#poshte khat ya khat haei k mikhahi shartish koni 

#if shart

#shart --> javabesh True False

#== != > >= < <=
#isdigit() is....()


#4 ta space
#1 tab ()balaye caps lock



a=10


if a==10:
    print('salam')




'''
python hamishe

a=100
if a==10:
    
    
chizi dg nmibine


ta zamani k shart False --> hamino mibine

ag True shod baz mishe -->

a=100
print('salam')

'''


a=10


if a==10:
    print('salam')
    print('khodafez')
    b=19
    c=b*10
    d=c+98
    print(d)
    
    
#ta madami k yek tab jolo tarim




a=10

if a ==10:
    print('salam')
    print('khobi')
    
print('khodafez')


'''
salam
khobi
khodafez


'''



a=20

if a ==10:
    print('salam')
    print('khobi')
    
print('khodafez')



'''
ta madami k shoma yek tab fasele darid jozve badaneye shart hesab msihid

salam , khoobi jozve sharte , ag true bashe ejramsihe

ag biay biron az shart (bargardi ) sare lini

khate mostaghel
shart tRUE , FASLE , 

khodafesz ejra mishe

chon shoma fght dakehel if ro sharti krdid


khodafez


'''







'''
3 no shart darim



1- Just if (fght yek if ) darim


if shart:
    dastoor1
    dastoorat.....
    

mesle yek rahzan --> hame daran obor mikonan
migarde fgth onaei k Shart True hast ro majbor b ejra mikone


rahzan kenare rahe, fgth kasaei gardanbande tala daran (True)
migiratesho majbro mikone, gardanbdo --> ejra konan




Agar shart True bod inkaro kon, age nabood velesh kon





2- If - else (do rahi besazi)

agar true bod kare 1 , ag nabod kare 2 

karavan ->iste bazresi -->hame do gehsmat mishan

true --> kare 1 , false --> kare2

forodgah , ag mardi --> mardoone 
khanomi --> banovan

2 rahi baz koni





'''

#mesle yek karavan a haye mtoefgavet

#ife khali --> fght onaei True 

#a==10 ->Truye --
#majbioreshon kone b anajme yek kar

#prin kon salam --> gardanbadro dar bair


a=10


if a==10:
    print('salam')


#salam


a=5
if a==10:
    print('salam')


#agar True bod --> dastor ejra she ,
#age nabood --> velesh koon  hichi nis





if a==10:
    print('salam')

#agar a ==10 (true) -->salam
#age nabod (false)-->hichi\
    
    
    
    
#dorahi if else

if a==10:
    print('salam')   
else:
    print('khodafez')


'''

Just if --> (noe aval)
       Shart(a==10)
           |
           |
         -----
       |        |
      True      False
       |         |
    dastoor     |
 print(salam)    |
      |         |
      |         |
       ----------- 
           |




2- IF else

       Shart(a==10)
           |
           |
         -----
       |        |
      True      False
       |         |
     dastor1     dastoor2
     Printsalam    khodafez
     |              |
     |              |
     --------------
           | 
           



3- if elif else

do rahi haye too dar too

       Shart(a==10)
           |
           |
         --------------
       |               |
      True          False
       |              |
     dastor1        shart2  (bna dastore 2)
                      |
                  ------
                 |       |
                True    False
               dastor2    dastoor3 (else)
           
           
         
          
         
            
       Shart(a==10)
           |
           |
         --------------
       |               |
      True          False
       |              |
     dastor1        shart2  (bna dastore 2)
                      |
                  ------
                 |       |
                True    False
               dastor2    shart3
               
               
               
           
           

'''


#-----just if
a=20
if a==10:
    print('salam')



#a=10--->salam
#a=!10 (20) ->khali

#agar true bod kare 1 , ag nabod velesh kon





#2--> if else (dorahi)

a=20
if a==10:
    print('salam')
    
else:
    print('khodafez')


#a=10 (true) -->salam
#a!=10 (20) (false) ---> khodafez






a=12

if a>18:
    print('khosh amadid')
else:
    print('ghanoni nist')


print('khodafez')

'''
      code ghabli
          |
        a>18 (shart)
          |
     ----------------------
   |                      | 
  True                   False
   |                       |
   |                       |  
print(khosh amadid)        print('ghanoni nist')
   |                       |
   |                       |  
     ----------------------
            |
        edame code
            |
       print('khodafez')



a=30

if a>18:
else:


print('khodafez')



'''


'''
a=30 ---->
khosh amadid
khodafez



a=12

ghanoni nist
khodafez


'''
#else if --> elif

if a>18:
    print('salam')
    
elif a>14:
    print('saaaalaaaam')

else:
    print('ghanoni nist')


'''

      a>18
      
        |
        
   True       False
salam          a>14 (a<18 --> a>14)
             |
        true     false
    (14<a<18)      (a<14)
     saaaalaaam     ghanoni nist



'''




#----------------------------------------
'''
Mahsool begirim


Website (amazon, digicala ,....)


Moshtari miad --> customer side
Foroshande miad --> User side 


user side -->gehsmati hast k shoam 

miri toosh , name mahsol , name brand, gheymat ro vared mikoni 

va sabt mishe


mikhahim hamchin systemi besazim






'''



print('Salam be foroshgahe FANAVARI CO khosh omadid')

answer = input('aya mikhahid mahsooli ezafe konid?')


#shart --> true false beshe

if answer=='yes':
    print('bale ezafe mikonam')


'''
yes -->bale ezafe mikonam


no--->hichi etefagh nmiofte

man goftam 

'''





#sherkat --> age nevshjt yes --> begi ok ezafe mikonam
#ag no --> mamnoon az shoma
#inaj dorahie

#rahe true --> ok ezafe mikonm no --> mamnon

print('Salam be foroshgahe FANAVARI CO khosh omadid')

answer = input('aya mikhahid mahsooli ezafe konid?')


#shart --> true false beshe

if answer=='yes':
    print('bale ezafe mikonam')
else:
    print('mamnoon')


'''
Salam be foroshgahe FANAVARI CO khosh omadid
aya mikhahid mahsooli ezafe konid? --> yes
bale ezafe mikonam



Salam be foroshgahe FANAVARI CO khosh omadid
aya mikhahid mahsooli ezafe konid? --> no
mamnoon


Salam be foroshgahe FANAVARI CO khosh omadid
aya mikhahid mahsooli ezafe konid?chekahabar 
mamnoon



Salam be foroshgahe FANAVARI CO khosh omadid
aya mikhahid mahsooli ezafe konid?dsakjadshgdas	32	eq8wa
mamnoon


'''


'''
Policy jadid

age gof yes --> begoo bale ezafer miokonm

ag yes nabod --> ag no neveshte --> mamnon komaki khedmati
ag chzie dg nevesht --> yes / no javab bde



'''



print('Salam be foroshgahe FANAVARI CO khosh omadid')

answer = input('aya mikhahid mahsooli ezafe konid?')

#shart --> true false beshe

if answer=='yes':
    print('bale ezafe mikonam')
elif answer=='no':
    print('mamnoon khemdat az mast')
else:
    print('shoma faghat bayad ba yes/no javab bedi')
    
    
    
'''


yes --> 
Salam be foroshgahe FANAVARI CO khosh omadid
aya mikhahid mahsooli ezafe konid?yes
bale ezafe mikonam



no --->
Salam be foroshgahe FANAVARI CO khosh omadid
aya mikhahid mahsooli ezafe konid?no
mamnoon khemdat az mast



chekahabr 
Salam be foroshgahe FANAVARI CO khosh omadid
aya mikhahid mahsooli ezafe konid?chekahabr soltan
shoma faghat bayad ba yes/no javab bedi



'''





'''
Github --> 



1---> yek foroshgah baraye moshtari besazid (customer side)

bege salam aya mikhahid kharid konid? age goft yes , begid befarmaeid ,
 age harchi dg gof veelsh konid




2----> yek foroshgah baraye moshtari besazid (customer side)
begid salam aya mikhahid kahrid konid? ag goft yes --> yaddasht mikonam ,
 ag goft na ya harchizi --> besiar awli



3 --> yek foroshgah baraye moshtari ebsazi (customer side)
begid salam aya mikhahid kharid konid? age gof yes --> yad dahst mikonm,, 
no -> mamnoon, ag harchi dg -> fght ba yes o no javab bedahid







#--------

print('Salam be foroshgahe FANAVARI CO khosh omadid')

answer = input('aya mikhahid mahsooli ezafe konid?')

#shart --> true false beshe

if answer=='yes':
    print('bale ezafe mikonam')
elif answer=='no':
    print('mamnoon khemdat az mast')
else:
    print('shoma faghat bayad ba yes/no javab bedi')
    
    
    
    
4----> hamin mesale foroshgah fanavari (User side) --> yek moshkel dare

do ta moshkel
moshkel ro hal konid

4.1--> yes --> Yes --> javab
4.2--> fasele yes --> javabe gahalt



5---> vaghty k taraf nvsht yes kochik bozorg faslee --> ag
javabesh yes bood (takmil tarin halat) , mahsol ro az taraf begire 
yek listi dahste bashid bename
products --> b tahe in list ezafe konidesh

yes --> esme mahsolo bego -> esme mahsolo minevise--> berizid tahe yek list (products)




'''








