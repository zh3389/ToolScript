from fastapi import FastAPI, Body
from transformers import pipeline


"""
# 环境搭建
pip install fastapi uvicorn
pip install transformers
"""
question_answerer = pipeline('question-answering')
ner_pipe = pipeline("ner")
app = FastAPI()


@app.post("/question_answerer")
def get_anwser(context: str = Body('My name is Jack. I want to go to America',
                                description="填入需要提取数据文本的主体."),
               question: str = Body('Where does Jack want to go ?', description="提出你想提取数据的问题."),):
    result = question_answerer({'context': context, 'question': question})
    return result


@app.post("/NER")
def get_ner(text: str = Body('My name is Jack. I want to go to America',
                             description='填入需要提取数据文本的主体'), ):
    result = ner_pipe(text)
    if len(result) > 0:
        res = []
        for dic in result:
            dic["score"] = float(dic["score"])
            dic["index"] = int(dic["index"])
            dic["start"] = int(dic["start"])
            dic["end"] = int(dic["end"])
            res.append(dic)
        return res
    else:
        return []


# uvicorn main:app --host 0.0.0.0 --port 60000
