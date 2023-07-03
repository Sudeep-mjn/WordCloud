import sys
import numpy as np
from PIL import Image #for image handeling
import wikipedia 
from wordcloud import WordCloud,STOPWORDS # remove words like a, an ,the...


a = str(input("Enter the name which you want to wordcloud :"))
title = wikipedia.search(a)[0] #search the title from wikipedia
page = wikipedia.page(title)
text = page.content  # to extract the content of topic
print(text)

bg = np.array(Image.open("abc.png"))  #base on which our word will apear
unwanted_words = set(STOPWORDS)
wordcloud = WordCloud(background_color="black", max_words= 400, mask= bg , stopwords=unwanted_words)
wordcloud.generate(text)
wordcloud.to_file("ayo.png")  #save in given name
