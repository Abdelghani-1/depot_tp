import os
import pickle
import numpy as np

os.chdir("\\Users\\roubaabd\\Documents\\TP5\\")

dico={'R101':10,'R102':10,'R103':10,'R104':10,'R105':10,'R106':10,'R107':10,'R108':10,'R109':10,
    'R110':10,'R111':10,'R112':10,'R113':10,'R114':10,'R115':10,'SAE11':10,'SAE12':10,'SAE13':10,
    'SAE14':10,'SAE15':10,'SAE16':10}

with open('donnees',"wb") as fichier:
    pickle.dump(dico, fichier)

with open('donnees',"rb") as fichier:
    notes = pickle.load(fichier)

coef_ue1={
    'R101':10,'R102':10,'R103':12,'R104':10,'R105':0,'R106':5,'R107':0,'R108':6,'R109':0,
    'R110':5,'R111':4,'R112':2,'R113':5,'R114':5,'R115':0,'SAE11':20,'SAE12':20,'SAE13':0,
    'SAE14':0,'SAE15':0,'SAE16':7,
}
coef_ue2={
    'R101':4,'R102':0,'R103':2,'R104':8,'R105':6,'R106':0,'R107':0,'R108':0,'R109':0,
    'R110':5,'R111':5,'R112':2,'R113':9,'R114':9,'R115':3,'SAE11':0,'SAE12':0,'SAE13':29,
    'SAE14':0,'SAE15':0,'SAE16':7,
}
coef_ue3={
    'R101':4,'R102':0,'R103':2,'R104':0,'R105':0,'R106':5,'R107':15,'R108':6,'R109':4,
    'R110':5,'R111':5,'R112':2,'R113':0,'R114':0,'R115':3,'SAE11':0,'SAE12':0,'SAE13':0,
    'SAE14':20,'SAE15':20,'SAE16':7,
}

moyenne = np.average(list(notes.values()), weights=list(coef_ue1.values()))
print('Moyenne semestre:', round(moyenne, 2)) 