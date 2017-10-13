from itertools import combinations

def JaccardIndex(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    ans = 1 - float(len(set1 & set2)) / len(set1 | set2)
    return round(ans, 2)

entity1 = "big old red square heavy"
entity2 = "big new blue square light"
entity3 = "small old red circle heavy"
entity4 = "small new red circle heavy"
entity5 = "small old blue square light"
entity6 = "big new blue circle light"

entity_dict={'entity1':entity1,'entity2':entity2,'entity3':entity3,'entity4':entity4,'entity5':entity5,'entity6':entity6}
entity_list = [entity1,entity2,entity3,entity4,entity5,entity6]

for item1,item2  in list(combinations(entity_dict.items(),2)):
    print("Jaccard Distance between {} and {} : {}".format(item1[0],item2[0],JaccardIndex(item1[1],item2[1])))


