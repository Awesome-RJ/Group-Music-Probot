from os import listdir, mkdir

if "raw_files" not in listdir():
    mkdir("raw_files")

from Group_Music_Probot.services.converter.converter import convert
