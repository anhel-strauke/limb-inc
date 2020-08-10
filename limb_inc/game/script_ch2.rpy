label chapter_2:

    scene bg express
    with fade

    pause 2.0
    $ add_email("violet-1")
    $ add_doc("kurt_profile")
    pause 1.0

    "A message? Ah, yes, that must be the incident report. I should have a look at that."
    if BELLA_TOLD_ABOUT_CYBER_HERALD:
        "And articles in the “Herald”, Bella said, on their website. Let’s see, where’s my tablet…?"

    $ show_tablet_modal()

    hide screen tablet_button

    pause 1.0
    "Kurt…"
    "How long has it been? Three years? Five? Time flies so fast these days."
    "Feels like only yesterday we celebrated passing the exams, discussing and arguing about Limbo and Dive theory."
    "It’s a shame we didn’t stay in touch after his transfer to the North-West Branch."
    "But what can you do – I’m not good with long distance relationships. Looks like neither is Kurt."
    "In all this time, I think he only wrote me twice, last time – three years ago."
    "Maybe it’s still somewhere in the mailing archives. I’ll see if I can find that letter."
    
    $ TABLET_IS_DISABLED = True
    show screen tablet_base
    $ renpy.pause(delay=0.7, hard=True)
    $ tablet_run_app("")
    pause 1.0

    $ tablet_run_app("tablet_app_email")

    "Okay, to get to the archives I need a voice command."
    me "Access to the Mail Server Archive. [FIRST_NAME]. [LAST_NAME]. Confirm."
    pause 0.5
    show screen tablet_mail_archive_entrance
    pause 1.0
    show screen tablet_mail_archive_granted
    pause 0.7
    show screen tablet_mail_archive_home

    "I should use the search."

    show screen tablet_mail_archive_home_search
    pause 0.7

    call screen tablet_mail_archive_search
    pause 0.5
    call screen tablet_mail_archive_searching
    show screen tablet_mail_archive_search_result

    "Aha, here it is. Kurt’s letter."

    show screen tablet_mail_archive_search_result_yes

    pause 0.7
    $ TAB_EMAIL_RECEIVED.append("kurt-old")

    call tablet_email_read("kurt-old") from _call_tablet_email_read
    $ tablet_run_app("tablet_app_email")
    announcement "This station is “Academy”. The next station is “West Branch”. Please mind the closing doors!"

    show kazimir ok at center

    hide screen tablet_app
    $ renpy.pause(delay=0.3, hard=True)
    hide screen tablet_base
    $ renpy.pause(delay=0.3, hard=True)
    $ TABLET_IS_DISABLED = False

    pause 1.0

    "Kid?"

    kid "Hey, how’s it going? What’s new?"

    menu:
        "Are you talking to me?":
            kid "Oh, sorry! I thought you were someone else."
            kid "And there’re no other seats free now. I have the latest issue of “Popular Mechanics” I can share as an apology."
        "Nothing new, another fight over the recycling landfill site." if "landfill" in CYBERHERALD_VISITED:
            kid "Hot stuff! By the way, a friend of mine from Math Methods faculty did a statistic estimation on the future of the landfill. Wanna see? I can flick you the file."
        "The new cyberdog model is out. Have you ever seen a real dog, kid?" if "cyberdog" in CYBERHERALD_VISITED:
            kid "Only on video. Dad used to have one when he was a kid, he showed me. Do you wanna see?"
        "Sorry, kid. Can’t talk right now.":
            kid "Then maybe I can interest you with our commercial offer? I can flick it to your tablet, if you want."

    "What a suspicious kid. Hope he’s not trying to slip me a virus."

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
        "Where did he go? What the hell was that?"
        show screen tablet_base
        $ renpy.pause(delay=0.7, hard=True)
        show screen tablet_file_destroyed
        "What??? What do you mean “file deleted”?!"
        "This tablet has corporate-class defence system, you can’t just delete a file in here!"
        hide screen tablet_app
        $ renpy.pause(delay=0.3, hard=True)
        hide screen tablet_base
        $ renpy.pause(delay=0.3, hard=True)
        $ TABLET_IS_DISABLED = False
        "What's going on?"
        pause 2.0
        "Oh, well. I still have a little time to read the files and rest."
    else:
        hide screen tablet_app
        $ renpy.pause(delay=0.3, hard=True)
        hide screen tablet_base
        $ renpy.pause(delay=0.3, hard=True)
        $ TABLET_IS_DISABLED = False
        "He's already gone! Typical little rascal. Good thing I didn’t let him “flick” anything."
        pause 2.0
        "Excellent! I still have a little time to read the files and rest."

    show screen tablet_button

    menu:
        "Take a nap":
            hide screen tablet_button
            scene black
            with dissolve
            pause 3.0
            announcement "We will shortly be arriving at: “Western Branch”. This train terminates here. All change please!"
            "So, here I am."
            jump chapter_3
    return

