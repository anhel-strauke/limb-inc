label chapter_7:
    scene bg corp_hall
    with dissolve
    hide screen tablet_button

    show violet interested at almost_right with dissolve

    pause 1.0

    vio "Doctor [LAST_NAME]? I’m Violet Sharp."
    vio "May I ask why the hell did you call for me even though I provided every detail in a report? There’s nothing more to add!"
    "Bella must have sent a request for testimony clarification."
    me "Did you notice anything unusual with Kurt lately?"
    show violet sad with dissolve
    vio "Apart from ignoring the protocol for the nullifying? Nothing."
    me "But what exactly led to passing? I understand the “system malfunction” concept, but it never caused a completely healthy person connected to Morpheus to die."
    vio "I don’t know, maybe he had weak blood vessels or something. Why won’t you check the autopsy report?"
    vio "I’m neither pathologist nor a crystal gazer! Answering your question is not under my expertise."
    "I wonder why she acts so hostile. Maybe she’s hiding something?"

    menu:
        "I suspect not everything you know found its way to the report, ms. Sharp. There’s no reason to be this mad.":
            show violet ok with dissolve
            vio "Not everything?!"
        "I understand your discontent, but I need your help to clarify the situation.":
            show violet ok with dissolve
            vio "Understand my discontent?!"

    vio "My wedding cruise started two days ago, but instead of being there I’m here, in the middle of this ridiculous incident!"
    vio "That I’m not even the cause of!!! I gave testimony to every damn… What else do you want from me?!"
    me "I’m sorry, ms. Sharp, it seems like now is not the time for this conversation."
    vio "Go to hell!…"
    hide violet with dissolve
    with hpunch
    pause 0.5
    "What a mood. How did Kurt even work with her?"

    show screen tablet_button
    $ add_email("boris_layla_file")
    menu:
        "Return to the patient’s room":
            jump chapter_8