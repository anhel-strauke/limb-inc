init python:
    import datetime

    if persistent.endings is None:
        persistent.endings = set()
    
    if persistent.endings_dates is None:
        persistent.endings_dates = {}
    
    def merge_endings(old, new, current):
        current.update(old)
        current.update(new)
        return current

    def merge_endings_dates(old, new, current):
        current.update(old)
        current.update(new)
        return current

    renpy.register_persistent("endings", merge_endings)
    renpy.register_persistent("endings_dates", merge_endings_dates)

    def register_ending_if_not_registered(ending):
        global NEW_ENDING_TITLE
        if ending not in persistent.endings_dates:
            persistent.endings_dates[ending] = (datetime.datetime.today(), FIRST_NAME[:], LAST_NAME[:])
            persistent.endings.add(ending)
            NEW_ENDING_TITLE = ENDING_TITLES.get(ending, "???")
            renpy.save_persistent()
    
    ENDING_TITLES = {
        "bad": _("They’ll Send Someone To Us"),
        "norm": _("See You Soon"),
        "good": _("Cognosce te Ipsum")
    }

    NEW_ENDING_TITLE = ""

init:
    default ENDING_UNLOCKED = ""

    transform trans_epilogue_bg:
        block:
            xpos 0 ypos 0 size (1920, 1080)
            alpha 0.0
            ease 3.0 alpha 1.0
        block:
            ease 2.0 alpha 0.9
            ease 2.0 alpha 1.0
            repeat
    transform trans_epilogue_bg2:
        ease 2.0 alpha 0.9
        ease 2.0 alpha 1.0
        repeat
    transform trans_epilogue_kurt_reset_x:
        xalign 0.35
    transform trans_epilogue_kurt:
        block:
            alpha 0.0 yalign 1.0
            2.0
            ease 1.0 alpha 0.6
        block:
            ease 2.0 alpha 1.0
            ease 2.0 alpha 0.6
            repeat
    transform trans_epilogue_kurt2:
        ease 2.0 alpha 1.0
        ease 2.0 alpha 0.6
        repeat
    transform trans_epilogue_kurt_shift:
        ease 0.5 xalign 0.7
    transform trans_epilogue_hans_appear:
        ease 0.5 xalign 0.25
    transform trans_epilogue_bg_fade:
        ease 0.5 alpha 0.6
    transform trans_epilogue_stabilize:
        ease 0.5 alpha 1.0

    image black_overlay = "#000000"
    transform trans_epilogue_ovl:
        xalign 0.5 yalign 0.5 size (1920, 1080) alpha 0.0
    transform trans_epilogue_ovl_alpha20:
        ease 1.0 alpha 0.2
    transform trans_epilogue_ovl_alpha40:
        ease 1.0 alpha 0.4
    transform trans_epilogue_ovl_alpha60:
        ease 1.0 alpha 0.6
    transform trans_epilogue_ovl_alpha80:
        ease 1.0 alpha 0.8
    transform trans_epilogue_ovl_alpha100:
        ease 1.0 alpha 1.0

label epilogue:
    $ renpy.music.set_volume(0.0)
    play music main_menu
    $ renpy.music.set_volume(1.0, delay=12.0)
    scene black
    with dissolve
    $ renpy.pause(delay=2.0, hard=True)
    show white at trans_epilogue_bg
    show kurt limb2 at trans_epilogue_kurt_reset_x
    show the31 ok at offscreenleft
    show the31 ok at trans_epilogue_kurt
    show kurt limb2 at trans_epilogue_kurt
    $ renpy.pause(delay=3.0, hard=True)
    $ NEW_ENDING_TITLE = ""

    kurt "[FIRST_NAME], friend! I am so happy to see you!"
    me "Kurt! Your consciousness is stable at last!"
    kurt "I seem to be in coma and you were sent to get me out?"
    me "You’re damn right! I thought for a while that I’ll be stuck with you in here."
    me "What the hell it was?! From whence is this guy inside your consciousness? How is that even possible?"
    kurt "Let me start at the beginning. I was called to erase a criminal by the name of Hans Nicht."
    kurt "The guy did convince me to take a peek inside his head before the purge, telling me he was not a criminal, that everything is not as I think it is." 
    kurt "He was persuasive as hell! Told that he was grown at a farm and the only crime he made is attempting to escape."
    me "And you did fall for it? Because you do know that they are going to tell you anything in the face of the purge." 
    kurt "I’ve seen a lot and he didn’t seem to be a criminal. And he looked weird."
    kurt "Also you can remember these articles from like ten years ago, about all these synthetic human organs and tissues are said to be grown as a whole “homunculus” person and not separately."
    me "Yes, but it’s a nonsense similar to those of a zombifying radiation emissions from magnet trains or religious fanatics’ resentment at an on-impregnation gene editing." 
    kurt "And you are wrong on this one! I saw it when I’ve connected to him! I saw it, [FIRST_NAME]!"
    kurt "“Farms”, “homunculi” like himself and what is done to them. And they’re humans! Yes, genetically modified and lab breeded, but they think and feel and will to live!" 
    kurt "I suppose I could see more if Violet wouldn’t pull the trigger… He was dead when I connected."
    kurt "I don’t know how it turned out that way, but a clout of his consciousness is living inside me ever since…"
    me "Do you understand that it sounds like a ravings of the madman?!"
    kurt "Yes, but you did see it for yourself!"
    me "I would have had decided us both went nuts, if I didn’t know you. We need to figure this all out properly. But let us get out of here first." 
    me "A light is a sign of a free consciousness, and you know that by yourself — let’s get out before your subconsciousness throws in something else…"
    pause 1.0

    if LIMBO_3_SUCCESS:
        if LIMBO_2_SUCCESS and LIMBO_1_SUCCESS:
            jump good_end
        else:
            jump normal_end
    else:
        if LIMBO_2_SUCCESS and LIMBO_1_SUCCESS:
            jump normal_end
        else:
            jump bad_end

