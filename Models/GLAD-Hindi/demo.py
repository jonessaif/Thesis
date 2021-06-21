import json
from subprocess import call
import os
with open ('demo_data.txt','r',encoding='utf8')as f:
    l = f.readline()

o = [
    {
        "dialogue_idx": 800,
        "dialogue": [
            {
                "turn_label": [
                    
                ],
                "asr": [
                    [
                        l,
                        1.0
                    ]
                ],
                "system_transcript": "",
                "turn_idx": 0,
                "belief_state": [
                    
                ],
                "transcript": l,
                "system_acts": []
            }
            ]}]



os.remove('data/woz_hin/ann/demo.json')
with open('data/woz_hin/raw/demo.json','w',encoding='utf8')as w:
     json.dump(o,w,ensure_ascii=False,indent=4)

call(['python','preprocess_data.py'])

call(["python","evaluate.py","--split=demo","exp/glad/default/"])


