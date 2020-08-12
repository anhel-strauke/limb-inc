init:
    default TAB_DOCS_AVAIL = ["medicine", "contract"]
    default TAB_DOCS_READ = set()
    default CURRENT_DOC_TITLE = ""
    default THIS_DOC_FIRST_TIME = False
    define doc = DynamicCharacter("CURRENT_DOC_TITLE")

init python:
    def tab_doc_attenion():
        global TAB_DOCS_AVAIL, TAB_DOCS_READ, TAB_DOCS
        for i in TAB_DOCS_AVAIL:
            if i not in TAB_DOCS_READ and TAB_DOCS[i].get("important", False):
                return True
        return False

label tablet_doc_read(doc_id):
    show screen tablet_app_docs_read(doc_id)
    python:
        CURRENT_DOC_TITLE = TAB_DOCS[doc_id]["name"]
        THIS_DOC_FIRST_TIME = doc_id not in TAB_DOCS_READ
        renpy.pause(delay=0.7, hard=True)
        TAB_DOCS_READ = TAB_DOCS_READ | {doc_id}
        renpy.call(TAB_DOCS[doc_id]["label"])
    return

## Documents List ########################################################################
init python:
    LIC = "{size=20}:::::: LIMBUS INC CONFIDENTIAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::{/size}"
    TAB_DOCS = {
        "report": {
            "name": _("Incident Report"),
            "descr": LIC + _("{p}{p}{size=60}Report{/size}{p}from Violet Sharp{p}{p}On the incident WBVS8306"),
            "label": "doc_report",
            "important": True
        },
        "secret": {
            "name": _("Transferred File"),
            "descr": _("You’re already familiar with the case?"),
            "label": "doc_secret"
        },
        "contract": {
            "name": _("Limbus Inc Contract"),
            "descr": LIC + (_("{p}{p}Employment Contract{p}{p}%s %s") % ("[FIRST_NAME]", "[LAST_NAME]")),
            "label": "doc_contract"
        },
        "medicine": {
            "name": _("Tenebrio STOP"),
            "descr": _("Instructions for use."),
            "label": "doc_medicine"
        },
        "morpheus": {
            "name": _("Morpheus User Instructions"),
            "descr": _("Official note for the diving specialists using Morpheus system."),
            "label": "doc_morpheus"
        },
        "anderson_dive": {
            "name": _(""),
            "descr": _(""),
            "label": "doc_anderson_dive"
        },
        "hans_nicht": {
            "name": _("Response From Archive"),
            "descr": LIC + _("{p}{p}{size=60}RESPONSE{/size}{p}FROM THE ARCHIVE{p}{p}Search term: “Hans Nicht”{p}{p}Replied by: Boris"),
            "label": "doc_hans_nicht",
            "important": True
        },
        "kurt_profile": {
            "name": _("Kurt Bachowski Profile"),
            "descr": LIC + _("{p}{p}{size=60}Kurt Bachowski{/size}{p}{p}Personal Profile"),
            "label": "doc_kurt_profile",
            "important": True
        },
        "miriam_profile": {
            "name": _("Miriam Bachowski Profile"),
            "descr": LIC + _("{p}{p}{size=60}Miriam Bachowski{/size}{p}{p}Personal Profile"),
            "label": "doc_miriam_profile",
        },
        "layla_profile": {
            "name": _("Layla Anderson Profile"),
            "descr": LIC + _("{p}{p}{size=60}Layla Anderson{/size}{p}{p}Personal Profile"),
            "label": "doc_layla_profile",
        },
        "violet_profile": {
            "name": _("Violet Sharp Profile"),
            "descr": LIC + _("{p}{p}{size=60}Violet Sharp{/size}{p}{p}Personal Profile"),
            "label": "doc_violet_profile"
        },
        "incident": {
            "name": _("Security Report"),
            "descr": LIC + _("{p}{p}Report on the incident{p}{size=60}WBVS8306{/size}{p}{p}Limbus inc. Security Service."),
            "label": "doc_incident"
        },
        "kurt_log": {
            "name": _(""),
            "descr": _(""),
            "label": "doc_kurt_log"
        },
        "homunculus_map": {
            "name": _(""),
            "descr": _(""),
            "label": "doc_homunculus_map"
        }
    }

## Documents Contents ####################################################################

