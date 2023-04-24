
conditions = ['Breathing Problem', 'Fever', 'Dry Cough', 'Sore throat',
       'Hyper Tension', 'Fatigue ', 'Abroad travel',
       'Contact with COVID Patient', 'Attended Large Gathering',
       'Visited Public Exposed Places',
       'Family working in Public Exposed Places']

class Condition:
    def __init__(self, name=None, value =None):
        self.name = name

        if name in ['Breathing Problem', 'Fever', 'Dry Cough', 'Sore throat',
       'Hyper Tension', 'Fatigue ', 'Abroad travel','Family working in Public Exposed Places']:
            self.question = 'Do you have ' + name.lower()
        elif name in ['Contact with COVID Patient', 'Attended Large Gathering',
       'Visited Public Exposed Places']:
            self.question = 'Recently, have you ' + name.lower()

        self.value = value