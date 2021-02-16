import requests
import json
import settings
import csv

def get_video_comment(video_id, part='snippet', order='time', text_format='plaintext', max_n=100):
    URL = 'https://www.googleapis.com/youtube/v3/'
    API_KEY = settings.API_KEY
    get_cnt = 0
    comments = [['video_id', 'comment', 'like_cnt', 'reply_cnt']]
    next_page_token = ''

    while (get_cnt < max_n):
        params = {
            'key': API_KEY,
            'part': part,
            'videoId': video_id,
            'order': order,
            'textFormat': text_format,
            'maxResults': max_n - get_cnt,
            'pageToken': next_page_token,
        }
        response = requests.get(URL + 'commentThreads', params=params)
        resource = response.json()

        for comment_info in resource['items']:
            get_data = []
            # コメント
            comment = comment_info['snippet']['topLevelComment']['snippet']['textDisplay']
            # グッド数
            like_cnt = comment_info['snippet']['topLevelComment']['snippet']['likeCount']
            # 返信数
            reply_cnt = comment_info['snippet']['totalReplyCount']

            get_data.extend((video_id, comment, like_cnt, reply_cnt))
            comments.append(get_data)

        # これ以上取得できるコメントがない場合
        if ('nextPageToken' not in resource):
            break
        
        get_cnt += resource['pageInfo']['totalResults']
        next_page_token = resource['nextPageToken']

    return comments

def store_comment_csv(file_path, comments):
    with open(file_path, 'w', newline="", errors="ignore") as f:
        writer = csv.writer(f)
        writer.writerows(comments)