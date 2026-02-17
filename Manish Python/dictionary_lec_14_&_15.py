labour_cost = {'ram': 100, 'shyam': 200, 'hari': 300}

labour_cost['ram'] = 150

print(labour_cost.keys())
print(labour_cost.values())
print(labour_cost.items())

for key, value in labour_cost.items():
    print(f"{key} has a cost of {value}")

print(labour_cost['ram'])

# Example of calculating total cost based on days worked and absent days

labour_cost = {"Mahesh": 500, "Ramesh": 400, "Mithilesh": 400, "Sumesh": 300, "Jagmohan": 1000, "Rampyare": 500}
absent = {"Mahesh": 3, "Jagmohan": 7}

days_worked = 50
total_cost = 0

for lab, wage in labour_cost.items():
    days_present = days_worked - absent.get(lab, 0)
    total_cost += wage * days_present

print(total_cost)
print(absent.get("Mahesh", 0))  # Default value if key not found

print("dictionary comprehension example")
labour_cost = {"Mahesh": 500, "Ramesh": 400, "Mithilesh": 400, "Sumesh": 300, "Jagmohan": 1000, "Rampyare": 500}
new_labour_cost = {key: labour_cost[key]+100 for key in labour_cost if labour_cost[key] > 400}
print(new_labour_cost)

# count no of times a word appears in a list and make new dictionary with word as key and count as value
name = "chetan mavale"
# letter_count = {letter: name.count(letter) for letter in name if letter != " "}
# print(letter_count)
letter_count = {}
# for letter in name:
#     if letter != " ":
#         letter_count[letter] = letter_count.get(letter, 0) + 1
# print(letter_count)
for char in name:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1
print(letter_count)

data = {"DERF":0,"POENKN":10,"DD":7,"MAINDATA":[{"IDD":"d3454355","BDD":"5678hfjhjh","LINKID":4,"HeaderFields":[{"FieldTypeName":"H1","Value":"false"},{"FieldTypeName":"H2","Value":"148877564"},{"FieldTypeName":"H3","Value":"20230930"},{"FieldTypeName":"H4","Value":"20231130"},{"FieldTypeName":"H5","Value":"2441.56"},{"FieldTypeName":"H6","Value":"0.00"},{"FieldTypeName":"H7","Value":"2411.56"},{"FieldTypeName":"H8","Value":"EUR"},{"FieldTypeName":"H9","Value":"00115190035"},{"FieldTypeName":"H10","Value":""},{"FieldTypeName":"H11","Value":"4500575382"},{"FieldTypeName":"H12","Value":"0.00"},{"FieldTypeName":"H13","Value":""},{"FieldTypeName":"H14","Value":""},{"FieldTypeName":"H15","Value":"F0"},{"FieldTypeName":"H16","Value":"87"},{"FieldTypeName":"H17","Value":"0.00"},{"FieldTypeName":"H18","Value":""},{"FieldTypeName":"H19","Value":""},{"FieldTypeName":"H20","Value":"No"}],"CodingLines":[],"Tables":[{"N1":"233553","N2":"3555","N3":"ASDDDD","N4":"334324","N5":"900.00","N6":"1.29","N7":"387.00","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""},{"N1":"765765","N2":"67657657","N3":"ADFDFF)","N4":"667657","N5":"1000.00","N6":"1.94","N7":"1940.00","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""},{"N1":"67657","N2":"76576576576","N3":"SFDFFDFSDF","N4":"7667676","N5":"1000.00","N6":"0.11456","N7":"114.56","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""}],"INININ":"148877564","SDRER":"null"},{"IDD":"frret5","BDD":"5trtry4566","LINKID":4,"HeaderFields":[{"FieldTypeName":"H1","Value":"false"},{"FieldTypeName":"H2","Value":"ICI2300397"},{"FieldTypeName":"H3","Value":"20231219"},{"FieldTypeName":"H4","Value":"20240331"},{"FieldTypeName":"H5","Value":"76.44"},{"FieldTypeName":"H6","Value":"0.00"},{"FieldTypeName":"H7","Value":"76.44"},{"FieldTypeName":"H8","Value":"INR"},{"FieldTypeName":"H9","Value":"56676765"},{"FieldTypeName":"H10","Value":""},{"FieldTypeName":"H11","Value":"0.00"},{"FieldTypeName":"H12","Value":""},{"FieldTypeName":"H13","Value":""},{"FieldTypeName":"H14","Value":"F1"},{"FieldTypeName":"H15","Value":"87"},{"FieldTypeName":"H16","Value":"0.00"},{"FieldTypeName":"H17","Value":""},{"FieldTypeName":"H18","Value":""}],"CodingLines":[{"CODE1":0.0,"CODE2":76.44,"CODE3":"5645654","CODE4":"","CodingFields":[{"FieldName":"COL1","Value":"223DD666"},{"FieldName":"COL2","Value":"3454545"},{"FieldName":"COL3","Value":""},{"FieldName":"COL5","Value":""},{"FieldName":"COL5","Value":""}]}],"Tables":[],"INININ":"DER3434","SDRER":"null"}],"Final":"JKHJKLH0909908"}

count = 0

for item in data["MAINDATA"]:
    if "HeaderFields" in item:
        count += sum(1 for field in item["HeaderFields"] if "FieldTypeName" in field)

print("Total FieldTypeName count:", count)

for item in data["MAINDATA"]:
    if "value" in item:
        count += sum( 1 for i in item["value"] if "FieldTypeName" in i) #dictionary comprehension
print("Total value count:", count)

count =0
for i in data['MAINDATA']:
    for j in i['HeaderFields']:
        for k in j:
            if k =='FieldTypeName':
                count+=1
print(count)

lst = [1, 11, 23, 45, 67, 89, 100]

lst [2]= 22
print(lst)