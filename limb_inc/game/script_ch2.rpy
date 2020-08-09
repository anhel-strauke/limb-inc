
define announcement = Character("Announcement", color="#3a539b")
define kz = Character("Kid", color="#5c97bf")

label chapter_2:
    scene bg express
    with fade

    pause 2.0
    $ add_email("violet-1")
    $ add_doc("kurt_profile")
    pause 1.0

    "A message? Oh yeah, it must be a report on the incident. I better read it."
    "And Bella told me about some news on the Cyber Herald website. Where is my tablet?.."

    $ show_tablet_modal()

    hide screen tablet_button

    pause 1.0
    "Kurt…"
    "How long we haven't seen each other? Three years, five? Time flies too fast now."
    "It seems that only yesterday we were celebrating our exams in the Academy. We discussed the limbo and the Diving Theory."
    "Too bad we lost each other when he moved into the North-West Branch."
    "I'm not a pro in the relationships on the long distance. Looks like Kurt too."
    "I remember that during all this time he sent me two mails. The last one was three years ago."
    "I think is should be stored in the Mail Server Archive. May be I should restore it?"
    
    $ TABLET_IS_DISABLED = True
    show screen tablet_base
    $ renpy.pause(delay=0.7, hard=True)
    $ tablet_run_app("")
    pause 1.0

    $ tablet_run_app("tablet_app_email")

    "Okay, to access Mail Archive I need to issue a voice command."
    me "Access to the Mail Server Archive. [FIRST_NAME] [LAST_NAME]. Confirmation."
    pause 0.5
    show screen tablet_mail_archive_entrance
    pause 1.0
    show screen tablet_mail_archive_granted
    pause 0.7
    show screen tablet_mail_archive_home

    "I can search the archive."

    show screen tablet_mail_archive_home_search
    pause 0.7

    call screen tablet_mail_archive_search
    pause 0.5
    call screen tablet_mail_archive_searching
    show screen tablet_mail_archive_search_result

    "That's it. A message from Kurt."

    show screen tablet_mail_archive_search_result_yes

    pause 0.7
    $ TAB_EMAIL_RECEIVED.append("kurt-old")

    call tablet_email_read("kurt-old") from _call_tablet_email_read
    $ tablet_run_app("tablet_app_email")
    announcement "Academy station! Stand clear of the closing doors please!"

    show kazimir ok at center

    hide screen tablet_app
    $ renpy.pause(delay=0.3, hard=True)
    hide screen tablet_base
    $ renpy.pause(delay=0.3, hard=True)
    $ TABLET_IS_DISABLED = False

    pause 1.0

    "A kid?"

    kz "So? What are you reading?"

    menu:
        "Are you talking to me?":
            kz "Oh, sorry! I seem to be mistaken."
            kz "And now there are no another seat for me. I have a fresh Pop Mech issue. I can share it to you as an apologize."
        "Nothing new. That dump landfill story." if "landfill" in CYBERHERALD_VISITED:
            kz "This is hot! By the way, my friend from the Math faculty made a statistical investigation about that landfill future."
            kz "Results are pretty interesting. I can share it to you, if you want!"
        "New cyberdog model released recently. Kid, have you ever seen a real dog?" if "cyberdog" in CYBERHERALD_VISITED:
            kz "Only in the videos. My father had one in his childhood. Wanna see? I can share it to you."
        "Sorry, kid, I have no time to talk.":
            kz "May be you interested in our commercial offer than? I can share it to you."

    "What a suspicious kid. May be he want to share me a virus?"

    $ TABLET_IS_DISABLED = True
    show screen tablet_base
    $ renpy.pause(delay=0.7, hard=True)
    hide kazimir
    call screen tablet_receive_file
    if _return:
        call screen tablet_receive_file_process
        call screen tablet_receive_file_process_complete
        call tablet_doc_read("secret") from _call_tablet_doc_read
        hide screen tablet_app
        $ renpy.pause(delay=0.3, hard=True)
        hide screen tablet_base
        $ renpy.pause(delay=0.3, hard=True)
        "Where did he go? What was it?"
        show screen tablet_base
        $ renpy.pause(delay=0.7, hard=True)
        show screen tablet_file_destroyed
        "What??? What do you mean “file deleted”?!"
        "This is a tablet with corporation-class protection! Nobody can remotely delete files from it!"
        hide screen tablet_app
        $ renpy.pause(delay=0.3, hard=True)
        hide screen tablet_base
        $ renpy.pause(delay=0.3, hard=True)
        $ TABLET_IS_DISABLED = False
        "What happened?"
        pause 2.0
        "Ah, nevermind. I have some time to rest or read something on a tablet."
    else:
        hide screen tablet_app
        $ renpy.pause(delay=0.3, hard=True)
        hide screen tablet_base
        $ renpy.pause(delay=0.3, hard=True)
        $ TABLET_IS_DISABLED = False
        "He's gone! I bet he is a small fraud. Luckily I rejected downloading."
        pause 2.0
        "All right. I have some time to rest or read something on a tablet."

    show screen tablet_button

    menu:
        "Take a nap":
            pass

    return

