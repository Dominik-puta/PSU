import pandas as pd
import numpy as np
mtcars = pd.read_csv('mtcars.csv')
#print(len(mtcars))
#print(mtcars)
#print(mtcars.head(5))
#print(mtcars.tail(3))
#print(mtcars.info())
#print(mtcars.describe())


#1. Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)
print("1.--------------------------------------------------------------------------------------------")
print(mtcars.sort_values(by='mpg', ascending=False).head(5))

#Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
print("2.--------------------------------------------------------------------------------------------")
print(mtcars[mtcars['cyl'] == 8].sort_values(by='mpg', ascending=False).head(3))

#3. Kolika je srednja potrošnja automobila sa 6 cilindara?
print("3.--------------------------------------------------------------------------------------------")
print(mtcars[mtcars['cyl'] == 6]['mpg'].mean())

#4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
print("4.--------------------------------------------------------------------------------------------")
print(mtcars[(mtcars['cyl'] == 4) & (mtcars['wt'] >= 1) & (mtcars['wt'] <= 2.2)]['mpg'].mean())

#5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
print("5.--------------------------------------------------------------------------------------------")
print(mtcars[mtcars['am'] == 0].shape[0]) 
print(mtcars[mtcars['am'] == 1].shape[0]) 

#6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?
print("6.--------------------------------------------------------------------------------------------")
print(mtcars[(mtcars['am'] == 0) & (mtcars['hp'] > 100)].shape[0])

#7. Kolika je masa svakog automobila u kilogramima?
print("7.--------------------------------------------------------------------------------------------")
mtcars['wt'] = mtcars['wt'] * 1000 * 0.453592
print(mtcars['wt'])
