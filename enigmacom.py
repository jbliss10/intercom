from gpiozero import Button
from signal import pause
import sys
import requests

message = ""


kitchen = Button(17, bounce_time=0.1)
ash = Button(27, bounce_time=0.1)
stairs = Button(13, bounce_time=0.1)
juliet = Button(4, bounce_time=0.1)
office = Button(5, bounce_time=0.1)
bedroom = Button(6, bounce_time=0.1)


def send_kitchen():
    res = requests.get('http://localhost:5005/kitchen/say/'+message+'/50')
 #   res = requests.get('http://localhost:5005/family room/say/'+message+'/50')
    print("'"+message+ "' sent to Kitchen")

def send_ash():
  res = requests.get('http://localhost:5005/Ash/say/'+message+'/50')
  print("'"+message+"' sent to Ash")

def send_stairs():
   res = requests.get('http://localhost:5005/Stairway/say/'+message+'/60')
   res = requests.get('http://localhost:5005/Boys room/say/'+message+'/50')
   print("'"+message+"' sent to Stairs and Boys Room")

def send_juliet():
  res = requests.get('http://localhost:5005/Juliet/say/'+message+'/80')
  print("'"+message+"' sent to Juliet")

def send_office():
  res = requests.get('http://localhost:5005/Desk/say/'+message+'/50')
  print("'"+message+"' sent to Office")

def send_bedroom():
  res = requests.get('http://localhost:5005/Bedroom/say/'+message+'/50')
  print("'"+message+"' sent to Bedroom")

while message != "quit":
 message = input("Enigma: ")
 kitchen.when_pressed = send_kitchen
 ash.when_pressed = send_ash
 stairs.when_pressed = send_stairs
 juliet.when_pressed = send_juliet
 office.when_pressed = send_office
 bedroom.when_pressed = send_bedroom

pause()		

