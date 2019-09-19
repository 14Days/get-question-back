from flask import Blueprint, session, request
from app.models.questions import Questions
import app.utils.return_warp as warp

questions_page = Blueprint('questions', __name__, url_prefix='/questions')


@questions_page.route('', methods=['GET'])
def random_questions():
    user = session.get('user')

    if user is None:
        return warp.fail_warp('please login')

    num = int(request.args.get('num'))
    question_type = int(request.args.get('type'))

    if num is None or question_type is None:
        return warp.fail_warp('params error')
    if not (10 <= num <= 30 and 0 <= question_type <= 2):
        return warp.fail_warp('params error')

    questions_temp = Questions.select_question(num, question_type)
    questions_res = []
    for question in questions_temp:
        questions_res.append({
            'question': question.question,
            'answer1': question.answer1,
            'answer2': question.answer2,
            'answer3': question.answer3,
            'answer4': question.answer4,
            'correct': question.correct
        })

    return warp.success_warp(questions_res)
