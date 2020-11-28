
# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import time

import numpy as np
import matplotlib.pyplot as plt



file = open('reseau-cyclable.csv','r')
fichier_troncon = csv.DictReader(file, delimiter=';')
print("Analyse des données, veuillez patienter")

liste_releves = []
nombre_piste_by_periode = {
    'before2018': 0,
    'S1_2018': 0,
    'S2_2018': 0,
    'S1_2019': 0,
    'S2_2019': 0,
    'S1_2020': 0,
    'S2_2020': 0,
    'nb_mi_2018': 0,
    'nb_fin_2018': 0,
    'nb_mi_2019': 0,
    'nb_fin_2019': 0,
    'nb_mi_2020': 0,
    'nb_fin_2020': 0,
}

km_piste_by_periode = {
    'before2018': 0,
    'S1_2018': 0,
    'S2_2018': 0,
    'S1_2019': 0,
    'S2_2019': 0,
    'S1_2020': 0,
    'S2_2020': 0,
    'nb_km_mi_2018': 0,
    'nb_km_fin_2018': 0,
    'nb_km_mi_2019': 0,
    'nb_km_fin_2019': 0,
    'nb_km_mi_2020': 0,
    'nb_km_fin_2020': 0,
}


for row in fichier_troncon:
    liste_releves.append({'longueur': float(row['Longueur du troncon en km']),
    'date_troncon' : (row['Date de livraison']),
    })
file.close()

for row in liste_releves:

    # on verifie qu'il existe bien une valeur dans le champ date, si il n'en existe pas on lui attribut la valeur du 01/01/2000
    # Car comme nous l'avons expliqué, nous considérons les pistes non datées comme étant aménagées avant 2018
    if row['date_troncon'] != '':
        date_amenagement = time.strptime(row['date_troncon'], "%d/%m/%Y")
    else:
        date_amenagement = time.strptime('01/01/2000', "%d/%m/%Y")


    # Pour chaque semestre depuis 2018, on répertorie le nombre de troncons aménagés et leurs distance en KM
    if date_amenagement < time.strptime("01/01/2018", "%d/%m/%Y"):
        nombre_piste_by_periode['before2018'] += 1
        km_piste_by_periode['before2018'] += row['longueur']

    elif date_amenagement >= time.strptime("01/01/2018", "%d/%m/%Y") and date_amenagement < time.strptime("01/07/2018", "%d/%m/%Y"):

        nombre_piste_by_periode['S1_2018'] += 1
        km_piste_by_periode['S1_2018'] += row['longueur']

    elif date_amenagement >= time.strptime("01/07/2018", "%d/%m/%Y") and date_amenagement <= time.strptime("31/12/2018", "%d/%m/%Y"):
        nombre_piste_by_periode['S2_2018'] += 1
        km_piste_by_periode['S2_2018'] += row['longueur']


    elif date_amenagement >= time.strptime("01/01/2019", "%d/%m/%Y") and date_amenagement < time.strptime("01/07/2019", "%d/%m/%Y"):
        nombre_piste_by_periode['S1_2019'] += 1
        km_piste_by_periode['S1_2019'] += row['longueur']

    elif date_amenagement >= time.strptime("01/07/2019", "%d/%m/%Y") and date_amenagement <= time.strptime("31/12/2019", "%d/%m/%Y"):
        nombre_piste_by_periode['S2_2019'] += 1
        km_piste_by_periode['S2_2019'] += row['longueur']

    elif date_amenagement >= time.strptime("01/01/2020", "%d/%m/%Y") and date_amenagement < time.strptime("01/07/2020", "%d/%m/%Y"):
        nombre_piste_by_periode['S1_2020'] += 1
        km_piste_by_periode['S1_2020'] += row['longueur']

    elif date_amenagement >= time.strptime("01/07/2020", "%d/%m/%Y"):
        nombre_piste_by_periode['S2_2020'] += 1
        km_piste_by_periode['S2_2020'] += row['longueur']

