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
        match split:
            case 1:
                arrayConverted.append("01 - gloooong!")
            case 2:
                arrayConverted.append("02 - FF1")
            case 3:
                arrayConverted.append("03 - Wind Waker")
            case 4:
                arrayConverted.append("04 - Bombs")
            case 5:
                arrayConverted.append("05 - Deku Leaf")
            case 6:
                arrayConverted.append("06 - Quiver")
            case 7:
                arrayConverted.append("07- Enter Helmaroc")
            case 8:
                arrayConverted.append("08 - FF2")
            case 9:
                arrayConverted.append("09 - Bombs too strong")
            case 10:
                arrayConverted.append("10 - Light arrows")
            case 11:
                arrayConverted.append("11 - Puppet Ganon")
            case 12:
                arrayConverted.append("12 - Morth Hover")
            case 13:
                arrayConverted.append("13 - Ganondorf")
            case 14:
                arrayConverted.append("14 - Fini")
    return arrayConverted

def convertReasonResetToText(splits):
    arrayConverted = []
    for split in splits:
        match split:
            case 0:
                arrayConverted.append("Aucune")
            case 1:
                arrayConverted.append("Autres")
            case 2:
                arrayConverted.append("Saut raté / tilt")
            case 3:
                arrayConverted.append("Sploush")
            case 4:
                arrayConverted.append("Light cycle")
            case 5:
                arrayConverted.append("Attrapé par Moblin")
            case 6:
                arrayConverted.append("Perte du Storage")
            case 7:
                arrayConverted.append("Les cordes")
            case 8:
                arrayConverted.append("Nuit à mercentile")
            case 9:
                arrayConverted.append("Door Cancel Early")
            case 10:
                arrayConverted.append("Door cancel Late")
            case 11:
                arrayConverted.append("Enter Deku")
            case 12:
                arrayConverted.append("Les chus")
            case 13:
                arrayConverted.append("Lip crush")
            case 14:
                arrayConverted.append("Mauvais set-up Quiver")
            case 15:
                arrayConverted.append("Super Swim raté")
            case 16:
                arrayConverted.append("Daronned")
            case 17:
                arrayConverted.append("Sotage raté")
            case 18:
                arrayConverted.append("Morth raté")
            case 19:
                arrayConverted.append("Morth troll")
            case 20:
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