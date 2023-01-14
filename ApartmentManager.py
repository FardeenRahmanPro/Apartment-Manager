#Apartment Manager
#Created by: Fardeen Rahman
#27/11/2021 - 

#TODO:
#-Implements settings()

#IMPORTS
import os
import sys
import csv
import smtplib
from time import *
from math import *
from random import *
from datetime import *
import pygame.mixer
import pygame as pg


#CONSTANTS AND VARIABLES AND ARRAYS
global settingsArray
global apartment
settingsArray = []
apartment = []

#COLOURS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
lightGREEN = (124,252,0)
CYAN = (0,255,255)
ORANGE = (255,140,0)
BROWN = (139,69,19)

#Sets Up Pygame
pg.init()
pg.display.set_caption("Apartment Manager")

#Sets Up Window
windowInfo = pg.display.Info()
windowSurface = pg.display.set_mode((960, 640))

#FONTS
#nelipotFont = pg.font.Font('NelipotVPDemo-Style2.ttf', 128)

titleFont = pg.font.SysFont(None, 128)
mainScreenFont = pg.font.SysFont(None, 96)
waterLVLFont = pg.font.SysFont(None, 48)


#IMAGES
backgroundImage = pg.image.load("background.png").convert()

#FUNCTIONS
def setup():
    global settingsArray
    
    try:
        refreshSettings()
        
    except:
        settingsFile = open("Settings.csv", "x", newline = '')
        csvWriter = csv.writer(settingsFile)

        csvWriter.writerow(["STARTUP"])
        csvWriter.writerow(["Name:", input()])
        csvWriter.writerow(["Company:", input()])
        csvWriter.writerow(["Email:", input()])
        csvWriter.writerow(["Email Password:", input()])

        settingsFile.close()

        settingsFile = open("Settings.csv", "r+", newline = '')
        csvReader = csv.reader(settingsFile)
        
        for row in csvReader:
            settingsArray.append(row)
        
        refreshSettings()

def refreshSettings():
    global settingsArray

    settingsFile2 = open("Settings.csv", "r+", newline = '')
    refreshSettingsCSVReader = csv.reader(settingsFile2)
    settingsArray.clear()

    for row in refreshSettingsCSVReader:
        settingsArray.append(row)

    print(settingsArray)

    settingsFile2.close()

def evict(evictTenantEmailAddress):
    global settingsArray
    
    serverAddress = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    serverAddress.login(settingsArray[2][1], settingsArray[3][1])
    serverAddress.sendmail(settingsArray[2][1], evictTenantEmailAddress, "Hello")

    serverAddress.close()

def apartmentManager():
    global apartment
    
    windowSurface.blit(backgroundImage, [0,0])
    pg.display.update()

    apartmentFileName = input("What is the name of the apartment? ")

    try:
        apartmentFile = open(apartmentFileName + ".csv", "r+", newline = '')
        csvReader = csv.reader(apartmentFile)

        apartment = []

        for row in csvReader:
            apartment.append(row)

        print(apartment)
        
    except:
        print(apartmentFileName + ".csv COULD NOT BE FOUND")
        wantToCreateFile = input("Would you like to create it? ")
        
        if (wantToCreateFile == "Y"):
            apartmentFile = open(apartmentFileName + ".csv", "x")
            apartmentFile.close()
            apartmentFile = open(apartmentFileName + ".csv", "r+", newline = '')
            
            csvReader = csv.reader(apartmentFile)
            csvWriter = csv.writer(apartmentFile)

            apartment = []
            floorRoomCountArray = []

            numberOfFloors = input("How many floors are in this apartment? ")

            roomsPerFloor = int(input("How many rooms per floor? "))

            for i in range(0, int(roomsPerFloor)):
                floorRoomCountArray.append(roomsPerFloor)

            print(apartment, numberOfFloors, floorRoomCountArray)
            

            for i in range(0, int(numberOfFloors)):
                floor = []
                for j in range(0, roomsPerFloor):            
                    print(j)
                    name = input()
                    roomNumber = input()
                    email = input()
                    monthlyRent = input()
                    numberOfMonthsDue = input()

                    floor.append(name + "," + roomNumber + "," + email + "," + monthlyRent + "," + numberOfMonthsDue + "," + date.today().strftime("%Y") + "," + date.today().strftime("%m") + "," + date.today().strftime("%d"))

                    print(floor)

                apartment.append(floor)

            for i in range(0, int(numberOfFloors)):
                csvWriter.writerow(apartment[i])
                    
        else:
            pass
            
def settings():
    global settingsArray
    
    os.remove("Settings.csv")
    settingToEdit = "default"

    while (settingToEdit != "exit"):
        settingToEdit = input("What setting do you want to edit?")
        if (settingToEdit == "Name"):
            settingsArray[1][1] = input()
        elif (settingToEdit == "Company"):
            settingsArray[4][1] = input()
        elif (settingToEdit == "Email"):
            settingsArray[3][1] = input()
        elif (settingToEdit == "Email Password"):
            settingsArray[4][1] = input()

    newSettingsFile = open("Settings.csv", "x", newline = '')
    newSettingsFile.close()

    newSettingsFile = open("Settings.csv", "r+", newline = '')

    csvWriter = csv.writer(newSettingsFile)

    for line in settingsArray:
        csvWriter.writerow(line)

def notifications(apartment):
    currentDate = []

    currentDate.append(int(date.today().strftime("%Y")))
    currentDate.append(int(date.today().strftime("%m")))
    currentDate.append(int(date.today().strftime("%d")))

    for i in range(0, len(apartment)):
        for j in range(1, len(apartment[i])):
            unit = apartment[i][j]
            unit = unit[1:len(unit)-1]
            unitArray = unit.split(",")
            print(unitArray)
            #INCLUDE YEAR AND MONTH IN IF STATEMENT, SO DAY ESTABLISHED (WITH YEAR)  DOESN'T PASS
            if (int(date.today().strftime("%d")) == int(unitArray[7][2:4])):
                print("UNIT" + unitArray[1] + "'s" + " RENT DUE TODAY")

def lookup(apartmentFloorNumber, floorRoomNumber):
    room = apartment[apartmentFloorNumber][floorRoomNumber]

    
    
#TEXT

#MUSIC AND SOUNDS

#BACKGROUND

#SHAPES

#PRINTS TEXT

#DISPLAYS
setup()
