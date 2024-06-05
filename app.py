from flask import Flask ,request ,jsonify
import requests

app = Flask(__name__)

def currency_conversion_factor(source ,target):
    
    url = "https://currency-converter241.p.rapidapi.com/conversion_rate"

    querystring = {"from":source,"to":target}

    headers = {
    	"x-rapidapi-key": "08f1541678msh2a4747804150020p1237efjsn27b025299ffd",
    	"x-rapidapi-host": "currency-converter241.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()
    
    return response
    
    
@app.route("/" ,methods=["GET" ,"POST"])
def home():
    data = request.get_json()

    source_currency = data["queryResult"]["parameters"]["unit-currency"]["currency"]
    amount = data["queryResult"]["parameters"]["unit-currency"]["amount"]
    target_currency = data["queryResult"]["parameters"]["currency-name"]
    
    data = currency_conversion_factor(source_currency ,target_currency)

    final_amount = round(amount * data["rate"] ,2)
    
    response = {
        'fulfillmentText':"{} {} is {} {}".format(amount ,source_currency ,final_amount ,target_currency)
    }
    
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
    
    