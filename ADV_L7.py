"""
Created on Sun Oct  4 20:20:00 2026

@author: Ali Pilehvar Meibody


python programmer 

Eng(farsi) ----> Programmer --> Python


Matn -->
    yek jaei kar konid --> PRD , Task , project
    startup --> sorat masale --> Phase --> PRD
    
PRD (eng , Farsi) ---> Python




Junior --> taze kar
2,3sal (talash,zaman, prozhe) --> mid level
5,6 sal hadeaghal --> senior
8,9 sal --> Tech lead (CTO , CEO ,....)




#-----mafahim---------
IP --> har device (dastgahe electronici) yek address dare, ekhtesasi --> ip --> kode posti ,laptob,goshit,... beham vasl mishan
Server host (VPS) --> yek sherkati hast miad koli laptob(*) dre tooye yek vahedi jaei  hamashon b interner vaslan
be shoma ino ejare mide . ke shoam abrnamatono roosh run konid , harcheaghdr ke khastid , pool midid

laptob ? --> config haye --> RAM2 G , Hard 200 , internet 200 GB dar mah -- 

kharej az keshavr --> koli organziation (company) --> norvezh, alman , finalnd , ..... 
iran--> serve --> parspack , ...

agar ooon computer --> kheyli ghavi bashe, GPU (tesla , NVIDIA , ) pytorch ,.. -- Train, computation--> abar computer -> simorgh (amirkabir), ferdos (ferdosi) , esfehan


2 Gb RAM , 100 Gb HARD --> 1 million toman mahiane--> behem chi midan??
ip = 88.10.20.30 --> bastare internet k ghabele dastres
password --> mizaran



az laptabam --> Bash (terminal, cmd , powershell) , Terminus -> 
laptob (199.2332.100.100) ---->88.10.20.30 

laptabo miare baram bala

laptab OS esh chie? (Operating system) --> systeme amelesh chie?
microsoft (windos xp , 7 , 10, 11) , Macos (Macbook) , Linux (ubunto ,..)

linux --> safe siahe



website, web app darid

frontend --> Html/css/java script -->oon sheklo shamayel



Backend --> Python, ..  framework --> 
django --> Easyyadgiri , khodesh anjam , ghadimie, kondtare
fastapi -->  jadide, faste , AI data , astet az hame nazar baze --> sakhte yadgiri, daste toe



serveram --> alman 2g , 200gb hard --> 88...... 

az laptabam behesh vasl misham (terminus) yek folder misazam
file python, html ,hame inaro onja misazam
ooonaro main.py (Python) roo run --> hamishe rune -->listen
yek fiel ie k koli tabe toshem, kari nmikone


devops --> kasi ke in management haro mikone roo server




#--------------------
Laptob --> Macbook APM --> 199.2332.100.100

yek frdi shoma basi --> laptob --> 200 

mororgar firefox , safri,googl chrome)
google chrome --> getplutus.com 


getplutus.com (---request--->)getplutus.com 

sherkate jahani DNS Resolver --> getplutus.com  (poshtesh) -->88......


mane ali --> in computere almanam  --> getplutus.com
88...

abzar ha hastan -->Linux --> nginx ,.... --> ina request manageran
harchi request omad 

nginx --> .conf  -> har requesti k omd --> port 

computer --> 88.22.22.22:100 120 130 140 

port --> 120

88.22.22.22 --> Nginx --> 88.22.22.22:120

man file main.py rooye porte 120 listene gosh mide

arki request dad --> /  --> index.html ro befrest

index.html


man tooye mororgaram yek fiel index.html az website migiram

kare mororgrar ine ke in file ro render kone

<javascrpt>
    listen button(submit) --> handle_submit()

    def handle_submit():
      username = username.value
      password = password.values 

      request_data = {'username':username,  'password':password}

      request --> https://getplutus.com/login --> request_data






  </javascrpt>
  
  
  
---> getplutus.com/login --> 88.434434/login --> NGINX ---> main.py


tavabas
"""


sen  = float(input('senet cheghadre:'))

import fastapi 

@fastapi.get('/')
def main_page():
    return '/static/html/index.html'


    
@fastapi.get('/login')
def handle_login(username,password):
    #username --> database --> vojod dare ya nadare
    
    #passworda yekian ya nistan
    
    #age bood -->
    if True:
        return {'success':True , 'message':'be dashbaor khosh omadid'}
    else:
        return {'success':False , 'message':'user name ya password ghalate'}
    
    
    
        




