"""
OV: Simulate time-wasting via browsing pseudo-random sites/subpages

- Pick parent site, go to function for specific API/visit usage
    - reddit: Use reddit API to browse select subreddits/recent posts for 5-15 minutes
    - youtube: YT google API to pick random videos until length of viewing (5-15 min) is reached.
    - washingtonpost: curl recent storied every 2-5 min for 5-15 min
    - cnn: same as WP
    - Imgur:

"""
import os
import random
import time

from sites import *
from youtube import get_video


def main():
    time_waste = random.randint(300, 1500)
    #time_waste = random.randint(3, 5)
    print("need to waste {} seconds".format(time_waste))
    #action = main_sites[random.randint(0, len(main_sites)-1)]
    action = 'reddit'

    if action == 'youtube':
        channel_id = youtube_channels[random.randint(0, len(youtube_channels)-1)]
        time_spent = 0
        while time_spent < time_waste:
            watch_time = min(get_video(channel_id), time_waste)  # cap at wasted time max
            time_spent += watch_time
            time.sleep(watch_time)  # watching video
            time.sleep(10)  # finding new video

    elif action == 'reddit':
        subreddit = subreddits[random.randint(0, len(subreddits)-1)]
        print(subreddit)
        os.system('curl https://www.reddit.com/r/{}/'.format(subreddit))

    elif action == 'washingtonpost':
        p=1



if __name__ == "__main__":
    main()
