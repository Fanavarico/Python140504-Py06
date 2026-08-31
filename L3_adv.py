"""
Created on Sun Aug 30 20:25:16 2026

@author: Ali Pilehvar Meibody



ADV_L3



"""

'''
Python

human <--------Interface------>Machine(0,1 binary)

interface ->python -->zaban ->  grammar vocab

Ipython kernel --> ke betone python ro tabdil kone be 0,1 dastor bede be computer

IDE/Editor ---> code python minevsii -->run mizani --> ipython kernel -> ejra mikone


Spyder, vs code


spyder -- harchi minevsii dar yek file .py benevisi bayad
pythonic bashe

#  qout --> comment ya tozihat benevisi

harchizi gheyr az in -> 

1- Python built in function --> tavabe dakheli python

print() input() len() type() ,....
narenji --> yek kari anjam mide

2- keywords --> logice code ro beham bezani
if , else, for , while , def , and , or ,...

3- Unknown --> variable name --> zarf mikhay besaazi
esmesho --> sefid


variables

    3.1. Numbers (int, float, complex) ** * + - / || == !=  > < >= <=
    3.2. Bool (True , False )
    
    3.3. STR --> harf, esm, kalame, jomle -> qutation 'ali'  's'
            esm[index]  esm[0]  esm[4:8] 
            str.function()
            str.upper()
            tavabe ei bodan k khoroji midadan, emal nemishodn
            
            name = 'ali'
            
            upper(name) XXXXXX
            
            NEW_NAME = name.upper()
            
            print(name) --> ali
            new_name --> ALI
            
            .upper() .lower()
            
            1--> .upper() .lower() .capitalize() .title() .replace('a','b')
            2--> adad pas midan --> name.count('a')    name.find('a') ->index
            3--> Boolean (True,False) .isupper() .islower() 
            
    3.4. Iterables --> multiple values --> zarf beirizm
        3.4.1. List --> ordered (index) , changable , allow duplicated
            a=[10,20,30,40]
            a=[10,10,10,20,30]
            a[0]
            a[0]=200   ---> [200,20,30,40]
            
            list.function() --> a.append()  a.extend() 
            --> emal mishan , khoroji nemidan
            
            new_list=[10,20]
            new_list.append(30)
            
            print(new_list) --->[10,20,30]
            
            por karbord tarin iterable -> chant avalue ->
            
        3.4.2. Tuple --> ordered (index) ,unchanagable , allow duplicated
                a=(10,20,30)
                print(type(a))-->tuple
                
                a[0] -->10
                
                a[0]=200 --> error --> subscriptable --> nemitone
                
                database --> tavabe ei k , library, frameworki
                database -> paygahe dade -> HARD --> va tamame adad
                va megdhar ha oonja zkahir mishan --> multiple table
                
                database -> chandin jadval
                
                a=10 ---> RAM zakhire mishe , barnamaro mibndi , computer --> a 10 hichkodom
                
                moshtariat --> informatioento hamishe zakhire beshan --> HARD benveisim na ram
                
                database --> paygahe dade --> mysql , seqlite , ......
                
                database --> multiple table 
                
                framework, library --> data midi migiri --> tuple
                vasate kar chizi taghir peyda nakone [nakhaste] -->safety
                
                tuple --> listi hast ke changable nist
                
                
                a=(10,20,30)
                
                b=list(a)
                
                print(type(b))-->list --> chnaagble
                b[0]=200
                print(b)--> [200,20,30]
                
                a=tuple(b)
                
                a-->(200,20,20)
                
                casting --> 
                
        3.4.3. Set --> unordered (index) , unchanagable, no duplicate
        
        --> majmoe haye riazi , hazfe tekrari ha
            a = {10,20,30}
            
            a[0]--> index nadaram --> acces  ndri 
            
            
        3.4.4. Dictionary
        
        information -> etelaat dakhele yek variable berizi
        kar ba list sakhte
        
        a=['ali',30, 4400000, 091988888888]
        
        a[3]
        
        
        list
        index      value
        0          ali
        1           30
        
        
        a['phone']
        a['sen']
        a['esm']
        
        dictionary
        
        index value -> list,tuple
        
        key value -->  dictionary
        key1  val1
        key2  val2
        key3  val3
        
        a={'esm':'ali'  , 'sen':30 , 'pool':40000 ,'phone':'09197888888'}
        
        a['esm'] ---> ali
        a['sen'] -->30

                        
                




'''


#yek code ro run mikrdid --> SPYDER 
#IDE / Editor , kole code ro miad 
#ya oon ghesmati k select krdid