label doc_report:
    doc "The incident took place in the West Branch of Limbus inc."
    doc "16th of July at 20:00 Hans Nicht, the convict, was delivered to the Neural Research Department."
    doc "The case for us was to erase the convict’s memory in order to change his behavioral pattern, the procedure known as “nullifying”."
    doc "It’s considered rather non-difficult."
    doc "Kurt Bachowski, the team principal, has made a decision to perform the dive into convict’s mind using the Morpheus system himself."
    doc "After the dive started, the connection with Dr. Bachowski was lost."
    doc "I tried to trigger the ejection system to pull doctor’s mind out of limbo, but the malfunction of Morpheus system occurred."
    doc "The system registered that Dr. Bachowski fell into a deep coma. Hans Nicht has died during the dive.\n\nViolet Sharp, Limbus inc. staff assistant."
    return

label doc_secret:
    doc "You’re already familiar with the case?"
    doc "Take a closer look at the suspected one."
    doc "Hans Nicht. Hans that does not exist at all, if you translate from German."
    doc "Look where he still figured, I think you will find a lot of interesting."
    me "Kid, who do you think you…?"
    return

label doc_contract:
    doc "This agreement was concluded between Limbus Incorporated and [FIRST_NAME] [LAST_NAME]."
    doc "Bla bla bla. Boring legal stuff."
    return

label doc_kurt_profile:
    doc "Kurt Bachowski\nAge: 37\nLoyalty to the company: 9/10\nPosition: Senior Limbo Diving Specialist"
    doc "Company member for over 7 years."
    doc "Proved to be a hardworking employee, aware of the responsibilities coming with his position over this period."
    doc "Currently satisfied with the job. Continues training and improvement in his field. Good sense of detail."
    doc "Recommendations for transfer to another position: no recommendations."
    doc "Personality: 70\% careerist according to the estimation of the department experts."
    doc "Character: Ambitious, hardworking, sense of humor."
    doc "Values ​​his work as much as his family, maybe more."
    doc "Does not participate in writing reviews on colleagues under the pretext of being very busy."
    doc "Peer reviews: 95\% positive. Anonymous peer reviews: 85\% positive."
    doc "Marital status: stable, traditional marriage.\nSpouse: Miriam Bachowski.\nCommon child: Kazimir Bachowski."
    doc "Last check: three months ago. According to inspectors, the family appeared as a stable unit of society."
    doc "No visible mental or physical health issues were detected during individual scanning."
    doc "Last contact with third-party medical services: a month ago, private clinic for manual therapy."
    return

label doc_miriam_profile:
    doc "Miriam Bachowski\nAge: 34\nLoyalty to the company: 9/10\nPosition: teacher of mathematical analysis."
    doc "Company member for over 5 years. Demonstrated her high degree of responsibility over this period."
    doc "No registered conflict with her leadership. Easily converges with subordinates. Full adhesion to company values."
    doc "Character: balanced, sense of humor remaining within appropriate limits regarding the position held."
    doc "Feedback from students and colleagues: 98\% positive. Anonymous student and peer reviews: 93\% positive."
    doc "Marital status: stable, traditional marriage.\nSpouse: Kurt Bachowski.\nCommon child: Kazimir Bachowski."
    doc "Last check: three months ago. According to inspectors, the family appeared as a stable unit of society."
    doc "No visible mental or physical health issues were detected during individual scanning."
    doc "Last contact with third-party medical services: four months ago, private dentist."
    return

label doc_layla_profile:
    doc "Leila Andersen\nAge: 27\nLoyalty to the company: 3/10\nPosition: Technical limbo equipment preparation specialist."
    doc "Company member for over 3 years. Proved to be an energetic and inquisitive employee over this period."
    doc "Knowledge of the profession at a level superior to the position held."
    doc "Demonstrated a sharp mind, distinguished herself by providing unexpected technical solutions to complex issues. Presumably extrovert."
    doc "Recommendations for transfer to another position: no recommendations."
    doc "Peer reviews: 80\% positive. Anonymous peer reviews: 55\% positive."
    doc "Complaints from colleagues: systematic disturbance of silence during workflow. Prone to empty talk. Sings often."
    doc "Marital status: no official data. According to inspectors, living with a younger, visually impaired brother."
    doc "Last contact with third-party medical services: 14 days ago, ophthalmology clinic, regular procedures."
    doc "{i}Attached Note:{/i}\nHuman Resources Department → Security Service."
    doc "The employee needs more frequent behavior monitoring. Monthly reports required."
    doc "Auditor with sufficient expertise required to avoid situations registered as previous failures."
    return

