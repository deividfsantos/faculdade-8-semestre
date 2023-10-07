# Program to measure the similarity between  
# two sentences using cosine similarity. 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
# X = input("Enter first string: ").lower() 
# Y = input("Enter second string: ").lower() 
# X ="I love horror movies"
# Y ="Lights out is a horror movie"
# Z ="I hate movies"

X ="RPO services improve the efficiency of digital onboarding through blockchain technology."
Y ="RPO solutions support employer branding in augmented reality (AR) recruitment experiences."
Z ="The procurement department received the RPO for office supplies."

# tokenization 
X_list = word_tokenize(X)  
Y_list = word_tokenize(Y) 
Z_list = word_tokenize(Z)   

# sw contains the list of stopwords 
sw = stopwords.words('english')  
l1 =[]
l2 =[]
  
# remove stop words from the string 
X_set = {w for w in X_list if not w in sw}  
Y_set = {w for w in Y_list if not w in sw} 
Z_set = {w for w in Z_list if not w in sw} 

# form a set containing keywords of both strings  
rvector = X_set.union(Y_set)  
rvector2 = X_set.union(Z_set)  

for w in rvector: 
    if w in X_set: l1.append(1) # create a vector 
    else: l1.append(0) 
    if w in Y_set: l2.append(1) 
    else: l2.append(0)
c = 0
  
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 
print("similarity: ", cosine) 


l1 = []
l3 = []
for w in rvector2: 
    if w in X_set: l1.append(1) # create a vector 
    else: l1.append(0) 
    if w in Z_set: l3.append(1) 
    else: l3.append(0) 
c = 0


# cosine formula  
for i in range(len(rvector2)): 
        c+= l1[i]*l3[i] 
cosine = c / float((sum(l1)*sum(l3))**0.5) 
print("similarity: ", cosine) 