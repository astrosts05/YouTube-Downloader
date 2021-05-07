from os import system, name 
import os
from pytube import YouTube

global yt

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

clear()

def printInfo():
    #gets video and prints info about it
    link = input("Enter the link: ")
    yt = YouTube(link)

    #Title of video
    print("Title:")
    print(yt.title)
    print("                  ")

    #Number of views of video
    print("Views:")
    print(yt.views)
    print("                  ")

    #Length of the video
    ytlength = yt.length
    ytlengthMinute = ytlength/60
    print("Length of video:")
    print(ytlengthMinute,"minutes")
    print("                  ")

    #Rating
    print("Ratings: ")
    print(yt.rating)
    print("                  ")
    print("                  ")
    print("                  ")

    #Description of video
    print("Description: ")
    print(yt.description)
    print("                  ")
    print("                  ")
    print("                  ")
    print("                  ")
    print("                  ")
    print("                  ")
    cmd()

def videoD():
    #lets user download mp4 video
    link = input("Enter the link: ")
    yt = YouTube(link)
    quality = input("high or low quality? | ")
    #
    if quality == "high":
        #gets the high quality version of the video specified
        vQuality = yt.streams.get_highest_resolution()
        vQuality.download()
        print("downloaded " + yt.title)
        cmd()
        # 
    elif quality == "low":
        #gets the lower resolution of the video specified
        vQuality = yt.streams.get_lowest_resolution()
        vQuality.download()
        print("downloaded " + yt.title)
        cmd()
        #
    else:
        #if user can manage typing a simple command
        print("please input either 'yes' or 'no' ")
        cmd()
        #

def audioD():
    #allows user to download mp3 form audio from specified video
    link = input("Enter the link: ")
    yt = YouTube(link)
    vAudio = yt.streams.filter(only_audio=True)
    vAudio[0].download()
    fileTitle = yt.title + ".mp4"
    base = os.path.splitext(fileTitle)[0]
    os.rename(fileTitle, base + '.mp3')
    print("downloaded")
    cmd()

def interface():
    print("               ________                      .__                    .___            ")
    print("  ____   _____ \______ \   ______  _  ______ |  |   _________     __| _/___________ ")
    print("_/ ___\ /     \ |    |  \ /  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ |")
    print("\  \___|  Y Y  \|    `   (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/")
    print(" \___  >__|_|  /_______  /\____/ \/\_/|___|  /____/\____(____  /\____ |\___  >__|   ")
    print("     \/      \/        \/                  \/                \/      \/    \/       ")
    print("                                                                                    ")
    print("                                                                                    ")
    print("Commands:")
    print("                                                                                    ")
    print("video | gets and downloads the video from a link")
    print("audio | gets and downloads the audio from the video of a link provided")
    print("info  | shows info of provided youtube video from link")


def cmd():
    clear()
    interface()
    #allows user to interact
    command = input("CMD | ")

    if command == "video":
        #allows user to download a specified video
        videoD()
    elif command == "audio":
        #lets user download mp3 audio of specified video
        audioD()
    elif command == "info":
        #prints information of specified video
        printInfo()
    else:
        print("incorrect command")

cmd()


#maybe add a home screen?
#similar to twitter for cmd
#perhaps make a system that detects if a video has been inputted yet? if yt == null: ask for video; else: use yt
