'''import pickle             # user input api
from flask import Flask, jsonify, make_response, request
app = Flask(__name__)

@app.route('/')
def hello_geek():
    result = airpredict()
    return str(result)

    result = multi_airpredict


@app.route('/multi_airpredict',methods=["POST"])
def multi_predict():
    jsondata = request.get_json()
    
    #print('val' + str(jsondata[0]))
    for i in jsondata:
     print ('value' + str(i['neighbourhood_group']))
        print ('value' + str(i['neighbourhood']))
        print ('value' + str(i['latitude']))
        print ('value' + str(i['longitude']))
        print ('value' + str(i['room_type']))
        print ('value' + str(i['minimum_nights']))
        print ('value' + str(i['number_of_reviews']))
        print ('value' + str(i['reviews_per_month']))
        print ('value' + str(i['calculated_host_listings_count']))
        print ('value' + str(i['availability_365']))

    result = multi_predict(neighbourhood_group,neighbourhood,latitude,longitude,room_type,minimum_nights, 
                         number_of_reviews, reviews_per_month ,calculated_host_listings_count,availability_365)
    return make_response(jsonify({'result':str(0)}),200)
    
    


@app.route('/airpredict',methods=["POST"])
def hello_predict():
    neighbourhood_group  = str(request.json['neighbourhood_group'])
    neighbourhood  = str(request.json['neighbourhood'])
    latitude = str(request.json['latitude'])
    longitude  = str(request.json['longitude'])
    room_type  = str(request.json['room_type'])
    minimum_nights = str(request.json['minimum_nights'])
    number_of_reviews  = str(request.json['number_of_reviews'])
    reviews_per_month  = str(request.json['reviews_per_month'])
    calculated_host_listings_count = str(request.json['calculated_host_listings_count'])
    availability_365  = str(request.json['availability_365']) 

    result = airpredict(neighbourhood_group,neighbourhood,latitude,longitude,room_type,minimum_nights, 
                        number_of_reviews, reviews_per_month ,calculated_host_listings_count,availability_365)
    return make_response(jsonify({'result':str(result)}),200)

def airpredict(neighbourhood_group,neighbourhood,latitude,longitude,room_type,minimum_nights, 
                        number_of_reviews, reviews_per_month ,calculated_host_listings_count,availability_365):
    
    X_new = [[int(neighbourhood_group), int(neighbourhood), float(latitude),float(longitude),int(room_type),
              int( minimum_nights ),int(number_of_reviews),float(reviews_per_month),
              int( calculated_host_listings_count), int(availability_365 )]]  

    filename = 'airbnb_model.pkl'

    # load the model from disk
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(X_new)
    print(result)
    return result


if __name__ == "__main__":
    app.run(debug=True)   '''

    

# csv import api

import pickle
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)


def load_model():
    with open('airbnb_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

@app.route('/multi_airpredict', methods=["POST"])
def multi_predict():
    jsondata = request.get_json()
    data = []

    batch_size = 10

    for i in range(0, len(jsondata), batch_size):
        batch = jsondata[i:i+batch_size]

        for item in batch:
           
            neighbourhood_group = item['neighbourhood_group']
            neighbourhood = item['neighbourhood']
            latitude = item['latitude']
            longitude = item['longitude']  
            room_type = item['room_type']
            minimum_nights = item['minimum_nights']  
            number_of_reviews = item['number_of_reviews']
            reviews_per_month = item['reviews_per_month']  
            calculated_host_listings_count = item['calculated_host_listings_count']
            availability_365 = item['availability_365']  


            data_point = [[int(neighbourhood_group), int(neighbourhood), float(latitude),float(longitude),int(room_type),
              int( minimum_nights ),int(number_of_reviews),float(reviews_per_month),
              int( calculated_host_listings_count), int(availability_365 )]]

            data.append(data_point)

    model = load_model()

    data = np.array(data)
    
    data = data.reshape(-1, data.shape[-1])

    predictions = model.predict(data)

    return jsonify(predictions.tolist())

if __name__ == "__main__":
    app.run(debug=True)
