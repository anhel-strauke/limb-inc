label chapter_8:
    scene bg lab 
    with dissolve
    hide screen tablet_button

    show leyla ok at center with dissolve

    layla "Hey, turned your engine back on?"
    me "I don’t even know what affects the engine more — coffee or aggressive ladies?"
    layla "You’re not talking about me, right?"
    me "Sure not! Have you met Violet Sharp? Is she aways such… a…"
    layla "Bitch? Yeah, always! Don’t even want to think about her more than needed."
    me "Well, if you don’t, then let’s start."

    layla "Tell me when you are ready."
    show screen tablet_button
    menu:
        "Okay, I’m ready":
            hide screen tablet_button

    layla "We’re starting. Connecting you to the Morpheus."
    show leyla ok at right
    with ease
    pause 1.0
    layla "Pulse — normal."
    pause 0.5
    layla "Blood pressure — normal."
    pause 0.5
    layla "Concentration of biologically active substances in the blood – normal."
    pause 0.5
    layla "Electromagnetic brain activity — normal."
    pause 0.5
    layla "All systems nominal."
    pause 1.0
    show leyla ok at left
    with move
    layla "Injecting the serum…"
    pause 2.0
    show leyla ok at center
    with ease
    layla "Countdown!"
    pause 1.0
    $ layla(_("Three."), interact=False, advance=False)
    $ renpy.pause(delay=1.0, hard=True)
    $ layla(_("Two."), interact=False, advance=False)
    $ renpy.pause(delay=1.0, hard=True)
    $ layla(_("One."), interact=False, advance=False)
    $ renpy.pause(delay=1.0, hard=True)

    show limb_enter_1 at trans_limb_enter_1
    show limb_enter_2 at trans_limb_enter_2
    show limb_enter_3 at trans_limb_enter_3
    show black at trans_limb_enter_black

    $ renpy.pause(delay=2, hard=True)

    pause 0.5
    jump chapter_9
