default GAME_SCORE = 0
define DEFAULT_FIRST_NAME = _("Alex")
define DEFAULT_LAST_NAME = _("Smith")
default FIRST_NAME = ""
default LAST_NAME = ""
default BELLA_TOLD_ABOUT_CYBER_HERALD = False

transform trans_bg_hero_house_1:
    xalign 0.0 yalign 0.0 maxsize (1920, 1920)
    1.0
    ease 7.0 yalign 0.4

# The game starts here.

label start:
    scene black
    $ renpy.music.set_volume(0, delay=0.5)
    $renpy.pause(delay=1.0, hard=True)
    $ renpy.pause(delay=1.0, hard=True)
    play music main_character
    $ renpy.music.set_volume(1.0, delay=2.0)
    ## TODO: Add nightmare sounds
    pause 1.0
    narr_b "What is it?"
    pause 1.0
    narr_b "Kurt, is it you?"
    pause 1.0
    narr_b "Kurt, I’m coming! Kurt!…"
    pause 1.0
    stop music
    play sound call_1
    notif_b "BZZZZZZZZ~~~~~~"
    pause 1.0

    scene bg hero_house at trans_bg_hero_house_1
    with dissolve
    $ renpy.pause(delay=2.0, hard=True)
    play sound call_1
    notif "BZZZZZZZZ~~~~~~"
    pause 1.0

    play music corporation fadein 2.0
    if current_language_needs_gender_selection():
        menu:
            "Looks like I saw a nightmare.{#female}":
                $ CHARACTER_GENDER = 0
            "Looks like I saw a nightmare.{#male}":
                $ CHARACTER_GENDER = 1
    else:
        "Was it a nightmare...?"
    "I thought I saw Kurt, he needed help."
    "Kurt’s an old friend, haven’t seen him for a while."
    "I thought I heard the phone ring…?"

    play sound show_tablet
    show screen tablet_base
    $ renpy.pause(delay=1.0, hard=True)
    play sound ok
    show screen tablet_iface_login
    $ renpy.pause(delay=1.0, hard=True)

    "This is my tablet."
    "I need to log in my name to get access to the corporate network."

    play sound ok
label tablet_log_in:
    $ FIRST_NAME = __(DEFAULT_FIRST_NAME)
    $ LAST_NAME = __(DEFAULT_LAST_NAME)
    call screen tablet_login(_("Enter First Name:"), VariableInputValue("FIRST_NAME", returnable=True))
    call screen tablet_login(_("Enter Last Name:"), VariableInputValue("LAST_NAME", returnable=True))
    call screen tablet_yesno(_("[FIRST_NAME]\n[LAST_NAME]\nInformation Correct?"))

    if not _return:
        jump tablet_log_in

    $ renpy.retain_after_load()

    show screen tablet_iface_login_success
    pause 1.0
    play sound ok
    show screen tablet_iface_missed_call(FIRST_NAME, _("Bella Rabinovich"))
    $ renpy.restart_interaction()
    pause 0.5

    "Oh, a missed call from Bella, my boss. I guess something’s wrong."

    pause 0.3
    hide screen tablet_iface_missed_call
    show screen tablet_iface_incoming_call(_("Bella Rabinovich"), "bella on tablet")

    play sound call_1 loop
    "Here she is again."
    "I better answer that."

    $ tablet_reset_call_time()
    show screen tablet_iface_active_call(_("Bella Rabinovich"), "bella on tablet")
    stop sound
    play sound call_answer
    pause 1.0

    bella "[FIRST_NAME], you’re awake! Finally!" 
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
    $ BELLA_TOLD_ABOUT_CYBER_HERALD = True

label end_of_dialog_1:
    play sound cancel
    hide screen tablet_iface_active_call
    $ renpy.pause(delay=0.7, hard=True)
    play sound show_tablet
    hide screen tablet_base

    pause 1.0

    "Time to go."

    show screen tablet_button

    $ add_doc("kurt_profile")
    menu:
        "Move to the express station":
            hide screen tablet_button
            play sound footsteps
            scene white
            with dissolve
            $renpy.pause(delay=1.0, hard=True)
            jump chapter_2
    
    return
