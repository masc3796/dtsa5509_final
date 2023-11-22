import os
import csv

rootpath = "/home/matt/Documents/MSEE/DTSA5509_Machine_Learning_I_Supervised_Learning/Final_Project/faces/"

with open("data_index.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow([
        "path",
        "username",
        "direction",
        "mood",
        "sunglasses",
        "direction_left",
        "direction_right",
        "direction_straight",
        "direction_up",
        "mood_angry",
        "mood_happy",
        "mood_neutral", 
        "mood_sad", 
        "sunglasses_on"
        ])

    for root, dirs, files in os.walk(rootpath, topdown=False):
        for name in files:
            fname = os.path.join(root, name)
            
            if (not "_2" in fname) and (not "_4" in fname) and (".pgm" in fname):
            #if ("_4" in fname) and (".pgm" in fname):
            
                sp = fname.split("_")
                w.writerow([
                    rootpath + fname[2:],           #path
                    sp[0].split("/")[:-1][1],       #username
                    sp[1],                          #direction
                    sp[2],                          #mood
                    sp[3][:-4],                     #sunglasses
                    str(int(sp[1] == "left")),
                    str(int(sp[1] == "right")),  
                    str(int(sp[1] == "straight")),
                    str(int(sp[1] == "up")), 
                    str(int(sp[2] == "angry")), 
                    str(int(sp[2] == "happy")), 
                    str(int(sp[2] == "neutral")),                     
                    str(int(sp[2] == "sad")),                                         
                    str(int("sunglasses" in sp[3]))                                        
                ])
            
            
            

