import pandas as pd
import numpy as np
import nltk # nlkt: natural language toolkit is go to APT for Natural Language Processing (NPL) .
# NPL: concerned with interactions between computers and human(natural) language.How we program computers to understand natural language.
data = pd.read_csv(r"C:\!1 desktop\akka chelli\akka\reva\Python\StressData2.csv") # 'r' before the path string to address any special characters in the path, such as '\'
print(data.head(13))  # head():method returns the no of required rows from the dataset.If the no. of rows isn't specified displays first 5 rows 
print(data.isnull().sum()) # checks for null values

# Now we clan the dataset by removing stopwords,links,special symbols ,language errors etc
nltk.download('stopwords') 
# SnowballStememr is a stemming algorithm which is used to perform stemming 
stemmer = nltk.SnowballStemmer("english") 
stopword=set(stopwords.words("english"))  

