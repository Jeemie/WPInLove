# Declare images below this line, using the image statement.



image mainmenu:

    "images/bg1.png"
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 1.0
    linear 0.5 alpha 0.0
    pause 1.0
    "images/bg2.png"
    linear 1.0 alpha 1.0
    pause 1.0
    linear 0.5 alpha 0.0
    pause 1.0
    "images/bg4.png"
    linear 1.0 alpha 1.0
    pause 1.0
    linear 0.5 alpha 0.0
    "images/white.jpg"
    linear 0.50 alpha 1.0
    linear 0.25 alpha 0.0
    "images/bg3.png"
    linear 0.5 alpha 1.0
        
image mainmenu2:
    time 8.5
    block:
        "images/heart.png"
        linear 1.0 alpha 0.0
        pause 0.5
        linear 1.0 alpha 1.0
        pause 0.5
        repeat
    
image eileen happy = "eileen_happy.png"
image bg tree = "images/big_tree"
image bg black = "images/black.jpg"
image bg olin = "images/olin.jpg"
image bg goddardlab = "images/goddard_lab.jpg"
image bg dorm="images/dorm.jpg"

image fsassy = "images/female_sassy.png"
image fhappy = "images/female_happy.png"
image fangry = "images/female_angry.png"
image fsad = "images/female_sad.png"


image mhappy = "images/male_happy.png"
image msad = "images/male_sad.png"
image mangry = "images/male_angry.png"
image mshocked = "images/male_shocked.png"

image thappy = "images/twin_happy.png"
image tsad = "images/twin_sad.png"
image tangry = "images/twin_angry.png"
image tshocked = "images/twin_shocked.png"

image logo = "images/logo.png"

image placeholder animated:
    im.Scale("images/tryagain.png", 400, 800)
    pause 1
    im.Scale("images/tryagain2.png", 400, 800)
    pause 1
    repeat


# Declare characters used by this game.
define p = Character('Professor', color="#c8ffc8")
define male = Character('Male', color="#c8ffc8")
define female = Character('Female', color="#c8ffc8")


#Animation("images/tree.jpg", 2.0, "images/bg1.png", 2.0, "images/bg2.png", 2.0)
transform basicfade:
        on show:
            alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            linear 0.5 alpha 0.0    
           

transform dim:
    alpha 1.0
    linear 1.0 alpha 0.5
    
    
transform undim:
    alpha 0.5
    linear 1.0 alpha 1.0
    
transform fastfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0
    
#some labels

label splashscreen:
    scene white
    show logo at basicfade,truecenter
    with Pause(4)
    hide logo at basicfade
    scene black with dissolve
    with Pause(1)

    show text "Spell Shaded presents to you..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return
    
    
#show text "" at basicfade,truecenter with Pause(2.5)
#pause 1
#hide text at basicfade