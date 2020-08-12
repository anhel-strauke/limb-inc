init:
    default TAB_DIARY_CURRENT_LABEL = ""
    default TAB_DIARY_CURRENT_DATE = ""
    define diary = DynamicCharacter("TAB_DIARY_CURRENT_DATE", color="#707070")

init python:
    TAB_DIARY = [
        {
            "date": _("Apr 25"),
            "label": "diary_2504",
        },
        {
            "date": _("Apr 26"),
            "label": "diary_2604",
        },
        {
            "date": _("Apr 27"),
            "label": "diary_2704",
        },
        {
            "date": _("Apr 28"),
            "label": "diary_2804",
        },
        {
            "date": _("Apr 30"),
            "label": "diary_3004",
        },
        {
            "date": _("May 01"),
            "label": "diary_0105",
        },
        {
            "date": _("May 02"),
            "label": "diary_0205",
        },
        {
            "date": _("May 03"),
            "label": "diary_0305",
        },
        {
            "date": _("May 04"),
            "label": "diary_0405",
        },
        {
            "date": _("May 05"),
            "label": "diary_0505",
        },
        {
            "date": _("May 06"),
            "label": "diary_0605",
        },
        {
            "date": _("May 07"),
            "label": "diary_0705",
        },
        {
            "date": _("May 08"),
            "label": "diary_0805",
        },
        {
            "date": _("May 09"),
            "label": "diary_0905",
        },
        {
            "date": _("May 09"),
            "label": "diary_0905e"
        },
        {
            "date": _("May 10"),
            "label": "diary_1005"
        },
    ]

init:
    define DIARY_GRID_SIZE = (len(TAB_DIARY) / 4 + (1 if (len(TAB_DIARY) % 4 > 0) else 0))

label tablet_app_diary_play(lbl):
    $ TAB_DIARY_CURRENT_LABEL = lbl
    python:
        TAB_DIARY_CURRENT_DATE = "?"
        for item in TAB_DIARY:
            if item["label"] == lbl:
                TAB_DIARY_CURRENT_DATE = item["date"]
                break
    $ renpy.restart_interaction()
    $ renpy.call(lbl)
    $ TAB_DIARY_CURRENT_LABEL = ""
    $ renpy.restart_interaction()
    return

## Diary Records ##########################################################################

label diary_2504:
    diary "Can’t say today’s dive was successful."
    diary "Our team works great as always. We accomplished the goal, upstairs are approving, and there gonna be bonuses."
    diary "But…"
    diary "The problem is there’s that weird anxiety. I mean – more weird than usual."
    diary "Everything the “diver” sees, feels, every slightest shade of emotion are all based on something and has a cause."
    diary "The uncinscious sometimes notices more than our mind."
    diary "Nothing in limbo happens without reason. But this time nothing special even happened. At least Kurt says so, and he’s a reliable man."
    diary "And yet I felt like I’m missing something important. Like I’m staring at the wrong direction or can’t solve an optical illusion game for kids."
    diary "I’m gonna write down all my experiences."
    diary "It violates the company rules (№337, §B, personal responsibility for the withholding of thoughts, and №545, storing work-related information on a personal server), but I need to understand my own thought."
    return

label diary_2604:
    diary "It was hard to fall asleep tonight. Don’t know why."
    diary "My tranquilizers are prescribed by a very good doctor and used to always work well. I think I’m gonna need another appointment."
    diary "I’m sleepy as heck."
    diary "Another dive today."
    diary "If the case will be more complicated than the previous one, I’m not sure I’ll succeed."
    return

label diary_2704:
    diary "Yesterday’s dive went well, but I still felt exhausted and slept like a log afterwards."
    diary "Feeling like… a crumpled draft."
    diary "Can’t recall what my dreams were."
    return

label diary_2804:
    diary "Saw a next week diving schedule – three days off, yay!"
    diary "Gonna do papers and stuff and take a rest from all these thoughts. If I develop a limbo phobia, it’ll affect my career like somebody shat on it."
    diary "I really need a break and it’s fortunate that I didn’t need to ask for it."
    return
    
label diary_3004:
    diary "For the second day now all I’m thinking about is limbo."
    diary "Revising and rethinking my experiences, looking for the clues."
    diary "Honestly, it feels like a manic obsession or something."
    return

label diary_0105:
    diary "I dived today."
    diary "Results are fine I’d say."
    diary "But all the time I was in limbo apprehensions were eating me up. It felt like if I turn around there will be SOMETHING looking at me."
    diary "Or right in front of my face."
    diary "A few moments I really wanted to scream and just run for the hills."
    diary "The only thing stopping me was an instruction installed as a basic instinct – Kurt trained me well, kudos to him."
    diary "One of limbo rules: you lose control for half a second – no hella way you get it back."
    diary "Watch yourself, always watch yourself first."
    diary "It’s exhausting."
    diary "I’ll go get some sleep."
    return

