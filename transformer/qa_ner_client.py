import requests

"""
环境搭建
pip install requests
"""


def questionAnwser(context, question):
    post_data = {"context": context,
                 "question": question}
    resp = requests.post('http://1.116.81.93:60000/question_answerer', json=post_data)
    result = resp.json()
    return result


def ner(context):
    resp = requests.post('http://1.116.81.93:60000/NER', json=context)
    result = resp.json()
    return result

"""
命名体识别对应含义
O     在命名实体之外
B-MIS 一个杂项实体的开始
I-MIS 杂项实体
B-PER 一个人名的开头
I-PER 人名
B-ORG 组织名的开始
I-ORG 组织
B-LOC 地名的开始
I-LOC 地名
"""

if __name__ == '__main__':
    context = "My name is Jack. I want to go to America"
    question1 = "Where does Jack want to go ?"
    question2 = "Who wants to go to America ?"

    anwser1 = questionAnwser(context, question1)
    print(anwser1)  # {'score': 0.9820489883422852, 'start': 33, 'end': 40, 'answer': 'America'}
    anwser2 = questionAnwser(context, question2)
    print(anwser2)  # {'score': 0.981503963470459, 'start': 11, 'end': 15, 'answer': 'Jack'}
    result = ner(context)
    print(result)  # [{'entity': 'I-PER', 'score': 0.9989021420478821, 'index': 4, 'word': 'Jack', 'start': 11, 'end': 15}, {'entity': 'I-LOC', 'score': 0.9996431469917297, 'index': 11, 'word': 'America', 'start': 33, 'end': 40}]