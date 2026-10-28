import os
from collections import Counter
from datetime import datetime

log_file="C:\learning\python @\my projects\Python Log Generator & Event Logger"
log_file_path=os.path.join(log_file,"app.log")
with open (log_file_path , "r") as f :
    logs=f.readlines()

def Severity_summery():
    all_severity_levels=["DEBUG", "INFO", "WARNING", "ERROR" ,"CRITICAL"]
    severity_levels=[]
    for log in logs:
        log_split=log.split(" ")
        if len(log_split)>=3:
            severity_level=log_split[2]
            if severity_level in all_severity_levels:
                severity_levels.append(severity_level)
    items_count=Counter(severity_levels)
    print(items_count)
    print(f"most common three severity levels are,\n{(items_count.most_common(3))}")

def error_detective():
    error_list=[]
    for log in logs:
        if len(log.split(" "))>=3:
            severity_level=log.split(" ")[2]
            if severity_level=="ERROR":
                error_list.append(log)
    error_messages=[]
    for error in error_list:
        if len(error.split(": ",maxsplit=1))>=2:
            error_message=error.split(": ",maxsplit=1)[1].strip()
            error_messages.append(error_message)
    error_count=Counter(error_messages)
    print(error_count.most_common(3))

def Search_logs_by_keyword():
    key_word_match=False
    key_word=input("Enter keyword:").lower()
    if not key_word:
        print("Please enter something")
        return
    for log in logs:
        if key_word in log.lower():
            key_word_match=True
            print(log)
    if key_word_match==False:
        print("No matching log found")

def Filter_logs_by_severity():
    match_found=False
    all_severity_levels=["DEBUG", "INFO", "WARNING", "ERROR" ,"CRITICAL"]
    severity_level_input=input("Enter severity level:").upper()
    if not severity_level_input:
        print("Please enter something")
        return
    if severity_level_input not in all_severity_levels:
        print("Invalid severity level")
        return
    for log in logs:
        if len(log.split(" "))>=3:
            severity_level=log.split(" ")[2]
            if severity_level_input==severity_level:
                match_found=True
                print (log)
    if match_found==False:
        print("No matching log found")

def date_time():
    match_found=False
    start_time=input("Enter starting time:")
    if not start_time:
        print("Please enter a starting time!")
        return
    start_time=datetime.strptime(start_time,"%Y-%m-%d %H:%M:%S")
    end_time=input("Enter ending time:")
    if not end_time:
        print("Please enter a ending time!")
        return
    end_time=datetime.strptime(end_time,"%Y-%m-%d %H:%M:%S")
    if start_time>end_time:
        print("Please enter valid timestamp")
        return
    for log in logs:
        log_split=log.split(" ")
        try:
            if len(log_split)>3:
                d_t=f"{log_split[0]} {(log_split[1])}"
                d_t=datetime.strptime(d_t,"%Y-%m-%d %H:%M:%S")
                if start_time<=d_t<=end_time:
                    match_found=True
                    print(log)
        except ValueError as v:
            continue
    if match_found==False:
        print("no log is found during this timestamp")


def menu():
    while True:
        print("=====log analyzer and error detector menu=====")
        print("1.Log report summery")
        print("2.Detect error")
        print("3.Search log by keyword")
        print("4.Get log by severity level")
        print("5.Show logs between timestamp")
        print("6.Exit")

        try:
            choice=int(input("Enter your choice:"))
        except:
            print("Enter a valid choice!")
            continue
        if choice==1:
            Severity_summery()
        elif choice==2:
            error_detective()
        elif choice==3:
            Search_logs_by_keyword()
        elif choice==4:
            Filter_logs_by_severity()
        elif choice==5:
            date_time()
        elif choice==6:
            print("Exiting....")
            break
        else:
            print("Enter a valid choice!")
menu()
