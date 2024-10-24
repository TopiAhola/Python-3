
tuple1 = (1,2,3,4,5 )
sanakirja = {1 : tuple1 }

tuple2 = sanakirja[1]
print(tuple2)

for n in tuple2:
    print(n)
#mitä?

while True:
    try:
        int(input("Anna int"))
        break

    except ValueError:
        print("error")

