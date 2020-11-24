from dba import dba

dba.get_cursor().execute("select * from tbl_marca")


i = dba.get_cursor().fetchall()

for x in i:
    for a in x:
        print(a , end =" ")
print("\n")

    

