from astrapy import DataAPIClient
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

ENDPOINT = os.getenv("ASTRA_ENDPOINT")
TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")


@st.cache_resource
def get_db():
    client = DataAPIClient(TOKEN)
    db = client.get_database_by_api_endpoint(ENDPOINT)
    return db

db = get_db()
collection_names = ["personal_data", "notes"]

existing_collections = [c.name for c in db.list_collections()]
for collection in collection_names:
    if collection not in existing_collections:
        db.create_collection(collection)

    
personal_data_collection = db.get_collection("personal_data")
notes_collection = db.get_collection("notes")