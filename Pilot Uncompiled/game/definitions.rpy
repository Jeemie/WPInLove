# Declare images below this line, using the image statement.


image eileen happy = "eileen_happy.png"
image bg tree = "big_tree"
image fsassy = "female_sassy.png"
image fhappy = "female_happy.png"
image girlschool = im.Scale("images/schoolgirl.jpeg", 400, 800)
image girlangry = im.Scale("images/schoolgirla.jpeg", 400, 800)
image placeholder animated:
    im.Scale("images/tryagain.png", 400, 800)
    pause 1
    im.Scale("images/tryagain2.png", 400, 800)
    pause 1
    repeat
image olin = "images/olin.jpg"
image goddardlab = "images/goddard_lab.jpg"

# Declare characters used by this game.
define f = Character('Professor', color="#c8ffc8")
define m = Character('Male', color="c8ffc8")


transform basicfade:
        on show:
            alpha 0.0
            linear 1.0 alpha 1.0
        on hide:
            linear 0.5 alpha 0.0    