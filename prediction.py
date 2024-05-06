import pickle
import json
import warnings
import sys
import pandas as pd

symptoms = json.loads(sys.argv[1])
df = pd.DataFrame(symptoms,index=[0])

warnings.filterwarnings("ignore")

model_file =  open('./models/diseasepredictor.pkl', 'rb') 

model = pickle.load(model_file)

prediction = model.predict(df)


model_label = open('./models/predictonlabeler.pkl', 'rb') 
label = pickle.load(model_label)
prediction = label.inverse_transform(prediction)


print(json.dumps(prediction[0]))