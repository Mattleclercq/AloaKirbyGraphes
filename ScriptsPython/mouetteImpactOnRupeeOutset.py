import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def columnAsArrayInt(column):
    list = []
    lineHeader = 2
    actualLine = 0
    with open("ServerExposeGraphes/public/stats.csv", "r") as f:
        for line in f:
            if actualLine < lineHeader :
                actualLine += 1
            else :
                stats = line.split(",")
                value = stats[column]
                if value != "" and value.isnumeric():
                    list.append(int(value))
    return list

def columnAsArrayString(column):
    list = []
    lineHeader = 2
    actualLine = 0
    with open("ServerExposeGraphes/public/stats.csv", "r") as f:
        for line in f:
            if actualLine < lineHeader :
                actualLine += 1
            else :
                stats = line.split(",")
                value = stats[column]
                if value == "":
                    value = "0"
                list.append(value)
    return list

def printGraphe():
    array1 = columnAsArrayString(4)
    array2 = columnAsArrayString(6)
    # Convert array2 to numeric values (if it's not already numeric)
    array2 = pd.to_numeric(array2)

    # Create a DataFrame for easier manipulation
    df = pd.DataFrame({'array1': array1, 'array2': array2})

    # Group by array1 and calculate the mean of array2
    grouped_means = df.groupby('array1')['array2'].mean()

    # Plot the histogram
    ax = grouped_means.plot(kind='bar', color='skyblue')

    # Add labels and title
    plt.xlabel('Nombre de mouettes')
    plt.ylabel('Moyenne du nombre de Rubis après Outset')
    plt.title('Moyenne du nombre de Rubis après Outset par nombre de mouettes')

    plt.savefig('ServerExposeGraphes/public/mouetteImpactOnRupeeOutset.png')

printGraphe()