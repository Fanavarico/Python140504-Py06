"""
In The Name of GOD


Created on Sun Sep  6 20:05:17 2026

@author: Ali Pilehvar Meibody


ADV L4




Developer ---> programmer --> Barname nevis


Persian (Farsi) ---> Python

pas bayad yek loghat name dashte bashid ke bedonid az chi koja estefade konid

kheyli az concept haro yad gereftid , kheyli az chizharo nokato midon, 100 notes bedonid
ama 


masale miad , enmidonid khob az kodom concept va chegone esefade konid???




aval bayad shoma yek top level az kole dars dashte bashid (yek derakht na joziat)

kole python --> 3 bakhshe . har bakhsh felan zir bakhsh . zir bakhsh 100 ta nokte


Top level -> bakhsh o zirbaksh



1- Python built in functions --> Tavabeye dakhelie python -->nareni --> yek kari ro anajm midadan
    print() -->namayesh
    input() --> vorodi migrft
    type() , len()  , 
    int() , float() , complex() , list()  , tuple() , set() , dict() --> casting
    a = 10   ---> b  = float(a)  --> 10.0
    
    yek kari ro anjm bedi
    
    vaghty mikhahi namayesh bedi chizio ----> print()
    vaghty mihahi chizi begiri az user --> input()
    vaghty andazeye chizi ra mikhahi begiri --> len()
    vaghty mikhahi formate yek chizo b chize digar tabdil koni -> casting int() float() ,.....



2- Keywords --> banafsh
    logice python -> az bala b paein mikhone az chap b rast . 
    shoma agar in logic (mnategho) bekhahi beham bezani --> keywords estefade koni

    2.1 Conditional statement --> dastorate sharti
        vaghty yek ya chandin khat ro nemikhahi hamishe run beshe
        
        Age , dar soorati ke , shart --> if , if else , elif ........
        
        
        
        1---> vaghty chizi ro mikhahi catch koni --> begiri -->eroro begiri
            donbale yekseri afaradi -->just if
            if shart:
                dastooor
                
            az beyne hame fght kasani ro migiri ke shart true bashe --> dstor ejra she
            len(password)<8 --> print(eshtebahe)
            
            shart -> True False --> >= <= == != , .islower() isupper() , def --> True , false
            
            
        2--->dorahi doros koni--> ya in ya on , ya zoj ya fardd , ya psotive ya negatve, ya yes ya gheyre yes 
        
            if shart:
                dastoor1
            else:
                dastoor2
                
        3--> chanrahi dari --> dorhi haye too dar doo  if elif else
        
            multiple selection --> jam -->yekar , tafrigh --> yekar , taghsi -->yekar , zarb-->yekar
                                    positive --> mosbat, negatvive ->mabnfi -> sefr bod benevis 0 
                    
                        if operation=='jam':
                            c = a + b
                            print(c)
                            
                        elif operation =='tafrigh':
                            c = a - b 
                            print(c)
                        
                        elif operation=='zarb':
                            c = a * b
                            print(c)
                        elif operation =='taghsim':
                            c = a/b
                            print(c)
                            
                        else:
                            print('nmitavanbid chizi gheyr az jamo .. beneviosid')
                            
                            
            Range ha -> score beyen 20 ta 15 --> A , 15 ta 10 -> B zire 10 --> F
                
                if score>20:
                    print('nmitavand bish az 20 bashe')
                elif score>=15: #15-20
                    print('A')
                elif score>=10: #10-15
                    print('B')
                elif score>0 : #10-0
                    print('F')
                else:
                    print('nomre ke nmitone manfi bashad')
            
        

    
    2.2. Loops --> for , while
        tekrar koni , yek patterni tolid konid
        tekrare sabeti (10 bar salam) , tekrare dynamic (az 10 ta 3)
        vaghty mikhahi varede yek list beshi yek chizi beshi , done done ro bekeshi biron check kon -->iteration
        
        ta zamani ke --> while
        ta zmaani k password ro ghalat zad azash felano begir


3- Variable --> yek zarf --> vaghty chizi ra mikhahi daemi ya movaghat
    zakhire koni , bayad berizish dar yek zarf --> oon zarf -> mitone chandin no bashe
    3.1. Numebrs --> (int, float, complex)
        in zarf ro misazam k zakhire konam
        python ejaze mdie ye karaei ham bokoni
        operation --> c = a + b  | ** * / + - 
        comparison --> == != > >= < <= ---> Shart ha , while 
        
    3.2. String -> reshte --> horof, kalame, esm , jomle , brando.._.zarf 
            zarfe typesh --> string
            python ejaze mide yekseri taabe dare mizare taghirato nedo
            
            str functions --> lower()
            
            len(zarf)
            
            lower(zarf) XXXX --> zarf.lower() 
            
            in tavabe khoroji midahand, emal nemishan
            
            zarf = 'ali'
            new_zarf = zarf.lower() 
            
            listi dare --> .lower() .upper() .title() .replace() .strip() 
                            .find()  .count()
                            .is..-->True false
                            .islower()   .isupper() .istitle() .isdigit()
                            
                        =https://www.w3schools.com/python/python_ref_string.asp
                        
                        
        3.3.Boolean --> True , False --> javabe comparison , tavabe islower() --> 
                meyari hast ke bahash if , while o ina kar mikone
                
                
            
            
        3.4. Iterables --> chandin meghdar ro dakhele yek zarf bezarim
        
            3.4.1. List --> vaghty chandin meghdar ro mikhahi dakhele yek zar beiriz list
                ordered(index) , chnagbale, allow duplicated 
            a= [10,20,'Ali',True, 10.3232]
             a[index]
             a[index]
             
                     list functions --> .append() .pop() .remove() .clear()
                     a=[10,20]
                     a.append(40)
                     
                     a--> 10 , 20 ,40
                     emal mishan, khoroji nemdia
                     
            3.4.2. Tuple --> liste --> ordered(inde) , unchanagable , allow duplciated
                DB mortabete
                
            3.4.3. Set --> liste --> unordered(index),unchangable, No duplciated
                bishtr vaghty ba majmoei riaziat kar mikoni (eshterako, ...)
                hazfe chizaye tekrari koni 
                
                
            3.4.4. Dictionary ---> infromation (ensan (esm,sen ,..) ,
                                                product(code, name, price),
                                                model_ai(model=gpt,parameter, token , context))
            
            a=['ali',30,40000]
            
            sen --> a[1] 
            
            a['sen']
            
            index value
            0      ali
            1      30
            2     40000
            
            
            
            key    value
            esm     ali
            sen      30
            hesab    40000
            
            
            a={'esm':'ali' , 'sen':30 ,'hessab':40000 }
            
            a[0]  [1]
            
            a['esm']
                
                
            





"""



