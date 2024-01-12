
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import DateTime

# overall london average
london_average = 685.1015490533563
# overall wales average
wales_avrage = 705.5084337349397
# overall south average
south_average = 693.9317269076305
# overall West average
west_avrage = 706.5025817555938
# overall south average
middle_average = 691.4530120481927

database = ['James', 'Thomas', 'Cartwright', 'Allison', 'Battle', 'Lennon', 'Benitez', 'Voyle', 'Osman', 'Weir', 'Rhodes', 'Sharples', 'Rees', 'Morgan', 'Malenczyk','Kirby', 'Nunez', 'Sweet', 'Edwards', 'Thomas', 'Bray', 'Alston', 'Wu', 'Penn', 'Storey', 'Miller', 'Allan', 'Travis', 'Clemons']

# indavidual average fore people in london
James = 722.096386
Thomas = 693.108434
Cartwright = 744.120482
Allison = 636.301205
Battle = 691.036145
Lennon = 694.216867
Benitez = 614.831325



# indavidual average fore people in Wales
Voyle = 652
Osman = 758.795181
Weir = 692.987952
Rhodes = 679.397590
Sharples = 744.361446

# indavidual average fore people in South
Rees = 676.518072
Morgan = 769.120482
Malenczyk = 630.807229
Kirby = 624.457831
Nunez = 758.831325
Sweet = 703.855422

# indavidual average fore people in West
Edwards = 679.421687
Thomas = 689.807229
Bray = 708.686747
Alston = 692.879518
Wu = 748.915663
Penn = 759.132530

# indavidual average fore people in West
Storey = 685.566265
Miller = 679.361446
Allan = 725.445783
Travis = 721.289157
Clemons = 645.602410

df = pd.read_csv('Sales Stats.csv')

 # ------------------------------------------------------------------------------------------------------------

# Function to find the avrage of London commision
def london():
    date_London = ['01/01/2021', '02/01/2021', '03/01/2021', '04/01/2021', '05/01/2021',
             '06/01/2021', '07/01/2021', '08/01/2021', '09/01/2021','10/01/2021',
             '11/01/2021', '12/01/2021', '13/01/2021','14/01/2021', '15/01/2021',
             '16/01/2021', '17/01/2021','18/01/2021', '19/01/2021', '20/01/2021',
             '21/01/2021', '22/01/2021','23/01/2021', '24/01/2021', '25/01/2021',
             '26/01/2021','27/01/2021','28/01/2021','29/01/2021','30/01/2021',
             '31/01/2021','01/02/2021','02/02/2021','03/02/2021','04/02/2021',
             '05/02/2021','06/02/2021','07/02/2021','08/02/2021','09/02/2021',
             '10/02/2021', '11/02/2021', '12/02/2021', '13/02/2021', '14/02/2021',
             '15/02/2021', '16/02/2021', '17/02/2021', '18/02/2021', '19/02/2021',
             '20/02/2021', '21/02/2021', '22/02/2021', '23/02/2021', '24/02/2021',
             '25/02/2021', '26/02/2021', '27/02/2021', '28/02/2021', '01/03/2021',
             '02/03/2021', '03/03/2021', '04/03/2021', '05/03/2021', '06/03/2021',
             '07/03/2021', '08/03/2021', '09/03/2021', '10/03/2021', '11/03/2021',
             '12/03/2021','13/03/2021','14/03/2021', '15/03/2021', '16/03/2021',
             '17/03/2021', '18/03/2021', '19/03/2021', '20/03/2021', '21/03/2021',
             '22/03/2021','23/03/2021', '24/03/2021']
    # Creates a new df
    London_sales = df[df['Region'] == 'London'][date_London]
    # Finds the mean
    overall_London_average = London_sales.mean().mean()
    print(overall_London_average)
    london_average = London_sales.mean(axis=1)


def Jamesf():
    if James >= wales_avrage:
        print("Above")
        print("James has " + str(James) + " and his region avrage is " + str(wales_avrage))

    else:
        print("Below")
        print("James has " + str(James) + " and his region avrage is " + str(wales_avrage))


def Thomasf():
    if Thomas >= wales_avrage:
        print("Above")
        print("Thomas has " + str(Thomas) + " and his region avrage is " + str(wales_avrage))

    else:
        print("Below")
        print("Thomas has " + str(Thomas) + " and his region avrage is " +  str(wales_avrage))


