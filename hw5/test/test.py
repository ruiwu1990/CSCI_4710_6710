from sklearn.cluster import KMeans
import numpy as np

# this is how you should find files from parent folder in python3
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import util

sample_data = {
	'user_data':[
		# index	What country do you live in?	How old are you?	What is your gender?	To what extent do you feel FEAR due to the coronavirus?	To what extent do you feel ANXIOUS due to the coronavirus?	To what extent do you feel ANGRY due to the coronavirus?	To what extent do you feel HAPPY due to the coronavirus?	To what extent do you feel SAD due to the coronavirus?	Which emotion is having the biggest impact on you?	What makes you feel that way?	What brings you the most meaning during the coronavirus outbreak?	What is your occupation?  
		[1,"USA",70.0,"Male",2,2,1,2,2,"anticipation of whats going to happen next","Lot's of predictions from differnet resources","Family,Psychologist"],
		[2,"Switzerland",25.0,"Female",3,4,3,4,4,"A mix of awe and anxiety. Awe at how wonderful of a challenge this is for our world to tackle together (especially on issues that have plagued us for decades) and anxiety on how much we may not be thinking about those who are most vulnerable","Reading thought leadership articles and social media","Reading,Global Public Servant (WEF)"],
		[3,"USA",26.0,"Female",3,3,1,4,4,"A mix of happy to be safe and home and sad for people who aren’t","Seeing what’s happening in the news","Family,Student"],
		[4,"USA",11.0,"Male",2,1,5,1,3,"Anger,No sports" ,"Family,Student"],
		[5,"USA",28.0,"Male",4,3,4,1,4,"Anger","a system that cares about profit more than general wellbeing","trying to help","reporter"],
		[6,"USA",24.0,"Female",4,4,5,1,4,"Anger","The US federal government" ,"Friends","Graduate student"],
		[7,"USA",21.0,"Female",4,3,5,3,2,"Anger","People are not being responsible in doing their part in staying in doors. It is causing a major spread in our environment. Due to this spread, I am not allowed to be outdoors or stay in my apartment in Austin. I am very active outside, so this is a challenge for me to stay inside. ","Being alone,Student"],
		[8,"USA",22.0,"Male",3,4,5,2,1,"Anger","Inaction of the people and government","Friends","Janitor"],
		[9,"USA",39.0,"Male",2,2,4,1,2,"Anger","Impacts on day-to-day life","Exercising","Software Engineer"],
		[10,"USA",78.0,"Male",5,5,5,1,1,"Anger","National leadership incompetence","Family","Executive - retired"]		
	]
}

labels = util.cluster_user_data(sample_data['user_data'])
print("predicted labels are: ", labels)

split_result = util.split_user_data(sample_data['user_data'], labels)
print("Split original user data to:")
print(split_result)
print("Split_result length is: ", len(split_result))


