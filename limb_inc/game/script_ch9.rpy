transform trans_limb2_bg_appear:
    alpha 0.0
    xanchor 0.5 yanchor 0.5
    pos (1920 / 2, 1080 / 2)
    zoom 0.75
    parallel:
        ease 1.5 alpha 1.0
    parallel:
        ease 1.5 zoom 1.0 
    parallel:
        ease 1.5 rotate 9.6


transform trans_limb2_bg_moving:
    rotate_pad False
    block:
        ease 6.0 rotate -9.6
        ease 6.0 rotate 9.6
        repeat

transform trans_limb2_bg_moving_crazy:
    block:
        parallel:
            easeout 0.5 zoom 1.333333
        parallel:
            ease 0.5 rotate 0
    block:
        parallel:
            rotate 0
            linear 0.4 rotate 359.9
            repeat
        parallel:
            ease 1.0 zoom 2.4
            ease 1.0 zoom 1.333333
            repeat

transform trans_limb2_bg_leaving:
    block:
        parallel:
            rotate 0
            linear 0.4 rotate 359.9
            repeat
        parallel:
            ease 1.0 zoom 2.4
            ease 1.0 zoom 0.2

transform trans_limb2_white:
    size (1920, 1080)
    xalign 0.5
    yalign 0.5
    alpha 0.0
    time 1.5
    easeout 0.5 alpha 1.0


transform trans_kurt_sliding_wall:
    ypos 1080 rotate_pad False transform_anchor True
    ease 1.0 ypos 1080+200
    ease 1.0 rotate 15
    ease 10.0 ypos 1080+340

transform trans_move_almost_right:
    yalign 1.0
    ease 0.5 xalign 0.75

transform trans_move_center:
    yalign 1.0
    ease 0.5 xalign 0.5

transform trans_move_almost_left:
    yalign 1.0
    ease 0.5 xalign 0.25
    

init:
    default LIMBO_2_SCORE = 3
    default LIMBO_2_SUCCESS = False

