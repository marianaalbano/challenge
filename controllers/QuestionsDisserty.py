from model.Users import db
from model.Users import QuestionsDisserty as Disserty

from controllers.QuizController import QuizController

class QuestionsDisserty():
    def findAll(self):
        return Disserty.query.all()

    def findOne(self,id):
        return Disserty.query.get(id)

    def findByQuiz(self,id):
        return Disserty.query.filter_by(quiz_id=id).all()

    def insertQD(self, id, info):
        quiz = QuizController()
        q_id = quiz.findOne(id)
        qd = Disserty()
        qd.questions = info['question']
        qd.right_question = info['right_question']
        qd.quiz_id = q_id.id
        db.session.add(qd)
        return db.session.commit()


    
    def updateQD(self, id, info):
        qd = Disserty.query.get(id)
        qd.questions = info['question']
        qd.right_question = info['right_question']
        return db.session.commit()


    def removeQD(self, id):
        qd = Disserty.query.get(id)
        db.session.delete(qd)
        return db.session.commit()