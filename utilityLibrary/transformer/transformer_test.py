from transformers import pipeline

"""
# 环境搭建
pip install transformers
"""


def sequence_classification():
    """
    序列分类是根据给定的类数对序列进行分类的任务
    使用模型进行情感分析的示例：识别序列是正面的还是负面的。
    """
    classifier = pipeline("sentiment-analysis")
    result = classifier("I hate you")[0]
    print(f"label: {result['label']}, score: {round(result['score'], 4)}")
    result = classifier("I love you")[0]
    print(f"label: {result['label']}, score: {round(result['score'], 4)}")


def extractive_question_answering():
    """
    提取问答是从给定问题的文本中提取答案的任务
    使用模型进行问答的示例：从给定问题的文本中提取答案。
    """
    question_answerer = pipeline("question-answering")
    context = """Extractive Question Answering is the task of extracting an answer from a text given a question.
                 An example of a question answering dataset is the SQuAD dataset, which is entirely based on that task.
                 If you would like to fine-tune a model on a SQuAD task, you may leverage the examples/pytorch/question-answering/run_squad.py script.
                 """
    result = question_answerer(question="What is extractive question answering?", context=context)
    print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")
    result = question_answerer(question="What is a good example of a question answering dataset?", context=context)
    print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")


def masked_language_modeling():
    """
    掩码语言建模的任务是用掩码标记按顺序对标记进行掩码，并提示模型用适当的标记填充该掩码。
    这允许模型同时关注正确的上下文(掩码右侧的标记)和左侧的上下文(掩码左侧的标记)。这样的训练为需要双向上下文的下游任务创建了强大的基础。
    """
    unmasker = pipeline("fill-mask")
    from pprint import pprint
    pprint(unmasker(f"HuggingFace is creating a {unmasker.tokenizer.mask_token} that the community uses to solve NLP tasks."))


def text_generation():
    """
    在文本生成(又名 开放式文本生成)中，目标是创建一个连贯的文本部分，它是给定上下文的延续。
    """
    text_generator = pipeline("text-generation")
    print(text_generator("As far as I am concerned, I will", max_length=50, do_sample=False))


def named_entity_recognition():
    """
    命名实体识别 (NER) 是根据类别对令牌进行分类的任务，例如，将令牌识别为人、组织或位置。
    O     在命名实体之外
    B-MIS 一个杂项实体的开始，紧接着另一个杂项实体
    I-MIS 杂项实体
    B-PER 一个人名的开头，紧跟在另一个人的名字之后
    I-PER 人名
    B-ORG 一个组织紧接着另一个组织的开始
    I-ORG 组织
    B-LOC 一个位置的开始，紧接着另一个位置
    I-LOC 位置
    """
    ner_pipe = pipeline("ner")
    sequence = """Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO,
                  therefore very close to the Manhattan Bridge which is visible from the window."""
    print(ner_pipe(sequence))


def summarization():
    """
    摘要是将文档或文章摘要为较短文本的任务。
    """
    summarizer = pipeline("summarization")
    ARTICLE = """New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
                 A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
                 Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
                 In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
                 Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
                 2010 marriage license application, according to court documents.
                 Prosecutors said the marriages were part of an immigration scam.
                 On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.
                 After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective
                 Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.
                 All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say.
                 Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
                 Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
                 The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s
                 Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
                 Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
                 If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.
                 """
    print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))


def translation():
    """
    翻译是将文本从一种语言翻译成另一种语言的任务。
    """
    translator = pipeline("translation_en_to_de")
    print(translator("Hugging Face is a technology company based in New York and Paris", max_length=40))


if __name__ == '__main__':
    pass
    # sequence_classification()
    # extractive_question_answering()
    # masked_language_modeling()
    # text_generation()
    # named_entity_recognition()
    # summarization()
    # translation()
