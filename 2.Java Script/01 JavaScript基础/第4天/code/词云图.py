# 导入相关的库
import matplotlib
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image


# 加载并处理分词
text = open(r"C:\Users\QDM\Desktop\SAP出库价\9-07\ciyun.txt",
            encoding="gbk").read()
text = text.replace('\n', "").replace("\u3000", "")
text_cut = jieba.lcut(text)
text_cut = ' '.join(text_cut)

stop_words = open(r"C:\Users\QDM\Desktop\SAP出库价\9-07\ciyun.txt",
                  encoding="gbk").read().split("\n")

# 读取背景图片，也可以输入中文
background = Image.open(r"C:\Users\QDM\Desktop\fu.png")
graph = np.array(background)

word_cloud = WordCloud(font_path="simsun.ttc",
                       background_color="white",
                       mask=graph,  # 指定词云的形状
                       stopwords=stop_words)

# 渲染效果
word_cloud.generate(text_cut)
plt.subplots(figsize=(12, 8))
plt.imshow(word_cloud)
plt.axis("off")
