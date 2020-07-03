import json 
dictionary ={ 
    "john" : "go123", 
    "abby" : "xyz90", 
    "ellie" : "stay78", 
}   
with open("data.txt", "w") as outfile: 
    json.dump(dictionary, outfile) 


with open('sample.json', 'r') as openfile: 
  
    # Reading from json file 
    json_object = json.load(openfile) 
print(json_object) 
#print(type(json_object)) 