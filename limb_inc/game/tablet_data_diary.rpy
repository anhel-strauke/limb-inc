init:
    default TAB_DIARY_CURRENT_LABEL = ""
    default TAB_DIARY_CURRENT_DATE = ""
    define diary = DynamicCharacter("TAB_DIARY_CURRENT_DATE", color="#e0e0e0")

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
    diary "Despite all appearances, I cannot call today’s dive successful."
    diary "Indeed, our team has worked as smoothly as always. We have completed our task; our managemet was satisfied. We’ll have a bonus."
    diary "But…"
    diary "Something feels wrong, a strange and unusual anxiety. Stranger than ever."
    diary "And everything that the diver sees, all the sensations, all the echoes of emotions, no matter how unimportant or uneventful they seem… everything has some basis under it."
    diary "They resonate deep in the subconscious, and it notices more than rational perception."
    diary "In Limbo, nothing happens randomly. And this time nothing special happened. At least Kurt said that, and he's a reliable man."
    diary "And yet, I was haunted by the feeling that I was missing something important."
    diary "It feels like if I was looking in the wrong place — like in children’s pictures, where you need to search for a face in a jumble of leaves."
    diary "From now on, I will record my feelings."
    diary "This is a violation of company rules (No. 337, paragraph B, personal responsibility for concealing thoughts and No. 545, storing information related to work on a personal server),"
    diary "but I need to understand what stirred something within myself today."
    return

label diary_2604:
    diary "It was very difficult for me to sleep. I don’t understand why."
    diary "I’ve used my daily tranquilizers prescribed by a reliable doctor, they worked flawlessly until this night."
    diary "Perhaps I need to visit my doctor again."
    diary "Tiredness clouds my mind; I feel terribly sleepy."
    diary "Today there is one more dive."
    diary "I’m not sure if I can handle the task, if it is more difficult than the previous one."
    return

label diary_2704:
    diary "Yesterday’s dive went relatively well but I felt exhausted right after and fell asleep early in the evening."
    diary "I feel … limber as a dishrag."
    diary "I can't remember what I dreamed about."
    return

label diary_2804:
    diary "I have got a new dive schedule — and I got three vacation days, hurray!"
    diary "I will deal with the routine, taking a break from thinking about these strange hidden worlds."
    diary "If I develop a fear of Limbo, it will affect my career in the worst possible way."
    diary "I need a break and good thing is, I wasn't have to ask for it."
    return
    
label diary_3004:
    diary "This is my second day of the vacations and I can’t think about anything but Limbo."
    diary "I can’t stop replaying everything that happened to me there in my head looking for clues."
    diary "To be honest, this is starting to become a manic obsession."
    return

label diary_0105:
    diary "Today was a dive."
    diary "Based on the results, I can say that everything was pretty well."
    diary "However, while in Limbo, I was eaten by gloomy forebodings."
    diary "I felt that if I would turn around or look back, there would be something…"
    diary "Or something should appear just in front of my face."
    diary "Several times I wanted to scream and run away aimlessly."
    diary "The only thing that stopped me was a safety technique that was firmly embedded in my brain. Thanks to Kurt, he trained me."
    diary "One of Limbo's rules: if you lose self-control for half of a second, then you’ll never ever get it back."
    diary "Watch yourself. Always watch yourself first."
    diary "It is exhausting."
    diary "I should go to bed."
    return

label diary_0205:
    diary "I’ve never found myself awaken in the night in such fashion."
    diary "My bedsheets are still disgustingly sticky and soaked with a sweat."
    diary "It’s too hard to sleep now – I feel them constricting me."
    diary "My temperature is normal."
    diary "I can’t remember if I dreamed anything."
    diary "It’s time to go to work, or it will be first time for me being late."
    diary "A bad joke is in my head about the fact that nobody ever gets late to Limbo."
    diary "Will Kurt laugh? He seemed kind of tense these days too. Unfortunately, we don’t communicate much recently - it’s a work, family, etc…"
    return

