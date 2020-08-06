# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default FIRST_NAME = "Alex"
default LAST_NAME = "Smith"

init:
    transform trans_bg_hero_house_1:
        xalign 0.0 yalign 0.0 maxsize (1920, 1920)
        1.0
        ease 7.0 yalign 0.4

# The game starts here.

define bella = Character("Bella")
define me = DynamicCharacter("FIRST_NAME", color="#333333")

label start:

    scene black

    "TODO: Some bad nightmare is displaying here"
    "No, Kurth, NOOOOOOO!!!..."
    pause 1.0
    "{i}BZZZZZZZZ{/i}"
    pause 1.0

    $ renpy.pause(delay=0.5, hard=True)

    scene bg hero_house at trans_bg_hero_house_1
    with dissolve

    $ renpy.pause(delay=2.0, hard=True)

    pause 1.0
    "{i}BZZZZZZZZ{/i}"
    pause 1.0
    "Was it a nightmare?.."
    "It was Kurth. He's my old friend."
    "I haven't seen him for couple of years."
    "Have I heard a phone call?.."

    show screen tablet_base
    $ renpy.pause(delay=1.0, hard=True)
    show screen tablet_iface_login

    $ renpy.pause(delay=1.2, hard=True)

    "This is my tablet."
    "I need to enter my first and last name to log into the corporate network."

label tablet_log_in:
    call screen tablet_login(_("Enter First Name:"), VariableInputValue("FIRST_NAME", returnable=True))
    call screen tablet_login(_("Enter Last Name:"), VariableInputValue("LAST_NAME", returnable=True))
    call screen tablet_yesno(_("[FIRST_NAME]\n[LAST_NAME]\nInformation Correct?"))
    if not _return:
        jump tablet_log_in

    show screen tablet_iface_login_success
    pause 1.0
    show screen tablet_iface_missed_call(_("Bella Rabinovich"))
    $ renpy.restart_interaction()
    pause 0.5

    "Whoa, Bella is my boss. Something had happened."

    hide screen tablet_iface_missed_call

    show screen tablet_iface_incoming_call(_("Bella Rabinovich"), "bella on tablet")

    "Oh, great. She's calling again."
    "I should better answer the call."

    $ reset_call_time()
    show screen tablet_iface_active_call(_("Bella Rabinovich"), "bella on tablet")

    pause 1.0

    bella "Woke up already, [FIRST_NAME]?" 
    bella "No time for sleep, I have a mission for you."

    menu:
        "I don't know what happend, but I bet it will wait until I take my breakfast.":
            bella "You'll take your breakfast in the train."
        "I've seen a nightmare tonight.":
            bella "Looks like you're a prophet, huh?"
        "Some of our chiefs forgotten his safe password?":
            bella "No. The things are pretty serious this time."
    
    bella "Do you know the name Bachovsky?"
    bella "You should do, he's your classmate from the Academy."
    bella "Couple of hours ago he performed a very bad Morpheus dive. He was moved into the Western Office, and he is very unstable."
    bella "Go to the Western Office. I've mailed you his personal file, read it on the way."
    bella "His assistant is making a complete report on this case. She should send it to you in a hour."
    bella "I've ordered a train tickets, train leaves in 15 minutes. Hurry up."

    menu:
        "Yes, ma'am, affirmative, ma'am. Will send you a report upon arrival at the site.":
            jump end_of_dialog_1
        "Looks like things are bad indeed. More instructions, ma'am?":
            bella "Good that you asked. Our main priority is the information on this incident."
            bella "Kurth's life is important, of course, he is a valuable employee. But..."
            bella "If things will turn worse, you know the priorities."
        "But why me? Western Office has good specialists, they are at the site.":
            bella "Because he is our collegue, [FIRST_NAME]."
            bella "There is no one in the Western Office with such experience as yours. They just can't break into his head."
            bella "Also it's your chance to finally finish with that story on the Drake's case."
            bella "Hope you'll not fail this time."
    
    me "It will depend on the circumstances. I will not betray my principles."
    me "By the way, about the circumstances. Will I operate only with the personal file and the report?"
    bella "I'm giving you the extended permissions to access the Archive for this mission. Use it."
    bella "I will not be available until tomorrow, have to go to the Central Office for a meeting."
    me "Good luck, ma'am. I will mail you my report upon arrival to the Western Office."
    bella "Good luck, rather, you will need."
    bella "Check The Cyber News, there are some interesting articles today."
    bella "Bye."

label end_of_dialog_1:

    hide screen tablet_iface_active_call

    $ renpy.pause(delay=0.7, hard=True)

    hide screen tablet_base

    pause 1.0

    "Whoa. Time to go."

    return
