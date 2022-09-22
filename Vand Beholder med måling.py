
startafvandmåling = str(input("Vil du måle din Beholder? Ja/Nej:"))

if startafvandmåling == "Ja":
    vandmålingloop = True
    while vandmålingloop:

        # Input Kode, information om vandbeholder.
        beholder = int(input("Indtast Beholderens Størrelse i ml:"))
        brug = int(input("Indtast Forbruget i ml:"))

        # Vandbeholder Funktiont kode
        def vandmåling(beholder, brug):
            tilbage = beholder - brug
            procent = 100 * float(brug)/float(beholder)
            procenttilbage = 100 - procent

            print("")
            print("Beholderens størrelse er:", beholder, "ml")
            print("Brug af vand:", brug, "ml")
            print("Vand der er tilbage:", tilbage, "ml")
            print("procent tilbage:", procenttilbage, "%")
            print("")

            if procenttilbage == 100:
                print("Beholderen er stadig fuld.")
            elif procenttilbage >= 80:
                print("Du har stadig nok til at vande nogle flere planter.")
            elif procenttilbage >= 60:
                print("Du er ca halvvejs igennem beholderen, du kan stadig vande men bør snart genopfylde beholderen.")
            elif procenttilbage >= 40:
                print("Nu skal du snart genopfylde beholderen.")
            elif procenttilbage >= 20:
                print("Beholderen er snart tom.")
            elif procenttilbage >= 0:
                print("Du har en sjat tilbage.")
            elif procenttilbage == 0:
                print("Beholderen er tom.")
                print("Genopfyld Beholderen")

    # Calling af Funktion - vandmåler(beholder, brug)
        vandmåling(beholder, brug)
        print("-------------------------------------------------------")
        break
elif startafvandmåling == "Nej":
    print("")
    print("Lukker Programmet ned.")
    print("-------------------------------------------------------")