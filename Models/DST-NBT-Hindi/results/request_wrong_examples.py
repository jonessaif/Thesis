import json


f = open("woz_tracking.json",)

results = json.load(f)
print("Total Predictions: ", len(results))
wrong_req = []
wrong_food = []
wrong_area = []
wrong_price = []

for d in results:
	for turn in d['dialogue']:
		true_state = turn[1]['True State']
		prediction = turn[2]['Prediction']

		if set(true_state['request']) != set(prediction['request']):
			wrong_req.append(turn+[d["dialogue_idx"]])

		if true_state['food'] != prediction['food']:
			wrong_food.append(turn+[d["dialogue_idx"]])
		if true_state['area'] != prediction['area']:
			wrong_area.append(turn+[d["dialogue_idx"]])
		if true_state['price range'] != prediction['price range']:
			wrong_price.append(turn+[d["dialogue_idx"]])


print ("Wrong Prediction for 'request': ", len(wrong_req))
with open('wrong_req.json', 'w', encoding='utf-8') as outfile:
    json.dump(wrong_req, outfile, indent=4, ensure_ascii=False)

print ("Wrong Prediction for 'food': ", len(wrong_food))
with open('wrong_food.json', 'w', encoding='utf-8') as outfile:
    json.dump(wrong_food, outfile, indent=4, ensure_ascii=False)


print ("Wrong Prediction for 'price range': ", len(wrong_price))
with open('wrong_price.json', 'w', encoding='utf-8') as outfile:
    json.dump(wrong_price, outfile, indent=4, ensure_ascii=False)

print ("Wrong Prediction for 'area': ", len(wrong_area))
with open('wrong_area.json', 'w', encoding='utf-8') as outfile:
    json.dump(wrong_area, outfile, indent=4, ensure_ascii=False)        