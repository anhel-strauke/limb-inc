label chapter_11:
    hide screen tablet_button
    scene bg corp_hall
    with dissolve

    "I walk into the lobby of the neural research department. I focus on my movement and lean against the wall to keep from falling. My legs and arms are shaking."

    akz "You do not understand!"

    "I am so focused on myself that at first I do not notice the quarrel that erupted in the center of the room."

    mir "Kaz, listen to me!"

    "A young, strangely dressed guy snatches up with his mother. I look closely and find out…"

    me "You!"

    show kazimir ok at almost_right with dissolve
    show miriam ok at almost_left with dissolve

    me "You are that kid! From the train!"
    "I see a guy getting angry. It looks like he recognized me."
    mir "[FIRST_NAME], it’s Kazimir, our son."
    "Son? Kurt said he has a son? Surely he told in letters that I never read…"
    me "Hello Kazimir. My name is [FIRST_NAME], I…"
    kz "You are dad’s friend. I know. I know that you also work for these slave owners."
    show miriam sad with dissolve
    mir "Kaz, stop it!"
    "Youthful maximalism… I miss this time."
    "But it’s time to end the concert. The security guards started throwing unkind glances in our direction."
    me "Miriam, could you leave Kazimir and me for a minute?"
    show miriam ok with dissolve
    mir "Okay. Be stricter with him."
    show miriam angry with dissolve
    mir "Kaz, if I find out you were rude with [FIRST_NAME]…"
    me "Everything will be all right, Miriam. I assure you."
    hide miriam with dissolve

    me "So. What did you want from me on the train?"
    show kazimir facepalm with dissolve
    if "secret" in TAB_DOCS_READ:
        kz "I sent you a file. You forgot?"
        me "Refresh my memory."
    else:
        kz "I wanted to share you a file."
        me "What was it?"
    show kazimir ok with dissolve
    kz "I learned about one name. Hans Nicht. There is no such name."
    me "Interesting. How did you come up with this?"
    kz "Sorry, I can’t chat long in this slave office. I can only say that I have friends who can share information."
    me "Clear. How did you and your friends know that Hans Nicht doesn’t exist?"
    kz "We have our own methods. Here’s what you need to know."
    kz "This name appears frequently in internal corporate records that you will never see. This is the name of typical criminals, fugitives and sometimes corporate employees."
    me "What for?"
    kz "I don’t know yet. But I know that all these people have one thing in common."
    me "I’m listening carefully, Kaz."
    kz "First, promise me something."
    me "What promise?"
    kz "Promise me that you will bring my dad back from the coma."
    me "I promise to bring your father back."
    kz "Yeah. Okay."
    kz "In short, all these dudes are associated with a certain place."
    kz "Someone killed someone there, someone stole, but most of the Hans Nichts simply fled from there. It seems that everyone who escaped is found and, as my dad says, nullified."
    me "Interesting…"
    me "What is known about this place?"
    kz "Almost nothing."
    kz "All that I managed to dig was a few satellite images. Buildings are depicted there, something like barracks. There are no such structures on the official maps. And this is weird."
    "Strange buildings, barracks…"
    me "What’s the name of this place?"
    kz "I have no idea. But the guys from our team, that is…"
    kz "My friends mention in the ancient news about strange farms in different parts of the country, where they found superhumans, or something. But this is one hundred percent fake."
    me "Superhumans?"
    kz "Something like that. There was such a strange name mentioned… Gorukula or murkola, something like that."
    me "Homunculi?"
    kz "Yes! Exactly!"
    kz "Okay I have to go. Remember the promise!"

    hide kazimir with dissolve

    pause 1.0

    "I drink my third glass of coffee at the machine. I digest information."
    "He said exactly “Homunculus” and Kaz remembered this word. Coincidence?…"
    show violet interested at almost_right with dissolve
    vio "Have you already talked to Kazimir? That horrible family, right?"
    "Violet appeared so unexpectedly that I almost spilled coffee from a paper cup."
    me "And you know how to make an impression, Violet."
    vio "That’s not why I’m here, to be honest. I just wanted to tell you to ask limbo tech about Morpheus and her experiments with him."
    me "What do you have in mind? Can you be more specific?"
    vio "You will find out for yourself. Good luck."
    hide violet with dissolve

    show screen tablet_button
    $ add_email("boris_violet_file")
    menu:
        "Return to the patient’s room":
            jump chapter_12



    
