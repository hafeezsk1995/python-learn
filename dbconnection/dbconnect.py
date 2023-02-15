import mysql.connector
mydb = mysql.connector.connect(user="root",password = "mysql123",host="localhost",database="python_db")
mycursor = mydb.cursor(buffered=True)
# mycursor.execute("select * from usersdata")

# for i in mycursor: 
#    print("mydb",i)


# Create a table in db   

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
 

# crud operations
   # insert
# mycursor.execute("INSERT INTO customers (id,name,address) values (3,'hafeez','kdkr'), (4,'avins','hyd')")
# mydb.commit()


 

# list of employees
# mycursor.execute("select * from customers")

# for i in mycursor:
#     print("i",i)

# # first of employees
# mycursor.execute("select * from customers")
# print(mycursor.fetchone())


# Update 

# mycursor.execute("update customers set name = 'shaik Hafeez',address ='kdk1' where id =1 ")
# mydb.commit()
    

# delete 
mycursor.execute("delete from customers where id = 4")
mydb.commit()
mycursor.close() 