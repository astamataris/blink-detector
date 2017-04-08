import csv
import sys
import numpy as np
import pandas as pd #use the pandas module as a dataframe
from datetime import datetime

#tsv file has a total of 12 columns
data = [range(13)] #create a list from 0-12 since we need a total of 13 columns

#open tsv file as tsvin and return csv out,remember to add the rU
with open('40 blue vt.tsv', 'rU') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    for row in tsvin:
        data.append(row)

header = data[0] #assign the header to the first row of data
data.pop(0)        #remove the first row which corresponds to names given by tobii studio

header.append("Time")#add "Time" to the list to create a new column
header.append("Sum") #add "Sum" to the list to create a new column

for i in range(1, len(data)): #iterate through all columns skiping the first row

    if data[i][10] != '' and data[i][11] != '': #only use data that are not blank
        Sum = int(data[i][11]) + int(data[i][12]) #add data from columns 11 and 12
        data[i].append(Sum) #add the result to the last column

df = pd.DataFrame(data, columns=header) # create a new dataframe that uses the data list

#split the data into reading and tracking task

Reading = df[df.icol(7) == "Text 2_1.avi"] #select data from the sample text stimulus
Dot = df[df.icol(7) == "brown_mot_360_A.avi"] # select data from the dot tracking stimulus


Reading1 = Reading[0:len(Reading)/2:1] #split the data frame into the first part
Reading2 = Reading[len(Reading)/2:len(Reading):1] #split the data frame to the second part
Dot1 = Dot[0:len(Dot)/2:1] #split the data frame into the first part
Dot2 = Dot[len(Dot)/2:len(Dot):1]#split the data frame to the second part

Readings1 = Reading1[Reading1.Sum == 8] #only use rows that are possible blinks Sum == 8
Dots1 = Dot1[Dot1.Sum == 8] #only use rows that are possible blinks Sum == 8
Readings2 = Reading2[Reading2.Sum == 8] #only use rows that are possible blinks Sum == 8
Dots2 = Dot2[Dot2.Sum == 8] #only use rows that are possible blinks Sum == 8

i = 0  # initialise i to 0
counter = 0
duration = 0
while i < len(Readings1):
    s = i #set start as i
    e = s #set end as e
    while e < len(Readings1) - 1 and Readings1.index[e + 1] == Readings1.index[e] + 1: #first statement ensures we stay within bounds of df1 and the second checks if the next index number is an increment of 1
        e = e+1 # while correct, increment e by 1
      #Referencing cells df1.iat[0,77]

    Time = int(Readings1.iat[e, 10])-int(Readings1.iat[s, 10])
    #print "Time from " + str(Readings1.index[s]) + " to " + str(Readings1.index[e]) + " is " + str(Time)
    if s == e:
        i = i+1
    else:
        i = e + 1

    if Time > 59000 and Time < 400000: #if time is in rage of a blink specification
        counter += 1
        duration += int(Time)
print "---------------R E A D I N G   T A S K -- 1 S T   P A R T-------------------"
if counter > 0:
    print "Total Blinks: " + str(counter)
    print "Average Blink duration: " + str(int(duration)/counter)
else:
    print "Total Blinks: 0"
    print "Average Blink Duration: 0"

#print df.iat[1,24]
#print df.iat[len(df)-1,24]

initial_time = str(Readings1.iat[1, 9])
final_time = str(Readings1.iat[len(Readings1)-1, 9])
FMT = '%H:%M:%S.%f'
total_time = datetime.strptime(final_time, FMT) - datetime.strptime(initial_time, FMT)


print total_time.total_seconds()
print str(counter) + " blinks" + " in " + str(total_time.total_seconds()) + " seconds"

blink_rate_per_minute = (float(counter) * 60)/(float(total_time.total_seconds()))
print "Blink rate per minute is " + str(blink_rate_per_minute)
print "\n\n"

i = 0  # initialise i to 0
counter = 0
duration = 0
while i < len(Readings2):

    s = i #set start as i
    e = s #set end as e

    while e < len(Readings2) - 1 and Readings2.index[e + 1] == Readings2.index[e]+1: # first statement ensures we stay within bounds of df1 and the second checks if the next index number is an increment of 1
        e = e+1 # while correct, increment e by 1
      # Referencing cells df1.iat[0,77]

    Time = int(Readings2.iat[e, 10])-int(Readings2.iat[s, 10])
    #print "Time from " + str(Readings2.index[s]) + " to " + str(Readings2.index[e]) + " is " + str(Time) 
    if s == e:
        i = i+1
    else:
        i = e + 1

    if Time > 59000 and Time < 400000: #if time is in rage of a blink specification
        counter += 1
        duration += int(Time)

