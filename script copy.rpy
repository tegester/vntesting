# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
 
init:
    
    $ persistent.erica_end is None
    $ persistent.seth_end is None
    $ persistent.fox_end is None
    $ persistent.crow_end is None
    $ persistent.normal is None
    $ persistent.special_end is None
    
    if persistent.erica_end and persistent.seth_end and persistant.fox_end and persistent.crow_end and persistent.normal:
       $ persistent.special_end is True 
  
label start:
   
    $ persistent.erica_end is None
    $ persistent.seth_end is None
    $ persistent.fox_end is None
    $ persistent.crow_end is None
    $ persistent.special_end is None
    

        
label begin:

"pick one"

menu:
    "erica":
        if persistent.special_end is True:
            jump special
        else: 
            jump erica_end
    "seth":
        if persistent.special_end is True:
            jump special
        else:
            jump seth_end
    "fox":
        if persistent.special_end is True:
            jump special
        else:
            jump fox_end
    "crow":
        if persistent.special_end is True:
            jump special
        else:
            jump crow_end
    "none?":
        jump normal
        
label normal
        $ persistent.normal == True
        "That's fair."
        
return 

label erica_end:
        $ persistent.erica_end == True
        "Heyo!"
        
return

label seth_end:
        $ persistent.seth_end == True
        "Nice."

return

label fox_end:
        $ persistent.fox_end == True
        "Yip."

return 

label crow_end:
        $ persistent.crow_end == True
        "Caw."

return

label special:
        "Finally~!"

return