#===================================
#===================================
'''

    tamrine 1 - Jalase 2

'''
#===================================
#===================================


#-----------Q1------------
#harchi benevisi -> esme zarf midonatesh 
#yani fek mikone ye zarf dari be esmea
#ye zarf dari be esme ali1234345465

#gofti ke zarfe a ro mosavi bede ba megdhare dakhele zarfe ali
#error dade-->ma zarfi bename ali12344
#a = Ali1234567890

#man anzorma ine ke yek zarf bename a besaz , toosh meghdare ali123333

name= 'Ali1234567890'


#name='ali'
#name[0]--->'a'
#name[1]--> 'l'

#name[0:2] -> 0 1   al



name[0] #Out[2]: 'A'

name[1] #Out[3]: 'l'


#Value --> A l i 1 2 3 4 5 6 7 8  9  0
#Index --> 0 1 2 3 4 5 6 7 8 9 10 11 12

name[0:2] #Out[4]: 'Al'

#akharine->exclude-->shamel nemsihaavd

name[0:3] #Out[5]: 'Ali'

#pas mide? --> too y zarfe dg

zarf = name[0:3]

print(zarf)


adad = name[3:13]
print(adad) #1234567890


name= 'mohsen1234567890'
adad = name[3:13]
print(adad) #sen1234567


