init:
    default WAITING_FOR_BORIS_RESPONSE = False
label chapter_3:
    hide screen tablet_button
    scene bg corp_hall
    with dissolve

    pause 1.0
    "This is the Western Branch neural research department lobby."
    "Why, it’s Miriam."

    show miriam ok at center with dissolve
    mir "My goodness, [FIRST_NAME], is it really you? They said they would send someone to take care of Kurt!"
    mir "I’m so glad it’s you! You can bring him back out, can’t you?"

    menu:
        "Hello, Miriam! It’s really been a while! I wish we’d meet in better circumstances.":
            me "I know, now is not a great time but I have to talk to you about Kurt."
            mir "Sure! I’ll do my best to help! You can ask me anything."
            jump chapter_2_continue_with_miriam
        "Oh, Miriam, of course I’ll try to drag him out. That’s exactly why I’m here!":
            me "And it’s good you’re here too, we need to talk before I take the dive."
            mir "Sure! I’ll do my best to help! You can ask me anything."
            jump chapter_2_continue_with_miriam
        "Hello, Mrs. Bachowski. Unfortunately, my priority is to get the information…":
            me "…Although I will of course try to save the patient’s life. I have a few questions for you."
            show miriam angry with dissolve
            mir "Are you really going use that tone with me?"
            mir "You can list your questions and send in an official request."
            mir "I have no wish to continue this conversation."
            hide miriam with dissolve
            pause 2.0
            notif "BZZZZZZZZ~~~~~~"
            "Oh, a phone call."
            jump chapter_2_boris_calling

default miriam_questions_asked = set()

label chapter_2_continue_with_miriam:
    if len(miriam_questions_asked) < 2:
        menu:
            "Talk about Kurt's childhood" if "childhood" not in miriam_questions_asked:
                me "Do you think Kurt has any strong childhood memories?"
                mir "Oh, you know, Kurt loves to talk about trees and plants, flowers and mushrooms. I think he misses the forest."
                mir "We used to visit the eco-zone when Kurt worked in the North-West Branch but he said it’s nothing like the real thing."
                mir "There aren’t even real mushrooms."
                $ miriam_questions_asked.add("childhood")
                jump chapter_2_continue_with_miriam
            "Talk about Kurt's fears" if "fears" not in miriam_questions_asked:
                me "Is Kurt afraid of anything?"
                mir "That’s a difficult question, …"
                mir "…"
                mir "I think he was never afraid of anything or anyone. Except his father."
                mir "But he didn’t talk about it much. Maybe something happened between them in the past."
                $ miriam_questions_asked.add("fears")
                jump chapter_2_continue_with_miriam
            "Talk about Kurt's bad memories" if "memories" not in miriam_questions_asked:
                me "Do you think Kurt has any memories he doesn’t like?"
                mir "I think he doesn’t like that part of your work – with criminals. Where you completely erase their personality using Morpheus."
                mir "I think it’s called “the nullifying”. He’s always looks very glum after these assignments."
                $ miriam_questions_asked.add("memories")
                jump chapter_2_continue_with_miriam
    else:
        notif "BZZZZZZZZ~~~~~~"
        mir "You have a call, must be important. And I only have a couple of minutes of visiting time left."
        mir "We can talk later."
        hide miriam with dissolve

label chapter_2_boris_calling:
    $ TABLET_IS_DISABLED = True
    show screen tablet_base
    $ renpy.pause(delay=0.7, hard=True)
    show screen tablet_iface_incoming_call(_("Boris (Archivist)"), "boris on tablet")
    $ renpy.pause(delay=1.0, hard=True)
    $ tablet_reset_call_time()
    show screen tablet_iface_active_call(_("Boris (Archivist)"), "boris on tablet")
    pause 1.0
    boris "You can lead a horse to water, but you can't make him drink, as they say!"
    boris "Miriam Bachowski’s personal file is already in your “Documents” app."
    $ add_doc("miriam_profile", silent=False)
    boris "You have full access to the Archive for several hours but I still have no requests from you – you’re breaking my muscle!"
    menu:
        "Stop playing around with idiomatic expressions!":
            me "You can’t change them! Heart! “You’re breaking my heart!”"
            boris "Sounds ambiguous, doctor [LAST_NAME]."
            me "Here we go again! I’ll send you a couple of requests later. Bye!"
        "Sorry, Boris, I was too busy to get my hands on the Archive.":
            boris "This statement is incorrect. You can send a request by voice command."
            me "Here we go again! I’ll send you a couple of requests later. Bye!"
        "I do have a request for you actually." if "secret" in TAB_DOCS_READ:
            me "Can you give me all information on a perpetrator Hans Nicht? ID unknown."
            boris "Request received. Estimated time to answer: 12 minutes 47 seconds."
            boris "The answer will be sent to “Documents” app on your tablet."
            $ WAITING_FOR_BORIS_RESPONSE = True
            me "Thanks, Boris. Bye."
    hide screen tablet_iface_active_call
    $ renpy.pause(delay=0.7, hard=True)
    hide screen tablet_base
    $ TABLET_IS_DISABLED = False
    show screen tablet_button
    menu:
        "Move to the patient’s room":
            jump chapter_4