#ersal mikone --> Ipython kernel --> translate --> 0,1 bianry ->computer, ejra
#-->javabo bargardone --> console neshon bede

#vaghty mide ipython --> ipython mesle yek ensan az bala b paein
#az chap b rast mikhone --> koel manteghe geenrale python inde

#age shoma bekhahi in mantegh(logic) ro beham bezani -> Keywords (banafsh) estefade bokoni


sen=177566565560
print('salam')


#sen -->ssalam
#sen=177566565560



#fgth baraye sen haye balaye 20 era bshe

#python mikham begam agha az bal ab paein nakhon

#yek khat ya chandin khat ro , ye shartio check kon va bekhon

#-->conditional statement estefade konm





'''

Dastoorate sharti

be se bakhsh taghsim mikonam


1- Just if --> faghat if -> rahzanan 

fght afradi k shartesho True hast ejra mishe

shart True bashe --> ejra mikone
shart false bashe --> boro 

man yek rahzanam donbale onaei hastam k shart true hast
onaro majbor mikonm ejra konan

false-->beris




2- If else --> do rahi -> do rahi misaze
shart Tr

shart True bood kare 1 
shart false bod nago bikhial velesh kon --> kare 2

do rahi



3 - if elif else --> dorahi haye too dar too






'''
sen = int(input('senet chegahdre?:'))

if sen>10:
    print('salam')

#shart tRUE BASHE --> SEN>10 -->11,12,..-->salam ->edame code
#shart false bashe --> sen<=10 -->10,9,8,.. -->edame code





sen = int(input('senet chegahdre?:'))

if sen>10:
    print('salam')
else:
    print('khodafez')
    
#shart tRUE BASHE --> SEN>10 -->11,12,..-->salam
#hart false bashe --> sen<=10 -->10,9,8,..-->khodafez


#shart false shod vel nakon nemigam akre 2 , dorahi besazam , dorahi haye


#true --> salam
#faslse --> shart2 true shod --> khodafez1  false -> khodafez2


sen = int(input('senet cheghadre?:'))
ghad= int(input('ghadet chegahdre?:'))

if sen>10:
    print('salam')
elif ghad>160:
    print('khoafez1')
else:
    print('khodafez2')

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
           
           
         


Jalase ghabl --> email ersal nakardan

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
    


SUBJECT --> adv_l2_mana_ahadpanah   
            adv_ayoub_abedini

file ro ersal konid , addrese github

update -> baray eman mojadad addres egithub

email  :  ai.course22.alipilehvar@gmail.com

matn --> s salam 


'''



#=======================================
#=======================================
#=======================================

'''
Bgir --> input() , open() , django/fastapu --> def()
neshon bede , namayesh bede --> print()

agar , hart -> if 
            rahzan --> yek sharti mikhahi yek kari koni --> just if
            dorahi --> hatman bayad taghsim b dota bshe, shart mzire ya in bshe ya on sbeh --> if else
            dorahi haye too dar too -- ya in shod , ya oon shod 
                        chanta selection --> + ya - ya ya 
                        range --> sen>30 , 30 - 20  , 20 -10 
                        if elif elif elif ... else



'''



'''
1---> yek foroshgah baraye moshtari besazid (customer side)

bege salam aya mikhahid kharid konid? age goft yes , begid befarmaeid ,
 age harchi dg gof veelsh konid

'''
javab  = input('salam aya mikhahid kharid konid?')

if javab=='yes':
    print('befarmaeid')

#yes--> befarmaeid
#no --> hichii
#jsdhd-->hichi


'''
2----> yek foroshgah baraye moshtari besazid (customer side)
begid salam aya mikhahid kahrid konid? ag goft yes --> yaddasht mikonam ,
 ag goft na ya harchizi --> besiar awli

'''

javab  = input('salam aya mikhahid kharid konid?')

if javab=='yes':
    print('befarmaeed')
else:
    print('besiar awli')
    
    
#yes --> befarmaeid
#no -->besiar awli (nemige velesh)
#jdsghds --> besiar awli


#do rahi beyne yes va no nist
#do rahi beyne yes va gheyre yes
    



'''
3 --> yek foroshgah baraye moshtari ebsazi (customer side)
begid salam aya mikhahid kharid konid? age gof yes --> yad dahst mikonm,, 
no -> mamnoon, ag harchi dg -> fght ba yes o no javab bedahid


