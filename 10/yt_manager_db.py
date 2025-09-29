import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS videos(
              id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              time TEXT NOT NULL
              )""")

def list_videos():
   cursor.execute("SELECT * FROM videos")
   for row in cursor.fetchall():
      print(row[1])
def add_video(name, time):
   cursor.execute("INSERT INTO videos(name, time) VALUES(?,?)",(name, time))
   conn.commit()

def update_video(vid_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id=?",(new_name, new_time, vid_id))
    conn.commit()
def delete_video(vid_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(vid_id,))
    conn.commit()
def main():
    while True:
     
     print("\n Youtube manager pp with db.")
     print("1 List videos.")
     print("2 Add videos")
     print("3 Update videos")
     print("4 Delete videos")
     print("Exit the app.")
     choice = input("enter your choice")


     if choice =="1":
        list_videos()
     elif choice =="2":
        name = input("Enter the video name")
        time = input("Enter the video time")
        add_video(name, time)
     elif choice =="3":
        vid_id = input("Enter video id to update:")
        name = input("Enter the video name")
        time = input("Enter the video time")
        update_video(vid_id,name, time)
     elif choice =="4":
        vid_id = input("Enter video id to delete:")
        delete_video(vid_id)
     elif choice =="5":
        break
     else:
        print("Invalid choice")
    conn.close()


if __name__ == "__main__":
    main()