
transform trans_limb_enter_1:
    xalign 0.5 yalign 0.5 alpha 0.0 xoffset 0 yoffset 0
    block:
        parallel:
            linear 0.5 alpha 0.4
            easeout 1.0 alpha 0.8
        parallel:
            easeout 2 xoffset -120
        parallel:
            easeout 2 yoffset -72
transform trans_limb_enter_2:
    xalign 0.5 yalign 0.5 alpha 0.0 xoffset 0 yoffset 0
    block:
        parallel:
            linear 0.5 alpha 0.4
            easeout 1.0 alpha 0.8
        parallel:
            easeout 2 xoffset 120
        parallel:
            easeout 2 yoffset -72
transform trans_limb_enter_3:
    xalign 0.5 yalign 0.5 alpha 0.0 xoffset 0 yoffset 0
    block:
        parallel:
            linear 0.5 alpha 0.4
            easeout 1.0 alpha 0.8
        parallel:
            easeout 2 xoffset 5
        parallel:
            easeout 2 yoffset 120
transform trans_limb_enter_black:
    xalign 0 yalign 0 xpos 0 ypos 0 size (1920, 1080) alpha 0
    time 1.5
    easeout 0.5 alpha 1.0


label chapter_4:
    $ renpy.sound.set_volume(0.0, delay=0, channel="fxloop1")
    $ renpy.sound.set_volume(0.0, delay=0, channel="fxloop2")
    $ renpy.sound.play("audio/medical_ovl_1.ogg", channel="fxloop1")
    $ renpy.sound.play("audio/medical_ovl_2.ogg", channel="fxloop2")
    $ renpy.sound.set_volume(0.7, delay=1.0, channel="fxloop1")
    $ renpy.sound.set_volume(0.7, delay=1.0, channel="fxloop2")
    scene bg lab 
    with dissolve
    hide screen tablet_button

    pause 0.5
    show leyla ok at center with dissolve 

    layla "Hi! I’m Layla Anderson, a dive operator."

    menu:
        "Hi Layla. I’m [FIRST_NAME]. Nice to meet you.":
            pass
        "Good morning! I’m [FIRST_NAME] [LAST_NAME]. We can start the procedure.":
            pass
        "Dr. [FIRST_NAME] [LAST_NAME]. Senior limbo specialist. Let’s start?":
            pass
    
    layla "I think in your case we can skip obligatory instructions. You’re one of the most experienced specialists here after all."

    menu:
        "Yes, sure, let’s start.":
            layla "As you say."
        "No, we should follow the protocol.":
            layla "OK!"
            layla "During the process of diving you should maintain concentration, act reasonably and prudently."
            layla "Any actions that can lead to destabilisation of a patient’s state are forbidden."
            layla "Any actions that can cause a patient to question the reality of what is happening are leading to destabilisation of a patient’s state in 87.4\% of the cases studied."
            layla "The Emergency Ejection System is triggered a second after the specialist's pulse increases above the set rate."
            layla "One second of a real time equals from 5 to 20 minutes of subjective time in limbo."
            layla "Specialists with standard biometric indicators deviations within more than 1.5\% are prohibited from diving."
            me "The instructions are clear and understood."

    $ add_doc("morpheus")

    layla "Tell me when you are ready to start."
    show screen tablet_button
    menu:
        "Okay, I’m ready":
            hide screen tablet_button

    layla "We’re starting. Connecting you to the Morpheus."
    $ renpy.sound.set_volume(0.6, channel="fxloop3")
    $ renpy.sound.set_volume(0.6, channel="fxloop4")
    $ renpy.sound.set_volume(1.0, channel="fxloop5")
    play sound blip
    play fxloop3 "<loop 18.672>audio/morpheus_1.ogg"
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
    play sound blip
    play fxloop4 "<loop 8.050>audio/morpheus_2.ogg"
    play fxloop5 "<loop 46.169>audio/morpheus_3.ogg"
    layla "All systems nominal."
    pause 1.0
    show leyla ok at left
    with move
    layla "Injecting the serum…"
    play sound liquide
    pause 2.0
    show leyla ok at center
    with ease
    play sound blip
    layla "Countdown!"
    pause 1.0
    $ layla(_("Three."), interact=False, advance=False)
    $ renpy.pause(delay=1.0, hard=True)
    $ layla(_("Two."), interact=False, advance=False)
    $ renpy.pause(delay=1.0, hard=True)
    $ layla(_("One."), interact=False, advance=False)
    $ renpy.pause(delay=1.0, hard=True)

    $ renpy.sound.set_volume(0.0, delay=0.5, channel="fxloop1")
    $ renpy.sound.set_volume(0.0, delay=0.5, channel="fxloop2")
    $ renpy.sound.set_volume(0.0, delay=0.5, channel="fxloop3")
    $ renpy.sound.set_volume(0.0, delay=0.5, channel="fxloop4")
    $ renpy.sound.set_volume(0.0, delay=0.5, channel="fxloop5")
    play sound portal
    show limb_enter_1 at trans_limb_enter_1
    show limb_enter_2 at trans_limb_enter_2
    show limb_enter_3 at trans_limb_enter_3
    show black at trans_limb_enter_black

    $ renpy.pause(delay=2.0, hard=True)
    stop fxloop1
    stop fxloop2
    stop fxloop3
    stop fxloop4
    stop fxloop5
    pause 0.5
    jump chapter_5
