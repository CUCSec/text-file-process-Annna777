import os
import re
f=open(r'C:\Users\79084\Desktop\text-file-process-Annna777\text-file-process\log_files\201811123026.log',encoding="utf8")

l = list()
for line in f:
    line2=re.split(r'[：,]',line)
    l.append(line2[3])
t=l.count('201811123026')
print(t)