#az akahr joda kon


name= 'Ali1234567890'

#Value --> A l i 1 2 3 4 5 6 7 8  9  0
#Index --> 0 1 2 3 4 5 6 7 8 9 10 11 12
#index -->                     -3 -2  -1


name='ali'

name[-1] #Out[13]: 'i'

name[-2] #Out[14]: 'l'



name= 'Ali1234567890'

name[-1] #Out[15]: '0'

name[-2] #Out[16]: '9'

name[-1:-10]


name[-10:-1] #Out[20]: '123456789'

#name[-11:-1]



name='alipilehvar'

name[4:11] #Out[23]: 'ilehvar'
name[4:] #Out[24]: 'ilehvar'



name= 'Ali1234567890'

name[-10:] #Out[26]: '1234567890'


name= 'mohsen1234567890'
name[-10:] #Out[27]: '1234567890'



#q2---

zarf='09123456789'

zarf[1:4] #Out[29]: '912'



#q3---

name='alipilehvarmeibody'

name[0:11] #Out[32]: 'alipilehvar'
name[0:11:1] #Out[33]: 'alipilehvar'
#0 1 2

name[0:11:2] #Out[34]: 'aiievr'
#0 2 4 6 8 

cart='123456789'

cart[0:8:1] #Out[35]: '12345678'
cart[8:0:-1] #Out[37]: '98765432'
cart[8::-1] #Out[38]: '987654321'






#---------------
#Input --> str


#Q Pilehvar --> agar 2 kiklometr 2000 , agar zire 2 kilometr 5000

masafat = float(input('masafat ro bego be kilometer:'))


#do rahi 

#agar balaye 2 --> 20 000      | gheyre insorat 5000

if masafat>2:
    keraye=20000
else:
    keraye=5000
    
    
    



masafat = float(input('masafat ro bego be kilometer:'))

if masafat>2:
    keraye=20000
    print('keraye shoma hast',keraye)
else:
    keraye=5000
    print('kerayeue shoma hast',keraye)
    
    

    
masafat = float(input('masafat ro bego be kilometer:'))
if masafat>2:
    print('keraye shoma hast 20000')
else:
    print('kerayeue shoma hast 5000')
    
    
    
    
    
masafat = float(input('masafat ro bego be kilometer:'))

if masafat>2:
    keraye=20000
else:
    keraye=5000

print('keraye shoma hast:',keraye)

    
    
#------------------------

masafat = float(input('masafat ro bego be kilometer:'))
if masafat<2:
    keraye=200000
    
    print('keraye e shoma shod:',keraye)
    
else:
    keraye_avalie = 200000
    
    keraye_nahaei = keraye_avalie + 5000 * (masafat-2)
    print('keraye ye shom shoma shod:',keraye)
    
    



#------------------------------------------------
#------------------------------------------------
#------------------------------------------------




mablagh = float(input('mablagh ro behem begoo:'))

'''
1 000 000  - binahata --> 15%

500 000  - 1 000 000 -- 10%

0 - 500 000 --> hich




'''

if mablagh>1000000:
    print('15 darsad takhfif')
elif mablagh>500000:
    print('10 darsad takhfif')  #500 000 - 100000
elif mablagh>0: #0-50000
    print('no takhfif')
else:
    print('mablagh nemitavand manfi bashad')
    



mablagh = float(input('mablagh ro behem begoo:'))

if mablagh>1000000:
    print('15 darsad takhfif')
elif mablagh>500000:
    print('10 darsad takhfif')  #500 000 - 100000
elif mablagh>0: #0-50000
    print('no takhfif')
else:
    print('mablagh nemitavand manfi bashad')
    

#print mikone


#mablagh --> 

