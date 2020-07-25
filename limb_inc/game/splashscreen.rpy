label splashscreen:
    image black = "#000000"
    image atsg_logo = "splash/atsg.png"
    scene black
    $ renpy.pause(delay=0.5) # Use renpy.pause instead of usual pause instruction to prevent weird splash screen skipping on user click
    show text "{size=+30}{color=#fff}ТАК ВЫШЛО{/color}{/size}" at truecenter
    with fade
    $ renpy.pause(delay=2.0)
    hide text
    with fade
    $ renpy.pause(delay=0.5)
    show atsg_logo at truecenter
    with fade
    $ renpy.pause(delay=2.0)
    hide atsg_logo
    with fade
    $ renpy.pause(delay=0.5)
