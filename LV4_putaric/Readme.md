Zadatak 2
    U primjeru 4.2, osim što se koristi linearna regresija, model se proširuje korištenjem polinomskih značajki. To omogućava modelu da se prilagodi složenijim, nelinearnim obrascima podataka. U ovom primjeru se koristi polinomski model s 15. stupnjem.
Zadatak 3.
    Funkcija bude puno manje preciznija i podaci bude vise raštrkani ako ima malo ulaznih podataka, ako povećamo na više onda bliže aproksimiraju, pogotovo na 6 stupanj, ali puno dulje traje.
Zadatak 4.
    Data columns (total 12 columns):
     #   Column         Non-Null Count  Dtype  
        ---  ------         --------------  -----  
        0   name           6699 non-null   str    
        1   year           6699 non-null   int64  
        2   selling_price  6699 non-null   float64
        3   km_driven      6699 non-null   int64  
        4   fuel           6699 non-null   str    
        5   seller_type    6699 non-null   str    
        6   transmission   6699 non-null   str    
        7   owner          6699 non-null   str    
        8   mileage        6699 non-null   float64
        9   engine         6699 non-null   int64  
        10  max_power      6699 non-null   float64
        11  seats          6699 non-null   int64  
    Broj automobila proizvedenih 2012. godine: 575
Najčešći broj sjedala: 5
Automobil s najviše prijeđenih kilometara:
name             Maruti Wagon R LXI Minor
year                                 2010
selling_price                   12.175613
km_driven                          577414
fuel                               Petrol
seller_type                    Individual
transmission                       Manual
owner                        Second Owner
mileage                              18.9
engine                               1061
max_power                            67.0
seats                                   5
Name: 3067, dtype: object

Automobil s najmanje prijeđenih kilometara:
name             Maruti Eeco 5 STR With AC Plus HTR CNG
year                                               2011
selling_price                                  12.25009
km_driven                                             1
fuel                                                CNG
seller_type                                  Individual
transmission                                     Manual
owner                              Fourth & Above Owner
mileage                                            15.1
engine                                             1196
max_power                                          73.0
seats                                                 5
Name: 6514, dtype: object
Automobil s najvećom cijenom:
name             BMW X7 xDrive 30d DPE
year                              2020
selling_price                15.789592
km_driven                         5000
fuel                            Diesel
seller_type                 Individual
transmission                 Automatic
owner                      First Owner
mileage                          13.38
engine                            2993
max_power                        265.0
seats                                7
Name: 2591, dtype: object

Automobil s najmanjom cijenom:
name             Maruti 800 AC
year                      1997
selling_price        10.308919
km_driven                80000
fuel                    Petrol
seller_type         Individual
transmission            Manual
owner              Third Owner
mileage                   16.1
engine                     796
max_power                 37.0
seats                        4

Zadatak 6
prije kategoričkih varijabli 
Intercept: 9.565445188275561
Koeficijenti: [ 2.92625284 -0.30288254  0.57686021  1.08113747  2.57814168  0.32597065]
Evaluacija modela na trening skupu:
MAE (trening): 0.23559096921567996
MSE (trening): 0.09454327560980028
R2 (trening): 0.8342812231106719
Max Error (trening): 1.624906981177702

Evaluacija modela na test skupu:
MAE (test): 0.223886039752091
MSE (test): 0.08805752118653745
R2 (test): 0.8301986054506745
Max Error (test): 1.8057341698829852

Poslije kategoričkih varijabli

Intercept: 10.007839347764989
Koeficijenti: [ 2.81227099 -0.29616584  0.31196985  0.75631354  2.33303666  0.33054597
  0.21899472  0.22044934  0.07540382 -0.08512718  0.03874456 -0.16141644
 -0.13713156 -0.07661033  0.70508164 -0.11381192]
Evaluacija modela na trening skupu:
MAE (trening): 0.2270410147842479
MSE (trening): 0.08796228901257909
R2 (trening): 0.8458166077541833
Max Error (trening): 1.7218601250517835

Evaluacija modela na test skupu:
MAE (test): 0.21945411990682354
MSE (test): 0.08411994938757068
R2 (test): 0.8377914285689441
Max Error (test): 1.8030054805171147