'''

javab  = input('salam aya mikhahid kharid konid?:')

if javab =='yes':
    print('befaraeid yaddasht mikonam')
elif javab=='no':
    print('mamnoon')
else:
    print('fght ba yes o no javabbedid')
    

#yes0-->befarmaeid
#no-->mamnon
#jdsd --> ba yes o no javab bedid


'''
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



'''

catch --->

errori begiri , yeseriaro joloshono begiri --> rahzane mosbat
just if 

password --> agar zire 8 e behesh error bedi

just if 





do rahi dar --> ya in ya yekchize dg --> if else




do rahie too dar too 

    multipe selection -->if selection1 , elif selection2, elif selection3,...

    range -->


'''


password = input('password ro vared konid:')

if len(password)<8:
    print('nemishavad password zire 8 bashad')
    
    




password = input('password ro vared konid:')

if len(password)<8:
    #print('nemishavad password zire 8 bashad')
    #return
    raise ValueError('nemishavad password zire 8 bashad')
    
#liste error ha



#numb1  , numb2 , operation 

#agar jam --> felan kon
#tafrigh 
#taghsim 
#zarb

#multiple selection


#agar --> if 

numb1 = int(input('number 1 ro bede:'))
numb2 = int(input('number 2 ro bede:'))
operation = input('amaliateto begoo:')



if operation=='jam':
    javab = numb1 + numb2
elif operation=='tafrigh':
    javab  = numb1 - numb2
elif operation=='taghsim':
    javab= numb1 / numb2
elif operation=='zarb':
    javab = numb1 * numb2
else:
    #print()
    raise ValueError('Bayad opertion yeki az in kalamat bashad : [zarb,jam,tafrigh,taghsim]')

print('javabe shoma:',javab)






score = int(input('nomrat chand shode:'))
#agar score beyne 20 ta 15 A, 10 ta 15 B , zire 10 -> f

#20 ------15------10------0


if score>20:
    #print('eshtebah vared krdi')
    raise ValueError('Adad nemitavand bish az 20 bashad')
elif score>15: #20 - 15
    print('A')
elif score >=10:
    print('B')
elif score>=0: #0 -->10
    print('F')
else:
    #print('')
    raise ValueError('Nomre nemitavand manfi bashad')
    
    


#dota shart dari

#   ham in ham oon --> and (har joftesh) bayadie

# ya in ya --> hadegaha yeki az in shart ha --> or



#ham vaznesh bala 50 , ghadesh 170
vazn=0
ghad=0

if vazn>50  and ghad>170:
    print('salam')
    
#print('salam') --> True True


    #ya vaznesh bala 50 , ya ghadeh bala 170 -- 
    #hadegahal ghadesh bala 170 ya vaznesh bala 50 bashe

if vazn>50 or ghad>170:
    print('salam')

#true true -->mishe
#true false --> mishe
#false true --> mishe
#false false ---> print nmishe


if vazn>50:
    print('salam')
    

if not vazn>50:
    print('salam')
    
#ba paeini yeki
if vazn<=50:
    print('salam')



#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
''' 
1-python buuil in functions
2- keywords (if , else, elif , raise, and , or , not , in )





      Loops
      
Yek kari ro tekrar koni


'''




'''

        
    
adv_l3_name_lastname
ai.course22.alipilehvar@gmail.com
matn ham faramosh nashe

file befrestid
tarjih --> github link 

matn-->sohbati, soali , ayande ,...


        1 Ta mesal If
         
1---> Password begriid az user, password fght dar soorati 
be taraf begid (ba moafaighiat sabt shod) ke andazash bish az 8 bashad
hatman tarkibi az adad va horof bashad
hatman tarkibi az horofe bozorg va kochak bashad


        3 mesal Loop
        2,3 --> for loop
2--> a ] adade farde byene 30 ta 50 ro print konid
     b ] adade farde beyne 30 ta 7000 ro beshmorid, begid chantas (print kone y adad -->beeg chanta)
    c]  adade zoje beyne 60 ta 120 ro joda konid tooye yek list bename zoj_list
    
    
    
3--> yek listi darim be in nam , tedade afradi k esmeshon ba a shoro mishe ro bedast bairid --> for
my_users=['ali','vahid','hamid',...]


4--> while
oon masaleye foroshgah k miporsid aya mahsoli mikhahid?

agar goft yes --> begid befarmaeeid 
agar goft no --> begid besiar awli

agar harchize dige goft (n yes , na no) --> aval begid bayad ba yeso no javab bdi
mojadad -> aya mahsoli mikhahid?

va inkar ro onghdr anjam bdid ta benevise yes ya no

ta zamani k yes ya no nanevehst --> (ba yes o no javab bede) mahsol mikhahi?

'''






















