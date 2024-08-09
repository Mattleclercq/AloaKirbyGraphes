import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def columnAsArrayInt(column):
    list = []
    with open("ServerExposeGraphes/public/stats.csv", "r") as f:
        for line in f:
            stats = line.split(",")
            value = stats[column]
            if value != "" and value.isnumeric():
                list.append(int(value))
    return list

def columnAsArrayString(column):
    list = []
    with open("ServerExposeGraphes/public/stats.csv", "r") as f:
        for line in f:
            stats = line.split(",")
            value = stats[column]
            if value != "" and value.isnumeric():
                list.append(value)
    return list

def convertSplitToText(splits):
    arrayConverted = []
    for split in splits:
        if split == 1:
            arrayConverted.append("01 - gloooong!")
        elif split == 2:
            arrayConverted.append("02 - FF1")
        elif split ==  3:
            arrayConverted.append("03 - Wind Waker")
        elif split ==  4:
            arrayConverted.append("04 - Bombs")
        elif split ==  5:
            arrayConverted.append("05 - Deku Leaf")
        elif split ==  6:
            arrayConverted.append("06 - Quiver")
        elif split ==  7:
            arrayConverted.append("07- Enter Helmaroc")
        elif split ==  8:
            arrayConverted.append("08 - FF2")
        elif split ==  9:
            arrayConverted.append("09 - Bombs too strong")
        elif split ==  10:
            arrayConverted.append("10 - Light arrows")
        elif split ==  11:
            arrayConverted.append("11 - Puppet Ganon")
        elif split ==  12:
            arrayConverted.append("12 - Morth Hover")
        elif split ==  13:
            arrayConverted.append("13 - Ganondorf")
        elif split ==  14:
            arrayConverted.append("14 - Fini")
    return arrayConverted

def convertReasonResetToText(splits):
    arrayConverted = []
    for split in splits:
        if split == 0:
            arrayConverted.append("Aucune")
        elif split ==  1:
            arrayConverted.append("Autres")
        elif split ==  2:
            arrayConverted.append("Saut raté / tilt")
        elif split ==  3:
            arrayConverted.append("Sploush")
        elif split ==  4:
            arrayConverted.append("Light cycle")
        elif split ==  5:
            arrayConverted.append("Attrapé par Moblin")
        elif split ==  6:
            arrayConverted.append("Perte du Storage")
        elif split ==  7:
            arrayConverted.append("Les cordes")
        elif split ==  8:
            arrayConverted.append("Nuit à mercentile")
        elif split ==  9:
            arrayConverted.append("Door Cancel Early")
        elif split ==  10:
            arrayConverted.append("Door cancel Late")
        elif split ==  11:
            arrayConverted.append("Enter Deku")
        elif split ==  12:
            arrayConverted.append("Les chus")
        elif split ==  13:
            arrayConverted.append("Lip crush")
        elif split ==  14:
            arrayConverted.append("Mauvais set-up Quiver")
        elif split ==  15:
            arrayConverted.append("Super Swim raté")
        elif split ==  16:
            arrayConverted.append("Daronned")
        elif split ==  17:
            arrayConverted.append("Sotage raté")
        elif split ==  18:
            arrayConverted.append("Morth raté")
        elif split ==  19:
            arrayConverted.append("Morth troll")
        elif split ==  20:
            arrayConverted.append("Mort")
    return arrayConverted
    

def printGraphe():
    array1 = convertSplitToText(columnAsArrayInt(5))
    array2 = convertReasonResetToText(columnAsArrayInt(14))
    # Create a DataFrame for easier manipulation
    # Create a DataFrame for easier manipulation
    df = pd.DataFrame({'array1': array1, 'array2': array2})

    # Group by array1 and array2, and then count occurrences
    grouped = df.groupby(['array1', 'array2']).size().unstack(fill_value=0)

    # Define a colormap
    cmap = plt.get_cmap('tab20')  # 'tab20' has 20 distinct colors
    colors = cmap(np.linspace(0, 1, grouped.shape[1]))

    # Plot the histogram with specified colors
    grouped.plot(kind='bar', stacked=True, color=colors)

    # Add labels and title
    plt.xlabel('Split de reset')
    plt.ylabel('Nombre de reset')
    plt.title('Histograme split de reset en fct de raison du reset')

    # Place legend outside of the plot
    plt.legend(title='Raison de reset', bbox_to_anchor=(1.05, 1), loc='upper left')

    # Adjust layout to make room for the legend
    plt.tight_layout(rect=[0, 0, 1, 1])
    plt.savefig('ServerExposeGraphes/public/resetOnReason.png')

printGraphe()