@fastapi.get('/dashboard')
def handle_dashboard():
    pass





username = input('usernameto begoo:')



#script --> .py --> python .py 

print('etmame barname')



sen =input('seneto vared kon:')

sen = 20 

'''
Function kar mikonid

3 ta kare asli dare



Kare 1 ------> 

projct/
   | main.py
   |---account_management/
                   | bardasht.py
                   | variz.py
                   | mojoodi.py
    

tavabro tooye bardahst.py   vorodi --> BOX --> khoroji midan
tooye main.py import mikonid inaro 

kare2 ------>

package -> ketabkhone --> folder --> koli function, class
import 
1000 khat code bzniud --> estefade mikonid

capsool (function)


shabake asabi masnoei --> Artificial neural network (ANN)
--> ANN --> layer dare -> layer yekseri neuron dare
   Vorodi (data) [text] ---> layer1,layer2,layer3,laye4 ---> Khoroji (text)
   
   neuron b neuron , riaziat, jabro ,... 10000 khat neminevisid
   
   function(vorodi) --->kararo --> khoroji mide
   



kare 3 --> bahse listen

django , fastapi 

def tabe()-->  az front vorodi migiran-> anajm midan

@get(/login)
def signup(username,fullname, phone,email,password,confirm_password):
    
    too db mirize
    return True

    erro dad
    return False




'''


#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
'''
  Tamrine shomare shesh - jalase haftom

'''


'''
1
تحلیل متن
تابعی به نام analyze_text(text) بنویسید که موارد زیر را پیدا کند:

تعداد کلمات
تعداد حروف
تعداد اعداد
پرتکرارترین حرف
پرتکرارترین کلمه
طولانی‌ترین کلمه
کوتاه‌ترین کلمه
تعداد کلمات Palindrome
تعداد حروف بزرگ
تعداد حروف کوچک



{
    "words": ...,
    "letters": ...,
    "digits": ...,
    "most_common_letter": ...,
    "most_common_word": ...,
    "longest_word": ...,
    "shortest_word": ...,
    "palindrome_words": ...,
    "uppercase": ...,
    "lowercase": ...
}
'''


#getplutus.com/analyze_text 
def analyze_text(text):
    
    #tedade horof
    #len(text) #ham horof ro dar miare ham space ro 
    #text_without_space = text.replace(' ','')
    #letter_numbers = len(text_without_space)
    
    #tedade kalamat
    #words_list = text.split(' ')
    #word_numbers = len(words_list)
    
    jomle_without_numbers_list = []
    
    #*
    numbers_cunt = 0
    for character in text:
        if not character.isdigit():
            jomle_without_numbers_list.append(character)
            
        else:
            numbers_cunt =numbers_cunt + 1
            
    jomle_without_numbers = ''.join(jomle_without_numbers_list)
    
    #tedade kalame
    
    jomle_list = jomle_without_numbers.split(' ')
    
    #*
    word_numbers  = len(jomle_list)
    
    
    jomle_withotu_space = jomle_without_numbers.replace(' ','')
    
    #*
    letter_number = len(jomle_withotu_space)
    
    
    
    #listi az kalame
    #['in' ,'the' ,'name','of','god] --> jomle_list
    
    upper_count = 0
    lower_count = 0
    for kalame in jomle_list:
        if kalame.isupper():
            upper_count = upper_count +1
        else:
            lower_count = lower_count + 1
            
            
    final_dict={'words':word_numbers,
                'letters':letter_number,
                'digits':numbers_cunt,
                'uppercase':upper_count,
                'lowercase':lower_count}
    
    
    return final_dict
        
    
    



'''
تحلیل سفارش
تابعی به نام process_order(customer, *products, **options) بنویسید.

مثال:

process_order(
    "Ali",
    "Laptop",
    "Mouse",
    "Keyboard",
    total_price = 4000
    discount=10,
    tax=9,
    shipping=200000
)
تابعی بنویسید که سفارش را تحلیل کند.

خروجی:

{
    "customer": "Ali",
    "products": [...],
    "discount": 10,
    "tax": 9,
    "shipping": 200000,
    "final_price": ...
}
چالش:

اگر discount یا tax ارسال نشد، مقدار پیش‌فرض داشته باشد.

'''
'''
process_order(
    "Ali",
    "Laptop",
    "Mouse",
    "Keyboard",
    discount=10,
    tax=9,
    shipping=200000
)
'''

