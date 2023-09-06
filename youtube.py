import re
import json
import requests
import random
from bs4 import BeautifulSoup
import scrapetube


def get_video(channel_id: str):
    """
    Sends curl request for random video in channel, returning the length of that video in seconds

    :param channel_id:
    :return:
    """
    url = 'https://www.youtube.com/channel/{}'.format(channel_id)
    # Get the page source using requests and parse it using BeautifulSoup
    soup = BeautifulSoup(requests.get(url, cookies={'CONSENT': 'YES+1'}).text, "html.parser")

    # Extract the JSON data from the page source using regex
    data = re.search(r"var ytInitialData = ({.*});", str(soup.prettify())).group(1)
    # Parse the JSON data
    json_data = json.loads(data)
    # Extract channel information from the parsed JSON data
    channel_id = json_data['header']['c4TabbedHeaderRenderer']['channelId']

    # Scrape the videos using scrapetube
    chosen_video = list(scrapetube.get_channel(channel_id, limit=50, sort_by="newest"))[random.randint(0,49)]
    print("https://www.youtube.com/watch?v={}".format(chosen_video['videoId']))
    length = [int(x) for x in chosen_video['lengthText']['simpleText'].split(':')]
    print(length)
    if len(length) == 3:  # convert hours to minutes if hours in timestamp
        length[1] += length[0] * 60
        length = length[1:]

    print(length[0]*60 + length[1])
    return length[0]*60 + length[1]



