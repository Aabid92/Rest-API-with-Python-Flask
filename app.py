from flask import Flask, request
app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items":[
            {
                "name": "Chair",
                "price": 15.99
            },
            {
              "name": "Chair",
              "price": 15.99  
            }

        ]
    }
]



@app.route("/store", methods=["GET"])
def get_store():
    return {"stores": stores}


@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items":[]}
    stores.append(new_store)
    return new_store, 201

@app.route("/store/<string:name>/item", methods=["POST"])
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price":request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "store not found"}, 404






