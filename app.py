import requests
import json
import os
from get_comment import get_video_comment
from scene_emotion import get_scene_emotions
from extraction import split_comments
from flask import Flask, jsonify, make_response, request, Response
from mlask import MLAsk

app = Flask(__name__)

@app.route('/')
def index():
    name = "Hello World"
    return name

@app.route('/youtube_emotions', methods=['POST'])
def youtube_emotions():
    req_json = request.get_json()
    video_id = req_json['video_id']

    comments = get_video_comment(video_id, order='relevance', max_n=10000)
    comments = [row[1] for row in comments]
    comments = split_comments(comments[1:])
    scene_emotion = get_scene_emotions(comments)
    json_result = json.dumps(scene_emotion, sort_keys=True)
    return json_result

@app.route('/youtube_time_comment', methods=['POST'])
def youtube_time_comment():
    req_json = request.get_json()
    video_id = req_json['video_id']

    comments = get_video_comment(video_id, order='relevance', max_n=10000)
    comments = [row[1] for row in comments]
    comments = split_comments(comments[1:])

    time_comments = {}
    for comment in comments:
        if comment[0] in time_comments:
            time_comments[comment[0]].extend([comment[1]])
        else:
            time_comments[comment[0]] = [comment[1]]

    json_result = json.dumps(time_comments, sort_keys=True)
    return json_result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))