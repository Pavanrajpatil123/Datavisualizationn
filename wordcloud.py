
#advance visualization tools such as woed cloud and how to create them


import matplotlib.pyplot as plt 
from wordcloud import WordCloud 
#sample text data 
text = "python is programming language for data analysis and visualization. Python is used 
for machine learning ,Web development,and more.Python libraries such as numPy, Pandas 
and matplotlib are essential for data scientists." 
#Create word cloud object 
wordcloud = WordCloud(width=800 , height =400, background_color= 
'white').generate(text) 
#display the word cloud using matplotlib 
plt.figure(figsize=(10,5)) 
plt.imshow(wordcloud,interpolation='bilinear') 
plt.axis('off') #hide the axes 
plt.show()
