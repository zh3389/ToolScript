import spacy

"""
环境搭建
pip install spacy
"""

class TextNLP:
    def __init__(self):
        self.nlp = spacy.load("zh_core_web_sm")

    def analysis_sentence(self, text):
        try:
            doc = self.nlp(text)
        except:
            print(f"{'=' * 100}\n无可分析的文本\n{'=' * 100}\n")
            return None
        return doc

    def vis_doc_info(self, doc, show=False):
        doc_list = []
        for token in doc:
            info_dic = {}
            info_dic["词"] = token.text
            info_dic["索引"] = token.idx
            info_dic["词元"] = token.lemma_
            info_dic["是否为标点符号"] = token.is_punct
            info_dic["是否为空格"] = token.is_space
            info_dic["是否为停用词"] = token.is_stop
            info_dic["是否为语言字符"] = token.is_alpha
            info_dic["形状"] = token.shape_
            info_dic["词性"] = token.pos_
            info_dic["句法依赖"] = token.dep_
            info_dic["词性标签"] = token.tag_
            doc_list.append(info_dic)
            if show:
                print("-" * 100)
                print(str(info_dic))
        return doc_list
