## Usage

You can to install and configure MongoDB in your computer.<br> 
Or You can just create an account in [Mongo Atlas](https://account.mongodb.com/account/login) and connect to it.

- Download the [Fraud data](https://www.kaggle.com/paulosabinoreis/synthetic-financial-dataset-for-fraud-detection) from kaggle (original link: [Synthetic Financial Datasets For Fraud Detection](https://www.kaggle.com/ealaxi/paysim1)).
- Pull this repository to your computer.
- Create a file called "data" in the main directory and unzip "fraud_data" file there.

Remember to set the connection according to your own MongoDB settings in main.py.

```python
password="your_password" #os.getenv("MONGO_SERVER_PASSWORD")
db_name = "fraud_blocker_data"
```

Uncomment this and run. 

```python
# run(mongo)
```

If you are going to use MongoDB on your local computer, just delete the "client" parameter.

```python
# mongo = MongoDB(db_name, client)
mongo = MongoDB(db_name)
```

[<img align="right" width="60" height="60" src="https://github.com/pauloreis-ds/Paulo-Reis-Data-Science/blob/master/Paulo%20Reis/Pauloreis01.png">](https://github.com/pauloreis-ds)

---
