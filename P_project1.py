
"""
In The name of GOD

Created on Sun Nov  8 20:34:09 2026

@author: Ali Pilehvar Meibody




P Project ---> yek porozhe ei hast ke real hast baraye yek systeme
modirate quiz --> yek application ro besoorate Backende , kernelsh, enginesho
besazid



P-project --> man ta yejaei az code minevisam , p projecti ha --> takmilesh mikonan
too yek deadline --> badesh class project2 --> jalase akahr ebande --> khodam
takmil mikonam -->mabaes

M-porject --> yek pish tamrin mibinan , Yek goroh dar telegram bezanan mano add konan
idea (10 ideas) yekodom entkehab mikonan, shoro mikonan





1- Python built in fucntions
2- Keywords (IF (Conditional stateents) , loops (for,while) ,def (functions))
3- Class --> object oriented programming (OOP)
4- Database ORM ?? -> emroz sohbat mikonim rajebesh


harzaman --

a=10
b=40

---> RAM --> spyder ro bebandi, ya computer khamosh -->  gone miran tamom

biay systeme app eto , web appeto --> ram zkahire koni , zarf haye python (variables)
zakhrie koni --> 10000 moshatri dri, 100 information --> server yeho brghesh ghat she --> raft

daemi inaro negah dari --> table (jadval) , majmoei ee az jadavel --> database (paygahe dade)
--> HARD DISK --> bargh ham ebre -> zakhire hast


variable ha .. --> temporary ke logic haro anjam bdi , username , str konid , a esho 
if bezani for list ,... --> zakhire --> zarf --> (RAM --> HARD) 

bekhoni --> az HARD bekhooni




database --> sql --> structured query language (SQL) -->mese python

chndin database management (DBM) --> mysql, sqlite, postgresss --> yek managementi mikonan
ejaze midn shoma zabane sql toosh bzni , komak mikonan , excell , barnamas , TOOL (abzar)

mysql --> ghadimi tarin , konde ,
postgress --> jadid tarine, website --> complex learning curve

Sqlite --> light version az mysql --> db vasl bshi ,......


alan --> sqlite hast .

mysql , postgress
ketab, website,youtubr (aparat) ,  gpt ,..



SQL ---> user besazid

sql nasb konid , user besazid ---> root 

user haye motenave besazid


--> CREATE USER  IDENTIFIED BY password; 

database besazid --> CREATE DATABASE SHOPS;


database --> koli jadval tooshe

b har user dastrei b database ro midi

user1,user2,user3

db1,db2,db3

db(table1,table2,table3)


user1---->db1



DB --> table misazi


TABLE --> radif (row) , soton (column)

man mikham yek table besazam bename users --> chegone zakhire mishavand??


soton ---> id username, email, password 
radif --> yek user 0 alipilehvar alli@gmail.com 1234
                    1 mohsen mohsen@gmail.com 23382732
                    2 vahid 
                    3 hamid
                    



table --> koli kharid anjam mishe --> orders

table orders besazi -->

soton --> id , order_number, date, total_Price
radif --> 0    393322 , 17aban , 100 000
        1  2329328 , 18 aban , 1 000 000
        


table besazid --> dastore sql 

Terminal --> dastooro mizanm --> table --> hard sakhte mishe


Inkar sakhte --> skahte abdsh hey terminal, python????

ORM --> Object Ralational Mapper  (ORM)

haminkararo , sakhte table, vared krdne data too table, didane table


CReat
Read
update
delete
CRUD -> amaliat CRUD --> dastoori sql




pythonic inkaro konm? ---> ORM bale 



sqlite3

search too google --> Pypi esme ketabkhone --> toosh

samte chap bala --> dastore

pip install felan --> copy mikon


terminal,, mohitet --> mizani 


install mishe ketabkhone




"""

import sqlite3 

connection = sqlite3.connect('first_try.db')

#age vojod nadasht first_try.db --> misazi va behesh vasl mishe -> connection
#age vojod dasht first_try.db --> behesh vasl msihe --> connection


#connection --> mano b .db vasl mikone

#.db --> databasete --> koli table darone in db hast , datahat disk --> .db

#connection.cursor

cursor = connection.cursor()


#esme sotoon , type e sotooon, constraints

'''


Create TABLE users (
    column_name column_type constraints ,
    column_name column_type constraints ,
    column_name column_type constraints ,
    column_name column_type constraints )






type e sotooon
column_type
chap


sql                
INT                
VARCHAR(100)     str  ta 100 character      
TEXT             str boland
DECIMAL          float  DECIMAL(10,2)  93223832.22



constraints
PRIMARY KEY ---> kilide avali --> index 0 1 2 3 4 ,... sotone id

id INTEGER PRIMARY KEY

AUTO_INCREMENET --> khodesh update

UNIQUE --> 

NOT NULL --> khali bashe

'''





cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) ,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
    )""")



#IN YEK DASTOORE sql hast
#cursor -- > exceute mikone -> connection --> first_try.db

#too db az tarighe python --> sql run mikoni --> table misaze




connection.commit()



connection.close()




#-------
connection = sqlite3.connect('first_try.db')
cursor = connection.cursor()



#ORM --> Pythoni inkaro anjam bedam ---> Ketabkhon ei dairm bename
#sqlalchemy --> pythonic sql benevisam



'''
(base) apm@APMs-MBP ~ % cd desktop 
(base) apm@APMs-MBP desktop % mkdir project
(base) apm@APMs-MBP desktop % cd project
(base) apm@APMs-MBP project % pwd
/Users/apm/desktop/project





(base) apm@APMs-MBP ~ % cd desktop 
(base) apm@APMs-MBP desktop % mkdir project
(base) apm@APMs-MBP desktop % cd project
(base) apm@APMs-MBP project % pwd
/Users/apm/desktop/project
(base) apm@APMs-MBP project % python -m venv fanavari
(base) apm@APMs-MBP project % source fanavari/bin/activate
(fanavari) (base) apm@APMs-MBP project % deactivate



mac/linux --> source fanavari/bin/activate
powershell -->
cmd ---> 



pip install sqlalchemy


(base) apm@APMs-MBP project % pwd
/Users/apm/desktop/project
(base) apm@APMs-MBP project % source fanavari/bin/activate
(fanavari) (base) apm@APMs-MBP project % pip install sqlalchemy



(fanavari) (base) apm@APMs-MBP project % conda activate DL
(DL) (fanavari) apm@APMs-MBP project % pip install sqlalchemy








(fanavari) (base) apm@APMs-MBP project % touch database.py









#engine --> quiz.db
#sessionlocal --> engine 
#base 

dakhele database.py hastand




Table besazim ---> sakhte table--> jadval




(DL) (fanavari) apm@APMs-MBP project % touch models.py     


models.py --> ma jadavelo


CREATE TABLE users(
    id type constraint
    username type constrains
    email
    phone
    .....)


CREATE TABKE ....



--> class besazid tooye models.py

--> class ha ers bebare --> Base (decleerative base)


class --> table beshan



pip install pymysql



from sqlalchemy.engine import URL
database_url = URL.creeat(
    drivename='mysql+pymysql'
    username =
    password=
    host='localhost'
    port=3306
    database=)



engine = create_engine(database_url)



toye models --> table haro besazim

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer,primary_key=True,index=True)
    
    name  = Column(String,nullable=False)
    
    answer = relationship('Answers',back_populates='user')
    
    
    

file models.py --> koli class tooshe hamin , agar benevisi

python models.py --> hichi gharar nis beshe -> table skahte bshe

dastoor baraye sakhte table dashte bashi


file --> setup_db.py     main.py



from database import engine
from database import Base
#b besmela --> table ha sakhte beshan harmogeh main.py -->



Base.metadata.create_all(engine)



hardafe python main.py--> harkari kone --> table haro msiaze


table haei k hamone --> nmiad az aval pakeshon kone --> sare jashe

able haeye jadid , soton haye jadideto ezafe mikone .db


ya table jadide --> az aval misaze


porozhe ---> yek mini appe --> 4 5 ta question , options -->

yeki k run mikone appo --> username misaze, bad answer mide



soal ='sdfffddfd'
option1='3'
op


print()

input(...)


user??


dar models 4 ta table sakhatm --->

users , questions, choice, answer




yek fili dahst ebashim --> ke biad 3 ta question besazi --> databse

--> seed.py 


hamechio az main.py rikthm too seed.py k run krdim --> table haye models ro 
besaze va 



dakhele seed.py --> old_seed.py


from database import engine
from database import Base
#b besmela --> table ha sakhte beshan harmogeh main.py -->


print('Creating tables .........')
Base.metadata.create_all(engine)


#Base kasani ke metdata --> classs haei k ers borde shodid az Base

#create kon roo engine --> dtaabase.engine --> quiz.db -> database table haro besaz



#database --> koli table tooosh

print('Tables created successfully!')

from database import get_db

db = get_db()

print('Creating questions')

from models import Questions

q1 = Questions(text='What is python?')
db.add(q1)
db.commit()
db.referesh(q1)



#choice
# is program
# is web app
# is programming language -->dorose

#3 ta 

from models import Choice

ch1 = Choice(text='Is program',is_correct=False, question_id =q1.id )
ch2 = Choice(text='Is web app',is_correct=False, question_id =q1.id )
ch3 = Choice(text='Is programming language',is_correct=True, question_id =q1.id )

db.add(ch1)
db.commit()
db.referesh(ch1)

db.add(ch2)
db.commit()
db.referesh(ch2)

db.add(ch3)
db.commit()
db.referesh(ch3)



inja ma miaym soal haro misazim



main.py --> python main.py 

user biad --> esm benevise , soala namayesh dade beshe va javab bde





database.py --> sare jashe
models.py --> sare jashe

seed.py --> shoma soal tarh mikoni --> sadas
main.py --> run koni --> user baid soal ha dide bshe azash porside mishe



seed.py --> old_seed.py
main.py --> old_main.py



pas sakhtame hey biam benevisam 

tooye seeed -->
from models import Questions

q1 = Questions(text='What is python?')
db.add(q1)
db.commit()
db.referesh(q1)



nemitonm az tabe ei estefade konm-> create_question()




dakhele main -->
user = User(name=username)
db.add(user)
db.commit()
db.referesh(user)



create_user(username)



tavabe --> Create, Read , update , delete  (CRUD) --> crud.py koli tabe minevisam

seed.py , main.py --> importeshon mikonm




pas shoma tanha taklifeton ine

in file --> Project_p --> github --> download konid

tooye crud.py --> tavabe ro takmil konid



too har tabe --> besoorate fingilish tozih bedid chikar mikoni
baalye har khateton ye hashtag bznid tozih bdi har khat

tavabe ro takmil krdid

azashoon use konid --> seed.py and main.py 


tamam shdoio raft



---> Github

repository --> P_PROJECT_Ali_Pilehvar

 P_PROJECT
 
 
 
 
email --> payam bedid takmil shod --> telegram migim



'''