label diary_0205:
    diary "Never woke up in the middle of the night before."
    diary "The sheets are disgustingly wet and sticky. It’s hard to fall asleep again – feels like they strangle, suffocate me."
    diary "Temp is normal."
    diary "Can’t recall if I saw something in my sleep."
    diary "It’s time to go or I’ll be late to work for the first time ever."
    diary "The dark joke is cruising around my head – you never ever can be late to limbo."
    diary "Will Kurt find it funny? He’s also a little tense these days. Unfortunately we don’t communicate as much now as we used to - work, families, work…"
    return

label diary_0305:
    diary "Yesterday’s dive was the worst ever."
    diary "I failed."
    diary "In limbo the indescribably disgusting feeling was eating me up from the inside."
    diary "Somehing was off, it really was. Out the corner of my eye I kept noticing something… something black."
    diary "Some spots flashing by. Or just standing? I couldn’t understand even that."
    diary "It was not suppose to be happening anyway. Not like this, not with this patient. Not on that level of limbo!"
    diary "Even if our “swimming team” (dive operator, technicians, assistant and others) did something wrong with machine settings."
    diary "Maybe our psychologists failed with the patient’s profile."
    return

label diary_0405:
    diary "Woke up from a nightmare for the first time in my life."
    diary "The only things I remember are my desperate attempts to… run away? Swim away?"
    diary "It felt like I had no limbs, just a body, leaden, heavy, buried under hot, harsh blanket."
    diary "The pieces of darkness were chasing me, devouring the reality along the way. Or maybe they were crippling towards me from every direction and my desperate movements just helped them find me faster?"
    diary "What a relief – no limbo today. Just a normal, boring stuff."
    return

label diary_0505:
    diary "It’s very useful to keep notes."
    diary "I forgot absolutely everything about yesterday’s nightmares."
    diary "Feeling great, the temp is normal."
    diary "Another dive today."
    return

label diary_0605:
    diary "Yesterday’s dive went well, the goal is accomplished."
    diary "Limbo was… suspiciously normal, if this word is the right way to phrase it."
    diary "My nightmares though flourished like ever. Some paroxysms very similar to panic attack happened about ten times this night."
    diary "Every waking up was immediately followed by falling back into heavy sleeping full of sticky, sickening fear."
    diary "Pieces of darkness devouring me, becoming more and more anthropomorphic, then turned into eerie giant insects with a hive mind."
    diary "I think I need a medical appointment."
    diary "Just wondering - if I post on my web page asking friends for a good somnologist’s contacts – how long will it take until I get a call from upstairs?"
    diary "I don’t like our therapist that much and I also feel like I need a narrower specialist."
    return

label diary_0705:
    diary "Maybe these notes will become my medical history."
    diary "I almost completly forgot yesterday’s dreams but I recall writing them down."
    diary "It creep me out to read these notes – I seems to me that I’ll get stuck in limbo if I don’t cope with my shit."
    diary "Another dive today."
    diary "Should I ask for unpaid leave?"
    return

label diary_0805:
    diary "The last level of limbo took everything out of me. Damn, I love my job, I’m proud of my competence!"
    diary "But what happens now is something new and unexplainable."
    diary "Weird black spots started to replace the objects that limbo replaces the reality with."
    diary "They seem alive. Or having some sort of a goal at least."
    diary "Maybe it’s like the child’s imagination creates the monster under the bad out of darkness that’s always ready to grab your ancle."
    diary "What will be my dreams about today?"
    return

label diary_0905:
    diary "Some questions better left unanswered."
    diary "I just hope I’ll forget these by tomorrow."
    diary "Taking a day off."
    return

label diary_0905e:
    diary "Late evening."
    diary "I wanted to take a walk in my favorite park on the roof of Elite-Plasa, a giant entertainment center."
    diary "Eighteen floors up, only non-modified flowers and trees, four fountains and benches made from the real wood – a treat for those who understand."
    diary "The closest and most reliable path to appeasement is to rejoin with the nature at least for the paid hour, not the tai-tzu or morning yoga with personal instructor like people think these days."
    diary "Today this path failed me."
    diary "Every moment I stared into a distance, all the plants were moving."
    diary "I mean, not the way they always tremble a little in the under-dome air conditioning flow, but… moving towards me."
    diary "Every leaf and stalk of grass seemed to hide the darkness underneath."
    diary "I don’t even know how to describe it – it’s like something alien was hiding underneath the thin layer of reality, using every object like a paper screen."
    diary "Time to admit – I have a problem."
    diary "I need help. I’m booking an appointment tomorrow."
    return

label diary_1005:
    diary "Seems like my nightmares are some weird kind of dive. Too much in common there, in limbo and in reality."
    diary "What if I’m stuck? Stuck in limbo?"
    diary "No, don’t think, don’t think that."
    diary "There are no therapists in limbo, and I’m seeing one in just few hours."
    diary "Hope I won’t get sent to a nuthouse."
    return