a = 0b1010 #binary Literals
b = 100    #Decimal Literal
c = 0o310  #Octal Literal
d = 0x12c  #Hexazecimal Literal

coonn = {
    "host" : "localhost",
    "user" : "postgres",
    "pwd" : "root",
    "dbname" : "deliveries",
    "port" : 5432
}

def print_conn():
    print("-"*30)
    for x,y in coonn.items():
        print(str(x) + " is: \t|\t" + "" + str(y))
    print("-" * 30)

    print("-" * 30)
    list(map(lambda item : print(str(item[0]) + " is: \t|\t" + "" + str(item[1])), coonn.items()))
    print("-" * 30)
#Float Literal
float_1 = 10.5
float_2 = 1.5e2

#Complex Literal
x = 3.14j

print(a,b,c,d)
print(float_1,float_2)
print(x,x.imag,x.real)
print_conn()