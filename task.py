import sqlite3
#for create a database
movie_con=sqlite3.connect('Moviesdata.db')
print('db created or if create then connect with this..')

#to create a table 
movie_con.execute('create table Movies(id int primary Key not null,Movie_name text,actor text,actress text,director text,Year_of_release date)')
print('Movie Table Created...')

#insert items on database
movie_con.execute("insert into Movies values(1,'Ham sath sath hai','Salman Khan','Karisma Kapoor','Sooraj Barjatya',1999)")
movie_con.execute("insert into Movies values(2,'Mohabbatein','Sahrukh khan','Aishwarya Rai','Aditya Chopra',2000)")
movie_con.execute("insert into Movies values(3,'Baghban','Amitabh Bachchan','Hema Malini','Ravi Chopra',2003)")
print("All rows Inserted...")
movie_con.commit()

#to fatch the data from the database so we can easily show all record at run time
data=movie_con.execute("select * from Movies")
record=data.fetchall()
for row in record:
    print(row)