label diary_0305:
    diary "Yesterday dive was worse one."
    diary "The task was failed."
    diary "Inside Limbo I was simply consumed by a feeling of overwhelming abomination."
    diary "Everything was strange, very strange."
    diary "It was as if my peripheral vision had gone crazy and was constantly blurred with flashes of something… something black."
    diary "White spots furiously rushing in all directions clouded my sight."
    diary "Or where they standing still? I can’t remember, my mind is still blurred."
    diary "It shouldn’t happen. Not like this. Not with this patient. Not at this level of Limbo!"
    diary "Even if the dive team made some mistakes while preparing the equipment, this should’t ever happen."
    diary "The psychologists must be the ones who failed when giving us the “portrait” of this patient."
    return

label diary_0405:
    diary "For the first time in my life, I wake up from a nightmare."
    diary "I remember almost nothing, except my own screams and attempts …to swim away? run away?"
    diary "It felt like I had neither arms nor legs, only the feeling of my body, sluggish, swaddled with a too hot blanket."
    diary "Pieces of darkness were chasing after me, devouring the whole world along the way."
    diary "Or had they slid from all sides at once, my ridiculous twitching only helping them get to me faster?"
    diary "Fortunately, today there is no Limbo diving! Just the usual routine."
    return

label diary_0505:
    diary "It’s good that I’m keeping a diary."
    diary "I remember absolutely none of yesterday nightmares."
    diary "My health is excellent, body temperature is normal."
    diary "There is a scheduled dive today."
    return

label diary_0605:
    diary "Yesterday's dive was smooth, we completed the task."
    diary "Limbo was… suspiciously usual (if this adjective can be applied to it)."
    diary "But my nightmares blossoms like never before."
    diary "The panic attacks hit me at least a dozen times last night."
    diary "After every awakening I fell asleep full of sticky, nauseous fear."
    diary "The pieces of darkness that devoured me first became more and more anthropomorphic," 
    diary "and then turned into huge strange insects endowed with a single will."
    diary "I need a doctor."
    diary "Interesting: if I ask my friends to advise a good somniologist on my webpage, in how many minutes will the management call me?"
    diary "I don't like our corporate psychotherapist, and I probably need a more narrow specialist."
    return

label diary_0705:
    diary "Looks like this diary is becoming a medical history."
    diary "I hardly remember yesterday dreams, but I remember myself writing them down."
    diary "It’s scary to read my own records. I begin to feel like I will stuck in Limbo if I don’t hadle myself."
    diary "I’m diving today. Again."
    diary "Maybe I should take a vacation at my own expense?"
    return

label diary_0805:
    diary "The last level of Limbo almost finished me. Damn it, I love my job, and I’m proud of how good am I in it!"
    diary "But now something is happening, unknown, incomprehensible even to me."
    diary "Some strange black spots in Limbo began to replace what Limbo replaces reality with."
    diary "They seem alive to me. Or, at least, they have some strange goals."
    diary "This is probably like a child’s imagination that turns the darkness under the bed into a monster that will certainly grab your leg."
    diary "I wonder what will I dream about tonight?"
    return

label diary_0905:
    diary "There are questions that should be leaved without the answers."
    diary "I hope I will forget this dreams."
    diary "I’m taking a day off."
    diary "RECORD CONTINUED"
    diary "Evening."
    diary "I wanted to walk in my favorite park on the top of Elite Plaza."
    diary ".... RECORD ERROR"
    return

label diary_1005:
    diary "I think my nightmares are some strange kind of the dive. Too many overlaps between my dreams, Limbo, and reality."
    diary "Maybe I’m stuck? Maybe I’m in Limbo right now?"
    diary "No, I must not think about it in this way. It knocks me out."
    diary "There are no therapists in Limbo, and I have one. Appointment in a few hours."
    diary "Hope I will not end my day in the asylum."
    return