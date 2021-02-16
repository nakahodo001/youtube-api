from mlask import MLAsk
import re
import csv
import const

def get_csv(filepath):
    with open(filepath) as f:
        reader = csv.reader(f)
        data = [row for row in reader]

    return data

def get_emotion_point(emotions):
    emotion_point = [0] * const.EMOTION_CNT
    for emotion in emotions:
        emotion_point[const.EMOTION_ROMA.index(emotion)] += 1

    return emotion_point

def most_scene_emotions(scene_emotions):
    scene_most_emotions = {}
    for scene, emotions in scene_emotions.items():
        max_point = max(emotions)
        most_emotion = [const.EMOTION_KANJI[index] for index, point in enumerate(emotions) if max_point == point]
        scene_most_emotions[scene] = most_emotion

    return scene_most_emotions

def get_scene_emotions(data):
    emotion_analyzer = MLAsk()
    scene_emotions = {}

    for scene in data:
        res = emotion_analyzer.analyze(scene[1])

        # 感情値が無い時
        if res['emotion'] is None:
            continue

        emotion_point = get_emotion_point(res['emotion'])
        if scene[0] in scene_emotions:
            for index, point in enumerate(emotion_point):
                scene_emotions[scene[0]][index] += point
        
        else :
            scene_emotions[scene[0]] = emotion_point

    return most_scene_emotions(scene_emotions)