def Cartwrightf():
    if Cartwright >= wales_avrage:
        print("Above")
        print("Cartwright has " + str(Cartwright) + " and his region avrage is " + str(wales_avrage))

    else:
        print("Below")
        print("Cartwright has " + str(Cartwright) + " and his region avrage is " + str(wales_avrage))


def Allisonf():
    if Allison >= wales_avrage:
        print("Above")
        print("Allison has " + str(Allison) + " and his region avrage is " + str(wales_avrage))

    else:
        print("Below")
        print("Allison has " + str(Allison) + " and his region avrage is " + str(wales_avrage))

def Battlef():
    if Battle >= wales_avrage:
        print("Above")
        print("Battle has " + str(Battle) + " and his region avrage is " + str(wales_avrage))

    else:
        print("Below")
        print("Battle has " + str(Battle) + " and his region avrage is " + str(wales_avrage))

def Lennonf():
    if Lennon >= wales_avrage:
        print("Above")
        print("Lennon has " + str(Lennon) + " and his region avrage is " + str(wales_avrage))

    else:
        print("Below")
        print("Lennon has " + str(Lennon) + " and his region avrage is " + str(wales_avrage))


def Benitezf():
    if Benitez >= wales_avrage:
        print("Above")
        print("Benitez has " + str(Benitez) + " and his region avrage is " + str(wales_avrage))

    else:
        print("Below")
        print("Benitez has " + str(Benitez) + " ands region avrage is " + str(wales_avrage))


 # ---------------------------------------------------------------------------------------------------------

# Function to find the avrage of Wales commision
def wales():
    date_Wales = ['01/01/2021', '02/01/2021', '03/01/2021', '04/01/2021', '05/01/2021',
             '06/01/2021', '07/01/2021', '08/01/2021', '09/01/2021','10/01/2021',
             '11/01/2021', '12/01/2021', '13/01/2021','14/01/2021', '15/01/2021',
             '16/01/2021', '17/01/2021','18/01/2021', '19/01/2021', '20/01/2021',
             '21/01/2021', '22/01/2021','23/01/2021', '24/01/2021', '25/01/2021',
             '26/01/2021','27/01/2021','28/01/2021','29/01/2021','30/01/2021',
             '31/01/2021','01/02/2021','02/02/2021','03/02/2021','04/02/2021',
             '05/02/2021','06/02/2021','07/02/2021','08/02/2021','09/02/2021',
             '10/02/2021', '11/02/2021', '12/02/2021', '13/02/2021', '14/02/2021',
             '15/02/2021', '16/02/2021', '17/02/2021', '18/02/2021', '19/02/2021',
             '20/02/2021', '21/02/2021', '22/02/2021', '23/02/2021', '24/02/2021',
             '25/02/2021', '26/02/2021', '27/02/2021', '28/02/2021', '01/03/2021',
             '02/03/2021', '03/03/2021', '04/03/2021', '05/03/2021', '06/03/2021',
             '07/03/2021', '08/03/2021', '09/03/2021', '10/03/2021', '11/03/2021',
             '12/03/2021','13/03/2021','14/03/2021', '15/03/2021', '16/03/2021',
             '17/03/2021', '18/03/2021', '19/03/2021', '20/03/2021', '21/03/2021',
             '22/03/2021','23/03/2021', '24/03/2021']
    # Creates a new df
    Wales_sales = df[df['Region'] == 'Wales'][date_Wales]
    # Finds the mean
    overall_Wales_average = Wales_sales.mean().mean()
    print(overall_Wales_average)
    Wales_Avrages = Wales_sales.mean(axis=1)


def Voylef():
    if Voyle >= london_average:
        print("Above")
        print("Voyle has " + str(Voyle) + " and there region average is " + str(london_average))

    else:
        print("Below")
        print("Voyle has " + str(Voyle) + " and there region average is " + str(london_average))

def Osmanf():
    if Osman >= london_average:
        print("Above")
        print("Osman has " + str(Osman) + " and there region average is " + str(london_average))

    else:
        print("Below")
        print("Osman has " + str(Osman) + " and there region average is " + str(london_average))