def process_order(customer, *products, **options):
    #customer --> yek chiz
    #products -->(,,,,)  process_order(customer='ali', 229,39,30,430)
    #options --> {'key1':valye1} process_order(customer='ali', 229,39,30,430,'number':)
    
    
    #customer -> strin --> esm -->maslaan ali
    #products --> (laptopb,mouse,keyboard,,)
    #options  = {dicosunt = 10 , tax = 9 , shipping = 2000}
    disctount = options.get('discount',10)
    tax = options.get('tax',29)
    total_price = options.get('total_price')
    
    shipping = options.get('shipping')
    
    
    final_price = total_price - disctount/100 *total_price + tax/100 * total_price + shipping
    
    
    
    final_dict={'customer':customer,
                 'products':list(products),
                 'disctount':disctount,
                 'tax':tax,
                 'shipping':shipping,
                 'final_price':final_price
                 }
    
    return final_dict




'''
تحلیل لاگ‌های سیستم
داده‌ها به صورت زیر داریم:

logs = [
    ("Ali", "LOGIN", 200),
    ("Ali", "DOWNLOAD", 200),
    ("Sara", "LOGIN", 403),
    ("Reza", "LOGIN", 200),
    ("Sara", "LOGIN", 403),
    ("Sara", "LOGIN", 403),
]
سیستمی بسازید که:

تعداد Login موفق را پیدا کند.
تعداد Login ناموفق را پیدا کند.
اگر یک کاربر حداقل ۳ خطای 403 داشت، او را مشکوک اعلام کند.
تعداد عملیات هر کاربر را محاسبه کند.
گزارش نهایی تولید کند.


'''


def analyze_logs(logs:list):
    #logs --> [tuple,tuple,tuple]
    
    #*
    login_count=0
    
    #*
    un_authorize_count=0
    
    for user_log in logs:
        if user_log[1]=='LOGIN':
            if user_log[2]==200:
                login_count =login_count +1
            else:#403 405 ,
                un_authorize_count = un_authorize_count + 1
                
                
           
    user_informations={}
    
    for user_log in logs:
        if user_log[2] == 403:
            if user_log[0] in user_informations:
                user_informations[user_log[0]] = user_informations[user_log[0]] +1
                
            else:
                user_informations[user_log[0]] = 1
          
    #**
    mashkook_users=[]
    
    for user,number in user_informations.items():
        if number>=3:
            mashkook_users.append(user)
            
            
    
    
    user_statictiscs={}
    
    for user_log in logs:
        if user_log[0] in user_statictiscs:
            user_statictiscs[user_log[0]] = user_statictiscs[user_log[0]] + 1 
            
        else:
            user_statictiscs[user_log[0]]=1
            
    
    
    #print
    
    final_dict={'success_login_attemps':login_count,
                'unsuccessful_login_attemps':un_authorize_count,
                'suspecious_users':mashkook_users,
                'user_operations_statistics':user_statictiscs}
    
    return final_dict






def analyze_logs(logs:list):
    #logs --> [tuple,tuple,tuple]
    #*
    login_count=0
    
    #*
    un_authorize_count=0
    user_statictiscs={}
    user_informations={}
    
    mashkook_users=[]
    
    
    for user_log in logs:
        if user_log[1]=='LOGIN':
            if user_log[2]==200:
                login_count =login_count +1
            else:#403 405 ,
                un_authorize_count = un_authorize_count + 1
                
        
        if user_log[0] in user_statictiscs:
            user_statictiscs[user_log[0]] = user_statictiscs[user_log[0]] + 1 
            
            
        else:
            user_statictiscs[user_log[0]] = 1
        
        
        if user_log[2]==403:
            if user_log[0] in user_informations:
                user_informations[user_log[0]] = user_informations[user_log[0]] + 1
                
            else:
                user_informations[user_log[0]]=1
        
            
        
    for user,number in user_informations.items():
        if number>=3:
            mashkook_users.append(user)
            
                
    
         
    
    #print
    
    final_dict={'success_login_attemps':login_count,
                'unsuccessful_login_attemps':un_authorize_count,
                'suspecious_users':mashkook_users,
                'user_operations_statistics':user_statictiscs}
    
    return final_dict


'''

tamrine shomare 6 --> 3,4 moond

tamrine shomare 7 



'''

