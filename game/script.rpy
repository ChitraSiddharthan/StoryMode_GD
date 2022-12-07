# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ruth = Character("ruth")


# The game starts here.

label start:

label background:

scene bg neuron
with fade
init:
    image bg neuron:
        "bg neuron.jpg"
        zoom 2.5

"The basic building blocks of the brain and nervous system are neurons (also known as neurones or nerve cells)."
"Neurons are the cells that receive sensory information from the outside world, give motor commands to our muscles, and transform and relay electrical signals at each stage along the way."

label sprites:

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
   "Ohh... I forgot that you can't see me...WAIT"
hide bg neuron
show ruth  happy2
init:
    image ruth happy2:
        "ruth happy2.jpg"
        zoom 2.5

"ruth" "Hey there.... "
"ruth"  "Let's together learn how brain neurons work and how important are they by playing Eyewire"
"ruth" "Let's start with basic"


 
"ruth"  "Let's visit our lab and start with our Quest"
scene bg lab 2
with fade
init:
    image bg lab 2:
        "bg lab 2.jpg"
        zoom 1.5
hide bg lab 2

show frustrated kindergarten kid
init:
    image frustrated kindergarten kid:
        "frustrated kindergarten kid.jpg"
        zoom 2.5

"ruth" "Look's like trouble"
"ruth" "Lakshaya and Pranav have always been like this "
hide frustrated kindergarten kid 

show cube1
init:
    image cube1:
        "cube1.jpg"
        zoom 1.5
"ruth" "Let's help these kids resolve their fights by solving first cube"
hide cube1

show solution cube1
init:
    image solution cube1:
        "solution cube1.jpg"
        zoom 1.5
"ruth" "Impressive"
hide solution cube1


show happy kindergarten kid 
init:
    image happy kindergarten kid:
        "happy kindergarten kid.jpg"
        zoom 2.5
#show ruth happy2
"ruth" "Ohh my it was not that hard handling those kindergartens... was it"
"ruth" "Good Job.... Let's move on to next cube"
hide happy kindergarten kid 

"ruth" "Do you like Environmental studies"
"ruth" "I used to love the subject "
"ruth" "Your next task is to help Avantika complete her EVS homework "
show ruth  happy2
init:
    image ruth happy2:
        "ruth happy2.jpg"
        zoom 2.5

hide confused science 

show cube1
init:
    image cube1:
        "cube1.jpg"
        zoom 1.5
"ruth" "Your next task is to help Avantika complete her EVS homework "
hide cube1

show solution cube1
init:
    image solution cube1:
        "solution cube1.jpg"
        zoom 1.5
"ruth" "Impressive"
hide solution cube1
"ruth" " Avantika is just too elated to complete her homework early"
show happy science
init:
    image happy science:
        "happy science.jpg"
        zoom 3.5
#hide happy science

"ruth" "Now how about Science"
"ruth" "Let's quickly move on to next cube help Pruthvi solve a Science Quiz"

show confused 
init:
     image confused:
      "confused.jpg"
      zoom 2.5

hide confused

show ruth  happy2
init:
    image ruth happy2:
        "ruth happy2.jpg"
        zoom 2.5

"ruth" "Let's help Tanu solve her math puzzle "

show tanu
init:
    image tanu:
        "tanu.jpg"
        zoom 2.5
hide tanu

"ruth" "Meet Tanu who needs your help with Mathematics."

show cube1
init:
    image cube1:
        "cube1.jpg"
        zoom 1.5
#"ruth" "Your next task is to help Avantika complete her EVS homework "
hide cube1

show solution cube1
init:
    image solution cube1:
        "solution cube1.jpg"
        zoom 1.5
"ruth" "Impressive"
hide solution cube1

show tanu happy
init:
    image tanu happy:
        "tanu happy.jpg"
        zoom 2.5
    # This ends the game.
hide tanu happy

return
