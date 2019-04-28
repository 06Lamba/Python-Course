# Question 1
pl1CSV = './MPHYG001_files/python_language_1/python_language_1_data.csv'

import numpy as np
import os
import json
import matplotlib.pyplot as plt
import math


def csv2json(csvName):
  pl1Data = open(csvName)

  station = np.genfromtxt(pl1Data, delimiter=',',
                            names=['year','day','rainfall'],
                            dtype=[int, int, float])                        

  the_dict = {}

  for i in station[1:]:
    year,day,rain = tuple(i)
    if str(year) not in the_dict.keys():
      the_dict[str(year)] = []

    the_dict[str(year)].append(rain)

  with open('myFile.json', 'w') as fp:
      json.dump(the_dict, fp)


csv2json(pl1CSV)

def plotData(fileName,year,col='b'):
  with open(fileName, 'r') as f:
    myData = json.loads(f.read())
  #print(myData[str(year)])
  y = myData[str(year)]
  x = range(1, len(y)+1)
  plt.plot(x,y,col)
  plt.xlabel('day of year')
  plt.ylabel('rainfall (mm/day)')
  plt.show()
  plt.savefig('year.png')

def plotMeanData(fileName,start,finish):
  with open(fileName, 'r') as f:
    myData = json.loads(f.read())
  x = range(start, finish+1)
  y = []
  for key in x:
    rain = myData[str(key)]
    y.append(np.mean(rain))
  plt.plot(x,y)
  plt.xlabel('year')
  plt.ylabel('mean rainfall (mm/day)')
  plt.show()
  plt.savefig('years.png')

def cor(rainfall_value):
  return rainfall_value * 1.2**np.sqrt(2)

def loop(data):
  newData = []
  for rain in data:
    newData.append(cor(rain))
  return newData

def comp(data):
  return [cor(rain) for rain in data]
  

