# Warm Up Bot
Are you tired of sitting down to do creative work and struggling to get started? Do you wish you had a way to warm up your mind and get your creative juices flowing? Look no further than the Warm Up Bot! With Github actions and a CSV file, you can generate a personalized list of warm-up exercises to execute every day.

## Who is this for:
This tool is perfect for anyone looking to optimize their creative routine. Whether you're a painter or someone who needs to warm up before a workout, the Warm Up Bot has got you covered.

# How to use this

## Setting this up for your account

### Step 1 
Turn on Github Actions for your repo. It's by default off but go into settings and switch it on. 
![image](https://user-images.githubusercontent.com/24465934/224672276-29a8cac1-44ec-4904-a281-5821b1adb29f.png)


### Step 2 
Set Workflow Actions to read and write - this is so your integration can drop tasks into the Issues tab.
![image](https://user-images.githubusercontent.com/24465934/224672308-3aa4ebc7-2067-409f-9c67-57196002bf5f.png)

## Generating a warm up routine

### Step 3
Create exercises you want to generate for your to-do list. 

You do this by adding tasks in the kata.csv (named after the [exercises you do in karate](https://en.wikipedia.org/wiki/Kata))

Currently, it's one excercise per Genre so feel free to have a good play around to see what works for you. 

The format of exercises (with examples) is as follows: 

  | Task to do   | Details on the task to do   | Genre of Task |
  |--------------|--------------|--------------|
  | TASK | DETAILS OF TASK SUCH AS URL| ART  |
  | PUSH UPS | HOW MANY TO DO | GYM   |
  | READ A FRENCH ARTICLE | LINK TO FRENCH WEBSITE | FRENCH |

In kata.csv is an example of various art exercises I do before I draw.

Feel free to overwrite it with your own exercises!

Once you set that up and push it to your main branch, every midnight, a cron job using Github Actions will run for you and create a To Do list for you! Assuming you've done everything right, you'll get emailed everyday.

[See an example](https://github.com/vikadilly/creativeroutinebot/issues/11)

# Want to support this project? 

Just shout out about it and let me know what's on your mind on my Twitter [@vikadilly](https://twitter.com/vikadilly)

If you make your tasks list public, let me know and I am more than happy to link them so others can use them!