label good_end:
    "I feel a warm light enshrouding me. The coma recedes. It’s time for us to return."
    me "Come on, Kurt. It’s time to go."
    kurt "Lord, I’ve been here forever…"
    "We are both professionals who know the protocol by heart. I don’t have to explain to him what to do."
    kurt "Who is at the system now? Layla? I hope she didn’t fall asleep at the control panel."
    me "Everything will be alright. Come on."
    "We both begin to raise our left hand slowly and smoothly. We focus all our attention on this action."
    "At this borderline level of Limbo, our consciousness still has access to the physical body."
    "With full concentration, we can do simple movements in the real world."
    "When we were both just learning to immerse in Limb, mastering such “internal” gymnastics was included in the basic program of the course." 
    pause 1.0
    layla "Oh shit! They get out!"
    "Now somewhere in the patient’s room, the Limbo Technician sees the left arms of both comatose patients suddenly begin to rise up."
    "An unusual sight, I guess."
    layla "I see! I see you both, doc!"
    layla "Initiating the return procedure. Follow my voice."
    play sound blip
    kurt "Her voice is much nicer than Violet’s, I’ll tell you."
    # "Limb Technician ’s voice greets us in the real world, as if a wife meets her husband after a long shift."
    kurt "You know, I’ll probably quit…"
    me "Huh. You won’t be able to go on without this job…"
    layla "Return in FIVE."
    kurt "Who am I kidding?"
    me "Yourself first."
    "I’ve been through this a thousand times. I told myself that I had already decided everything. Apply to the boss, but then took the applications back."
    layla "FOUR."
    "We are tormented by insomnia and rare hallucinations. When we fall asleep, we see nightmares."
    kurt "I wonder how Miri and Kaz are…"
    "The human brain is both a gift and a curse. Our consciousness is scraps of our own and others’ images, a jumble of Rorschach spots and cybernet advertising."
    layla "THREE."
    "When I look at other people, I think we are all in one global Limbo now. We are cooked in this informational soup, similar to the paintings of Salvador Dali."
    kurt "I certainly won’t get into your head, [FIRST_NAME]"
    me "Thank you for your honesty."
    kurt "Just to let you know."
    layla "TWO."
    "But who but us? Who, besides us, can jump into the human mind, full of secrets, desires, anxieties, the darkest needs?"
    "Plunge, as if in the cold waters of the ocean and get out of there a person drowning in their own dreams. No matter what color, creed or set of beliefs…"
    kurt "Probably, we have to write a bunch of reports on this matter."
    me "You’re right."
    "I hope he is smart enough not to mention in the reports what we learned from Thirty-one."
    kurt "You know, I only pray that the fragments of {i}HIS{/i} consciousness remain in Morpheus, and not follow us in nightmares."
    layla "ONE."
    pause 1.0
    hans "Cognosce te Ipsum."
    scene white
    with dissolve
    layla "OPEN YOUR EYES."
    play sound portal_out
    python:
        ENDING_UNLOCKED = "good"
        register_ending_if_not_registered(ENDING_UNLOCKED)

    jump the_end

