#encoding=utf-8

import jieba
import codecs

class Seg(object):
    stopwords = []
    stopword_filepath="stopwordList//stopword.txt"

    def __init__(self):
        pass

    # def read_in_stopword(self):#读入停用词
    #     file_obj = codecs.open(self.stopword_filepath,'r','utf-8')
    #     while True:
    #         line = file_obj.readline()
    #         line=line.strip('\r\n')
    #         if not line:
    #             break
    #         self.stopwords.append(line)
    #     file_obj.close()

    def cut(self,sentence):
        seg_list = jieba.cut(sentence)#切词

        results = []
        for seg in seg_list:
            results.append(seg)
        return results
            
    def cut_for_search(self,sentence):
        seg_list = jieba.cut_for_search(sentence)

        results = []
        for seg in seg_list:
            results.append(seg)



