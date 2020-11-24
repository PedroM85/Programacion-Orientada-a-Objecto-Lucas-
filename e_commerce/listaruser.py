from dba import dba

dba.get_cursor().execute("select id_user,nombrecom, fechanac, sexo,telefono,email, ciudad from tbl_usuarios")

 


i = dba.get_cursor().fetchall()


for y in i:
    print(y)

print("\n")    