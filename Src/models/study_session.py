# definição da classe StudySession (OPÇÃO 1)

class StudySession:
    def __init__ (self, subject, topic, duration, date):
        self.subject = subject
        self.topic = topic
        self.duration = duration
        self.date = date

    def show_details (self):
        print("Matéria:", self.subject)
        print("Tópico Estudado:", self.topic)
        print("Duração:", self.duration)
        print("Data:", self.date)

sessions = []