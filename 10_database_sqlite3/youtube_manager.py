import sqlite3
conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    print("\nList of a Videos")
    print("*" * 60)
    for row in cursor.fetchall():
        print(row)
    print("*" * 60)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(index, name, time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?", (name, time, index))
    conn.commit()

def delete_video(index):
    cursor.execute("DELETE FROM videos WHERE id=?", (index,))
    conn.commit()

def main():
    while True: 
        
        print("\n Youtube Manager with SQLite3 || Choose an Option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a Youtube video Details")
        print("4. Delete a Youtube Video")
        print("5. Exit the App")

        choose = input("Enter Your Choice: ")

        match choose:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter the Video Name: ")
                time = input("Enter the Video Time")
                add_video(name, time)
            case '3':
                index = input("Enter Video Id to Update: ")
                name = input("Enter the Video Name: ")
                time = input("Enter the Video Time")
                update_video(index, name, time)
            case '4':
                index = input("Enter Video Id to Delete: ")
                delete_video(index)
            case '5':
                break
            case _:
                print("Invalid Choice!")
    conn.close()

if __name__ == "__main__":
    main()