label chapter_9:
    play music limbo_1 fadein 1.0
    scene black
    with dissolve
    hide screen tablet_button
    $ LIMBO_2_SCORE = 3

    show bg limb2 at trans_limb2_bg_appear

    $ renpy.pause(delay=1.8, hard=True)

    show bg limb2 at trans_limb2_bg_moving

    me "Kurt… do you hear me?"

    show kurt limb at center with dissolve

    kurt "[FIRST_NAME]! Are you real?"
    "Incredible. I finally found him."
    me "Of course I’m real! Do you want to ask me a verification question?"
    kurt "It makes no sense. My memory is damaged now and Limbo can do anything to me. Why are you here?"
    me "To get you out, of course. You're in a coma, Kurt!"
    kurt "Just as I thought. Too bright and clear images for a simple nightmare. We need to get out as soon as possible."
    "Kurt is with me – It’s only half of it."
    "Now we must break the trap of the subconscious to return to the border between Limbo and reality and get out of the coma."
    me "Any idea where we are?"
    kurt "It looks like the mind palace."
    kurt "We’re going to take the stairs and open all the doors we come across until we find the right one."
    me "Should we go up or down?"
    kurt "It doesn’t matter. The space itself is distorted. That’s Limbo."
    play sound footsteps
    pause 1.0
    kurt "For example, this one…"
    play sound footsteps_alt
    show kurt at trans_move_almost_right
    play sound locked
    kurt "Closed!"
    ahans "There is something that died long ago, but we can see it live now."
    "What the hell!?"
    play sound footsteps_alt
    show kurt at trans_move_center
    kurt "It’s him."
    me "What are you talking about?"
    kurt "Extraneous consciousness. I can feel how it controls Limbo."
    me "Looks like now it’s going to ask us some riddles?"
    kurt "If we guess, we can go through the door."
    me "All right, let’s try. If an animal or a person died 10 years ago, we cannot see him alive today, right?"
    kurt "Hmm… So it’s with a tree that was cut down a few years ago — now it cannot be seen flowering or alive. What are we talking about?"
    ahans "There is something that died long ago, but we can see it live now."

    menu:
        "Seasons?":
            $ LIMBO_2_SCORE -= 1
            ahans "WRONG"
        "Star?":
            ahans "RIGHT"
        "Human consciousness?":
            $ LIMBO_2_SCORE -= 1
            ahans "WRONG"
    
    ahans "Like an echo, starlight reaches us after a certain amount of time."

    play sound door_open
    kurt "Look! The seal is broken and the door opens."
    show kurt at trans_move_almost_right
    kurt "Emptiness."
    me "Damn it! We break our head over the riddle in vain."
    kurt "Maybe that’s part of it. And I liked the riddle – it’s beautiful."
    play sound footsteps_alt
    show kurt at trans_move_center
    $ renpy.pause(delay=0.5, hard=True)
    play sound footsteps
    pause 1.0
    "We are walking further up the spiral stairs of Kurt’s memory."
    "Again the door, again — the seal."
    pause 1.0
    me "Try to open it. I don't want to stay here."
    play sound footsteps_alt
    show kurt at trans_move_almost_left
    $ renpy.pause(delay=0.5, hard=True)
    play sound locked
    kurt "Closed. What a surprise, huh?"
    play sound footsteps_alt
    show kurt at trans_move_center
    ahans "Look at him closely, but you will not see him.\nIf you see him, you can no longer see anything.\nSometimes he tells the truth, but more often he lies."
    ahans "He can make you walk, even if you don't want to.\nAll people see it, but not everyone remembers it."
    me "Do you have any ideas?"
    kurt "Are you talking about the speaker or the riddle?"
    me "Any ideas, Kurt. Let's shake up your memory."
    kurt "The voice sounds familiar to me, but I can’t catch the thought. Everything is like in a fog."
    kurt "And the riddle… It is exactly some kind of broad concept in the answer. Limbo is a world of surrealism and abstraction. It’s like…"
    me "Drugs influence?"
    kurt "Sort of that."
    kurt "I’ll try touch the door again…"
    play sound footsteps_alt
    show kurt at trans_move_almost_left
    $ renpy.pause(delay=0.5, hard=True)
    play sound locked
    ahans "Look at him closely, but you will not see him.\nIf you see him, you can no longer see anything.\nSometimes he tells the truth, but more often he lies."
    ahans "He can make you walk, even if you don't want to.\nAll people see it, but not everyone remembers it."

    menu:
        "Hallucinations?":
            $ LIMBO_2_SCORE -= 1
            ahans "WRONG"
        "The wish?":
            $ LIMBO_2_SCORE -= 1
            ahans "WRONG"
        "The dream?":
            ahans "RIGHT"
    
    play sound door_open
    ahans "You people cannot learn to control the dreams. This makes you helpless in the world of illusions."
    kurt "Emptiness again!"
    play sound footsteps_alt
    show kurt at trans_move_center
    kurt "Moving on?"
    "It’s weird that Kurt can’t remember whose voice it is. Usually our subconscious is connected with the owner of Limbo anyway."
    "So Kurt didn’t created this Limbo. Then who controls it?"
    me "Let’s go. I’m starting to get nervous."
    kurt "Oh, don't worry, [FIRST_NAME]. In the worst case, we… will stay here forever."
    "Unless corporate employees disconnect us from a life support system…"
    play sound footsteps
    pause 1.0
    kurt "Another door. I'll try."
    play sound footsteps_alt
    show kurt at trans_move_almost_right
    $ renpy.pause(delay=0.5, hard=True)
    play sound locked
    ahans "You cannot see it, you cannot touch it, you cannot hear it, you cannot smell it.\nIt lives behind the stars and under the mountains. It ends the life and kills laughter."

    menu:
        "Death?":
            $ LIMBO_2_SCORE -= 1
            ahans "WRONG"
        "The Universe?":
            $ LIMBO_2_SCORE -= 1
            ahans "WRONG"
        "The darkness?":
            ahans "RIGHT"
    if LIMBO_2_SCORE <= 0:
        jump limb2_dropout
    
    play sound door_open
    ahans "Eternal Darkness."
    ahans "From the darkness I came out into the light and the man became my God. He gave me a name…"
    ahans "HOMUNKULUS."

    "What did he say? Homunculus?"

    me "I see a dim light at the end of this hallway. Let's go there, Kurt."
    kurt "I’m… going… Oh…"

    play sound kurt_fall
    show kurt at almost_right, trans_kurt_sliding_wall
    "Bachowski holds his head. Leaning back, he slowly slides down the wall."
    me "Kurt! What’s happened?"
    kurt "…my head is exploding! Ah!"
    "He covers his ears with his hands, then releases them and looks at his hands. Kurt's palms are covered in blood."
    "He looks at me and I see tears in his eyes."
    kurt "It won't let me go. I can't get out, [FIRST_NAME]."

    ahans "DOES IT HURT YOU? I LIVE WITH THIS PAIN FOR AS LONG AS I CAN REMEMBER."
    "What is it? What is it?!"
    "Some kind of a twisted artificial intelligence? Another glitch in Morpheus?"
    me "I’m here to get you out of your coma, Kurt."
    me "We’ll get out together!"
    ahans "NOT NOW!"

    hide kurt with moveoutbottom

    show bg limb2 at trans_limb2_bg_moving_crazy

    "WHAT?!"
    "Something grabbed me and carried me up."
    "I fly through the endless floors of Kurt’s mind palace, farther and farther from my goal."
    "The bright light blinds my eyes and I feel very dizzy."
    "Amid the vile laughter of an unknown creature, I leave Limb."
    show bg limb2 at trans_limb2_bg_leaving
    show white at trans_limb2_white
    $ renpy.music.set_volume(0.0, delay=4.0)
    $ renpy.pause(delay=3.5, hard=True)
    play sound portal_out_emerg
    $ LIMBO_2_SUCCESS = True
    $ renpy.pause(delay=1.0, hard=True)
    jump chapter_10


label limb2_dropout:
    $ LIMBO_2_SUCCESS = False
    play sound medical_alert loop
    show darkred at trans_red_shroud
    $ renpy.pause(delay=0.5, hard=True)
    kurt "[FIRST_NAME], where are you? [FIRST_NAME]!…"
    stop sound
    play sound portal_out_emerg
    $ renpy.pause(delay=1.5, hard=True)
    jump chapter_10



