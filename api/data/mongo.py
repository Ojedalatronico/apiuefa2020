from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
user=os.getenv("MONGO_USER")
password=os.getenv("MONGO_PASS")

URL=f"mongodb+srv://{user}:{password}@uefa.kgpdy.mongodb.net"

db=MongoClient().get_database("UEFA")