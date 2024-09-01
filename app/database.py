from pymongo import MongoClient
import ssl

def connect_db():
    try:
        client = MongoClient(
            "mongodb+srv://ameay35:3rBNNKtaOoEmQEUJ@cluster0.bgykyvk.mongodb.net/kimo_db",
            tls=True, 
            tlsAllowInvalidCertificates=False
        )
        db = client['kimo_db']
        return db
    except Exception as e:
        print(f"An error occurred while connecting to MongoDB: {e}")
        raise
