# please change the path to your own directory and file

srt_need_to_transcript = 'E:/作业/570/p2-group-1/captions.srt'
transcript_file = './transcript.csv'

# code operation
import os
import re
import csv
import time

# function to get the data from srt file
lines_collection = "line#,time,text\n"
with open(srt_need_to_transcript, 'r', encoding='utf-8') as f:
    print("Reading srt file...")
    Counter = 1
    for line in f:
        new_line = re.sub(r'\n', '', line)
        new_line = re.sub(r',', ':', new_line)
        if not new_line:
            lines_collection += "\n"
            continue
        lines_collection += new_line + ","

#function to write the data to csv file
with open(transcript_file, 'w', encoding='utf-8') as f:
    f.write(lines_collection)
    print("Successfully write to csv file")
