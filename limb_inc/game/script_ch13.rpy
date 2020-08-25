init:
    default LIMBO_3_SCORE = 3
    default LIMBO_3_MASK_ON = False
    default LIMBO_3_SUCCESS = False
    default L3_TOLD_ABOUT_ARTIFICIAL_HUMANS = False

    transform trans_bg_alpha0:
        alpha 0.0
    transform trans_bg_alpha20:
        ease 1.0 alpha 0.2
    transform trans_bg_alpha40:
        ease 1.0 alpha 0.4
    transform trans_bg_alpha60:
        ease 1.0 alpha 0.6
    transform trans_bg_alpha80:
        ease 1.0 alpha 0.8
    transform trans_bg_alpha100:
        ease 1.0 alpha 1.0
    transform left_from_center:
        yalign 1.0 xalign 0.35
    transform almost_almost_right:
        yalign 1.0 xalign 0.9
    transform almost_almost_left:
        yalign 1.0 xalign 0.1
    
    image the31 small:
        "the31 ok.png"
        zoom 0.8

label chapter_13:
    play music limbo_2 fadein 1.0
    scene black
    with dissolve
    show bg_limb3_1 at truecenter with dissolve
    $ LIMBO_3_SCORE = 3

    $ renpy.pause(delay=1.0, hard=True)
    "I… This place…"

    pause 1.0
    play sound footsteps_alt
    show violet limb at almost_right with dissolve
    vio "Doctor, patient is ready. We can start."
    "What patient? Am I on the operating table?"
    play sound footsteps_loud
    show kurt limb2 at left with dissolve
    stop sound
    kurt "Thanks, Violet."
    kurt "I thought these tough guys from the security service with their stupid briefing won’t let me in."
    "Kurt! It’s me, [FIRST_NAME]!"

    pause 1.0
    "Damn! I can’t make a sound! Is it a gag in my mouth or..."
    vio "Doc, you know these guys are hammers. And for the hammer everyone else seems to be a nail."
    kurt "Most certainly..."
    kurt "Well, we’ve got a standard procedure. Nullifying, phase one, everything as usual."

    pause 1.0
    kurt "Is the Morpheus ready?"
    vio "System is on, patient’s hooked up. I’ve run through the checklist, everything is normal."
    "Metallic frame of the Morpheus. I’m chained to the system. I’ve… I’ve dived just recently… How did I end up here?" 
    "Maybe I was sank in Limbo for all this time and now I’m back?.."

    pause 1.0
    kurt "Well, let us see."
    play sound ok
    kurt "Name: Hans Nicht. Age: nineteen. Gender: male. Hm-m-m…"
    vio "Something’s wrong, doc?"
    kurt "Look at him. Does not look like a “nineteen” to me. Neither I’d say he is male..."
    vio "Hah. Plastic surgery is galloping forward, doc. Today’s youth tend to have various body parts added or removed. As long as they have enough credit."
    kurt "I seem to be falling behind the fashion. Let us proceed…"

    pause 1.0
    play sound ok
    kurt "Criminal violation: misinformation and causing a property damage to the corporation."
    vio "I’ve always been amazed by your dedication to details. Does his crime make any difference to us, doc?" 
    vio "Let’s just dust off the Morpheus and nullify him. Our job is that simple."

    pause 1.0
    "It’s a swap. I’m inside a criminal’s body! How it is possible to happen in Limbo?!"

    pause 1.0
    show the31 small at center behind violet with dissolve
    ahans "An unpleasant situation. Right?"
    "What? It’s you! You should be in my place! I’m not Hans!"
    ahans "So do I. I’m Thirty-one. “Hans Nicht” is how the call us before nullifying."
    kurt "Violet, crack the full-face mask open. He is trying to say something."
    vio "Doctor, we have nothing to speak of with criminals."
    kurt "Violet, please remain the excellent assistant as you are and open the patient’s mask."
    play sound footsteps_alt
    show violet limb at offscreenright with move

    pause 1.0
    play sound clank_clank_chink
    notif "CLANK CLANK CHINK"
    $ renpy.pause(delay=0.5, hard=True)
    play sound footsteps_alt
    show violet limb at almost_right with move
    me "You must lie in here, not me, you scum!"
    vio "I’ve warned you."
    kurt "Interesting…"
    kurt "To whom you are addressing, if I may inquire?"

    menu:
        "To your assistant.":
            vio "Now that’s something new. Usually I’m asked to lay by."
        "To you, doctor.":
            kurt "Well, I’ve done nothing unlawful to nullify me… But this was a good joke. Bravo."
        "To that half-dead!":
            $ LIMBO_3_SCORE -= 1
            kurt "Whom you are speaking about? There is only three of us in this room."
    # 2 scores left

    show the31 small at left behind kurt with dissolve
    show bg_limb3_2 behind violet, kurt, the31 at truecenter, trans_bg_alpha0
    show bg_limb3_2 at trans_bg_alpha20
    hans "You fool. You brainless meat. They can neither see nor hear me."
    show bg_limb3_2 at trans_bg_alpha40
    hans "This is my Limbo."
    show bg_limb3_2 at trans_bg_alpha60
    hans "My world."
    show bg_limb3_2 at trans_bg_alpha80
    hans "My jail."
    show bg_limb3_2 at trans_bg_alpha100
    hans "Both doctor and you are inside it. And that means you are going to play by my rules…"
    me "What are you trying to get? I’ve done nothing to you!"
    vio "Maybe I should close his mouth, doctor?"
    kurt "Everything’s fine, Violet."
    kurt "Look, Hans Nicht, I am here to conduct a special procedure. You have done nothing to me but I must execute a direction I was given…"

    show the31 small at center behind violet with dissolve
    hans "So you wanted to know the truth? Here it is."
    hans "Here’s what happened back then."
    hans "Feel what I’ve felt when they chained me to the bed, put the helmet on my head, and closed my mouth."
    hide bg_limb3_1

    menu:
        "I need to retrieve my friend, get him back!":
            hans "Friend?… Maybe I’ll let you to do this, but first…"
        "Release me, please!":
            $ LIMBO_3_SCORE -= 1
            hans "I was asking, threatening and begging too… Did they have mercy on me? I want you to tell me that."
        "Go to hell you sick bastard!":
            $ LIMBO_3_SCORE -= 1
            hans "Trying to turn me responsible for your death? You humans are so pathetic."
    # 1 score left

    vio "Hey, Hans — one more word and I’ll forget to inject you an anesthesia before the procedure."
    kurt "Violet, you are the woman of science!"
    kurt "Sometimes it seems that you come to the Limbo department just recently…"
    pause 1.0
    hans "To ask, to beg, to trade and to promise is not enough… You need to have a will to {i}live{/i}."
    hans "Show me how a human can WILL TO LIVE."
    hans "If you succeed and won’t be nullified by Kurt — you will know the truth for which you dived the Limbo so deep."
    hans "And — who knows — perhaps you will manage to save your friend."
    hide the31 with dissolve
    "This creature. It’s not a Kurt’s cautiousness projection for sure. He’s… a foreigner. A someone else’s mind trapped inside the deep level of Limbo."
    "But how is that possible?"

    pause 1.0
    play sound blip
    vio "I’ve plugged in and checked the contacts. Morpheus system is entirely ready, doc. We can start."
    kurt "Thank you, Violet."
    kurt "Put a mask on him to save his teeth."

    "I wonder what happens if Kurt will complete a nullifying procedure. Is it a truth that creature had said?" 
    "If it is so, me and Kurt will be stuck at this level of Limbo forever and nobody will bring us back to the real world."

    play sound footsteps_out
    show violet limb at offscreenright with move
    pause 1.0

    $ LIMBO_3_MASK_ON = True
    menu:
        "Please don’t!":
            $ LIMBO_3_SCORE -= 1
            vio "Calm down. It will end before you even notice."
        "Wait, doctor! I need to tell you something important!":
            pass
        "You’re bluffing you freak! Nothing will happen!":
            $ LIMBO_3_SCORE -= 1
            show the31 small at center behind kurt with dissolve
            hans "Ha-ha-ha! You will find out soon!"
            hide the31 with dissolve

    if LIMBO_3_SCORE <= 0:
        jump limb_3_dropout
    
    kurt "Violet, wait."
    $ LIMBO_3_MASK_ON = False
    play sound footsteps_alt
    show violet limb at almost_right with move
    
    pause 1.0

    show the31 small at center behind kurt with dissolve
    show bg_limb3_3 behind violet, kurt, the31 at truecenter, trans_bg_alpha0
    show bg_limb3_3 at trans_bg_alpha40
    hans "Nice try. What you will do next?"
    show bg_limb3_3 at trans_bg_alpha60
    kurt "What’s the problem, Hans?"
    show bg_limb3_3 at trans_bg_alpha100

    $ L3_TOLD_ABOUT_ARTIFICIAL_HUMANS = False
    menu:
        "I’m not a regular human. I am an artificially grown homunculus!" if L2_HEARD_HOMUNCULUS:
            kurt "Ho-munculus?… I’ve heard that before somewhere."
            $ L3_TOLD_ABOUT_ARTIFICIAL_HUMANS = True
        "I’m not a regular human. I am an artificially grown Gorukula!" if not L2_HEARD_HOMUNCULUS:
            kurt "Go-ru-what? You’re kidding me, right?"
            $ LIMBO_3_SCORE -= 3
        "I have some highly important information!":
            $ LIMBO_3_SCORE -= 1
            vio "Yes-yes, some info of a global importance. You should call for the corporation CEO right now…"
        "You are Kurt, and you are Violet — I know you and you know me!":
            $ LIMBO_3_SCORE -= 1
            hans "Ha-ha-ha!"
    hide bg_limb3_2
    if LIMBO_3_SCORE <= 0:
        jump limb_3_dropout

    show bg_limb3_4 behind violet, kurt, the31 at truecenter, trans_bg_alpha0
    show bg_limb3_4 at trans_bg_alpha20
    hans "Nullifying is an unattainable luxury."
    show bg_limb3_4 at trans_bg_alpha40
    hans "They could just have me wasted, but it would cost the corporation a fair sum."
    show bg_limb3_4 at trans_bg_alpha80
    hans "And they still can find a use for my healthy organs."
    show bg_limb3_4 at trans_bg_alpha100
    hide the31 with dissolve
    
    pause 1.0

    if L3_TOLD_ABOUT_ARTIFICIAL_HUMANS:
        kurt "Artificial human… Yes, there was something like that."
        kurt "Which explains that strange appearance of yours and a lack of sexual identity…"
    else:
        kurt "Hm-m-m… I’ve just remembered something."
        kurt "He looks like an artificial human… Yes, there was something like that."
        kurt "Which explains his strange appearance and a lack of sexual identity…"
    vio "You are not going to believe in that rumour, doc."
    kurt "I remember an informational explosion about ten years ago. They were writing about some farms that days… Homunculus protection movement was forming…"
    kurt "Yes, that’s how they were called."
    vio "Sleazes like this are common enough to appear at my social media page for several times a day."  
    vio "Does it change our job somehow, doc?"
    "I’ve managed to plant a grain of doubt in him. Means me being on the right track."
    "That… human, or homunculus, it doesn’t matter — I’m curious if it was acting the same?"
    hide bg_limb3_3

    pause 1.0
    kurt "Violet, if he, or she, or it is a biologically reproduced human, than nullifying can cause some serious consequences." 
    vio "Which ones, doctor? He’ll stutter for the rest of his life?"
    kurt "Perhaps. And it is also possible for us to end up responsible for boiling his brain up."
    kurt "It’s the first time I meet a… homunculus. And I’m not able to predict the consequences of a procedure by hundred percent."
    vio "You are exaggerating, Doctor Bachowski! Structure of his tissues has no difference from the human one!" 
    vio "Being born in a bulb does not make him any special for the Morpheus system."

    menu:
        "Dive the Limb, doc, and you will know it all.":
            $ LIMBO_3_SCORE -= 1
            show the31 small at center behind kurt, violet with dissolve
            hans "You must not expose your desire. You need to learn so much…"
            hide the31 with dissolve
        "My brain consists of an artificial tissue. System will not work with a material like this.":
            $ LIMBO_3_SCORE -= 1
            vio "One of the Morpheus’ sensing units is for identifying any departures from the norm or pathologies the patient have."
            vio "If you were quite a different breed — we would knew it already."
        "I’m a human, doc. Yes, I was grown at a specialised farm. But I am {i}human{/i}.":
            kurt "I can see that."
    if LIMBO_3_SCORE <= 0:
        jump limb_3_dropout
    
    show the31 small at left behind kurt with dissolve
    hans "For a human it’s complicated to perceive a different world picture. They think in cliches, build up an illusory world of their own." 
    hans "And this is when you come in. You destroy their comfort with your knowledge and they hate you enough to be ready to kill."
    "No. Kurt is different. I believe in him."
    kurt "Tell me about these farms, Hans. What is going on there?"
    show the31 small at center behind violet with dissolve
    show bg_limb3_5 behind violet, kurt, the31 at truecenter, trans_bg_alpha0
    show bg_limb3_5 at trans_bg_alpha40
    with hpunch
    hans "No! No! I don’t want to get back there!…"
    show bg_limb3_5 at trans_bg_alpha100
    vio "This is beyond our duty, doctor! There is a job description..."
    kurt "Your job description is to follow my instructions!"
    kurt "Hans Nicht, are the homunculi farms real and what’s going on there?"
    hans "Go on. Tell him."
    hide the31 with dissolve

    menu:
        "They are. I was caught trying to escape from there.":
            show the31 small at center behind kurt with dissolve
            hans "Great. Exactly what he wanted to hear."
            hide the31 with dissolve
        "It is a fictional place made up for scaring the criminals.":
            $ LIMBO_3_SCORE -= 1
            kurt "And am I supposed to believe in that?"
        "You’ll need to dive in limbo with me to know this, doc":
            $ LIMBO_3_SCORE -= 1
            vio "He’s provoking you, doc. Don’t bite it!"
    hide bg_limb3_4
    if LIMBO_3_SCORE <= 0:
        jump limb_3_dropout
    
    $ renpy.sound.set_volume(0.0, channel="fxloopm1")
    play fxloopm1 limbo_2_ol
    $ renpy.sound.set_volume(1.0, delay=2.0, channel="fxloopm1")
    kurt "Nullifying is off."
    play sound footsteps_alt
    show kurt at left_from_center with move

    pause 1.0
    kurt "Violet, prepare the Morpheus for a dive. I will try to figure out a homunculus’ consciousness from the inside and change his behaviour patterns."
    show violet limb at almost_almost_right with move
    vio "You… You can’t! You just can’t do it! He is a criminal!"
    kurt "And he’s also a human, Violet. Just like us. Even more human than us!"
    kurt "Look at him. It’s terrifying for me to imagine what’s going on in this place they call “farms” if Hans had to escape it."
    vio "Bachowski, you are sacrificing your career for the sake of a human you even don’t know! And the “human” part is an open question."
    kurt "Maybe I’m sacrificing something more than my career. But I won’t be able to go on living after doing that."
    play sound footsteps_out
    show kurt at offscreenleft with move
    pause 1.0
    play sound blip
    $ renpy.sound.set_volume(0.6, channel="fxloop3")
    play fxloop3 "<loop 18.672>audio/morpheus_1.ogg"
    kurt "I’m ready. Fix a helmet on the patient and prepare a dive to Limbo!"
    vio "All right, doctor..."
    play sound footsteps_alt
    show violet at center with move
    pause 1.0
    play sound blip
    show the31 ok at almost_almost_left with dissolve
    hans "Congratulations. You made it."
    $ renpy.pause(delay=0.5, hard=True)
    show violet limb_gun
    $ renpy.pause(delay=0.7, hard=True)
    stop fxloopm1
    stop fxloop3
    play sound single_shot
    show white at trans_limb1_shoot
    $ notif(_("{fast}BANG!"), interact=False, advance=False)
    with hpunch
    $ notif(_("{fast}BANG!"), interact=False, advance=False)
    $ renpy.pause(delay=0.1, hard=True)
    hide the31
    hide kurt
    hide violet
    hide bg_limb3_1
    hide bg_limb3_2
    hide bg_limb3_3
    hide bg_limb3_4
    hide bg_limb3_5
    $ notif(_("{fast}BANG!"), interact=False, advance=False)
    $ renpy.pause(delay=0.9, hard=True)
    hide white
    hide window
    
    $ renpy.sound.set_volume(0.1, channel="fxloop1")
    play fxloop1 medical_alert

    hans "A-a-h!"

    "DAMN! She shot my head at the exact moment of dive."
    "My consciousness had already been flown to Limbo, but it was not enough to make a strong connection to the system."
    "That’s why Morpheus have had a malfunction and Kurt Bachowski went into coma."
    "But I am not me…"
    "I am him. And now this is his world. Forever."
    stop fxloop1
    $ renpy.music.set_volume(0.0, delay=2.0)
    $ renpy.pause(delay=4.0, hard=True)

    $ LIMBO_3_SUCCESS = True

    jump epilogue

label limb_3_dropout:
    pause 1.0
    kurt "All right."
    $ renpy.sound.set_volume(0.6, channel="fxloop3")
    play fxloop3 "<loop 18.672>audio/morpheus_1.ogg"
    if not LIMBO_3_MASK_ON:
        kurt "Violet, put the mask on him."
        play sound footsteps_out
        show violet limb at offscreenright with move
        $ renpy.pause(delay=1.0, hard=True)
        play sound clank_clank_chink
    kurt "On my command, start the nullifying process phase one."
    "No, no, noooo!"
    if LIMBO_3_MASK_ON:
        play sound footsteps_alt
        show violet limb at almost_right with move
    $ renpy.pause(delay=1.0, hard=True)
    play sound blip
    kurt "Now."

    play sound portal_out_emerg
    stop fxloop3
    $ LIMBO_3_SUCCESS = False
    scene black
    with dissolve
    $ renpy.music.set_volume(0.0, delay=2.0)
    $ renpy.pause(delay=4.0, hard=True)
    jump epilogue