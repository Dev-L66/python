import pymongo
import os
import dotenv
from bson import ObjectId

dotenv.load_dotenv()


client = pymongo.MongoClient(os.environ.get("MONGODB_URI"), tlsAllowInvalidCertificates=True)
# tlsAllowInvalidCertificates=True not a good practice
db =client["ytmanager"]
videos_collection = db["videos"]

print(videos_collection)


def list_videos():
    videos = videos_collection.find()
    for video in videos:
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}" )

def add_video(name, time):
    videos_collection.insert_one({"name":name, "time":time})

def update_video(vid_id,new_name, new_time):
    videos_collection.update_one({"_id":ObjectId(vid_id)},{"$set":{"name":new_name, "time":new_time}})    

def delete_video(vid_id):
    videos_collection.delete_one({"_id":ObjectId(vid_id)})

def main():
   while True:
       print("Youtube Manager")
       print("1 List videos")
       print("2 Add videos")
       print("3 Update videos")
       print("4 Delete videos")
       print("5 Exit the app")
       choice =input("Enter your choice: ")

       if choice == "1":
           list_videos()
       elif choice == "2":
           name=input("Enter video name")
           time=input("Enter video time")
           add_video(name, time)
       elif choice == "3":
           vid_id=input("Enter video id to update:")
           name=input("Enter video name")
           time=input("Enter video time")
           update_video(vid_id,name, time )
       elif choice == "4":
           vid_id=input("Enter video id to update:")
           delete_video(vid_id)
       elif choice == "5":
           break
       else:
           print("Invalid choice")



if __name__ == "__main__":
     main()