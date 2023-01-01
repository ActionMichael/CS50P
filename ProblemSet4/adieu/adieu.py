import inflect

"""
Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""
#取一個liberay功能，且給一個簡寫
p = inflect.engine()

#make a space list to memory name what you tipe in
names = []

#一直問
while True:
    try:
        name = input("Name: ")
        #一有新增就一直往後疊加到list裡
        names.append(name)
    except EOFError:
        #create a new line and stop loop
        print()
        break

print("Adieu, adieu, to "+p.join(names))
