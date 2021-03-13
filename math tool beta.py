print("Hello, created by HeaZzY . Good luck ")

Request_coefdir = int(input("Calculer un coef directeur ? 1=oui 2=non : "))

if Request_coefdir == 1:
    coef_dir_type = int(input("C'est une augmentation ? 1=oui 2= non:"))
    if coef_dir_type == 1:
        Pourcent_augment = float(input("augmentation de combien de pourcent ?:"))
        coef_dir_augment = 1 + Pourcent_augment / 100
        print(coef_dir_augment)
    else:
        Pourcent_descendent = float(input("diminution de combien de pourcent ?:"))
        coef_dir_dimin = 1 - Pourcent_descendent / 100
        print(coef_dir_dimin)

else:
    pass


Pourcent_coef_dir = int(input("Calculer avec un coef directeur ? 1=oui 2=non"))

if Pourcent_coef_dir == 1:
    coef_directeur = float(input("coeficient directeur="))
    valeur_initiale = float(input("valeur initiale="))
    Somme_de_tt = valeur_initiale
    Temps = int(input("sur combien de temps ou combien de fois"))
    for i in range(1,Temps + 1):
        valeur_initiale = valeur_initiale * coef_directeur
        Somme_de_tt = Somme_de_tt + valeur_initiale
        print("valeur initiale apres " + str(i ) + "ans,mois,jour,heure..." + str(valeur_initiale))
    print("la valeur de tt apres " + str(Somme_de_tt))

else:
    pass

Requestpourcent2 = int(input("calculer un pourcentage? ou autre sans coef directeur? 1=oui 2=non"))

if Requestpourcent2 == 1:
    Requestpourcent1 = int(input("Calculer un pourcentage? 1 = oui 2 = non"))

    if Requestpourcent1 == 1:

        Effectif_totale = float(input("Effectif_totale="))
        Valeur_partiel = float(input("Valeur_partiel="))
        Pourcent = Valeur_partiel / Effectif_totale * 100
        print(str(Pourcent) + " %" + " tres tres bien jouer")
    else:
        print("pour calculer un nombre avec un pourcentage.")
        pourcentage = float(input("pourcentage="))
        total = float(input("total="))
        Result2 = pourcentage / 100 * total
        print(str(Result2))

else:
    pass
