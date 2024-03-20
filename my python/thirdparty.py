 
# inding out every sentense on london wikipedia page where the word population is mentioned


import wikipedia

london = wikipedia.page("london")

splitword =london.content.split(".")
splitpopulation =[]
for sentence in splitword:
    if("population" in sentence):
        splitpopulation.append(sentence)

print(splitpopulation)



# xakz kwhx xzcn ctnc