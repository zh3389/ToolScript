import pandas as pd
from sklearn.metrics import confusion_matrix


class MachineLearningEvaluate:
    def __init__(self, dataframe_path="acc_data.csv"):
        self.source_data = pd.read_csv(dataframe_path)
        self.labels = []
        for x in self.source_data["label"]:
            if x not in self.labels:
                self.labels.append(x)
        print("数据一共有:", len(self.source_data))
        print("标签类别有:", self.labels)

    def confusionMatrix(self, label_list, predict_list):
        """获得标签和预测之间的混淆矩阵"""
        res = confusion_matrix(label_list, predict_list)
        # print(res)
        res = res.reshape(-1).tolist()
        return res

    def get_acc(self, matrix, class_name="**类别"):
        """计算混淆矩阵的各种评价指标"""
        TP, FP, FN, TN = matrix
        accuracy = (TP + TN) / (TP + FN + FP + TN)  # 准确率accuracy 反映分类器或者模型对整体样本判断正确的能力
        precision = TP / (TP + FP)  # 精确率precision 预测的正样本中有多少是真实的正样本 值越大越好
        recall = TP / (TP + FN)  # 召回率recall, 也称为真阳率, 命中率(hit rate) 正样本被预测为正样本占总的正样本的比例 值越大越好
        false_alarm = FP / (FP + TN)  # 误报率false alarm, 也称为假阳率, 虚警率, 误检率 值越小越好
        miss_rate = FN / (TP + FN)  # 漏报率miss rate, 也称为漏警率, 漏检率 值越小越好
        specificity = TN / (FP + TN)  # 特异度specificity 负样本被预测为负样本占总的负样本的比例
        f1score = (2 * precision * recall) / (precision + recall)  # 平衡precision少预测为正样本和recall基本都预测为正样本的单维度指标缺陷
        print(f"{'=' * 50} {class_name} {'=' * 50}\n"
              f"TP:{TP}, FP:{FP}, FN:{FN}, TN:{TN}\n"
              f"{accuracy}\t准确率accuracy 反映分类器或者模型对整体样本判断正确的能力\n"
              f"{precision}\t精确率precision 预测的正样本中有多少是真实的正样本 值越大越好\n"
              f"{recall}\t召回率recall 也称为真阳率,命中率(hit rate)正样本被预测为正样本占总的正样本的比例 值越大越好\n"
              f"{false_alarm}\t误报率false alarm 也称为假阳率,虚警率,误检率 值越小越好\n"
              f"{miss_rate}\t漏报率miss rate 也称为漏警率,漏检率 值越小越好\n"
              f"{specificity}\t特异度specificity 负样本被预测为负样本占总的负样本的比例\n"
              f"{f1score}\t平衡precision F1-score 少预测为正样本和recall基本都预测为正样本的单维度指标缺陷")

    def get_class_acc(self):
        for class_name in self.labels:
            data = self.source_data.copy()
            data.label[data.label != class_name] = "未知"
            data.predict[data.predict != class_name] = "未知"
            matrix = self.confusionMatrix(data["label"].tolist(), data["predict"].tolist())
            self.get_acc(matrix, class_name)


if __name__ == '__main__':
    mle = MachineLearningEvaluate()
    mle.get_class_acc()
