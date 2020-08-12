init:
    default LIMBO_1_SCORE = 3
    default LIMBO_1_SUCCESS = False
    image darkred = "#96281b"
    image white = "#ffffff"

transform trans_limb1_bg_appear:
    alpha 0.0
    xalign 0.5 yalign 0.5
    pos (1920 / 2, 1080 / 2)
    zoom 1.375
    parallel:
        ease 1.5 alpha 1.0
    parallel:
        ease 1.5 zoom 1.0 

transform trans_limb1_bg_moving:
    ease 0.1 alpha 1.0
    block:
        parallel:
            ease 3.4 alpha 0.6
            ease 5.6 alpha 1.0
            ease 3.0 alpha 0.7
            ease 2.6 alpha 1.0
            ease 1.2 alpha 0.7
            ease 2.4 alpha 1.0
            ease 4.0 alpha 0.6
            ease 2.95 alpha 1.0
            repeat
        parallel:
            ease (5.2 * 4.5) xoffset -273
            ease (7.1 * 4.5) xoffset -129
            ease (8.9 * 4.5) xoffset 37
            ease (8.1 * 4.5) xoffset 241
            ease (7.8 * 4.5) xoffset 328
            ease (9.4 * 4.5) xoffset -129
            ease (5.9 * 4.5) xoffset -349
            ease (9.3 * 4.5) xoffset 8
            repeat
        parallel:
            ease (7.3 * 4.5) yoffset -164
            ease (5.9 * 4.5) yoffset -119
            ease (9.0 * 4.5) yoffset 118
            ease (9.3 * 4.5) yoffset -13
            ease (6.3 * 4.5) yoffset -94
            ease (9.4 * 4.5) yoffset 119
            ease (7.8 * 4.5) yoffset -68
            repeat

transform trans_limb1_bg_shake:
    parallel:
        0.1
        xpos ((1920 / 2) + 1)
        0.1
        xpos ((1920 / 2) - 1)
        0.1
        xpos (1920 / 2)
        0.1
        xpos ((1920 / 2) + 1)
        repeat
    parallel:
        ypos ((1080 / 2) - 1)
        0.05
        ypos ((1080 / 2) + 0)
        0.05
        ypos ((1080 / 2) - 1)
        0.05
        ypos ((1080 / 2) + 1)
        0.05
        ypos (1080 / 2)
        0.05
        repeat
    parallel:
        ease 0.2 alpha 1.0
        ease 0.2 alpha 0.7
        repeat
transform trans_limb1_kurt_blink:
    alpha 0.0
    ease 0.3 alpha 1.0
    0.3
    ease 0.3 alpha 0.0
transform trans_limb1_kurt_blink2:
    alpha 0.0
    ease 0.3 alpha 1.0
    ease 0.5 alpha 0.6
    ease 0.5 alpha 1.0
    0.4
    ease 0.5 alpha 0.6
    ease 0.3 alpha 0.0
transform almost_right:
    yalign 1.0
    xalign 0.75
transform almost_left:
    yalign 1.0
    xalign 0.25

transform trans_limb1_shoot:
    size (1920, 1080)
    xalign 0.5
    yalign 0.5
    alpha 0.0
    linear 0.1 alpha 1.0
    linear 0.3 alpha 0.0

