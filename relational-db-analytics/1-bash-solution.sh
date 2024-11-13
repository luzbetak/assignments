#!/bin/bash
#-----------------------------------------------------------------------#
# Bash/Shell Question
# Question: How do I list all text files in the current directory 
# (excluding subdirectories) that have been modified in the last month?
#-----------------------------------------------------------------------#
#
find . -maxdepth 1 -name "*.txt" -mtime -30