#on affecte le nombre de piste à la fin de chaque semestre depuis 2018

nombre_piste_by_periode['nb_mi_2018'] = nombre_piste_by_periode['before2018'] + nombre_piste_by_periode['S1_2018']
nombre_piste_by_periode['nb_fin_2018'] = nombre_piste_by_periode['nb_mi_2018'] + nombre_piste_by_periode['S2_2018']
nombre_piste_by_periode['nb_mi_2019'] = nombre_piste_by_periode['nb_fin_2018'] + nombre_piste_by_periode['S1_2019']
nombre_piste_by_periode['nb_fin_2019'] = nombre_piste_by_periode['nb_mi_2019'] + nombre_piste_by_periode['S2_2019']
nombre_piste_by_periode['nb_mi_2020'] = nombre_piste_by_periode['nb_fin_2019'] + nombre_piste_by_periode['S1_2020']
nombre_piste_by_periode['nb_fin_2020'] = nombre_piste_by_periode['nb_mi_2020'] + nombre_piste_by_periode['S2_2020']

#on affecte le nombre de piste à la fin de chaque semestre depuis 2018
km_piste_by_periode['nb_km_mi_2018'] = km_piste_by_periode['before2018'] + km_piste_by_periode['S1_2018']
km_piste_by_periode['nb_km_fin_2018'] = km_piste_by_periode['nb_km_mi_2018'] + km_piste_by_periode['S2_2018']
km_piste_by_periode['nb_km_mi_2019'] = km_piste_by_periode['nb_km_fin_2018'] + km_piste_by_periode['S1_2019']
km_piste_by_periode['nb_km_fin_2019'] = km_piste_by_periode['nb_km_mi_2019'] + km_piste_by_periode['S2_2019']
km_piste_by_periode['nb_km_mi_2020'] = km_piste_by_periode['nb_km_fin_2019'] + km_piste_by_periode['S1_2020']
km_piste_by_periode['nb_km_fin_2020'] = km_piste_by_periode['nb_km_mi_2020'] + km_piste_by_periode['S2_2020']


x = np.array(["debut 2018", "mi 2018", "debut 2019", "mi 2019", "debut 2020","mi 2020", "aujourd'hui"])
y = np.array([
    nombre_piste_by_periode['before2018'],
    nombre_piste_by_periode['nb_mi_2018'],
    nombre_piste_by_periode['nb_fin_2018'],
    nombre_piste_by_periode['nb_mi_2019'],
    nombre_piste_by_periode['nb_fin_2019'],
    nombre_piste_by_periode['nb_mi_2020'],
    nombre_piste_by_periode['nb_fin_2020']
])




#on affecte le nombre de Km de piste à la fin de chaque semestre depuis 2018
x1 = np.array(["debut 2018", "mi 2018", "debut 2019", "mi 2019", "debut 2020","mi 2020", "aujourd'hui"])
y1 = np.array([
    km_piste_by_periode['before2018'],
    km_piste_by_periode['nb_km_mi_2018'],
    km_piste_by_periode['nb_km_fin_2018'],
    km_piste_by_periode['nb_km_mi_2019'],
    km_piste_by_periode['nb_km_fin_2019'],
    km_piste_by_periode['nb_km_mi_2020'],
    km_piste_by_periode['nb_km_fin_2020']
])



#recupération du fichier CSV concernant les comptages de cycliste de l'année 2019
file_comptage_2019 = open('2019_comptage-velo-donnees-compteurs-2.csv','r')
fichier_comptage_2019 = csv.DictReader(file_comptage_2019, delimiter=';')

