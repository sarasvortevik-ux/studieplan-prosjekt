
# Lister for emner
emnekoder = []       # inneholder emnekodene, f.eks. "MAT100"
semestre = []        # inneholder om emnet undervises i "høst" eller "vår"
studiepoeng = []     # inneholder antall studiepoeng for hvert emne

# Studieplan med 6 semestre (hver er en liste med indekser til emner)
studieplan = [[] for _ in range(6)]  # oppretter 6 tomme lister

#funksjoner

def lag_nytt_emne():  # funksjon for å lage et nytt emne
    kode = input("Skriv emnekode: ").strip()  # leser emnekode
    semester = input("Undervises i (høst/vår): ").strip().lower()  # leser semester
    poeng = int(input("Antall studiepoeng: "))  # leser studiepoeng som heltall

    emnekoder.append(kode)  # legger emnekoden i lista
    semestre.append(semester)  # legger semesteret i lista
    studiepoeng.append(poeng)  # legger studiepoengene i lista

    print("Emne lagt til.")

def legg_til_emne_i_studieplan():  # funksjon for å legge emne til studieplan
    print("Tilgjengelige emner:")  # skriver ut alle emner
    for i, kode in enumerate(emnekoder):  # går gjennom alle registrerte emner
        print(i, kode, semestre[i], studiepoeng[i], "sp")  # viser info med indeks

    indeks = int(input("Velg emne (skriv nummer): "))  # velger hvilket emne (via indeks)
    sem_nr = int(input("Legg til i semester (1–6): ")) - 1  # velger hvilket semester (0–5)

    # sjekk at emnet ikke allerede finnes i planen
    for s in studieplan:
        if indeks in s:
            print("Emnet er allerede lagt til i studieplanen.")
            return  # avslutter funksjonen

    # sjekk at semesteret passer med sesongen
    if semestre[indeks] == "høst" and sem_nr not in [0, 2, 4]:
        print("Høstemner kan bare legges i semester 1, 3 eller 5.")
        return
    if semestre[indeks] == "vår" and sem_nr not in [1, 3, 5]:
        print("Våremner kan bare legges i semester 2, 4 eller 6.")
        return

    # sjekk at det ikke overstiger 30 studiepoeng
    total = 0  # teller totale studiepoeng i semesteret
    for i in studieplan[sem_nr]:
        total += studiepoeng[i]  # legger sammen poeng for emner i semesteret
    if total + studiepoeng[indeks] > 30:
        print("Ikke plass i semesteret (maks 30 studiepoeng).")
        return

    # hvis alt er gyldig, legg til emnet
    studieplan[sem_nr].append(indeks)
    print("Emne lagt til i semester", sem_nr + 1)

def skriv_ut_emner():  # funksjon som viser alle emner
    print("Registrerte emner:")
    for i, kode in enumerate(emnekoder):
        print(kode, semestre[i], studiepoeng[i], "sp")

def skriv_ut_studieplan():  # funksjon som viser hele studieplanen
    print("Studieplan:")
    for i, sem in enumerate(studieplan):  # går gjennom hvert semester
        print("Semester", i + 1, ":")
        if len(sem) == 0:
            print("  Ingen emner.")
        else:
            for idx in sem:  # går gjennom emnene i semesteret
                print(" ", emnekoder[idx], studiepoeng[idx], "sp")
        print()

def sjekk_gyldighet():  # funksjon for å sjekke om studieplanen er gyldig
    gyldig = True  # antar at planen er gyldig til å begynne med
    for i, sem in enumerate(studieplan):
        total = 0
        for j in sem:
            total += studiepoeng[j]  # teller opp totale studiepoeng i semesteret
        if total != 30:
            print("Semester", i + 1, "har", total, "studiepoeng (ikke gyldig).")
            gyldig = False
    if gyldig:
        print("Studieplanen er gyldig (alle semestre har 30 studiepoeng).")

def lagre_til_fil():  # funksjon som lagrer alt til fil
    with open("emner.txt", "w") as f:  # åpner fil for skriving
        for i in range(len(emnekoder)):
            f.write(emnekoder[i] + "," + semestre[i] + "," + str(studiepoeng[i]) + "\n")

    with open("studieplan.txt", "w") as f:
        for sem in studieplan:
            linje = ",".join(str(i) for i in sem)  # gjør om tall til tekst
            f.write(linje + "\n")
    print("Data lagret til fil.")

def les_fra_fil():  # funksjon som leser inn filer
    emnekoder.clear()
    semestre.clear()
    studiepoeng.clear()

    with open("emner.txt") as f:
        for linje in f:
            kode, sem, sp = linje.strip().split(",")
            emnekoder.append(kode)
            semestre.append(sem)
            studiepoeng.append(int(sp))

    studieplan.clear()
    with open("studieplan.txt") as f:
        for linje in f:
            if linje.strip() == "":
                studieplan.append([])  # tomt semester
            else:
                indekser = [int(i) for i in linje.strip().split(",")]
                studieplan.append(indekser)
    print("Data lest inn fra fil.")

#meny
while True:  # hovedmeny som kjører helt til brukeren avslutter
    print()
    print("1. Lag et nytt emne")
    print("2. Legg til et emne i studieplanen")
    print("3. Skriv ut alle registrerte emner")
    print("4. Skriv ut studieplanen")
    print("5. Sjekk om studieplanen er gyldig")
    print("6. Lagre emner og studieplan til fil")
    print("7. Les inn emner og studieplan fra fil")
    print("8. Avslutt")

    valg = input("Velg: ")

    if valg == "1":
        lag_nytt_emne()
    elif valg == "2":
        legg_til_emne_i_studieplan()
    elif valg == "3":
        skriv_ut_emner()
    elif valg == "4":
        skriv_ut_studieplan()
    elif valg == "5":
        sjekk_gyldighet()
    elif valg == "6":
        lagre_til_fil()
    elif valg == "7":
        les_fra_fil()
    elif valg == "8":
        print("Avslutter programmet.")
        break
    else:
        print("Ugyldig valg, prøv igjen.")
