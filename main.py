from fraud_blocker_mongo_lib.os import MainDir, join_paths
from fraud_blocker_mongo_lib.database import MongoDB
import dotenv
import os
import pandas as pd


def create_mongo_doc(data):
    dictionary = {}

    dictionary['step'] = data['step']
    dictionary['type'] = data['type']
    dictionary['amount'] = data['amount']
    dictionary['origin'] = {'name': data['nameOrig'],
                            'balance': [{'old_balance': data['oldbalanceOrg']},
                                        {'new_balance': data['newbalanceOrig']}]}
    dictionary['destination'] = {'name': data['nameDest'],
                                 'balance': [{'old_balance': data['oldbalanceDest']},
                                             {'new_balance': data['newbalanceDest']}]}
    dictionary['isFlaggedFraud'] = data['isFlaggedFraud']
    dictionary['isFraud'] = data['isFraud']

    return dictionary


def create_pk(dict_file, primary_key):
    for dictionary in dict_file: # Creates a PK if necessary
        dictionary["_id"] = dictionary.pop(primary_key)
    return dict_file


def run(mongo):
    directory = MainDir(__file__)

    file = os.listdir(directory.DATA_DIR)[0]
    print(f"\nLoading {file}...")
    data = pd.read_csv(join_paths(([directory.DATA_DIR, file])))

    print(f"Inserting Data...")
    collection_name = "transactions"
    for index, row in data.iterrows():
        dict_file = create_mongo_doc(row)

        # pk = # TO DEFINE
        # dict_file = create_pk(dict_file, pk)
        mongo.collection(collection_name).insert_one(dict_file)
    print(f"Collected and Uploaded {collection_name} Data!")


if __name__ == "__main__":
    # dotenv.load_dotenv(dotenv.find_dotenv(os.path.expanduser(".env")))
    password="your_password" #os.getenv("MONGO_SERVER_PASSWORD")
    db_name = "fraud_blocker_data"

    client = f'''mongodb+srv://fraud_blocker:{password}@fraudblockercluster.rmouk.mongodb.net/{db_name}?retryWrites=true&w=majority'''
    mongo = MongoDB(db_name, client)

    # Connect to MongoDB and Insert Data
    # run(mongo)
    print("Done!")