def Weirf():
    if Weir >= london_average:
        print("Above")
        print("Weir has " + str(Weir) + " and there region average is " + str(london_average))

    else:
        print("Below")
        print("Weir has " + str(Weir) + " and there region average is " + str(london_average))


def Rhodesf():
    if Rhodes >= london_average:
        print("Above")
        print("Rhodes has " + str(Rhodes) + " and there region average is " + str(london_average))


    else:
        print("Below")
        print("Rhodes has " + str(Rhodes) + " and there region average is " + str(london_average))


def Sharplesf():
    if Sharples >= london_average:
        print("Above")
        print("Sharples has " + str(Sharples) + " and there region average is " + str(london_average))


    else:
        print("Below")
        print("Sharples has " + str(Sharples) + " and there region average is " + str(london_average))


# --------------------------------------------------------------------------------------------------------------

# Function to find the avrage of South commision
def south():
    date_South = ['01/01/2021', '02/01/2021', '03/01/2021', '04/01/2021', '05/01/2021',
             '06/01/2021', '07/01/2021', '08/01/2021', '09/01/2021','10/01/2021',
             '11/01/2021', '12/01/2021', '13/01/2021','14/01/2021', '15/01/2021',
             '16/01/2021', '17/01/2021','18/01/2021', '19/01/2021', '20/01/2021',
             '21/01/2021', '22/01/2021','23/01/2021', '24/01/2021', '25/01/2021',
             '26/01/2021','27/01/2021','28/01/2021','29/01/2021','30/01/2021',
             '31/01/2021','01/02/2021','02/02/2021','03/02/2021','04/02/2021',
             '05/02/2021','06/02/2021','07/02/2021','08/02/2021','09/02/2021',
             '10/02/2021', '11/02/2021', '12/02/2021', '13/02/2021', '14/02/2021',
             '15/02/2021', '16/02/2021', '17/02/2021', '18/02/2021', '19/02/2021',
             '20/02/2021', '21/02/2021', '22/02/2021', '23/02/2021', '24/02/2021',
             '25/02/2021', '26/02/2021', '27/02/2021', '28/02/2021', '01/03/2021',
             '02/03/2021', '03/03/2021', '04/03/2021', '05/03/2021', '06/03/2021',
             '07/03/2021', '08/03/2021', '09/03/2021', '10/03/2021', '11/03/2021',
             '12/03/2021','13/03/2021','14/03/2021', '15/03/2021', '16/03/2021',
             '17/03/2021', '18/03/2021', '19/03/2021', '20/03/2021', '21/03/2021',
             '22/03/2021','23/03/2021', '24/03/2021']
    # Creates a new df
    South_sales = df[df['Region'] == 'South-East'][date_South]
    # Finds the mean
    overall_South_average = South_sales.mean().mean()
    print(overall_South_average)
    South_Avrages = South_sales.mean(axis=1)

def Reesf():
    if Rees >= south_average:
        print("Above")
        print("Rees has " + str(Rees) + " and there region average is " + str(south_average))


    else:
        print("Below")
        print("Rees has " + str(Rees) + " and there region average is " + str(south_average))

def Morganf():
    if Morgan >= south_average:
        print("Above")
        print("Morgan has " + str(Morgan) + " and there region average is " + str(south_average))


    else:
        print("Below")
        print("Morgan has " + str(Morgan) + " and there region average is " + str(south_average))


def Mclenczykf():
    if Malenczyk >= south_average:
        print("Above")
        print("Mclenczykf has " + str(Malenczyk) + " and there region average is " + str(south_average))


    else:
        print("Below")
        print("Mclenczykf has " + str(Malenczyk) + " and there region average is " + str(south_average))


def Kirbyf():
    if Kirby >= south_average:
        print("Above")
        print("Kirby has " + str(Malenczyk) + " and there region average is " + str(south_average))


    else:
        print("Below")
        print("Kirby has " + str(Malenczyk) + " and there region average is " + str(south_average))

def Nunezf():
    if Nunez >= south_average:
        print("Above")
        print("Nunez has " + str(Nunez) + " and there region average is " + str(south_average))

    else:
        print("Below")
        print("Nunez has " + str(Nunez) + " and there region average is " + str(south_average))

