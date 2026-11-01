# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen")
define narrator = Character("")

init python:
    def fuck_off(a,b):
        a+=1
        renpy.say(narrator,"fuck off")
        if b==1:
            renpy.say(narrator,"I'm so fucking miserable")
        return a 

    cruelty = 0
    fuck_off1 = 0
    bitchiness = 0
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #now eileen happy

    # These display lines of dialogue.

    narrator "This will be the base for our 'sandbox' little thing"
    label menu1:
        menu:
            #"You decide to..."
                
                "Punch a tree":
                    python:
                        fuck_off1 = fuck_off(fuck_off1,0)
                    jump menu1

                "Cry a little":
                    python:
                        fuck_off1 = fuck_off(fuck_off1,1)
                        bitchiness += 1
                    jump menu1
                
                "Kill ..." :
                    menu:
                        "A random citizen|citisen (i don't care how it's should've been written)":                       
                                narrator "Geez, my guy, chill."
                                narrator "+1 cruelty"
                                python:
                                    cruelty += 1
                                    renpy.say(narrator, f"cruelty = {cruelty}")
                                jump menu1
                            
                        "Your own mother": 
                                narrator "Woah... There's a lot to unpack, isn't it? Too bad that we've got a game to make and not a fucking therapy session!"
                                narrator "+1 day off the schedule"
                                jump menu1

                "Stats":
                    python:
                        renpy.say(narrator, f"Bitchiness={bitchiness}\nFuck off={fuck_off1}\nCruelty={cruelty}")
                    jump menu1

            
    # This ends the game.

    return
