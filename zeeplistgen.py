import os, csv
from tkinter import filedialog
from datetime import date
today = str(date.today().strftime("%d%m%Y"))
folder,amountOfLevels ,levels,start= filedialog.askdirectory(),0,[],0
for r, d, f in os.walk(folder):
    print('|',end='')
    for file in f:
        if file.lower().endswith('.zeeplevel'):
            with open(r+'/'+file, 'r') as file:
                level=list(csv.reader(file))
            Author,UID=level[0][1],level[0][2]
            WorkshopID=r.replace('\\','/').split('/')[-2]
            Name=r.replace('\\','/').split('/')[-1]
            levels.append([UID,WorkshopID,Name,Author])
            amountOfLevels+=1
zeeplist=f"""{{
    "name": "zeeplistgen{today}",
    "amountOfLevels": {amountOfLevels},
    "roundLength": 20,
    "shufflePlaylist": true,
    "UID": [],
    "levels": ["""
for i in levels:
    zeeplist+=f"""
        {{
            "UID": "{i[0]}",
            "WorkshopID": {i[1]},
            "Name": "{i[2]}",
            "Author": "{i[3]}"
        }},
"""
zeeplist=zeeplist[:-2]
zeeplist+="""
    ]
}"""
with open(f'zeeplistgen{today}.zeeplist', 'w', encoding='utf-8', errors='ignore') as f:
    f.write(zeeplist)