import praw, requests, re, glob, PIL, shutil, os

reddit = praw.Reddit(client_id="56F4l_V2nA4HnEF2xwLCVg", client_secret="j9F5gfWzCMLt68do3kotY4hUTiP_UA",
                     user_agent="Calvin&Hobbes Scraper")
# hot_posts = reddit.subreddit('calvinandhobbes').hot(limit=100)
image_list = []
# users = reddit.user('u/CalvinBot').get_submitted()

for post in reddit.redditor('CalvinBot').submissions.top(limit=1000):
    try:
        url = post.url
        file_name = url.split("/")
        if len(file_name) == 0:
            file_name = re.findall("/(.*?)", url)
        file_name = file_name[-1]
        if "." not in file_name:
            pass
        else:
            print(file_name)
            r = requests.get(url)
            with open(file_name, "wb") as f:
                f.write(r.content)
            image_list.append(file_name)
    except OSError:
        print("Not an Image! Continuing")

# Solution was meant to take ALL posts from r/Calvinandhobbes, sort them by RGB value to determine what is and isn't a
# strip, and sort accordingly. Because the bot already posts only strips, this solution was not implemented.
'''suspiciousImages = []
notSuspicious = []
for images in image_list: 
    try:
        img = PIL.Image.open(images).convert('RGB')
        w, h = img.size
        pixelThreshold = (w * h) * .5
        suspiciousPixels = 0
        for i in range(w):
            for j in range(h):
                r, g, b = img.getpixel((i, j))
                if r != g != b:
                    suspiciousPixels += 1
        if suspiciousPixels >= pixelThreshold:
            suspiciousImages.append(images)
        else:
            notSuspicious.append(images)
    except OSError:
        print("Not an Image! Continuing.")'''

try:
    os.mkdir('strips')
except OSError:
    print("Creation of Directory Failed!")
else:
    print('Creation Successful.')


for images in image_list:
    try:
        shutil.move(images, "strips")
    except OSError:
        print('Failed! Continuing.')
