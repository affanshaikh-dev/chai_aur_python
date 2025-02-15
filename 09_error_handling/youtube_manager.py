import json

def load_data(file):
    try: 
        with open(file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(file, videos):
    with open(file, 'w') as f:   
        json.dump(videos, f)

def list_all_videos(videos):
    print("\nList of a Videos")
    print("*" * 60)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("*" * 60)

def add_video(file, video):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    video.append({'name': name, 'time': time})
    save_data_helper(file, video)
 
def update_video(file, videos):
    list_all_videos(videos)
    index = int(input("Enter The Video Number to update"))
    if(1<= index <= len(videos)):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name':name, 'time':time}
        save_data_helper(file, videos)
    else: 
        print("Invalid Index Selected")

def delete_video(file, videos):
    list_all_videos(videos)
    index = int(input("Enter The Video Number to Delete: "))
    if(1<= index <= len(videos)):
        del videos[index-1]
        save_data_helper(file, videos)


def main():
    file = 'youtube.txt'
    videos = load_data(file)
    while True: 
        print("\n Youtube Manager || Choose an Option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a Youtube video Details")
        print("4. Delete a Youtube Video")
        print("5. Exit the App")

        choose = input("Enter Your Choice: ")

        match choose:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(file, videos)
            case '3':
                update_video(file, videos)
            case '4':
                delete_video(file, videos)
            case '5':
                break
            case _:
                print("Invalid Choice!")

if __name__ == "__main__":
    main()