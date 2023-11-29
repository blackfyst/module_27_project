#!/usr/bin/env python3

import os
import requests
import json

# path = "/data/feedback/" # VM URL file system
path = "/home/donsacafq/Module_27_project/data/feedback/"

def list_files():
    """Get list of files"""
    file_list = os.listdir(path)
    return file_list

def convert_data_from_files_and_upload(file_list):
    """Convert the data from the files into a dictionary then use the Python requests module to post the dictionary to a running web service in the correct format"""
    for file in file_list:
        dictionary = dict()
        data_line = 0
        titles = ["title", "name", "date", "feedback"]
        url = "http://34.31.174.147/feedback/"
        if file.endswith('.txt'):
            with open(os.path.join(path, file)) as my_file:
                for line in my_file:
                    key = titles[data_line]
                    dictionary[key] = line.strip()
                    data_line += 1
                # response = requests.post(url, data=dictionary)
                response = 202 # In lieu of post request above
                if response != 201: #.status_code != 201:
                    print(response)
        else:
            print("{} is not a txt file.".format(os.path.join(path, file)))

def main():
    convert_data_from_files_and_upload(list_files())

if __name__ == "__main__":
    main()