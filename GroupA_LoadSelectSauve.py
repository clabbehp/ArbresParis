#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      klab
#
# Created:     11/06/2019
# Copyright:   (c) klab 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
# librairie pandas
import pandas
import csv
import numpy as np

print('télécharge le fichier "les-arbres.csv" avec selection des colonnes utilisable pour l’analyse du client')
df = pandas.read_csv("C:\data\BigData_ViaPython\les-arbres.csv",
    usecols = ['IDBASE','ARRONDISSEMENT','DOMANIALITE','LIBELLEFRANCAIS','HAUTEUR (m)','geo_point_2d'],
    dtype = {'IDBASE': int,'HAUTEUR (m)': int},
    sep=';')

#change le nom de l'entete afin de supprimer les caracteres non autorisés
df.rename(columns={'HAUTEUR (m)': 'HAUTEUR_m'}, inplace=True)

# sauve le nouveau fichier en csv sur le PC
print('**** sauve le nouveau fichier en csv ****')
df.to_csv(r'C:\data\BigData_ViaPython\Datas_arbres.csv',
    index = None, header=True, encoding = 'iso-8859-1',
    sep=';')
print('telechargement effectué et sauvegarde sur le PC effectuée')

#reponse aux questions :
print("**** creation d'un dictionnaire avec les arrondissement de Paris **** ")
Adrt=['PARIS 10E ARRDT','PARIS 11E ARRDT','PARIS 12E ARRDT','PARIS 13E ARRDT','PARIS 14E ARRDT','PARIS 15E ARRDT','PARIS 16E ARRDT',
    'PARIS 17E ARRDT','PARIS 18E ARRDT','PARIS 19E ARRDT','PARIS 1ER ARRDT','PARIS 20E ARRDT','PARIS 2E ARRDT','PARIS 3E ARRDT',
    'PARIS 4E ARRDT','PARIS 5E ARRDT','PARIS 6E ARRDT','PARIS 7E ARRDT','PARIS 8E ARRDT','PARIS 9E ARRDT']

# creation d'une liste avec les arrondissments de paris uniquement
listParis=df.loc[df['ARRONDISSEMENT'].isin(Adrt),:]

#creation d'un pivot pour afficher arrondissement x Hauteur_m (TCD)
pivot=(listParis.pivot_table(index=['ARRONDISSEMENT'],values=['HAUTEUR_m'],aggfunc='count'))

# tri du resultat
result=pivot.sort_values('HAUTEUR_m', ascending=False)
print("Dans quel arrondissement de Paris se trouvent le plus grand nombre d'arbres?",result[0:1])

#creation d'un pivot pour afficher arrondissement x Hauteur_m (TCD)
pivot=(listParis.pivot_table(index=['ARRONDISSEMENT'],values=['HAUTEUR_m'],aggfunc='count'))

# tri du resultat
result=pivot.sort_values('HAUTEUR_m', ascending=True)
print("Dans quel arrondissement de Paris se trouvent le moins grand nombre d'arbres?",result[0:1])