def Sweetf():
    if Sweet >= south_average:
        print("Above")
        print("Sweet has " + str(Sweet) + " and there region average is " + str(south_average))

    else:
        print("Below")
        print("Sweet has " + str(Sweet) + " and there region average is " + str(south_average))


# --------------------------------------------------------------------------------------------------------------

# Function to find the average of West commision
def west():
    date_West = ['01/01/2021', '02/01/2021', '03/01/2021', '04/01/2021', '05/01/2021',
             '06/01/2021', '07/01/2021', '08/01/2021', '09/01/2021','10/01/2021',
             '11/01/2021', '12/01/2021', '13/01/2021','14/01/2021', '15/01/2021',
             '16/01/2021', '17/01/2021','18/01/2021', '19/01/2021', '20/01/2021',
             '21/01/2021', '22/01/2021','23/01/2021', '24/01/2021', '25/01/2021',
             '26/01/2021','27/01/2021','28/01/2021','29/01/2021','30/01/2021',
             '31/01/2021','01/02/2021','02/02/2021','03/02/2021','04/02/2021',
             '05/02/2021','06/02/2021','07/02/2021','08/02/2021','09/02/2021',
             '10/02/2021', '11/02/2021', '12/02/2021', '13/02/2021', '14/02/2021',
             '15/02/2021', '16/02/2021', '17/02/2021', '18/02/2021', '19/02/2021',
             '20/02/2021', '21/02/2021', '22/02/2021', '23/02/2021', '24/02/2021',
             '25/02/2021', '26/02/2021', '27/02/2021', '28/02/2021', '01/03/2021',
             '02/03/2021', '03/03/2021', '04/03/2021', '05/03/2021', '06/03/2021',
             '07/03/2021', '08/03/2021', '09/03/2021', '10/03/2021', '11/03/2021',
             '12/03/2021','13/03/2021','14/03/2021', '15/03/2021', '16/03/2021',
             '17/03/2021', '18/03/2021', '19/03/2021', '20/03/2021', '21/03/2021',
             '22/03/2021','23/03/2021', '24/03/2021']
    # Creates a new df
    West_sales = df[df['Region'] == 'South-West'][date_West]
    # Finds the mean
    overall_West_average = West_sales.mean().mean()
    print(overall_West_average)
    West_Avrages = West_sales.mean(axis=1)



def Edwardsf():
    if Edwards >= west_avrage:
        print("Above")
        print("Edwards has " + str(Edwards) + " and there region average is " + str(west_avrage))

    else:
        print("Below")
        print("Edwards has " + str(Edwards) + " and there region average is " + str(west_avrage))

def Thomasf():
    if Thomas >= west_avrage:
        print("Above")
        print("Thomas has " + str(Thomas) + " and there region average is " + str(west_avrage))

    else:
        print("Below")
        print("Thomas has " + str(Thomas) + " and there region average is " + str(west_avrage))

def Brayf():
    if Bray >= west_avrage:
        print("Above")
        print("Bray has " + str(Bray) + " and there region average is " + str(west_avrage))


    else:
        print("Below")
        print("Bray has " + str(Bray) + " and there region average is " + str(west_avrage))

def Alstonf():
    if Alston >= west_avrage:
        print("Above")
        print("Alston has " + str(Alston) + " and there region average is " + str(west_avrage))

    else:
        print("Below")
        print("Alston has " + str(Alston) + " and there region average is " + str(west_avrage))


def Wuf():
    if Wu >= west_avrage:
        print("Above")
        print("Wu has " + str(Wu) + " and there region average is " + str(west_avrage))


    else:
        print("Below")
        print("Wu has " + str(Wu) + " and there region average is " + str(west_avrage))

def Pennf():
    if Penn >= west_avrage:
        print("Above")
        print("Penn has " + str(Penn) + " and there region average is " + str(west_avrage))

    else:
        print("Below")
        print("Penn has " + str(Penn) + " and there region average is " + str(west_avrage))


# --------------------------------------------------------------------------------------------------------------

