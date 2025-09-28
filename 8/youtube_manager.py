import json 

def load_data():
    try:
      with open('youtubee.txt', 'r') as file:
        test = json.load(file)
        print(type(test))
        return test
    except FileNotFoundError:
        return []
                              
def save_data_helper(videos):
    with open('youtubee.txt','w') as file:
        return json.dump(videos, file)


def list_all_videos(videos):
    print("/n")
    print("*"*70)
    for index, video in enumerate(videos, start=1):
         print(f"{index},{video['name']}, {video['time']}.")
    print("/n")
    print("*"*70)


def add_video(videos):
    name = input("enter video name")
    time = input("Enter video time")
    videos.append({'name': name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of the video you want to update"))
    if 1<=index <= len(videos):
        name = input("Enter video name")
        time = input("Enter video time")
        videos[index-1] = {'name': name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid index")

       
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the number of the video you want to delete"))
    if 1<= index <= len(videos):    
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index")



def main():
    videos= load_data()
    while True:
        print("Youtube Manager | choose an option: \n")
        print("1. List favourite videos.")
        print("2. Add a youtube video.")
        print("3. Update youtube video.")
        print("4. Delete a youtube video.")
        print("5.Exit the app.")
        choice = input("Enter your choice:  ")
        print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case"5":
                break
            case _:
                print("Invalid choice")
            
if __name__ == "__main__":
    main()