label chapter_5:
    scene black
    with dissolve
    hide screen tablet_button
    $ LIMBO_1_SCORE = 3

    show bg limb1 at trans_limb1_bg_appear

    $ renpy.pause(delay=1.8, hard=True)

    show bg limb1 at trans_limb1_bg_moving

    "Incredible! Every dive is like first time."
    pause 1.0
    me "Kurt! Buddy, it’s me, [FIRST_NAME]! Remember?"
    pause 1.0
    "So cold. The whole world seems frozen. Air smells of trouble."
    "The instructions designed by the Corporation don’t provide a clear method of extracting a patient from a coma."
    "Every case is unique and depends on the patient and their state of mind."
    "However, there is a list of things that are absolutely forbidden in limbo. One of them is to lose guard."
    pause 1.0
    kurtboy_anon "No use… It can’t be done…"
    "I don’t see him but I hear a voice. A child’s voice. Kurt Bachowski’s child unconscious is somewhere nearby."
    me "Kurt! Do you hear me?"
    show kurt boy at trans_limb1_kurt_blink, almost_left
    kurtboy "Who’s here...? I can’t see you! Are you a ghost?"
    "Another thing is not to ruin the patient’s dream."
    "I can observe the illusions of Kurt’s dream and point his mind in the right direction."
    "But if I interfere and try to break the illusion, the fragile world of limbo will fall."
    pause 1.0
    show kurt boy at trans_limb1_kurt_blink, almost_right
    kurtboy "I’ve been here for so long! There’s no way out… Ghost, do you know where I am?"
    menu:
        "You’re in limbo.":
            $ LIMBO_1_SCORE -= 1
            show kurt boy at trans_limb1_kurt_blink, center
            kurtboy "What a strange word. I don’t like it."
        "You’re in a coma! Between life and death!":
            $ LIMBO_1_SCORE -= 1
            show kurt boy at trans_limb1_kurt_blink, center
            kurtboy "If you’re telling the truth, Ghost, then I am beyond help…"
        "It’s just a dream, my friend.":
            show kurt boy at trans_limb1_kurt_blink, center
            kurtboy "I’m in a dream? Cool!"
    # 2 scores left at this point
    "I must play his game."
    "I need to piece together all the scraps of Kurt’s consciousness so that he can restore his memory and come out of the coma."
    pause 1.0
    show kurt boy at trans_limb1_kurt_blink, almost_right
    kurtboy "Ghost… Are you here?"
    "His voice echoes from the grey sky."
    "This piece of Kurt’s consciousness is so tiny that doesn’t even have an image in limbo."
    "I must be careful not to lose it."
    me "I’m here. Kurt."
    show kurt boy at trans_limb1_kurt_blink, center
    kurtboy "Ghost, why do you call me Kurt?"
    "Damn! Seems like he’s fallen much deeper than we thought."
    "It’s useless to explain the situation to him at this point."
    "I must follow the protocol and try to get his memory back."
    pause 1.0
    me "Do you remember how you got here?"
    show kurt boy at trans_limb1_kurt_blink, center
    kurtboy "Hmm… No. I’m lost and I can’t get out."
    me "But now you’re not alone! Not everyone gets a ghost friend."
    show kurt boy at trans_limb1_kurt_blink, center
    kurtboy "Hm. Are you a friend though? Ghosts can be evil."

    menu:
        "Remember Casper? I’m just like that!":
            show kurt boy at trans_limb1_kurt_blink, almost_right
            kurtboy "Wow! Cool!"
        "I’m the keeper of nice dreams. I only come to good boys.":
            show kurt boy at trans_limb1_kurt_blink, almost_right
            kurtboy "Like Cyber Santa?"
        "Does it matter? Just trust me!":
            $ LIMBO_1_SCORE -= 1
            show kurt boy at trans_limb1_kurt_blink, almost_left
            kurtboy "That’s exactly what an evil ghost would say…"
    # 1 score left, no need to check for an interrupt

    me "Look around you. Does anything seem familiar?"
    show kurt boy at trans_limb1_kurt_blink, left
    kurtboy "Those mushrooms up there. I used to pick them, but really small. Together with…"
    "I must help him or he’ll never remember."
    me "You walked in the woods with your…"
    menu:
        "Brother?":
            $ LIMBO_1_SCORE -= 1
            show kurt boy at trans_limb1_kurt_blink, almost_right
            kurtboy "I don’t remember my brother at all…"
        "Father?":
            show kurt boy at trans_limb1_kurt_blink, center
            kurtboy "Yes! Dad was there!"
        "Friends?":
            $ LIMBO_1_SCORE -= 1
            show kurt boy at trans_limb1_kurt_blink, almost_right
            kurtboy "I didn’t have friends…"
    # Now it can be a game over
    if LIMBO_1_SCORE <= 0:
        jump limb1_dropout

    show kurt boy at trans_limb1_kurt_blink2, center
    kurtboy "Me and Dad used to walk in the woods."
    kurtboy "These red mushrooms were everywhere, I leaned down to pick one but Dad stopped me."
    show kurt boy at trans_limb1_kurt_blink2, center
    kurtboy "“Wait, Kurt!” he said “Redcaps are very poisonous!”"
    me "Looks like you remembered your name."
    show kurt boy at trans_limb1_kurt_blink2, center
    kurtboy "Yes… My name is Kurt! I live…"

    menu:
        "In a forest cabin?":
            $ LIMBO_1_SCORE -= 1
            show kurt boy at trans_limb1_kurt_blink, almost_left
            kurtboy "I never even saw a forest cabin!"
        "On a farm?":
            show kurt boy at trans_limb1_kurt_blink2, center
            kurtboy "We live on a farm!"
        "In a small village?":
            $ LIMBO_1_SCORE -= 1
            show kurt boy at trans_limb1_kurt_blink, almost_left
            kurtboy "Never heard about these vi-lla-ges… What are they?"
    if LIMBO_1_SCORE <= 0:
        jump limb1_dropout

    show kurt boy at trans_limb1_kurt_blink2, center
    kurtboy "Dad repairs big cars that harvest the crops and Mom looks after the animals."
    kurtboy "And there’s a little forest just like this one near the farm."

    me "You’re lucky, my friend. All farms were abandoned long ago."
    show kurt boy at trans_limb1_kurt_blink2, almost_left
    kurtboy "And if you climb up to the roof at night you can see the city lights. Lots and lots of lights… Oh…"
    me "Everything alright, Kurt?"
    show kurt boy at trans_limb1_kurt_blink2, almost_right
    kurtboy "Yes, it’s just I remembered how Dad took me…"

    menu:
        "Fishing?":
            $ LIMBO_1_SCORE -= 1
            show kurt boy at trans_limb1_kurt_blink, almost_left
            kurtboy "I hate fishing!"
        "To work?":
            $ LIMBO_1_SCORE -= 1
            show kurt boy at trans_limb1_kurt_blink, almost_left
            kurtboy "No… I had enough work at the farm…"
        "Hunting?":
            show kurt boy at trans_limb1_kurt_blink, center
            kurtboy "Yes. He told me: “Come, Kurt. Today you’re gonna become a man”"
    if LIMBO_1_SCORE <= 0:
        jump limb1_dropout
    
    show kurt boy at trans_limb1_kurt_blink2, almost_right
    kurtboy "We went to the nearest forest. I picked edible mushrooms on the way. And then we saw…"
    me "What did you see, Kurt?"
    show kurt boy at trans_limb1_kurt_blink, almost_right
    kurtboy "It was a deer. But not like on the pictures in textbooks."
    show kurt boy at trans_limb1_kurt_blink2, almost_right
    kurtboy "He was so small and hungry and…"
    me "You met a real deer? That must’ve been so cool! You got really lucky that time, Kurt."
    me "These days all animals died out, all woods are chopped down. We only got artificially-grown decorations."
    show kurt boy at trans_limb1_kurt_blink2, almost_left
    kurtboy "No, it wasn’t cool at all. The deer stopped when it saw us. Then Dad shot it with his gun."
    pause 1.0
    me "Oh, God…"
    pause 1.0

    show bg limb1 at trans_limb1_bg_shake

    show kurt boy at trans_limb1_kurt_blink, center
    kurtboy "The deer ran and Dad ran after him. I ran after Dad until I got very tired and fell."
    show kurt boy at trans_limb1_kurt_blink, center
    kurtboy "Then he came back, grabbed my hand and dragged me to the opening where the deer lied…"
    "Limbo starts to change, I touched on some troublesome memories."
    show kurt boy at trans_limb1_kurt_blink, right
    kurtboy "Dad! No! I don’t want to!"

    "There’s no way back. To restore his memory, he must relive this one to the end, no matter how traumatic it is."
    "And I must help him with it."

    show kurt boy at trans_limb1_kurt_blink, left
    kurtboy "Dad, put it away! I don’t want to do it!"

    menu:
        "I’LL DO IT MYSELF":
            $ LIMBO_1_SCORE -= 1
            show kurt boy at trans_limb1_kurt_blink, almost_right
            kurtboy "Noooo!"
        "I SAID – SHOOT!":
            show kurt boy at trans_limb1_kurt_blink, almost_right
            kurtboy "{i}*sob*{/i} Okay…"
            $ renpy.pause(delay=0.5, hard=True)
            $ notif(_("SHOT!"), interact=False, advance=False)
            show white at trans_limb1_shoot
            $ renpy.pause(delay=1.0, hard=True)
            hide white
            hide window
        "BE A MAN, KURT. TAKE THE GUN AND PULL THE TRIGGER!":
            show kurt boy at trans_limb1_kurt_blink, almost_right
            kurtboy "Dad…"
            $ renpy.pause(delay=0.5, hard=True)
            $ notif(_("SHOT!"), interact=False, advance=False)
            show white at trans_limb1_shoot
            $ renpy.pause(delay=1.0, hard=True)
            hide white
            hide window
    if LIMBO_1_SCORE <= 0:
        jump limb1_dropout
    
    show bg limb1 at trans_limb1_bg_moving

    pause 2.0
    me "It’s okay, buddy."
    me "You did what you had to do. Kurt. Don’t worry about it."
    show kurt boy at trans_limb1_kurt_blink, center
    kurtboy "But it was still… alive. It was alive until I… {i}*sob*{/i}"

    menu:
        "I know what you must feel. I’m really sorry.":
            show kurt boy at trans_limb1_kurt_blink, center
            kurtboy "Thanks, Ghost…"
        "Come on! There’ll be other deer!":
            $ LIMBO_1_SCORE -= 1
            show kurt boy at trans_limb1_kurt_blink, center
            kurtboy "Not true!"
        "You shouldn’t beat yourself up because of some animal!":
            $ LIMBO_1_SCORE -= 1
            show kurt boy at trans_limb1_kurt_blink, center
            kurtboy "{i}*sob*{/i}"
    if LIMBO_1_SCORE <= 0:
        jump limb1_dropout
    
    show kurt boy at trans_limb1_kurt_blink, center
    kurtboy "Don’t go, Ghost! {i}*sob*{/i}"
    me "It’ll be alright, I’m here."
    pause 1.0
    "Sometimes you can’t do anything to help. But sometimes it’s enough to just be there and listen."
    $ LIMBO_1_SUCCESS = True
    scene black
    with dissolve

    $ renpy.pause(delay=1.0, hard=True)
    jump chapter_6

label limb1_dropout:
    $ LIMBO_1_SUCCESS = False
    hide kurt
    hide bg limb1 with dissolve
    scene darkred
    with dissolve
    "Damn! I've destabilized him! Emergency eject triggered."
    jump chapter_6
    