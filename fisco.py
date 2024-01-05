import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
a=list(range(0, 85001, 8000))
autonomo = pd.DataFrame({'fatturato autonomo': a})
autonomo['imponibile contributivo']=autonomo['fatturato autonomo']*0.78
autonomo['contributi']=autonomo['imponibile contributivo']*0.2623
autonomo['imponibile fiscale'] = autonomo['imponibile contributivo']-autonomo['contributi']
autonomo['imposte 15%']=autonomo['imponibile fiscale']*0.15
autonomo['netto']=autonomo['fatturato autonomo']-autonomo['contributi']-autonomo['imposte 15%']
autonomo
larghezza_barre = 0.2  # Imposta la larghezza delle barre

plt.bar(autonomo.index - larghezza_barre, autonomo['netto'], color='green', width=larghezza_barre, label='Netto')
plt.bar(autonomo.index, autonomo['imposte 15%'], color='red', width=larghezza_barre, label='Imposte 15%')
plt.bar(autonomo.index + larghezza_barre, autonomo['contributi'], color='blue', width=larghezza_barre, label='Contributi')
plt.xticks(range(len(autonomo['fatturato autonomo'])),autonomo['fatturato autonomo']/1000)
# Aggiunta di etichette
plt.xlabel('Fatturato in migliaia di Euro')
plt.ylabel('Euro')
plt.title('Grafico Netto, Imposte e Contributi per Lavoratore Autonomo - Forfettario')
plt.legend()
plt.show()

a=list(range(0, 85001, 8000))
dipendente = pd.DataFrame({'Costo dipendente': a})

# Definisci la funzione per calcolare le imposte in base alle aliquote
def calcola_imposte(reddito):
    if reddito <= 15000:
        return reddito * 0.23
    elif 15001 <= reddito <= 28000:
        return 3450 + (reddito - 15000) * 0.25
    else:
        return 3450 + 3250 + (reddito - 28000) * 0.45

def calcola_sgravio(imponibile):
  if imponibile<25001:
    return imponibile*0.07
  elif imponibile<35001:
    return imponibile*0.06
  else:
    return 0


def calcola_detrazione_lavoro_dipendente(reddito_complessivo):
    if reddito_complessivo <= 15000:
        detrazione = max(1880, 690)
    elif 15000 < reddito_complessivo <= 28000:
        detrazione = 1910 + 1190 * ((28000 - reddito_complessivo) / 13000)
    elif 28000 < reddito_complessivo <= 50000:
        detrazione = 1910 * ((50000 - reddito_complessivo) / 22000)
    else:
        detrazione = 0  # Nessuna detrazione oltre i 50000 euro

    return detrazione


dipendente['RAL']=dipendente['Costo dipendente']/1.22
dipendente['sgravio contributivo']=dipendente['RAL'].apply(calcola_sgravio)
dipendente['contributi']=dipendente['RAL']*0.11-dipendente['sgravio contributivo']


dipendente['imponibile fiscale'] = dipendente['RAL']-dipendente['contributi']

dipendente['imposte']=dipendente['imponibile fiscale'].apply(calcola_imposte)- dipendente['imponibile fiscale'].apply(calcola_detrazione_lavoro_dipendente)
dipendente['netto']=dipendente['RAL']-dipendente['contributi']-dipendente['imposte']
dipendente

larghezza_barre = 0.2  # Imposta la larghezza delle barre

plt.bar(dipendente.index - larghezza_barre, dipendente['netto'], color='green', width=larghezza_barre, label='Netto')
plt.bar(dipendente.index, dipendente['imposte'], color='red', width=larghezza_barre, label='Imposte - IRPEF')
plt.bar(dipendente.index + larghezza_barre, dipendente['contributi'], color='blue', width=larghezza_barre, label='Contributi')
plt.xticks(range(len(dipendente['Costo dipendente'])),dipendente['Costo dipendente']/1000)
# Aggiunta di etichette
plt.xlabel('Costo dipendente in migliaia di Euro')
plt.ylabel('Euro')
plt.title('Grafico Netto, Imposte e Contributi per Lavoratore dipendente')
plt.legend()
plt.show()


a=list(range(0, 85001, 8000))
ordinario = pd.DataFrame({'fatturato ordinario': a})

def calcola_detrazione_lavoro_autonomo(reddito):
    if reddito <= 5500:
        detrazione = 1265
    elif 5500.01 <= reddito <= 28000:
        detrazione = 500 + (765 * ((28000 - reddito) / 22500))
    elif 28000.01 <= reddito <= 50000:
        detrazione = 500 * ((50000 - reddito) / 22000)
    else:
        detrazione = 0  # Nessuna detrazione oltre i 50000 euro

    return detrazione


ordinario['costi']=ordinario['fatturato ordinario']*0.22
ordinario['imponibile contributivo']=ordinario['fatturato ordinario']-ordinario['costi']
ordinario['contributi']=ordinario['imponibile contributivo']*0.2623

ordinario['imponibile fiscale'] = ordinario['imponibile contributivo']-ordinario['contributi']
ordinario['detrazione lav autonomo']=ordinario['imponibile fiscale'].apply(calcola_detrazione_lavoro_autonomo)
ordinario['imposte']=ordinario['imponibile fiscale'].apply(calcola_imposte)-ordinario['detrazione lav autonomo']
ordinario['netto']=ordinario['fatturato ordinario']-ordinario['contributi']-ordinario['imposte']
ordinario


larghezza_barre = 0.2  # Imposta la larghezza delle barre

plt.bar(ordinario.index - larghezza_barre, ordinario['netto'], color='green', width=larghezza_barre, label='Netto')
plt.bar(ordinario.index, ordinario['imposte'], color='red', width=larghezza_barre, label='Imposte - IRPEF')
plt.bar(ordinario.index + larghezza_barre, ordinario['contributi'], color='blue', width=larghezza_barre, label='Contributi')
plt.xticks(range(len(ordinario['fatturato ordinario'])),ordinario['fatturato ordinario']/1000)
# Aggiunta di etichette
plt.xlabel('Fatturato in migliaia di Euro')
plt.ylabel('Euro')
plt.title('Grafico Netto, Imposte e Contributi per Lavoratore autonomo regime ordinario')
plt.legend()
plt.show()


larghezza_barre = 0.2  # Imposta la larghezza delle barre

plt.bar(ordinario.index - larghezza_barre, ordinario['netto'], color='green', width=larghezza_barre, label='Netto ordinario')
plt.bar(ordinario.index , autonomo['netto'], color='blue', width=larghezza_barre, label='Netto forfettario')
plt.bar(ordinario.index + larghezza_barre, dipendente['netto'], color='red', width=larghezza_barre, label='Netto dipendente')


plt.xticks(range(len(ordinario['fatturato ordinario'])),ordinario['fatturato ordinario']/1000)
# Aggiunta di etichette
plt.xlabel('Fatturato/Costo in migliaia di Euro')
plt.ylabel('Euro')
plt.title('Confronto Netto fra Regime ordinario, autonomo e dipendente')
plt.legend()
plt.show()
