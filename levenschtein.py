__author__ = 'user'

from nltk.metrics.distance import edit_distance
import distance

#  transposition flag allows transpositions edits (e.g., “ab” -> “ba”),

# method calculating the edit distance between normal tweet and spam tweets
def distance_to_spam(normal,spam_list):
    distance_list = []
    for spam in spam_list:
        distance_list.append(edit_distance(normal,spam,transpositions=False))
    return distance_list

# calculate the average score of distance list
def average(list):
    return sum(list)/len(list)

spam_list = ["@edg_esport win @Cloud9 and pick up their first win at #Worlds2017! #EDGWIN","@Cloud9 lost to @edg_esport in today’s first game. #NAFIGHTING","@FNATIC take down @Cloud9 and pick up their first win at #Worlds2017! #FNCWIN","@edg_esport take down @Cloud9 and pick up their first win at #Worlds2017! #EDGWIN Watch here: http://watch.na.lolesports.com/en_US/","@edg_esport take down @Cloud9 and pick up their first win at #Worlds2017! #EDGWIN Watch here: http://watch.euw.lolesports.com/en_GB/","Live lolesports now displayed on : http://watch.euw.lolesports.com/en_GB/ @edg_esport vs @Cloud9 #Worlds2017! #EDGWIN","@edg_esport win @Cloud9 and pick up their first win at #CN>NA? #NAFIGHTING","@edg_esport pick up their second win of the day as they take down @ahq_eSportsClub! #Worlds2017#EDGWIN","Live lolesports now displayed on : http://watch.na.lolesports.com/en_US/@edg_esport vs @ahq_eSportsClub #Worlds2017! #EDGWIN","Live lolesports now displayed on : http://watch.euw.lolesports.com/en_GB/ @edg_esport against @Cloud9 #Worlds2017! #EDGWIN","@edg_esport win @Cloud9 and pick up their first win at #Worlds2017! ","@Cloud9 lost to @edg_esport in today’s first game.","@FNATIC take down @Cloud9 and pick up their first win at #Worlds2017!","@edg_esport take down @Cloud9 and pick up their first win at #Worlds2017! Watch here: http://watch.na.lolesports.com/en_US/","@edg_esport take down @Cloud9 and pick up their first win at #Worlds2017! Watch here: http://watch.euw.lolesports.com/en_GB/","Live lolesports now displayed on : http://watch.euw.lolesports.com/en_GB/ @edg_esport vs @Cloud9 #Worlds2017!","@edg_esport win @Cloud9 and pick up their first win at #CN>NA?","@edg_esport pick up their second win of the day as they take down @ahq_eSportsClub! #Worlds2017","Live lolesports now displayed on : http://watch.na.lolesports.com/en_US/@edg_esport vs @ahq_eSportsClub  #EDGWIN","Live lolesports now displayed on : http://watch.euw.lolesports.com/en_GB/ @edg_esport against @Cloud9 #EDGWIN"]

# 5 normal tweets
n1 = "@edg_esport take down @Cloud9 and pick up their first win at #Worlds2017! #EDGWIN"
n2 = "League of Legends Live: A Concert Experience at #Worlds2017"
n3 = "Super Galaxy 2017 skins are available now! Learn more HERE!"
n4 = "If I had to do it all over again, I would have done it the same way - @RekklesLoL"
n5 = "Who will make it out of Group D ? The #Worlds2017 Group Stage continues NOW!"

print(distance_to_spam(n1,spam_list))
print(distance_to_spam(n2,spam_list))
print(distance_to_spam(n3,spam_list))
print(distance_to_spam(n4,spam_list))
print(distance_to_spam(n5,spam_list))

print(average(distance_to_spam(n1,spam_list)))
print(average(distance_to_spam(n2,spam_list)))
print(average(distance_to_spam(n3,spam_list)))
print(average(distance_to_spam(n4,spam_list)))
print(average(distance_to_spam(n5,spam_list)))