print "---------------R E A D I N G   T A S K -- 2 N D   P A R T-------------------"
if counter > 0:
    print "Total Blinks " + str(counter)
    print "Average Blink duration " + str(int(duration)/counter)
else:
    print "Total Blinks 0"
    print "Average Blink Duration 0"

#print df.iat[1,24]
#print df.iat[len(df)-1,24]

initial_time = str(Reading2.iat[1, 9]) 
final_time = str(Readings2.iat[len(Readings2)-1, 9])
FMT = '%H:%M:%S.%f'
total_time = datetime.strptime(final_time, FMT) - datetime.strptime(initial_time, FMT)


print total_time.total_seconds()
print str(counter) + " blinks" + " in " + str(total_time.total_seconds()) + " seconds"

blink_rate_per_minute =  (float(counter) * 60)/(float(total_time.total_seconds()))
print "Blink rate per minute is " + str(blink_rate_per_minute)
print "\n\n"

i=0  # initialise i to 0
counter = 0
duration = 0
while i < len(Dots1):

    s = i #set start as i
    e = s #set end as e

    while e < len(Dots1)-1 and Dots1.index[e + 1] == Dots1.index[e] + 1: # first statement ensures we stay within bounds of df1 and the second checks if the next index number is an increment of 1
        e = e+1 # while correct, increment e by 1
      # Referencing cells df1.iat[0,77]

    Time = int(Dots1.iat[e, 10])-int(Dots1.iat[s, 10])
    #print "Time from " + str(Dots1.index[s]) + " to " + str(Dots1.index[e]) + " is " + str(Time) 
    if s == e:
        i = i + 1
    else:
        i = e + 1

    if Time > 59000 and Time < 400000: #if time is in rage of a blink specification
        counter += 1
        duration += int(Time)

print "---------------T R A C K I N G   T A S K -- 1 S T   P A R T------------------"

if counter > 0:
    print "Total Blinks " + str(counter)
    print "Average Blink duration " + str(int(duration)/counter)
else:
    print "Total Blinks 0"
    print "Average Blink Duration 0"
from datetime import datetime

#print df.iat[1,24]
#print df.iat[len(df)-1,24]

initial_time =  str(Dots1.iat[1, 9]) 
final_time = str(Dots1.iat[len(Dots1)-1, 9])
FMT = '%H:%M:%S.%f'
total_time = datetime.strptime(final_time, FMT) - datetime.strptime(initial_time, FMT)


print total_time.total_seconds()
print str(counter) + " blinks" + " in " + str(total_time.total_seconds()) + " seconds"

blink_rate_per_minute = (float(counter) * 60)/(float(total_time.total_seconds()))
print "Blink rate per minute is " + str(blink_rate_per_minute)

i = 0  # initialise i to 0
counter = 0
duration = 0
while i < len(Dots2):

    s = i #set start as i
    e = s #set end as e

    while e < len(Dots2) - 1 and Dots2.index[e + 1] == Dots2.index[e] + 1: # first statement ensures we stay within bounds of df1 and the second checks if the next index number is an increment of 1
        e = e+1 # while correct, increment e by 1
      # Referencing cells df1.iat[0,77]
   
    Time = int(Dots2.iat[e, 10])-int(Dots2.iat[s, 10])
    #print "Time from " + str(Dots2.index[s]) + " to " + str(Dots2.index[e]) + " is " + str(Time) 
    if s == e:
        i = i+1
    else:
        i = e + 1
       
    if Time > 59000 and Time < 400000: #if time is in rage of a blink specification
        counter += 1
        duration += int(Time)
        
print "---------------T R A C K I N G   T A S K -- 2 N D   P A R T------------------"

if counter > 0:
    print "Total Blinks " + str(counter)
    print "Average Blink duration " + str(int(duration)/counter)
else:
    print "Total Blinks 0"
    print "Average Blink Duration 0"
from datetime import datetime

#print df.iat[1,24]
#print df.iat[len(df)-1,24]

initial_time = str(Dots2.iat[1, 9])
final_time = str(Dots2.iat[len(Dots2)-1, 9])
FMT = '%H:%M:%S.%f'
total_time = datetime.strptime(final_time, FMT) - datetime.strptime(initial_time, FMT)


print total_time.total_seconds()
print str(counter) + " blinks" + " in " + str(total_time.total_seconds()) + " seconds"

blink_rate_per_minute = (float(counter) * 60)/(float(total_time.total_seconds()))
print "Blink rate per minute is " + str(blink_rate_per_minute)

