from dba import dba

dba.get_cursor().execute("select * from tbl_ciudad")

 


i = dba.get_cursor().fetchall()

#for x in range(1 , len(i), 1):
for x in i:
    for a in x:
        print(a , end =" ")
print("\n")

    

