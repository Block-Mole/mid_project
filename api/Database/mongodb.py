from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

client = MongoClient(os.getenv("URL"))
db = client.get_database("euro2020_mp")