#new_mablagh = mablagh - (darsad/100) * mablagh


mablagh = float(input('mablagh ro behem begoo:'))

if mablagh>1000000:
    new_mablagh = mablagh - 15/100 * mablagh
    print('new mablagh : ', new_mablagh)
elif mablagh>500000:
    new_mablagh = mablagh - 10/100 * mablagh
    print('new mablagh : ', new_mablagh)
elif mablagh>0: #0-50000
    new_mablagh = mablagh - 0/100 * mablagh
    print('new mablagh : ', new_mablagh)
else:
    print('mablagh nemitavand manfi bashad')
    



    


mablagh = float(input('mablagh ro behem begoo:'))

if mablagh>1000000:
    new_mablagh = 85 / 100 *  mablagh 
    print('new mablagh : ', new_mablagh)
elif mablagh>500000:
    new_mablagh = 90/100 * mablagh 
    print('new mablagh : ', new_mablagh)
elif mablagh>0: #0-50000
    new_mablagh = 100/100 * mablagh 
    print('new mablagh : ', new_mablagh)
else:
    print('mablagh nemitavand manfi bashad')
    
    




mablagh = float(input('mablagh ro behem begoo:'))

if mablagh>1000000:
    new_mablagh = 0.85 *  mablagh 
    print('new mablagh : ', new_mablagh)
elif mablagh>500000:
    new_mablagh = 0.9 * mablagh 
    print('new mablagh : ', new_mablagh)
elif mablagh>0: #0-50000
    new_mablagh = mablagh 
    print('new mablagh : ', new_mablagh)
else:
    print('mablagh nemitavand manfi bashad')
    
    
    
    


#-----
shomare_kart = input('shomare karo bede')

pish_shomare = shomare_kart[0:5]


#dorahi -> ya ine banke sahahr, ya in nist Unknown (nashenakhte)
#if else

#shart --> psih shomare aya barabar hast ba 6104 -->bank melat


if pish_shomare == '6104':
    #bank='banke mellat'
    print('banke melat hast')
else:
    #bank='nashenakhte Unknown'
    print('bank nashenakhte ast')
    
    
    
    
#-------
saat = float(input('saat ro begoo:'))

#zire 0 --> manfi--> saat nemitavanbd manfi
#0-12 ->sob
#12-16 --> zohr
#16-18 --> asr
#18-24 -->shab
#24 - binahat --> nmitavand bish az 24 bashad



#range-->if else elif -->

if saat>24:
    print('nmeitavand saat bish az 24 bashad')
elif saat>18: #18 - 24
    print('shab')
elif saat>16: #16 - 18
    print('asr')
elif saat>12:
    print('zohr')
elif saat>=0:
    print('sob')
else:
    print('saat nemitavand shab bashad')
    
    
    
    
    




#===================================
#===================================
'''

    tamrine 2 - Jalase 3

'''
#===================================
#===================================




#===================================
#===================================
'''

    tamrine 5 - Jalase 5

'''
#===================================
#===================================

#---password

password = input('password :')


if len(password)>=8:
    if not password.isupper():
        if not password.islower():
            if not password.isdigit():
                if not password.isalpha():
                    
                    count=0
                    for character in password:
                        #if character =='@' or character
                        if character in ['@','#','$','%']:
                            count = count + 1
                            
                    if count !=0:
                        print('password dorost hast')
                    else:
                        print('az character estefade kon')

                else:
                    print('nmeitone hamsh hroof bashe')
                
            else:
                print('hamash adad nmitone bashe')
                
            
        else:
            print('na hamsh koochike')
        
    else:
        print('na hamsh bzoorge to bayad kochik ham bezani')
        
else:
    print('ramze shoma zire 8 ragham hast')





password = input('password :')

count=0
for character in password:
    #if character =='@' or character
    if character in ['@','#','$','%']:
        count = count + 1





if len(password)<8:
    print('password zire 8 raghaame')
