# blink-detector

This script was my first ever project with programming and was used in my final year project for my BSc in Psychology.
____
## Project statement
Based on the succes of software like [f.lux](https://justgetflux.com/) I decided to investigate the effect of pressence/absence of red light on displays and how we fatigue. To achieve this, I altered the display settings of the screens reducing red and blue hues to zero respectively.</br>
Participants were asked to read two passages and track two dots moving in brownian motion. Each participant had to carry out the four tasks in red and blue hues respectively while they were being eyetracked using a [Tobii Pro TX300](http://www.tobiipro.com/product-listing/tobii-pro-tx300/) eyetracker. Using the raw data exported in a tsv file I wrote an analytic algorithm that measured the number of valid blinks and their average duration. 
___
## The algorithm
The alogithm first removes data that are not valid (no tracking recorded for both eyes). Secondly it splits the data per test and then iterates through the data to count the number of blinks and their duration. Using these values number of blinks and their total duration, blink rate per minute and average blink duration are also calculated. Results are retunred in the console for each test.
___
## Requirements
Before you can ran the script you will need to istall the following with pip:
* [pandas](http://pandas.pydata.org/)
* [numpy](http://www.numpy.org/)
