label chapter_10:
    scene bg lab 
    with dissolve
    hide screen tablet_button

    show leyla ok at center with dissolve

    layla "Are you okay? The system registered enormous indicators deviation! It’s like Morpheus went crazy!"
    "Even through the eyelids a lamp above the examination table blinds me. It does not help the dizziness."
    "The heart is pounding like a hammer. Hearing Layla shout, I lift my head…"

    with hpunch
    notif "Gurrrrrrrrgle…"
    layla "Doctor…"
    "Coffee, biscuit and the sandwich I had on the train accompanied with gastric juice land on the floor. "
    with hpunch
    "Somebody kill me."
    layla "I’ll call a medic!"
    me "Don’t! Just bring me some water."
    show leyla ok at offscreenleft with move

    "While Layla went to the lobby for water, I’m trying to collect my thoughts. Kurt and that… Homunculus? Is that what they called themselves?"
    "Who are they? What is it?"
    "Some part of Kurt’s mind? A distinct personality? Maybe a result of Morpheus malfunctions?"
    notif "BZZZZZZZZ~~~~~~"
    "Damn… I hope it’s not her…"

    $ TABLET_IS_DISABLED = True
    show screen tablet_base
    $ renpy.pause(delay=0.7, hard=True)
    show screen tablet_iface_incoming_call(_("Bella Rabinovich"), "bella on tablet")
    $ renpy.pause(delay=1.0, hard=True)
    $ tablet_reset_call_time()
    show screen tablet_iface_active_call(_("Bella Rabinovich"), "bella on tablet")
    pause 1.0
    bella "Report back."
    bella "Oh. You look… not great."
    "I see my reflection on the tablet screen and feel sick again."
    me "It’s {i}MUCH{/i} worse than I expected."
    bella "Details."
    "I collect myself. A part of me still can’t believe what happened. I think corporate language would address it as “an emergency situation”."
    me "I met Kurt. To start with."
    bella "Great. It means his mind is stable and we can drag him back out. Why is he not with you?"
    me "Something is holding him back. To continue with."
    bella "You said “holding him back”?.."
    "I look at the tablet screen and hear Bella’s voice."
    "Despite the distance separating us I feel the concern that can easily transfer to dismay; it does not happen only because she has a backbone."
    me "Hard to explain. Won’t let go, controls, shuts the way out…"
    me "It’s not a part of Kurt’s mind, the intelligence level is too high."
    bella "Contacted?"
    me "Yes. Several times."
    bella "Able to describe the visuals?"
    me "There are no visuals. I mean, I haven’t seen it. Only heard."
    bella "How the intelligence level is shown?"
    me "Riddles. He played freaking riddles with me and Kurt!"
    bella "Maybe Kurt is into riddles and you met the projection of it in limbo."
    me "And said projection started to control limbo all of a sudden?"
    bella "What?.. It’s not possible."
    me "That’s what I’m thinking as well."
    "But I felt it. That tension, like a dark cloud hanging over me. It feels like this cloud is still here."
    me "This… something opened and closed portals between the layers of limbo. Somehow it caused Kurt to suffer from severe migraines."
    me "It kicked me out of limbo. I still don’t understand {i}HOW{/i}…"
    bella "Listen to me. I understand that you had to go through a very hard dive."
    bella "But Kurt is still there. With this… whatever it is."
    bella "And you are the only one who can drag him out of there."
    me "I need a rest."
    bella "A minute here is hours in limbo. Don’t forget that."
    bella "Collect all the info you can from the archive, Kurt’s friends and relatives. Maybe we’re missing something."
    bella "You are a professional; I believe you can work through this. Hanging up."
    me "Oooof…"
    hide screen tablet_iface_active_call
    $ renpy.pause(delay=0.7, hard=True)
    hide screen tablet_base
    $ TABLET_IS_DISABLED = False

    "I love this job."

    pause 1.0
    show leyla ok at center with move 
    layla "Here’s the water."
    me "Thanks, Layla."
    "My head feels better, but my “battery” is almost empty. I could use some caffeine-based stimulant right now."
    me "I’ll take a little walk before the next dive."
    layla "What? You’re going to dive again? In that condition? You need a check-up!"
    me "I have very little choice. Check-ups take loads of time and we don’t have any."
    me "I’m gonna dive until that dude on the left puts his left arm in the air."

    "Layla’s right. It’s a severe violation of the protocol. I’m risking myself and risking Kurt."
    "But maybe this is exactly what that something from limbo wants?"
    "Thinks that I won’t come again, chicken out and leave it as it is? Well in this case it’s gonna be surprised."

    pause 1.0

    jump chapter_11


