import random
import winsound
import time


# winsound.PlaySound("b", winsound.SND_ASYNC | winsound.SND_LOOP )

# correct_sound = pygame.mixer.Sound.play('c')
# wrong_sound = pygame.mixer.Sound('w')

# music = pygame.mixer.music.load('b.wav')
# pygame.mixer.music.play(-1)


questions = {
    "Ce planeta este cunoscuta ca fiind denumita 'Planeta Rosie'?: ":"marte",
    "Care este cel mai populat oras din lume?: ":"tokyo",
    "Ce tara este supranumita 'Tara soarelui rasare'?: ":"japonia",
    "Cati ani a condus Nicolae Ceausescu tara noastra?: ":"24",
    "Care este cel mai lung fluviu din europa?: ":"volga",
    "Cine este autorul operei 'Flautul fermecat': ":"mozart",
    "Carui personaj din opera lui Shakespeare ii apartine expresia 'To be or not to be'?: ":"hamlet",
    "Care este capitala Luxemburgului?: ":"luxemburg",
    "De câte ori a fost căsătorită actrița Angelina Jolie?: ":"3",
    "Care este moneda oficială a Bulgariei?: ":"leva",
    "Ce ţară din America de Sud are cea mai mare suprafaţă?: ":"brazilia",
    "Care este cea mai mare pasăre care trăiește pe Pământ?: ":"strutul",
    "Cine a inventat becul?: ":"thomas edison",
    "Câte strofe are poezia „Luceafărul”, semnată de Mihai Eminescu?: ":"98",
    "Câte continente există pe Pământ?: ":"7",
    "Ce inseamna RIP?: ":"rest in peace",
    "Ce inseamna BRB?: ":"be right back",
    "Ce inseamna WTF?: ":"what the fuck",
    "Ce inseamna AFK?: ":"away from keyboard",
    "Ce inseamna LMAO?: ":"laughing my ass off",
    "Cati ani are Andrei Sirop?: ":"21",
    "In ce limbaj de programare este scris acest joc?: ":"python",
    "Care este densitatea populatiei unei tari cu 1.000.000 locuitori si 1.000.000 km^2 suprafata?(locuitori pe km^2): ":"1",
    "Rezultatul urmatorului calcul: 1+2+(3+4+5)x0 este: ":"3",
    "In ce an s-a scufundat Titanicul?: ":"1912",
    "Cati copii are Traian Basescu?: ":"2",
    "Cine a scris romanul Ion?: ":"liviu rebreanu",
    "Ce rau trece prin Bucuresti?: ":"dambovita",
    "Care este singura echipa de fotbal din Romania care a castigat CUPA CAMPIONILOR EUROPENI?: ":"steaua",
    "Cine a spus „Zarurile au fost aruncate”?:":"caesar",
    "La ce varsta a fost crucificat Iisus Hristos?: ":"33",
    "Pe drapelul carei tari sta scris “Ordine şi progres”?: ":"brazilia",
    "Cine a exclamat „Evrika”?: ":"arhimede",
    "Din ce tara izvoraste Dunarea?: ":"germania",
    "În ce oraș a avut loc Olimpiada unde gimnasta Nadia Comăneci a primit nota 10 pe linie?: ":"montreal",
    "Câte state are Statele Unite ale Americii?: ":"50",
    "Unde s-a născut Ion Creangă?: ":"humulesti",
    "Care este capitala Rusiei?: ":"moscova",
    "Ce personalitate se afla pe bancnota de 1 leu?: ":"nicolae iorga",
    "Ce personalitate se afla pe bancnota de 5 lei?: ":"george enescu",
    "Ce personalitate se afla pe bancnota de 10 lei?: ":"nicolae grigorescu",
    "Ce personalitate se afla pe bancnota de 50 lei?: ":"aurel vlaicu",
    "Ce personalitate se afla pe bancnota de 100 lei?: ":"ion luca caragiale",
    "Ce personalitate se afla pe bancnota de 200 lei?: ":"lucian blaga",
    "Ce personalitate se afla pe bancnota de 500 lei?: ":"mihai eminescu",
    "In ce tara s-a nascut Adolf Hitler?: ":"austria"
    }

money = 0
# winsound.PlaySound("dup", winsound.SND_ASYNC | winsound.SND_ALIAS )
# winsound.PlaySound("dup",winsound.SND_FILENAME)

print("Acesta este un joc de inteligenta!")
print("Nu uita ca este un joc pe bani reali.")
print("Raspunzi corect, castigi un leu.")
print("Raspunzi gresit, pierzi 1 leu.")
print("Scopul este sa ajungi cat mai departe si sa ii iei toti banii lui Andrei!!")
print("Prima intrebare urmeaza in 5 secunde ...")
print("")
time.sleep(3.5)

def moneys(x):
    global money
    money += x
    print("In momentul actual ai {} lei.".format(money))

def intrebare():
    question = random.choice(list(questions.keys()))
    answer = input(question).lower().strip()
    if answer == questions.get(question).lower().strip():
        time.sleep(2)
        # winsound.PlaySound("c", winsound.SND_ASYNC )
        print("")
        print("Ai raspuns corect si ai castigat 1 leu!!")
        moneys(1)
    else:
        time.sleep(2)
        # winsound.PlaySound("w", winsound.SND_ASYNC | winsound.SND_ALIAS )
        print("")
        print("Ai raspuns gresit si ai pierdut 1 leu!!")
        moneys(-1)

def ready():
    global alegeri
    alegeri = ("da","nu")
    pregatit = input("Esti pregatit pentru urmatoarea intrebare?: ")
    while pregatit not in alegeri:
        pregatit = input("Esti pregatit pentru urmatoarea intrebare?: ")
    if pregatit == "da":
        # winsound.PlaySound("n", winsound.SND_ASYNC | winsound.SND_ALIAS)
        print("Ma bucur sa aud asta!")
        print("")
        return True
    elif pregatit == "nu":
        # winsound.PlaySound("e", winsound.SND_ASYNC | winsound.SND_ALIAS )
        return False

# def leave():
  #   leave_game = input("Esti sigur ca vrei sa parasesti jocul cu {} lei?: ".format(money))
   #  while leave_game not in alegeri:
    #     leave_game = input("Esti sigur ca vrei sa parasesti jocul cu {} lei?: ".format(money))
    # if leave_game == "da":
     #    return False
    # elif leave_game == "nu":
     #    ready()


    
while True:
    time.sleep(1.5)
    intrebare()
    if not ready():
        if money < 0:
            money = money * -1
            print("Ai terminat jocul cu o datorie la Andrei de {} lei.".format(money))
        elif money > 0:
            print("Uhh, se pare ca Andrei are o datorie la tine in valoare de {} lei.".format(money))
        else:
            print("Ai fost un jucator neutru, ai terminat pe 0.")
        break

while True:
    pass
    