label doc_violet_profile:
    doc "Violetta Sharp\nAge: 30\nLoyalty to the company: 10/10\nPosition: Senior Limbo Specialist Assistant."
    doc "Company member for over 4 years. Proved herself to be a responsible employee, aware of her duty to the corporation over this period."
    doc "Pedantic, smart, careerist. Demonstrates a high level of social responsibility, willingly participates in writing peer reviews."
    doc "Displayed behavioral boundaries enabling, but not interfering with, acceptable socialization level."
    doc "Peer reviews: 90\% positive. Anonymous peer reviews: 55\% positive."
    doc "Marital status: plans to create a social unit in the near future. Future spouse: Susan McKinzley, not registered an employee of the company."
    doc "No visible mental or physical health issues were detected during individual scanning."
    doc "According individual monitoring, the employee does not speak about work at home."
    doc "Last contact with third-party medical services: 2 months ago."
    return

label doc_medicine:
    doc "Take 1 tablet a day for sleep disorders, obsessions, irritability, hysterical seizures."
    doc "For audible and visual hallucinations, suicidal tendencies or self-harm, increase the dose to 2 tablets per day."
    doc "Attention! This treatment must be taken continuously for at least 10 days minimum."
    doc "Overdosing may lead to consequences which may need to be assessed and dealt with by requesting the help of a specialist."
    return

label doc_incident:
    doc "July 17. Suspect Testemony."
    doc "Name: Violet Sharp.{p}Occupation: Scientific assistant (Morpheus experimental installation)."
    doc "Suspected in: Arrest resistance, attmept to damage corporation property, misconduct."
    doc "INCIDENT DETAILS:\nAt July, 16 the suspect was doing an intelligence as an undercover agent while working in the team of dr. K. Bachowski."
    doc "During search a psychotropic substance and a gun was found in the pocket of her robe."
    doc "It lead to her arrest on the above accusations."
    doc "During search at suspect’s home 20 packets of the different forbidden drag-active psychotropic medicines were found."
    doc "Note:\nBecause of suspect’s unstable mental state her testemony had changed several times. This delirium excludes any dialog probability."
    doc "At the current moment we are waiting for a medical conclusion about her condition."
    doc "All drugs found in suspect’s pocket and house were withdrawn."
    doc "Interrogation was performed by D. Wes, security officer, Limbus inc."
    return

label doc_hans_nicht:
    doc "Name: Hans Nicht\nAge: N/A\nID: N/A"
    doc "Total number of incidents figuring Hans Nicht: 17\nInvestigated incidents: 15\nInvestigations ended with nullifying: 10"
    doc "Investigations ended with death of the perpetrator: 3\nClassified investigations: 5"
    doc "CRIME SCENES:\n• Western Branch: 1\n• Eastern Branch: 1"
    doc "• North-West Branch: 1\n• Pacific Branch: 2\n• Special Sahara Branch: 3"
    doc "• Transcarpathian Branch: 2\n• Eurasian Branch: 2\n• Crime scene unknown: 5"
    doc "OFFENSE TYPES:\n• Theft of the trade secret: 12\n• Damaging corporation’s property: 7"
    doc "• Disinformation leading to injury: 7\n• Other offenses: 9"
    if THIS_DOC_FIRST_TIME:
        "Sahara Branch?… It was closed like… 80 years ago? How old is this Hans?"
        "Hm-m-m… Either he is immortal dude able to travel in space and time, nullified ten times, by the way…"
        "Or there are 17 different offenders, with no ID, with the same name, and with suspiciously similar set of offenses."
        if "secret" in TAB_DOCS_READ:
            "That guy from the express was right. Curiouser and curiouser!"
    return

label doc_morpheus:
    doc "During the process of diving you should maintain concentration, act reasonably and prudently."
    doc "Any actions that can lead to destabilisation of a patient’s state are forbidden."
    doc "Any actions that can cause a patient to question the reality of what is happening are leading to destabilisation of a patient’s state in 87.4\% of the cases studied."
    doc "The Emergency Ejection System is triggered a second after the specialist's pulse increases above the set rate."
    doc "One second of a real time equals from 5 to 20 minutes of subjective time in limbo."
    doc "Specialists with standard biometric indicators deviations within more than 1.5\% are prohibited from diving."
    return