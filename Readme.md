
# Pong!
This is the repository for the Pong game for the Big Data Expo 2022. To get everything up and running, follow the instructions below.


## Requirements
1. If you don't have python:
* Open up a terminal on your machine (Press Windows-key + r and type cmd on Windows or open Terminal on Mac)
* Type: pip install python and hit Enter
2. OR download Anaconda (comes with python, R and various Data Science tools!) (https://www.anaconda.com/)
3. Download Docker Desktop (https://www.docker.com/products/docker-desktop/)

## Setup a new python environment
1. Open up a terminal
2. Create e new environment using conda
3. Type **conda create pong-game webscrape python=3.6** and hit **Enter**
4. Type **conda activate pong-game** and hit **Enter**
5. Install the following packages
* conda install numpy
* conda install pandas
* conda install turtle
* conda install matplotlib
* pip install pyautogui

## Download the code
1. Open up a terminal
2. Navigate to the folder where you want to store the source code, for example C:\Documents\
3. Type **git clone https://github.com/pong-data/pong-game** in the terminal and hit **Enter**
4. The source code is now copied onto your machine

## Test the code
1. Open up a terminal
2. Navigate to the folder with the source code (e.g., C:\Documents\pong-game\)
3. Type **python main.py** and hit **Enter**
4. The pong game should now start.

## Create a Docker image
1. Open up a terminal
2. Navigate to the folder ..\pong-game\
3. Type **docker build -t pong-game .** and hit **Enter** <-- dot included in the command!
4. Type **docker run -it pong** and hit **Enter**
5. The game should now run in a docker container!