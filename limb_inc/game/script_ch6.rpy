label chapter_6:
    scene bg lab 
    with dissolve
    hide screen tablet_button
    
    show leyla ok at center with dissolve 
    layla "Dive duration – 10 seconds. Indicators – normal, reactions – normal. Pupillary light reflex is within the norm."
    layla "How are you feeling? You hear me good?"

    menu:
        "Yes, everything is great! As fresh as a daisy!":
            pass
        "It was harder than usual, but I think I’m alright.":
            pass
        "Hear you good. Feeling – not really. Wouldn’t mind a shot of a stimulant.":
            pass
    
    layla "How was it? There are some peculiarities with your indictions during the dive."
    layla "Electromagnetic brain activity is within the normal range, but the graph looks weird. Different from the usual."

    menu:
        "Guess it’s because he fell too deep into his childhood. I think I’ll get him at the second attempt!":
            pass
        "I noticed something unusual too, but it was all within the norm!":
            pass
        "I’m not ready to discuss the dive right now. I need some time to think over it!":
            pass
    
    notif "BZZZZZZZZZ~~~~~~~"
    me "Sorry, I have a call. I need to answer."
    layla "Sure, you can talk right here, I’ll reconfigure the machine."
    show leyla ok at right with move

    $ TABLET_IS_DISABLED = True
    show screen tablet_base
    $ renpy.pause(delay=0.7, hard=True)
    show screen tablet_iface_incoming_call(_("Bella Rabinovich"), "bella on tablet")
    "It’s Bella, like I thought. She probably wants to hear a report about the dive, don’t want to leave her waiting."
    $ renpy.pause(delay=0.5, hard=True)
    $ tablet_reset_call_time()
    show screen tablet_iface_active_call(_("Bella Rabinovich"), "bella on tablet")
    pause 1.0
    bella "Welcome back! Any results?"
    me "Some kind. Kurt fell too deep; I don’t know how many iterations I’m gonna need to bring him back."
    bella "The time is limited, you know. And Internal Affairs starts to show too much interest in this case. Be careful! Something smells bad here."
    menu:
        "Don’t worry, ma’am, I’ll get through!":
            pass
        "This case seems a little off to me too. Thanks for warning!":
            pass
        "As if something ever smelled good here…":
            pass
    bella "I’m expecting the results. Talk to you."
    hide screen tablet_iface_active_call
    $ renpy.pause(delay=0.7, hard=True)
    hide screen tablet_base
    $ TABLET_IS_DISABLED = False

    show leyla ok at center with move
    layla "She is stern, isn’t she? Where were we? Ah yes, your dive! Tell me about the colors, or maybe there were any quirky details?"
    me "Why are you interested?"
    layla "Limbo is astonishing; it’s much brighter than the real world. There is everything a human can imagine there, millions of colours and shades, incredible pictures painted by subconscious. How is it not interesting?"
    me "You’ve only experienced training dives and heard somebody else’s stories and it shows."
    me "It is more like a nightmare, disgustingly colorful, feverish delirium made up by an inflamed brain."
    me "There’s nothing romantic about it, trust me!"
    layla "Well I just think it’s been a while since your last vacation."
    me "It has been…"
    layla "Oh, your blood pressure is low, just noticed. You should have a snack."
    layla "Take a walk to the lobby, there’s a vending machine and a coffee machine as well."
    "Nice idea, a cup of strong coffee and a sweet bar is exactly what I need right now."
    me "Thanks Layla, I think I’ll follow your advice."
    
    show screen tablet_button

    if WAITING_FOR_BORIS_RESPONSE:
        $ add_email("boris_hans_nicht")
        $ WAITING_FOR_BORIS_RESPONSE = False
        pause 0.5
        "Oh, looks like Boris sent me a data on my request. I should check it out."

    menu:
        "Move to the lobby":
            jump chapter_7