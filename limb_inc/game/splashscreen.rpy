label splashscreen:
    image black = "#000000"
    image atsg_logo = "splash/atsg.png"
    image it_happens_logo = Text("IT HAPPENS", size=120, bold=True, xalign=0.5, yalign=0.5, color="#ffffff")
    scene black
    $ renpy.pause(delay=0.5) # Use renpy.pause instead of usual pause instruction to prevent weird splash screen skipping on user click
    show it_happens_logo at truecenter
    with fade
    $ renpy.pause(delay=2.0)
    hide it_happens_logo
    with fade
    $ renpy.pause(delay=0.5)
    show atsg_logo at truecenter
    with fade
    $ renpy.pause(delay=2.0)
    hide atsg_logo
    with fade
    $ renpy.pause(delay=0.5)
