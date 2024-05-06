import pickle 

model_label = open('./models/predictonlabeler.pkl', 'rb') 
label = pickle.load(model_label)
# prediction = label.inverse_transform([1])
# print(prediction)

for i in range(0,41):
    prediction = label.inverse_transform([i])
    print(prediction)