#creation d'un dictionnaire pour enregistrer les valeurs concernant l'année 2019
comptage_2019 = {
    'janvier': 0,
    'fevrier': 0,
    'mars': 0,
    'avril': 0,
    'mai': 0,
    'juin': 0,
    'juillet': 0,
    'aout': 0,
    'septembre': 0,
    'octobre': 0,
    'novembre': 0,
    'decembre': 0,
    'total': 0,
}
nb = 0
for row in fichier_comptage_2019:

    # on compte sur les compteurs présent avant 2018
    if row["Date d'installation du site de comptage"] <= "2018-01-01":
        nb += 1

        #on compte, pour chaque mois, le nombre de cycliste enregistré par tous les sites de comptages présent avant 2018
        if row['Date et heure de comptage'] >= "2019-01-01" and row['Date et heure de comptage'] < "2019-02-01":
            comptage_2019['janvier'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2019-02-01" and row['Date et heure de comptage'] < "2019-03-01":
            comptage_2019['fevrier'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2019-03-01" and row['Date et heure de comptage'] < "2019-04-01":
            comptage_2019['mars'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2019-04-01" and row['Date et heure de comptage'] < "2019-05-01":
            comptage_2019['avril'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2019-05-01" and row['Date et heure de comptage'] < "2019-06-01":
            comptage_2019['mai'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2019-06-01" and row['Date et heure de comptage'] < "2019-07-01":
            comptage_2019['juin'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2019-07-01" and row['Date et heure de comptage'] < "2019-08-01":
            comptage_2019['juillet'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2019-08-01" and row['Date et heure de comptage'] < "2019-09-01":
            comptage_2019['aout'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2019-09-01" and row['Date et heure de comptage'] < "2019-10-01":
            comptage_2019['septembre'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2019-10-01" and row['Date et heure de comptage'] < "2019-11-01":
            comptage_2019['octobre'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2019-11-01" and row['Date et heure de comptage'] < "2019-12-01":
            comptage_2019['novembre'] += int(row['Comptage horaire'])

        else:
            comptage_2019['decembre'] += int(row['Comptage horaire'])

        comptage_2019['total'] += int(row['Comptage horaire'])




#comptage des données pour 2018

file_comptage_2018 = open('2018_comptage-velo-donnees-compteurs.csv','r')
fichier_comptage_2018 = csv.DictReader(file_comptage_2018, delimiter=';')


comptage_2018 = {
    'janvier': 0,
    'fevrier': 0,
    'mars': 0,
    'avril': 0,
    'mai': 0,
    'juin': 0,
    'juillet': 0,
    'aout': 0,
    'septembre': 0,
    'octobre': 0,
    'novembre': 0,
    'decembre': 0,
    'total': 0,
}
nb2019 = 0
for row in fichier_comptage_2018:

    #on compte sur les compteurs présent avant 2018
    if row["Date d'installation du site de comptage"] <= "2018-01-01":
        nb2019 += 1

        #on compte, pour chaque mois, le nombre de cycliste enregistré par tous les sites de comptages présent avant 2018
        if row['Date et heure de comptage'] >= "2018-01-01" and row['Date et heure de comptage'] < "2018-02-01":
            comptage_2018['janvier'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2018-02-01" and row['Date et heure de comptage'] < "2018-03-01":
            comptage_2018['fevrier'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2018-03-01" and row['Date et heure de comptage'] < "2018-04-01":
            comptage_2018['mars'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2018-04-01" and row['Date et heure de comptage'] < "2018-05-01":
            comptage_2018['avril'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2018-05-01" and row['Date et heure de comptage'] < "2018-06-01":
            comptage_2018['mai'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2018-06-01" and row['Date et heure de comptage'] < "2018-07-01":
            comptage_2018['juin'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2018-07-01" and row['Date et heure de comptage'] < "2018-08-01":
            comptage_2018['juillet'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2018-08-01" and row['Date et heure de comptage'] < "2018-09-01":
            comptage_2018['aout'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2018-09-01" and row['Date et heure de comptage'] < "2018-10-01":
            comptage_2018['septembre'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2018-10-01" and row['Date et heure de comptage'] < "2018-11-01":
            comptage_2018['octobre'] += int(row['Comptage horaire'])

        elif row['Date et heure de comptage'] >= "2018-11-01" and row['Date et heure de comptage'] < "2018-12-01":
            comptage_2018['novembre'] += int(row['Comptage horaire'])

        else:
            comptage_2018['decembre'] += int(row['Comptage horaire'])

        comptage_2018['total'] += int(row['Comptage horaire'])




#comptage des données pour 2020

file_comptage_2020 = open('comptage-velo-donnees-compteurs.csv','r')
fichier_comptage_2020 = csv.DictReader(file_comptage_2020, delimiter=';')

comptage_2020 = {
    'janvier': 0,
    'fevrier': 0,
    'mars': 0,
    'avril': 0,
    'mai': 0,
    'juin': 0,
    'juillet': 0,
    'aout': 0,
    'septembre': 0,
    'octobre': 0,
    'novembre': 0,
    'decembre': 0,
    'total': 0,
}
nb2020 = 0
for row in fichier_comptage_2020:

    #on compte sur les compteurs présent avant 2018
    if row["Date d'installation du site de comptage"] <= "2018-01-01":


        #on compte à partir du 1er janvier 2020 du fait que le fichier soit sur 13 mois glissant
        #les données commencent donc des novembre 2019 que nous avonc déja comptabilisé précédemment
        if row['Date et heure de comptage'] >= "2020-01-01":
            nb2020 += 1
            #on compte, pour chaque mois, le nombre de cycliste enregistré par tous les sites de comptages présent avant 2018
            if row['Date et heure de comptage'] >= "2020-01-01" and row['Date et heure de comptage'] < "2020-02-01":
                comptage_2020['janvier'] += float(row['Comptage horaire'])

            elif row['Date et heure de comptage'] >= "2020-02-01" and row['Date et heure de comptage'] < "2020-03-01":
                comptage_2020['fevrier'] += float(row['Comptage horaire'])

            elif row['Date et heure de comptage'] >= "2020-03-01" and row['Date et heure de comptage'] < "2020-04-01":
                comptage_2020['mars'] += float(row['Comptage horaire'])

            elif row['Date et heure de comptage'] >= "2020-04-01" and row['Date et heure de comptage'] < "2020-05-01":
                comptage_2020['avril'] += float(row['Comptage horaire'])

            elif row['Date et heure de comptage'] >= "2020-05-01" and row['Date et heure de comptage'] < "2020-06-01":
                comptage_2020['mai'] += float(row['Comptage horaire'])

            elif row['Date et heure de comptage'] >= "2020-06-01" and row['Date et heure de comptage'] < "2020-07-01":
                comptage_2020['juin'] += float(row['Comptage horaire'])

            elif row['Date et heure de comptage'] >= "2020-07-01" and row['Date et heure de comptage'] < "2020-08-01":
                comptage_2020['juillet'] += float(row['Comptage horaire'])

            elif row['Date et heure de comptage'] >= "2020-08-01" and row['Date et heure de comptage'] < "2020-09-01":
                comptage_2020['aout'] += float(row['Comptage horaire'])

            elif row['Date et heure de comptage'] >= "2020-09-01" and row['Date et heure de comptage'] < "2020-10-01":
                comptage_2020['septembre'] += float(row['Comptage horaire'])

            elif row['Date et heure de comptage'] >= "2020-10-01" and row['Date et heure de comptage'] < "2020-11-01":
                comptage_2020['octobre'] += float(row['Comptage horaire'])

            elif row['Date et heure de comptage'] >= "2020-11-01" and row['Date et heure de comptage'] < "2020-12-01":
                comptage_2020['novembre'] += float(row['Comptage horaire'])

            else:
                comptage_2020['decembre'] += float(row['Comptage horaire'])

            comptage_2020['total'] += float(row['Comptage horaire'])



#creation du graphique relatant le nombre de cycliste par mois de chaque année
xcomptage = np.array(["Jan", "Fev", "Mars", "Avr", "Mai", "Juin", "Juil", "Aout", "Sept", "Oct", "Nov", "Dec"])
y2018 = np.array([
    comptage_2018['janvier'],
    comptage_2018['fevrier'],
    comptage_2018['mars'],
    comptage_2018['avril'],
    comptage_2018['mai'],
    comptage_2018['juin'],
    comptage_2018['juillet'],
    comptage_2018['aout'],
    comptage_2018['septembre'],
    comptage_2018['octobre'],
    comptage_2018['novembre'],
    comptage_2018['decembre']
])
y2019 = np.array([
    comptage_2019['janvier'],
    comptage_2019['fevrier'],
    comptage_2019['mars'],
    comptage_2019['avril'],
    comptage_2019['mai'],
    comptage_2019['juin'],
    comptage_2019['juillet'],
    comptage_2019['aout'],
    comptage_2019['septembre'],
    comptage_2019['octobre'],
    comptage_2019['novembre'],
    comptage_2019['decembre']
])
y2020 = np.array([
    comptage_2020['janvier'],
    comptage_2020['fevrier'],
    comptage_2020['mars'],
    comptage_2020['avril'],
    comptage_2020['mai'],
    comptage_2020['juin'],
    comptage_2020['juillet'],
    comptage_2020['aout'],
    comptage_2020['septembre'],
    comptage_2020['octobre'],
    comptage_2020['novembre'],
    comptage_2020['decembre']
])


#creation d'un dictionnnaire indiquant le nombre de passage de cycliste par semestre
comptage_trimestre = {
    'T1_2018': comptage_2018['janvier'] + comptage_2018['fevrier'] + comptage_2018['mars'],
    'T2_2018': comptage_2018['avril'] + comptage_2018['mai'] + comptage_2018['juin'],
    'T3_2018': comptage_2018['juillet'] + comptage_2018['aout'] + comptage_2018['septembre'],
    'T4_2018': comptage_2018['octobre'] + comptage_2018['novembre'] + comptage_2018['decembre'],
    'T1_2019': comptage_2019['janvier'] + comptage_2019['fevrier'] + comptage_2019['mars'],
    'T2_2019': comptage_2019['avril'] + comptage_2019['mai'] + comptage_2019['juin'],
    'T3_2019': comptage_2019['juillet'] + comptage_2019['aout'] + comptage_2019['septembre'],
    'T4_2019': comptage_2019['octobre'] + comptage_2019['novembre'] + comptage_2019['decembre'],
    'T1_2020': comptage_2020['janvier'] + comptage_2020['fevrier'] + comptage_2020['mars'],
    'T2_2020': comptage_2020['avril'] + comptage_2020['mai'] + comptage_2020['juin'],
    'T3_2020': comptage_2020['juillet'] + comptage_2020['aout'] + comptage_2020['septembre'],
    'T4_2020': comptage_2020['octobre'] + comptage_2020['novembre'] + comptage_2020['decembre'],
}

# construction du graphe de l'évolution du nombre de km de poste depuis 2018 e
def graphe_evolution_nombre_piste():
    x = np.array(["debut 2018", "mi 2018", "debut 2019", "mi 2019", "debut 2020", "mi 2020", "aujourd'hui"])
    y = np.array([
        nombre_piste_by_periode['before2018'],
        nombre_piste_by_periode['nb_mi_2018'],
        nombre_piste_by_periode['nb_fin_2018'],
        nombre_piste_by_periode['nb_mi_2019'],
        nombre_piste_by_periode['nb_fin_2019'],
        nombre_piste_by_periode['nb_mi_2020'],
        nombre_piste_by_periode['nb_fin_2020']
    ])

    plt.plot(x, y)
    plt.title("Nombre de piste depuis 2018")
    plt.show()


def graphe_evolution_nombre_km_piste():
    # on affecte le nombre de Km de piste à la fin de chaque semestre depuis 2018
    x1 = np.array(["debut 2018", "mi 2018", "debut 2019", "mi 2019", "debut 2020", "mi 2020", "aujourd'hui"])
    y1 = np.array([
        km_piste_by_periode['before2018'],
        km_piste_by_periode['nb_km_mi_2018'],
        km_piste_by_periode['nb_km_fin_2018'],
        km_piste_by_periode['nb_km_mi_2019'],
        km_piste_by_periode['nb_km_fin_2019'],
        km_piste_by_periode['nb_km_mi_2020'],
        km_piste_by_periode['nb_km_fin_2020']
    ])

    plt.plot(x1, y1)
    plt.title("Nombre de km de piste depuis 2018")
    plt.show()



def graphe_cycliste_chaque_annee():
    #creation du graphique relatant le nombre de cycliste par mois de chaque année
    xcomptage = np.array(["Jan", "Fev", "Mars", "Avr", "Mai", "Juin", "Juil", "Aout", "Sept", "Oct", "Nov", "Dec"])
    y2018 = np.array([
        comptage_2018['janvier'],
        comptage_2018['fevrier'],
        comptage_2018['mars'],
        comptage_2018['avril'],
        comptage_2018['mai'],
        comptage_2018['juin'],
        comptage_2018['juillet'],
        comptage_2018['aout'],
        comptage_2018['septembre'],
        comptage_2018['octobre'],
        comptage_2018['novembre'],
        comptage_2018['decembre']
    ])
    y2019 = np.array([
        comptage_2019['janvier'],
        comptage_2019['fevrier'],
        comptage_2019['mars'],
        comptage_2019['avril'],
        comptage_2019['mai'],
        comptage_2019['juin'],
        comptage_2019['juillet'],
        comptage_2019['aout'],
        comptage_2019['septembre'],
        comptage_2019['octobre'],
        comptage_2019['novembre'],
        comptage_2019['decembre']
    ])
    y2020 = np.array([
        comptage_2020['janvier'],
        comptage_2020['fevrier'],
        comptage_2020['mars'],
        comptage_2020['avril'],
        comptage_2020['mai'],
        comptage_2020['juin'],
        comptage_2020['juillet'],
        comptage_2020['aout'],
        comptage_2020['septembre'],
        comptage_2020['octobre'],
        comptage_2020['novembre'],
        comptage_2020['decembre']
    ])

    #traçage des courbes et affichage du graphique
    plt.plot(xcomptage, y2018,"o-", label="2018")
    plt.plot(xcomptage, y2019,"o-", label="2019")
    plt.plot(xcomptage, y2020,"o-", label="2020")
    plt.legend()
    plt.title("Nombre de cycliste par mois")
    plt.show()


def graphe_nombre_cycliste_trimestre():

    #creation des axes du graphique d'évolution du nombre de cycliste
    xtrimestre = np.array(["T1 2018", "T2 2018", "T3 2018", "T4 2018", "T1 2019", "T2 2019", "T3 2019", "T4 2019", "T1 2020", "T2 2020", "T3 2020"])
    ytrimestre = np.array([
        comptage_trimestre['T1_2018'],
        comptage_trimestre['T2_2018'],
        comptage_trimestre['T3_2018'],
        comptage_trimestre['T4_2018'],
        comptage_trimestre['T1_2019'],
        comptage_trimestre['T2_2019'],
        comptage_trimestre['T3_2019'],
        comptage_trimestre['T4_2019'],
        comptage_trimestre['T1_2020'],
        comptage_trimestre['T2_2020'],
        comptage_trimestre['T3_2020']

    ])


    plt.title("Nombre de cycliste par trimestre depuis 2018")
    plt.plot(xtrimestre, ytrimestre)
    ax = plt.subplot()
    ax.xaxis.get_children()[1].set_size(100)
    for label in ax.xaxis.get_ticklabels()[::2]:
           label.set_visible(False)
    plt.show()


def graphe_cycliste_par_nombre_km():
    #creation du graphique du nombre de cycliste en fonction du nombre de km
    xkmpiste = np.array([
        km_piste_by_periode['nb_km_mi_2018'],
        km_piste_by_periode['nb_km_fin_2018'],
        km_piste_by_periode['nb_km_mi_2019'],
        km_piste_by_periode['nb_km_fin_2019'],
        km_piste_by_periode['nb_km_mi_2020']
    ])

    ytrimestre = np.array([
        comptage_trimestre['T1_2018'] + comptage_trimestre['T2_2018'],
        comptage_trimestre['T3_2018'] + comptage_trimestre['T4_2018'],
        comptage_trimestre['T1_2019'] + comptage_trimestre['T2_2019'],
        comptage_trimestre['T3_2019'] + comptage_trimestre['T4_2019'],
        comptage_trimestre['T1_2020'] + comptage_trimestre['T2_2020']
    ])

    plt.scatter(xkmpiste, ytrimestre,  c=['blue', 'blue', 'orange', 'orange', 'green'])
    plt.xlabel("Nombre KM de piste")
    plt.ylabel("Nombre de cyclistes en million")
    plt.title("Evolution nombre de cycliste / KM de piste en semestre")
    plt.show()


#affichage des données importantes comme le nombre de cycliste chaque mois et le total par année et le nombre d'enregistrement étuider pour trouver ces valeurs.
def affichage_nombre_cycliste_2018():
    print("Nombre de cycliste en 2018 par mois pour un total de ", nb, "comptages : ")
    for cle,valeur in comptage_2018.items():
        print(cle , " : ", valeur)
    print("\n")

def affichage_nombre_cycliste_2019():
    print("Nombre de cycliste en 2019 par mois pour un total de ", nb2019, "comptages : ")
    for cle,valeur in comptage_2019.items():
        print(cle , " : ", valeur)
    print("\n")

def affichage_nombre_cycliste_2020():
    print("Nombre de cycliste en 2020 par mois pour un total de ", nb2020, "comptages : ")
    for cle,valeur in comptage_2020.items():
        print(cle , " : ", valeur)

def commande():
    print("1 = Graphique du nombre de piste \n"
          "2 = Graphique du nombre de km de piste\n"
          "3 = Graphique du nombre de cycliste par trimestre \n"
          "4 = Graphique du nombre de cycliste en fonction du nombre de km de piste\n"
          "5 = Graphique du nombre de cycliste par mois sur les 3 années\n"
          "6 = Valeur nombre de cycliste en 2018\n"
          "7 = Valeur nombre de cycliste en 2019\n"
          "8 = Valeur nombre de cycliste en 2020\n"
          "exit =  Quitter l'application\n"
          )


print("Analyse terminée")
choix = ""
while choix != "exit":

    print("Choisissez ce que vous voulez faire, faites 'commande' pour connaitre les commandes de l'application")
    choix = input()

    if choix == 'commande':
        commande()
    elif choix == "1":
        graphe_evolution_nombre_piste()
    elif choix == "2":
        graphe_evolution_nombre_km_piste()
    elif choix == "3":
        graphe_nombre_cycliste_trimestre()
    elif choix == "4":
        graphe_cycliste_par_nombre_km()
    elif choix == "5":
        graphe_cycliste_chaque_annee()
    elif choix == "6":
        affichage_nombre_cycliste_2018()
    elif choix == "7":
        affichage_nombre_cycliste_2019()
    elif choix == "8":
        affichage_nombre_cycliste_2020()
    elif choix == "exit":
        exit()
    else:
        print("Cette commande n'existe pas")