label normal_end:
    "I feel a warm light enshrouding me. The coma recedes. It’s time for us to return."
    me "Come on, Kurt. It’s time to go."
    kurt "Lord, I’ve been here forever…"
    "We are both professionals who know the protocol by heart. I don’t have to explain to him what to do."
    kurt "Who is at the system now? Layla? I hope she didn’t fall asleep at the control panel."
    me "Everything will be alright. Come on."
    "We both begin to raise our left hand slowly and smoothly. We focus all our attention on this action."
    "At this borderline level of Limbo, our consciousness still has access to the physical body."
    "With full concentration, we can do simple movements in the real world."
    "When we were both just learning to immerse in Limbo, mastering such “internal” gymnastics was included in the basic program of the course." 
    pause 1.0
    layla "Oh shit! They get out!"
    "Now somewhere in the patient’s room, the Limbo Technician sees the left arms of both comatose patients suddenly begin to rise up."
    "An unusual sight, I guess."
    layla "I see! I see you both, doc!"
    layla "Initiating the return procedure. Follow my voice."
    play sound blip
    pause 1.0
    $ renpy.music.set_volume(0.0, channel="fxloopm1")
    play fxloopm1 limbo_1
    $ renpy.music.set_volume(0.0, delay=2.0)
    $ renpy.music.set_volume(1.0, delay=2.0, channel="fxloopm1")
    kurt "No… I can’t do that…"
    "Kurt lowers his hand slowly. What is he doing ?!"
    kurt "You know, I seem to stay…"
    me "What?! Are you crazy?"
    layla "Return in FIVE."
    kurt "I can’t just go away. I have been living here with {i}HIM{/i} for a while. You have no idea what {i}HIM{/i} had to go through."
    me "Who are you talking about, Kurt?"
    hans "ABOUT ME"
    layla "Return in FOUR."
    layla "Doctor, why did Bachowski lower his hand? Is everything OK?"
    hans "I AM A PART OF THE SUBCONSCIOUSNESS OF KURT NOW. LIMBO MADE US ONE WHOLE."
    kurt "Sorry, [FIRST_NAME]!"
    me "I can’t believe it! We have come back from the deep Limbo, but the Thirty-one is still with us! How is this possible?!"
    layla "Return in THREE."
    layla "Doctor, if you can hear me, I can’t stop the process!"
    layla "If Bachowski is next to you, let him give a signal!"
    "Kurt’s face is full of pity, he is torn between the desire to break out into the real world and a sense of duty. Duty to whom? To an unknown homunculus?"
    "I can to catch his gaze. I catch a cold metallic glint in Kurt’s eyes, like Thirty-one’s."
    kurt "You see, he is going to stay with me when I go out! There will be {i}TWO PERSONS{/i} in me. How can I live with it? Think what could happen if he took control of my body!"
    me "I’m sure we can find a way out of this situation, Kurt!"
    kurt "I can’t risk! My family will be in danger next to me… And without them…"
    kurt "Better to just stay here."
    layla "Return in TWO."
    "It is not right. I almost pulled Kurt out."
    "I could bring him back if I tried harder!"
    kurt "Forgive me, my friend. Don’t forget what you’ve learnt here."
    me "Kurt, I’ll be back for you! Can you hear me?"
    hans "YOU HAVE TO DIVE MUCH DEEPER."
    "I don’t care what it takes. I’ll get my friend out of this bastard’s clutches."
    kurt "Tell Miriam that I love her…"
    layla "Return in ONE."
    stop music
    hans "SEE YOU SOON."
    scene white
    with dissolve
    layla "OPEN YOUR EYES."
    play sound portal_out
    $ ENDING_UNLOCKED = "norm"
    $ register_ending_if_not_registered(ENDING_UNLOCKED)
    jump the_end

