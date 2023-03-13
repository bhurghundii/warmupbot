# Creative Routine Bot
Using Github actions and a CSV file, randomly geneate a to-do list to execute every day!
No SaaS subscription required!

## Purpose 
I use this tool personally to give me a list of excercises to warm up against before I start painting. 
You can use to create add spice to your workout routines, or to learn a language or whatever requires some kind of random task.

## How to use this

### Step 1 
Turn on Github Actions for your repo. It's by default off but go into setitngs and switch it on. 

### Step 2 
Set Workflow Actions to read and write - this is so your integration can drop tasks

### Step 3
Create excercises you want to generate for your to-do list. 

In kata.csv is an example of various art excercises I do before I draw. 

Feel free to overrwrite it with your own excercise but the format for tasks should go like this: 

| Task to do | Details on the task to do | Genre of Task 

Once you set that up and push it to your main branch, every midnight, a Chron job will run for you and create a To Do list for you! 

[See an example](https://github.com/vikadilly/creativeroutinebot/issues/11)
