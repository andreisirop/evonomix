import random
from tkinter import *
while False:
    app = Tk()
    app.title("Jocul piatra hartie foarfeca")
    label = Label(app,text="Textt")
    label.pack()
    app.mainloop()


print("")

print("Acest joc se numeste: Piatra-Hartie-Foarfeca iar scopul este sa alegi una dintre cele trei variante.")

print("De retinut ca:\n-piatra bate foarfeca\n-hartia bate piatra\n-foarfeca bate hartia\n-jocul se termina la egalitate daca ambii jucatori au ales aceeasi variatie")



while True:

    alegeri = ["piatra","hartie","foarfeca"]


    print("")
    alegerea = input("Introdu alegerea ta(piatra,hartie,foarfeca): ").strip().lower()
    print("")

    while alegerea not in alegeri:

        alegerea = input("Introdu alegerea ta(piatra,hartie,foarfeca): ").strip().lower()

    alegerea_calculatorului = random.choice(alegeri)
    print("Computerul a ales {}!!".format(alegerea_calculatorului))
    print("")

    if alegerea == alegerea_calculatorului:
        print("Este egalitate!!")
    if alegerea == "piatra" and alegerea_calculatorului == "hartie":
        print("Din pacate ai pierdut, mai incearca!!")
    if alegerea == "piatra" and alegerea_calculatorului == "foarfeca":
        print("Ai castigat, esti cel mai tare!!")
    if alegerea == "foarfeca" and alegerea_calculatorului == "piatra":
        print("Din pacate ai pierdut, mai incearca!!")
    if alegerea == "foarfeca" and alegerea_calculatorului == "hartie":
        print("Ai castigat, esti cel mai tare!!")
    if alegerea == "hartie" and alegerea_calculatorului == "piatra":
        print("Ai castigat, esti cel mai tare!!")
    if alegerea == "hartie" and alegerea_calculatorului == "foarfeca":
        print("Din pacate ai pierdut, mai incearca!!")

    joaca_din_nou_alegeri = ["da","nu"]
    print("")
    joaca_din_nou = input("Doresti sa joci iara? Da sau Nu ?: ").strip().lower()
    while joaca_din_nou not in joaca_din_nou_alegeri:
        joaca_din_nou = input("Doresti sa joci iara? Da sau Nu ?: ").strip().lower()
    if joaca_din_nou == "da":
        joaca_din_nou == True
    else:
        break
        
        




    
    
      