# Function to find the average of Middle commision
def middle():
    date_Middle = ['01/01/2021', '02/01/2021', '03/01/2021', '04/01/2021', '05/01/2021',
             '06/01/2021', '07/01/2021', '08/01/2021', '09/01/2021','10/01/2021',
             '11/01/2021', '12/01/2021', '13/01/2021','14/01/2021', '15/01/2021',
             '16/01/2021', '17/01/2021','18/01/2021', '19/01/2021', '20/01/2021',
             '21/01/2021', '22/01/2021','23/01/2021', '24/01/2021', '25/01/2021',
             '26/01/2021','27/01/2021','28/01/2021','29/01/2021','30/01/2021',
             '31/01/2021','01/02/2021','02/02/2021','03/02/2021','04/02/2021',
             '05/02/2021','06/02/2021','07/02/2021','08/02/2021','09/02/2021',
             '10/02/2021', '11/02/2021', '12/02/2021', '13/02/2021', '14/02/2021',
             '15/02/2021', '16/02/2021', '17/02/2021', '18/02/2021', '19/02/2021',
             '20/02/2021', '21/02/2021', '22/02/2021', '23/02/2021', '24/02/2021',
             '25/02/2021', '26/02/2021', '27/02/2021', '28/02/2021', '01/03/2021',
             '02/03/2021', '03/03/2021', '04/03/2021', '05/03/2021', '06/03/2021',
             '07/03/2021', '08/03/2021', '09/03/2021', '10/03/2021', '11/03/2021',
             '12/03/2021','13/03/2021','14/03/2021', '15/03/2021', '16/03/2021',
             '17/03/2021', '18/03/2021', '19/03/2021', '20/03/2021', '21/03/2021',
             '22/03/2021','23/03/2021', '24/03/2021']
    # Creates a new df
    Middle_sales = df[df['Region'] == 'West-Midlands'][date_Middle]
    # Finds the mean
    overall_Middle_average = Middle_sales.mean().mean()
    print(overall_Middle_average)
    Middle_Avrages = Middle_sales.mean(axis=1)


def Storeyf():
    if Storey >= middle_average:
        print("Above")
        print("Storey has " + str(Storey) + " and there region average is " + str(middle_average))

    else:
        print("Below")
        print("Storey has " + str(Storey) + " and there region average is " + str(middle_average))

def Millerf():
    if Miller >= middle_average:
        print("Above")
        print("Miler has " + str(Storey) + " and there region average is " + str(middle_average))

    else:
        print("Below")
        print("Miler has " + str(Storey) + " and there region average is " + str(middle_average))

def Allanf():
    if Allan >= middle_average:
        print("Above")
        print("Allan has " + str(Allan) + " and there region average is " + str(middle_average))

    else:
        print("Below")
        print("Allan has " + str(Allan) + " and there region average is " + str(middle_average))

def Travisf():
    if Travis >= middle_average:
        print("Above")
        print("Travis has " + str(Travis) + " and there region average is " + str(middle_average))


    else:
        print("Below")
        print("Travis has " + str(Travis) + " and there region average is " + str(middle_average))

def Clemonsf():
    if Clemons >= middle_average:
        print("Above")
        print("Clemons has " + str(Clemons) + " and there region average is " + str(middle_average))

    else:
        print("Below")
        print("Clemons has " + str(Clemons) + " and there region average is " + str(middle_average))


# ---------------------------------------------------------------------------------------------------------------
def month1f():
    month1 = df[['01/01/2021', '02/01/2021', '03/01/2021', '04/01/2021', '05/01/2021',
                 '06/01/2021', '07/01/2021', '08/01/2021', '09/01/2021','10/01/2021',
                 '11/01/2021', '12/01/2021', '13/01/2021','14/01/2021', '15/01/2021',
                 '16/01/2021', '17/01/2021','18/01/2021', '19/01/2021', '20/01/2021',
                 '21/01/2021', '22/01/2021','23/01/2021', '24/01/2021', '25/01/2021',
                 '26/01/2021','27/01/2021','28/01/2021','29/01/2021','30/01/2021',
                 '31/01/2021']]
    df_sum = month1.T[1:30]
    df_sum1 = sum(df_sum)
    print(df_sum1)

