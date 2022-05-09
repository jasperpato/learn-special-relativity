from . import db
from .models import Test, TestQuestion, TestAnswer

def populate():
    print('doing it')
    qs = [
    [ # Test 1
        "A spaceship is travelling towards a star at 100,000m/s. In the " + \
        "reference frame inside the spaceship, the speed of the light rays " + \
        "from the star to the spaceship would be closest to…",

        "A person running away from a light bulb and a person running " + \
        "towards a light bulb would measure the speed of the emitted " + \
        "light to be…",

        "True or False? A person accelerating in their car can use the " + \
        "theory of special relativity to measure space-time.",
    
        "True or false? The speed of a spaceship is the same in all " + \
        "reference frames.",

        "Space-time permeates how many dimensions?"
    ],
    [ # Test 2
        "True or false? The light beam travelled a larger distance in the " + \
        "reference frame outside of the train than in the reference frame " + \
        "inside the train.",

        "In which reference frame did time flow slower throughout the " + \
        "journey of the light beam?",

        "If time flows slower in observer X’s frame of reference compared " + \
        "to observer Y, would X age faster or slower than Y?",

        "True or False? Considering γ >= 1, the proper time interval is " + \
        "always the smallest time interval that can be observed between " + \
        "two events.",

        "If we performed this train experiment and measured time passing " + \
        "on extremely precise instruments, would we really observe time " + \
        "passing at difference rates depending on relative speeds?"
    ],
    [ # Test 3
        "For v=0.866c, what is the value of the Lorentz factor as an integer?",

        "The duration of the journey from Earth to the planet is the " + \
        "time interval between two events: the spaceship leaving Earth " + \
        "and the spaceship arriving on the other planet. Which observer " + \
        "witnesses these two events at the same point in space within " + \
        "their reference frame?",

        "During the journey from the planet back to Earth, which twin " + \
        "observes proper time?",

        "If the journey from Earth to the planet takes 10 years for the " + \
        "twin inside the spaceship, how many years will it take for the " + \
        "twin on Earth?",

        "When reunited, how much older will the twin on Earth be compared " + \
        "to the twin who travelled through space?"
    ]]
    ans = [
    [ # Test 1
        ['299,892,458 m/s', '299,792,458 m/s', '299,692,458 m/s', '299,992,458 m/s'],
        ['The same', 'Different'],
        ['True', 'False'],
        ['True', 'False'],
        None
    ],
    [ # Test 2
        ['True', 'False'],
        ['Inside the train', 'Outside the train'],
        ['Faster', 'Slower'],
        ['True', 'False'],
        ['Yes, this would really happen', 'No, this is only theoretical']
    ],
    [ # Test 3
        None,
        ['Twin in the spaceship', 'Twin on Earth'],
        ['Twin in the spaceship', 'Twin on Earth'],
        None,
        None
    ]]
    correct = [
        [2, 1, 2, 2, "4"],
        [1, 1, 2, 1, 1],
        ["2", 1, 1, "20", "20"]
    ]
    for t in range(len(qs)):
        #if not Test.query.filter_by(id=t+1).first():
        db.session.add(Test(number=t+1))
        for q in range(len(qs[t])):
            #if not TestQuestion.query.filter_by(id=q+1).first()
            db.session.add(TestQuestion(
                number = q+1,
                text = qs[t][q],
                answer = correct[t][q] if isinstance(correct[t][q], str) else None,
                test_number = t+1
            ))
            if ans[t][q] is None: continue
            q_id = TestQuestion.query.filter_by(number=q+1, test_number=t+1).first().id
            for a in range(len(ans[t][q])):
                db.session.add(TestAnswer(
                    number = a+1,
                    text = ans[t][q][a],
                    correct = a+1 == correct[t][q],
                    question_id = q_id
                ))
    db.session.commit()
