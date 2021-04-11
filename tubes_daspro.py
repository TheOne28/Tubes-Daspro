import os, math, sys, time, argparse, datetime


folder_name = "a"

#Fungsi Load
load_condition = False

parser = argparse.ArgumentParser()
parser.add_argument("--location", "-l", help = "Masukkan nama folder", default = "")
args = parser.parse_args()

if(args.location == folder_name):
    load_condition = True
    print("Selamat datang di Program")
elif(args.location != ""):
    print("Nama folder salah")
else:
    print("Silahkan masukkan nama folder")
    