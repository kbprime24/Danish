import pyttsx3
import pyjokes

# First voice
engine = pyttsx3.init()
engine.say("Wow Danish, you are fantastic. You made a program.")
engine.runAndWait()

print("Follow these questions and answer them.")

name = input("What is your name: ")
hobby = input("What is your favourite hobby? ")
fav_number = input("What is your favourite number? ")
fav_colour = input("What is your favourite colour? ")

print("Friend's names:")
friend_name = input("What is your friend's name? ")
father_name = input("What is your father name? ")
mother_name = input("What is your mother name? ")
uncle_name = input("What is your uncle name? ")

print("Fantastic! Thanks for your answers.")

joke = pyjokes.get_joke()
print(joke)

# Second voice
engine = pyttsx3.init()
engine.say("Wow! You are a genius and a good programmer.")
engine.runAndWait()