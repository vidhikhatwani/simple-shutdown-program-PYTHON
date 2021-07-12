import os

shutdown = input("Do you want to shutdown your computer ? (Y/N): ")
  
if shutdown == 'N':
    exit()
else:
    os.system("shutdown /s /t 1")
