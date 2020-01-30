list_input_a = ["52","253","35","spy","2351"]

list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass

print(list_input_a)
print(list_number)