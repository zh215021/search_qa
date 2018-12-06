#encoding=utf-8

from cutWords import Seg
from fileObject import FileObj
from sentenceSimilarity import SentenceSimilarity
from sentence import Sentence
import time
from time import ctime
import threading
file_obj = FileObj(r"dataSet/train_q.txt")
train_sentences = file_obj.read_lines()
with open("dataSet/train_a.txt", 'r', encoding='utf-8') as file_answer:
    line = file_answer.readlines()

seg = Seg()

# 训练模型
ss1 = SentenceSimilarity(seg)
ss1.set_sentences(train_sentences)
ss1.TfidfModel()  # tfidf模型

ss2 = SentenceSimilarity(seg)
ss2.set_sentences(train_sentences)
ss2.LsiModel()  # LSI模型

def tfidf_model(sentence):
    top = ss1.similarity(sentence)
    answer_index = top[0][0]
    answer = line[answer_index]
    return top[0][1],answer

def lsi_model(sentence):
    top = ss2.similarity(sentence)
    answer_index = top[0][0]
    answer = line[answer_index]
    return top[0][1],answer
def thread_model(sentence):
    threads = []
    t1 = threading.Thread(target=tfidf_model, args=(sentence,))
    threads.append(t1)
    t2 = threading.Thread(target=lsi_model, args=(sentence,))
    threads.append(t2)
    return threads
if __name__ == '__main__':
    while True:
        sentence = input("你好，请输入：")
        start = time.time()
        sim1,answer1 = tfidf_model(sentence)
        sim2,answer2 = lsi_model(sentence)
        # for t in thread_model(sentence):
        #     t.start()
        # t.join()
        print(str(answer1))
        # else:
        #     print(str(answer2))
        end = time.time()
        print("运行时间是："+str(end-start)+'s')
