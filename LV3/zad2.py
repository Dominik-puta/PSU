import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
mtcars = pd.read_csv('mtcars.csv')


#1. Pomoću barplot-a prikažite na istoj slici potrošnju automobila s 4, 6 i 8 cilindara s pandas
mtcars.groupby('cyl')['mpg'].mean().plot(kind='bar')
plt.xlabel('Broj cilindara')
plt.ylabel('Srednja potrošnja (mpg)')
plt.title('Srednja potrošnja automobila s različitim brojem cilindara')
plt.show()


#2. Pomoću boxplot-a prikažite na istoj slici distribuciju težine automobila s 4, 6 i 8 cilindara
mtcars.boxplot(column='wt', by='cyl')
plt.xlabel('Broj cilindara')
plt.ylabel('Težina automobila (wt)')
plt.title('Distribucija težine automobila s različitim brojem cilindara')
plt.suptitle('')
plt.show()
#3. Pomoću odgovarajućeg grafa pokušajte odgovoriti na pitanje imaju li automobili s ručnim mjenjačem veću potrošnju od automobila s automatskim mjenjačem?
mtcars.boxplot(column='mpg', by='am')
plt.xlabel('Vrsta mjenjača (0 = automatski, 1 = ručni)')
plt.ylabel('Potrošnja (mpg)')
plt.title('Potrošnja automobila s različitim vrstama mjenjača')
plt.suptitle('')
plt.show() #Imaju vecu potrosnju od automobila s automatskim mjenjacem
#4. Prikažite na istoj slici odnos ubrzanja i snage automobila za automobile s ručnim odnosno automatskim mjenjačem.
plt.scatter(mtcars[mtcars['am'] == 0]['hp'], mtcars[mtcars['am'] == 0]['qsec'], color='blue', label='Automatski mjenjač')
plt.scatter(mtcars[mtcars['am'] == 1]['hp'], mtcars[mtcars['am'] == 1]['qsec'], color='orange', label='Ručni mjenjač')
plt.xlabel('Snaga (hp)')
plt.ylabel('Ubrzanje (qsec)')
plt.title('Odnos ubrzanja i snage automobila s različitim vrstama mjenjača')
plt.legend()
plt.show()
