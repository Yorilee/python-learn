dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin" : "필리핀"
}

key = input("> Access Key :")

if key in dictionary :
    print(dictionary[key])
else :
    print("Key Value Not Exists..")