def month2f ():
    month2 = df[['01/02/2021','02/02/2021','03/02/2021','04/02/2021',
                 '05/02/2021','06/02/2021','07/02/2021','08/02/2021','09/02/2021',
                 '10/02/2021', '11/02/2021', '12/02/2021', '13/02/2021', '14/02/2021',
                 '15/02/2021', '16/02/2021', '17/02/2021', '18/02/2021', '19/02/2021',
                 '20/02/2021', '21/02/2021', '22/02/2021', '23/02/2021', '24/02/2021',
                 '25/02/2021', '26/02/2021', '27/02/2021', '28/02/2021']]
    df_sum1 = month2.T[1:]
    df_sum2 = sum(df_sum1)
    print(df_sum2)

def month3f():
    month3 = df[['02/03/2021', '03/03/2021', '04/03/2021', '05/03/2021', '06/03/2021',
                 '07/03/2021', '08/03/2021', '09/03/2021', '10/03/2021', '11/03/2021',
                 '12/03/2021','13/03/2021','14/03/2021', '15/03/2021', '16/03/2021',
                 '17/03/2021', '18/03/2021', '19/03/2021', '20/03/2021', '21/03/2021',
                 '22/03/2021','23/03/2021', '24/03/2021']]
    df_sum2 = month3.T[1:]
    df_sum3 = sum(df_sum2)
    print(df_sum3)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

data = {'London':685.10, 'Wales':705.51, 'West-Midlands':691.45,
        'South-West':713.14, 'South-East':693.93}
Regions = list(data.keys())
values = list(data.values())


plt.bar(Regions, values, color='maroon',width=0.4)

plt.xlabel("Regions")
plt.ylabel("Numbers")
plt.title("Average of regions")
plt.show()

data = {'Month1':435, 'Month2':435, 'Month3':435}
Months = list(data.keys())
values = list(data.values())


plt.bar(Months, values, color='maroon',width=0.4)
plt.xlabel("Months")
plt.ylabel("Numbers")
plt.title("Best Performing Months")
plt.show()

def mainmen():
        print("---Main Menue----")
        print("What would you like to look at?")
        Question1 = input("Weather Indivual Salesmen are above or belowe there regons avrage(1), Avrage For each region(2), How each month performs(3): ")

        if Question1 == "1":
            saleschose = input("Pick a salesman: ")


            if saleschose == "James":
                Jamesf()

            elif saleschose == "Thomas":
                Thomasf()

            elif saleschose == "Cartwright":
                Cartwrightf()

            elif saleschose == "Allison":
                Allisonf()

            elif saleschose == "Battle":
                Battlef()

            elif saleschose == "Lennon":
                Lennonf()

            elif saleschose == "Benitez":
                Battlef()

            elif saleschose == "Voyle":
                Voylef()

            elif saleschose == "Osman":
                Osmanf()

            elif saleschose == "Weir":
                Weirf()

            elif saleschose == "Rhodes":
                Rhodesf()

            elif saleschose == "Sharples":
                Sharplesf()

            elif saleschose == "Rees":
                Reesf()

            elif saleschose == "Morgan":
                Morganf()

            elif saleschose == "Malenczyk":
                Mclenczykf()

            elif saleschose == "Kirby":
                Kirbyf()

            elif saleschose == "Nunez":
                Nunezf()

            elif saleschose == "Sweet":
                Sweetf()

            elif saleschose == "Edwards":
                Edwardsf()

            elif saleschose == "Thomas":
                Thomasf()

            elif saleschose == "Bray":
                Brayf()

            elif saleschose == "Alston":
                Alstonf()

            elif saleschose == "Wu":
                Wuf()

            elif saleschose == "Penn":
                Pennf()

            elif saleschose == "Clemons":
                Clemonsf()

            elif saleschose == "Travis":
                Travisf()

            elif saleschose == "Allan":
                Allanf()

            elif saleschose == "Miller":
                Millerf()

            elif saleschose == "Storey":
                Storeyf()

            elif saleschose != database:
                print("Invalid Input Restart Program")

            else:
                print("может быть неэффективно, но это работает (:")

        if Question1 == "2":
            print("London :")
            london()
            print("Wales :")
            wales()
            print("West-Middlands :")
            middle()
            print("South-West :")
            west()
            print("South-East :")
            south()

        if Question1 == "3":
            print("Month 1: ")
            month1f()
            print("Month 2: ")
            month2f()
            print("Month 3: ")
            month3f()

        Question2 = input("Return to Maim Menue? (Y/N): ")

        if Question2 == "Y":
            mainmen()

        else:
            exit()


mainmen()
