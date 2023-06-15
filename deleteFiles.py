import os
from datetime import datetime

#constant to set the max number of days allowed to each file, since its creation until the current day of execution
MAX_DAYS = 14

#get the date from the current day 
today = datetime.now() 

#A tuple to store the desired paths. The following paths are just examples
dir_paths = ("C:\\","C:\\Test-folder-to-github")

for path in dir_paths:
    if os.path.exists(path): 
        try:
            for file in os.listdir(path):
                print(file)
                ##timestamp from the creation of the file    
                timestamp = os.path.getmtime(os.path.join(path,file)) 

                ##convert the timestamp to readable date like yyyy-mm--dd hh:mm:ss:ms
                file_creation = datetime.fromtimestamp(timestamp)

                #Calculate the difference from the current date minus file's creation date                                 
                diff = today - file_creation

                #Check if the result of the difference is greater than MAX_DAYS and if the file's type is .mp4 or .mp3
                if diff.days >= MAX_DAYS and (file.endswith(".mp4") or file.endswith(".mp3")):                    
                    os.remove(os.path.join(path, file))                    

        except OSError as e:
            print(f'Error: {e.filename} - {e.strerror}')
            
    else:
        print("No such file or directorys")
    
    

