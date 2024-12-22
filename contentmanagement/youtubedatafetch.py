# -*- coding: utf-8 -*-

import os
import googleapiclient.discovery
import datetime
from django.utils import timezone
from .models import Channel, Video
import re

def fetchchanneldetails():
    print("Fetching channel details...")
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyA4wmO-rqHg2VuBziv6LFWoXpOSb5z-t0E"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    # Fetch channel details
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        forHandle="@miccamerastories"
    )
    response = request.execute()
    title = response['items'][0]['snippet']['title']
    description = response['items'][0]['snippet']['description']
    subscribers = response['items'][0]['statistics']['subscriberCount']
    views = response['items'][0]['statistics']['viewCount']
    videos = response['items'][0]['statistics']['videoCount']
    
    channel = Channel.objects.all()[0]
    channel.name = title
    channel.description = description
    channel.subscribers = subscribers
    channel.views = views
    channel.videos = videos
    channel.save()

    # Fetch videos from the playlist
    request2 = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=10000,
        playlistId="UUXKcBUDoHQoZESfTWKuoUlQ"
    )
    response = request2.execute()
    videoids = [item['contentDetails']['videoId'] for item in response['items']]

    for videoid in videoids:
        request3 = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=videoid
        )
        response = request3.execute()
        item = response['items'][0]

        # Get video duration in ISO 8601 format (e.g., PT5M30S)
        duration_iso = item['contentDetails']['duration']
        
        # Convert duration to total seconds
        duration_match = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", duration_iso)
        hours = int(duration_match.group(1) or 0)
        minutes = int(duration_match.group(2) or 0)
        seconds = int(duration_match.group(3) or 0)
        total_duration_seconds = hours * 3600 + minutes * 60 + seconds
        # Filter out videos shorter than 1 minute (60 seconds)
        if total_duration_seconds <= 60:
            continue

        title = item['snippet']['title']

        description = item['snippet']['description']
        url = f"https://www.youtube.com/watch?v={videoid}"
        thumbnail = item['snippet']['thumbnails']['high']['url']
        created_at = timezone.make_aware(datetime.datetime.strptime(item['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ"))
        likes = int(item['statistics'].get('likeCount', 0))
        views = int(item['statistics'].get('viewCount', 0))

        video, created = Video.objects.get_or_create(videoId=videoid)

        # Update fields
        video.title = title
        video.description = description
        video.url = url
        video.thumbnail = thumbnail
        video.created_at = created_at
        video.views = views
        video.likes = likes

        # Save the object
        video.save()

if __name__ == "__main__":
    fetchchanneldetails()
