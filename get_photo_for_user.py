from pymongo.mongo_client import MongoClient
from enter_to_mongoDB import url

#get photo for user
try:
    uri = url
    client = MongoClient(uri)
    db = client.db_photosGener
    collection = db.photos
    # get all the documents from the collection db
    while True:
        for document in collection.find({}):
            print(f"ID: {document['id']}, "
                  f"Status: {document['status']},"
                  f"Prompt: {document['prompt']}",
                  f"Time: {document['time']}",
                  f"Url: {document['url']}")
        print("-------------------------------------------------------------------")
        print(collection.count_documents({}))
        #delete photo from db
        if collection.count_documents({}) >= 1000:
            prompt = input("Enter your request id for delete: ")
            collection.delete_one({"id": int(prompt)})
            print("Well done! Your deleted one photo!")
            print("-------------------------------------------------------------------")
        else:
            # get photo from db
            prompt = input("Enter your request id for see: ")
            url_document = collection.find_one({"id": int(prompt)})
            print(url_document['url'])
            print("-------------------------------------------------------------------")


except Exception as error:
    print(error)
    print('Not connected to MongoDB')