#!/usr/bin/env python3

#Author ID: 131382228

import subprocess

def free_space():
    df = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    dfOutput = df.communicate()
    return dfOutput[0].decode('utf-8').strip()

print(free_space())
