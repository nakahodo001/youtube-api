import requests
import json
import settings
import csv

def print_video_comment(video_id, part='snippet', order='time', text_format='plaintext', max_n=10):
    params = {
        'key': API_KEY,
        'part': part,
        'videoId': video_id,
        'order': order,
        'textFormat': text_format,
        'maxResults': max_n,
    }
    response = requests.get(URL + 'commentThreads', params=params)
    resource = response.json()

    with open('./test2.json', 'w') as f:
        json.dump(resource, f, indent=4)

    comments = [['video_id', 'comment', 'like_cnt', 'reply_cnt']]
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

    return comments

def store_comment_csv(file_path, comments):
    with open(file_path, 'w', newline="", errors="ignore") as f:
        writer = csv.writer(f)
        writer.writerows(comments)

URL = 'https://www.googleapis.com/youtube/v3/'
API_KEY = settings.API_KEY
video_id = 'QNSR8pl38EM'
file_path = './comment/' + video_id + '.csv'

comments = print_video_comment(video_id, order='relevance', max_n=10000)
#print(comments)
store_comment_csv(file_path, comments)