label bad_end:
    "I feel a warm light enshrouding me. The coma recedes. It’s time for us to return."
    me "Come on, Kurt. It’s time to go."
    kurt "Lord, I’ve been here forever…"
    "We are both professionals who know the protocol by heart. I don’t have to explain to him what to do."
    kurt "Who is at the system now? Layla? I hope she didn’t fall asleep at the control panel."
    me "Everything will be alright. Come on."
    "We both begin to raise our left hand slowly and smoothly. We focus all our attention on this action."
    "At this borderline level of Limbo, our consciousness still has access to the physical body."
    "With full concentration, we can do simple movements in the real world."
    "When we were both just learning to dive in Limbo, mastering such “internal” gymnastics was included in the basic program of the course." 
    pause 1.0
    layla "Oh shit! They get out!"
    "Now somewhere in the patient’s room, the Limb Technician sees the left arms of both comatose patients suddenly begin to rise up."
    "An unusual sight, I guess."
    layla "I see! I see you both, doc!"
    layla "Initiating the return procedure. Follow my voice."
    play sound blip
    $ renpy.pause(delay=1.0, hard=True)
    stop music
    play sound door_slam
    show kurt limb2 at trans_epilogue_kurt_shift
    show the31 ok at trans_epilogue_hans_appear
    $ renpy.music.set_volume(1.0, channel="fxloopm1")
    play music limbo_0
    play fxloopm1 limbo_0_ol
    with hpunch
    hans "NOT SO FAST."
    $ renpy.pause(delay=0.5, hard=True)
    show kurt limb2 at trans_epilogue_kurt2
    show the31 ok at trans_epilogue_kurt2
    show white at trans_epilogue_bg2
    "The Thirty-one appears before us."
    "His touch is like an electric shock."
    "He grabbed both of our hands and dropped them."
    kurt "A-a-ah!"
    me "What the hell!"
    layla "Return in FIVE. What? What’s going on, doc?"
    kurt "He’s here, he won’t let us go!" 
    me "How did you escape? You should have stayed in Limbo!"
    hans "I TOLD YOU. THIS IS MY WORLD."
    hans "THE WHOLE LIMB IS MY PRISON…"
    $ renpy.sound.set_volume(0.3, channel="fxloop1")
    play fxloop1 medical_alert
    layla "CANCEL! CANCEL RETURN PROCEDURE!"
    hans "AND YOU’RE GOING TO STAY HERE WITH ME!"
    "It can’t be! It just can’t be!"
    layla "Doctor, if you can hear me, give a SIGNAL!"
    layla "If Bachowski is next to you, let him also give a SIGNAL!"
    $ renpy.sound.set_volume(0.0, delay=8.0, channel="fxloop1")
    "I try to raise my hand, but it is caught in the steel hand of the homunculus. Trying to do something else, but I’m paralyzed. The body is not responding."
    "Kurt is writhing in pain. I can hear Leila shouting out emergency instructions."
    "Is this really the end?"
    kurt "[FIRST_NAME]!"
    me "Resist, Kurt!"
    me "Don’t let him carry us away!"
    stop fxloop1
    show white at trans_epilogue_bg_fade
    show kurt at trans_epilogue_stabilize
    show the31 at trans_epilogue_stabilize
    "The bright light fades, and I feel a little dizzy. These are clear symptoms of immersion."
    "The Thirty-one takes us back to the deep Limbo."
    me "Let us go, you bastard!"
    show black_overlay at trans_epilogue_ovl
    show black_overlay at trans_epilogue_ovl_alpha20
    $ renpy.music.set_volume(0.8, delay=1.0)
    $ renpy.music.set_volume(0.8, delay=1.0, channel="fxloopm1")
    hans "I WAS LONELY FOR SO LONG."
    show black_overlay at trans_epilogue_ovl_alpha40
    $ renpy.music.set_volume(0.6, delay=1.0)
    $ renpy.music.set_volume(0.6, delay=1.0, channel="fxloopm1")
    hans "NOW I HAVE YOU."
    show black_overlay at trans_epilogue_ovl_alpha60
    $ renpy.music.set_volume(0.4, delay=1.0)
    $ renpy.music.set_volume(0.4, delay=1.0, channel="fxloopm1")
    hans "WE WILL NOT BE BORED, YOU’LL SEE."
    show black_overlay at trans_epilogue_ovl_alpha80
    hans "I HAVE SO MUCH TO SHOW YOU."
    show black_overlay at trans_epilogue_ovl_alpha100
    $ renpy.music.set_volume(0.0, delay=1.0, channel="fxloopm1")
    $ renpy.pause(delay=1.0, hard=True)
    stop fxloopm1
    narr_b "Leila, get me out. Please…"
    hans_b "CALM DOWN. THEY’LL SEND SOMEONE TO US SOON."
    $ ENDING_UNLOCKED = "bad"
    $ register_ending_if_not_registered(ENDING_UNLOCKED)
    jump the_end

label the_end:
    $ renpy.music.set_volume(0.0, delay=4.0)
    $ renpy.music.set_volume(0.0, delay=4.0, channel="fxloopm1")
    scene black
    with dissolve
    $ renpy.pause(delay=3.0, hard=True)
    jump credits