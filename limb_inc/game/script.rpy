default FIRST_NAME = "Alex"
default LAST_NAME = "Smith"

transform trans_bg_hero_house_1:
    xalign 0.0 yalign 0.0 maxsize (1920, 1920)
    1.0
    ease 7.0 yalign 0.4

# The game starts here.

define bella = Character("Bella")
define me = DynamicCharacter("FIRST_NAME", color="#333333")
define narrator = Character(what_italic=True)

label start:
    scene black
    "{b}TO DO:{/b} Some bad nightmare is displayed here, waiting for the art"
    "{b}TO DO:{/b} Like “No, Kurt, NOOOOOOO!!!...” (or something like this, idk)"
    pause 1.0
    "{i}BZZZZZZZZ~~~~~~{/i}"
    pause 1.0

    scene bg hero_house at trans_bg_hero_house_1
    with dissolve
    $ renpy.pause(delay=2.0, hard=True)
    "{i}BZZZZZZZZ~~~~~~{/i}"
    pause 1.0
    "Was it a nightmare...?"
    "I thought I saw Kurt, he needed help."
    "Kurt’s an old friend, haven’t seen him for a while."
    "I thought I heard the phone ring…?"

    show screen tablet_base
    $ renpy.pause(delay=1.0, hard=True)
    show screen tablet_iface_login
    $ renpy.pause(delay=1.0, hard=True)

    "This is my tablet."
    "I need to log in my name to get access to the corporate network."

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

    "Oh, a missed call from Bella, my boss. I guess something’s wrong."

    hide screen tablet_iface_missed_call
    pause 0.3
    show screen tablet_iface_incoming_call(_("Bella Rabinovich"), "bella on tablet")

    "Here she is again."
    "I better answer that."

    $ tablet_reset_call_time()
    show screen tablet_iface_active_call(_("Bella Rabinovich"), "bella on tablet")

    pause 1.0

    bella "[FIRST_NAME], you're awake! Finally!" 
    bella "No time to lose, you have an urgent case."

    menu:
        "I don’t know what it is but I think it can wait ‘til after breakfast.":
            bella "You’ll eat on the express."
        "I just had a horrible dream.":
            bella "What are you, a psychic now?"
        "Somebody from high command forgot their password again?":
            bella "This time it’s serious."
    
    bella "Does the name Bachowski ring a bell?"
    bella "You should remember him from the Academy."
    bella "He took a bad {i}dive{/i} a couple of hours ago, he’s in the West Branch now – very unstable."
    bella "I want you to go there ASAP. I sent you his profile, you can look at it on the way."
    bella "His assistant is already writing a full report on the incident. She’ll send it to you in a few minutes."
    bella "I got you a pass for the express departing in 15 minutes. You better hurry. "

    menu:
        "Understood. I’ll call you when I get there.":
            jump end_of_dialog_1
        "This does sound serious. Any further instructions?":
            bella "Since you asked – the priority here is to get information about the incident."
            bella "Kurt’s life is important too, of course, he’s a valuable employee, but…"
            bella "If something goes wrong… well, I think you understand."
        "But why me? West Branch has its specialists and they’re already there.":
            bella "Because he’s our colleague, [FIRST_NAME]."
            bella "Nobody from West Branch is experienced enough to break into his head."
            bella "And also, because this is an excellent chance to cover up that case with Drake."
            bella "I hope you won’t screw up this time?"
    
    me "It will all depend on the circumstances. In any case, I’ll stand by my principles."
    me "Talking of circumstances – I’ll just have the profile and the report?"
    bella "I gave you full access to the Archive for the duration of the investigation, use that."
    bella "I’ll be out ‘til tomorrow, going to the Central Office for a meeting. I have to go now."
    me "Good luck, ma’am! I’ll send you a report when I get to West Branch."
    bella "You’re the one who will need luck!"
    bella "If you’ll have the time, have a look at today’s “Cyber Herald” – couple of interesting articles there."

label end_of_dialog_1:
    hide screen tablet_iface_active_call
    $ renpy.pause(delay=0.7, hard=True)
    hide screen tablet_base

    pause 1.0

    "Time to go."

    show screen tablet_button

    menu:
        "Go to the express station":
            hide screen tablet_button
            jump chapter_2
    
    return
