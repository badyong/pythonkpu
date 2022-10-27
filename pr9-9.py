import wikipedia
import matplotlib.pyplot as plt
from  wordcloud import WordCloud
wiki = wikipedia.page('Artificial intelligence')
text = wiki.content
wordcloud =WordCloud(width = 2000, height = 1500).generate(text)
plt.figure(figsize=(40, 30))
plt.imshow(wordcloud)
plt.show()