label chapter_12:
    scene bg lab
    with dissolve
    hide screen tablet_button

    show leyla ok at center with dissolve

    layla "How are you feeling? You look 10 percent better."
    me  "Thank you, Leila. This is the best compliment I’ve ever received."
    "Someone removed my vomit from the floor."
    "There are some medications and stimulants on the couch."
    me "Did you put that in case of my pass out?"
    layla "Yeah. So as not to run around the building looking for a medic later."
    "You better get yourself a sedative."
    "Although she’s worth it, she’s smart. Forecasting is a rare skill in our time of carelessness."
    layla "I’m preparing Morpheus. In a minute everything will be ready to dive."
    show leyla ok at left with move

    me "Kurt’s condition?"
    "I asked not for information. I see that his pulse quickened and he doesn’t breath well."
    "He’s running out."

    layla "Kurt is on the verge of a stroke. Morpheus records high brain activity. Whatever happens in his mind — it’s clearly not good."
    "Hold on, Kurt. I’ll be back soon"
    me "Layla. Can I ask you a couple of questions?"
    layla "Yes of course."
    me "Have you done any experiments with the Morpheus system?"
    "She is silent for a while, looking away. Then she turns to me."
    pause 1.0
    show leyla ok at center with move
    layla "Did Violet tell you that?"
    "Ha-ha!"
    me "Everything is good. I’m not a cop or a security officer."
    me "It is very important for me to know what is happening with the system, that’s all."
    layla "Pff… I like my job and I am a big fan of science since school, and…"
    me "Come on without long preambles."
    layla "Hmm. When I was just studying the Morpheus system, I wondered, is it possible to store the consciousness of a dead person in Limbo?"
    layla "I could not sleep straight — so I was interested."
    me "Of course impossible. Consciousness needs a biological carrier if we are talking about a human consciousness."
    layla "Not at all! Have you ever taken Morpheus apart? Did you see what was inside it?"
    "What does she mean?"
    me "Tons of boards? Morpheus can be repaired only in special laboratories of the corporation. Specialized technicians are responsible for this."
    layla "That’s it! Even Limb technicians like myself are not allowed to dismantle Morpheus."
    layla "And why? Like, shouldn’t we know {i}everything{/i} about the system we work with?"
    "Admittedly, it makes sense."
    show leyla ok at center with move
    me "What do you think is inside the system?"
    layla "You started to understand! That’s what I’ve been thinking all this time."
    layla "What could be inside the machine which somehow keeps the consciousness of the people connected to it in a single realm? Think yourself."
    "I’ve been thinking about this for years. Those strange, foreign nightmares in my dreams, hallucinations and illusions that I observe after diving…"
    me "I guess you’re not ready to admit it’s just a glitch in the Morpheus program."
    layla "It’s not my style to believe in coincidence. And then I made an experiment. I connected myself to a person who was dying."
    me "You’re crazy. What if the management find out about this?"
    layla "It knew. I was given a permission. Under the supervision of a qualified employee."
    me "Okay. And what did you see in Limbo?"
    layla "Nothing. Nothing at all."
    layla "Morpheus did not generated Limbo. I wandered in the dark. Spoke to the Void. And then returned easily."
    me "So your experiment proved nothing?"
    pause 1.0
    layla "My experiment proved that Violet Sharp is a bitch. She thwarted my research!"
    me "Why do you think so?"
    layla "Violet was that qualified employee. I was so upset about the failure of the experiment that I did not immediately understand why it failed."
    layla "Later I realized thet she just disconnected that dying man from the system and made fun of me talking to myself."
    layla "But I relized it too late."
    "Well well…"
    me "I’ve already wasted enough time. Start up the system and give a report."
    show leyla ok at right with move
    pause 2.0
    
    layla "Get ready."

    show leyla ok at center with move
    pause 1.0
    $ layla(_("Diving through Three."), interact=False, advance=False)
    $ renpy.pause(delay=1.0, hard=True)
    $ layla(_("Two."), interact=False, advance=False)
    $ renpy.pause(delay=1.0, hard=True)
    $ layla(_("One."), interact=False, advance=False)
    $ renpy.pause(delay=1.0, hard=True)

    show limb_enter_1 at trans_limb_enter_1
    show limb_enter_2 at trans_limb_enter_2
    show limb_enter_3 at trans_limb_enter_3
    show black at trans_limb_enter_black

    $ renpy.pause(delay=2, hard=True)

    pause 0.5
    jump chapter_13


