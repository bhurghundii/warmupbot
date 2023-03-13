# Warm Up Bot
Ever sat down to do a creative work, only to struggle to get started? What you need is a warm up!
Using Github actions and a CSV file, randomly geneate a warm up excercise list to execute every day!

## Who is this for: 
Optimise your creative routine by generating a list of ** warm up excercises ** to get started against.
I use this tool personally to give me a list of excercises to warm up against before I start painting but ** you can use this for any other task such as workout routines ** 

## Why use this:
It's totally free and completely self-contained on Github. 
This is good as this means you own your bots and don't require any extra SaaS subscriptions to get yourself a plan that works for you!

# How to use this

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

# Want to support this project? 

We need technical help to write tests and extend this to support other data formats and potentially other tasks.

If you make your tasks list public, let me know and I am more than happy to link them so others can use them!

## Got ideas or improvements? Here are my socials: 
Twitter - [@vikadilly](https://twitter.com/vikadilly)