elif password.isdigit():
    print("bayad horof dashte bashi")
elif password.isalpha():
    print('na bayad adad bashi')
elif password.islower():
    print('na nabayad hamash kochik bashe')
elif password.isupper():
    print('na nabayad hamash bozorg bashe')
elif count==0:
    print('bayad character dashte bashi')
else:
    print('passworde shoam sabt shod')





word ='aaabbccccd'


for i in word:
    print(i)

'''
a
a
a
b
b
c
c
c
c
d
'''



word ='aaabbccccd'


for w in word:
    print(w)


#-------

word ='aaabbccccddd'

old_w=''

count=0

all_count=[]
all_character=[]
for w in word:
    
    if old_w==w:
        count=count+1
    else:
        all_count.append(count+1) # 2 bar tekrar + 1 boode
        all_character.append(old_w)
        count = 0 
        
        
    old_w=w
        
    #print(w)



print(all_count) #[1, 3, 2, 4]

print(all_character) #['', 'a', 'b', 'c']


new_list=[]
for i in range(1,len(all_count)):
    new = all_character[i] + str(all_count[i])
    new_list.append(new)
    
print(new_list) #['a3', 'b2', 'c4']

final = ''.join(new_list)
print(final) #a3b2c4


    

#---------------


word ='aaabbccccddd'

old_w=''

count=0

all_count=[]
all_character=[]
for i in range(0,len(word)):
    
    if old_w==word[i]:
        count=count+1
        if i==len(word)-1:
            all_count.append(count+1)
            all_character.append(old_w)
            
    else:
        all_count.append(count+1) # 2 bar tekrar + 1 boode
        all_character.append(old_w)
        count = 0 
        
        
    old_w=word[i]
        
    #print(w)



print(all_count) #[1, 3, 2, 4, 3]

print(all_character) #['', 'a', 'b', 'c', 'd']




new_list=[]
for i in range(1,len(all_count)):
    new = all_character[i] + str(all_count[i])
    new_list.append(new)
    
print(new_list) #['a3', 'b2', 'c4', 'd3']

final = ''.join(new_list)
print(final) #a3b2c4d3



#---------------
#---------------
#---------------
'''
برنامه‌ای بنویسید که یک متن از کاربر دریافت کرده و گزارش زیر را تولید کند:

Total characters
Total words
Total letters
Total digits
Total spaces
Total uppercase
Total lowercase
Longest word
Shortest word
Most repeated character
Most repeated word

'''


sentence = input('sentence ro behem bede:')

# fasele --> character

#--q1.1
total_characters = len(sentence)

#--q1.2
word_lists = sentence.split(' ')
totalword = len(word_lists)




'''
new_sentence = sentence.replace(' ','')
new_list=[]
for i in new_sentence:
    if i not in ['@','#','$','%','^','&','*']:
        new_list.append(i)

        
total_letters = len(new_list)
'''

total_letters=0
for i in sentence:
    if i.isalpha():
        total_letters = total_letters + 1
    
    



total_digits=0
for i in sentence:
    if i.isdigit():
        total_digits = total_digits + 1
    


total_spaces=0
for i in sentence:
    if i==' ':
        total_spaces = total_spaces + 1
    



total_upper_case=0
for i in sentence:
    if i.isupper():
        total_upper_case = total_upper_case + 1
    

        

total_lower_case=0
for i in sentence:
    if i.islower():
        total_lower_case = total_lower_case + 1





word_lists = sentence.split(' ')
#max(word_lists)

max_len=0
max_word=''

for word in word_lists:
    word_len = len(word)
    if max_len < word_len:
        max_word = word
        max_len = word_len

print('word maximum len:',max_word)





word_lists = sentence.split(' ')

#min(word_lists)


min_len=100000000
min_word=''

for word in word_lists:
    word_len = len(word)
    if min_len > word_len:
        min_word = word
        min_len = word_len





'''

ai.course22.alipilehvar@gmail.com



'''
