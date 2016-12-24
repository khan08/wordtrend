import pickle
import nltk
from trainer.process import get_feature, preprocess
from nltk import NaiveBayesClassifier
__author__ = 'Kang'
print("Start Processing")
rating1 = preprocess(open("data/ratingOneReviews.txt","r").readlines(),1)
rating2 = preprocess(open("data/ratingTwoReviews.txt","r").readlines(),2)
rating3 = preprocess(open("data/ratingThreeReviews.txt","r").readlines(),3)
rating4 = preprocess(open("data/ratingFourReviews.txt","r").readlines(),4)
rating5 = preprocess(open("data/ratingFiveReviews.txt","r").readlines(),5)
print("Processing Finished")

print("Start Tokenize")
frequency_list = pickle.load(open("data/allWords.pickle","rb"))
raw_inputs=[rating1,rating2,rating3,rating4,rating5]
input=[]
for j in raw_inputs:
    for i in j:
        tuple=(get_feature(i[0],frequency_list),i[1])
        input.append(tuple)
print("Tokenize Finished")

print("Start Training")
training = input[:int(.7*len(input))]
test = input[int(.7*len(input)):]
classifier = NaiveBayesClassifier.train(training)
with open("C:/users/Kang/trunk/classifier/naiveBayes.pickle","wb") as f:
    pickle.dump(classifier,f,protocol=2)
print("Training Finished")

print("Start Testing")
print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, test)) * 100)
for tup in test:
    pass
    print(classifier.classify(tup[0]),tup[1])

'''
    #Call Google API -> 1. get city rating 2. get city reviews
    jsonData = GoogPlac(lat,lon,500,key)
    results = jsonData['results']
    for result in results:
        id = getID(result)
        try :
            reviews = GoogDetail(id, key)['result']['reviews']
            for review in reviews:
                text = review['text'].replace('\n','')
                if text == '':
                    continue
                rating = review['rating']
                #For each review -> process each review --> input
                input = get_feature(text)
                #train classifier
                bayesClassifier.train((input,rating))
        except Exception:
            continue
    break;
    #save classifier



#input --> classifier
#---------------------
#test -> classifier --> output
'''