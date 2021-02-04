from mlask import MLAsk
import re
import csv

EMOTION = {
    'suki': '好',
    'ikari': '怒',
    'kowa': '怖',
    'yasu': '安',
    'iya': '嫌',
    'aware': '焦',
    'takaburi': '昂',
    'odoroki': '驚',
    'haji': '恥',
    'yorokobi': '喜'
}

EMOTION_ROMA = [
    'suki', 'ikari', 'kowa', 'yasu', 'iya', 'aware',
    'takaburi', 'odoroki', 'haji', 'yorokobi'
]

EMOTION_KANJI = [
    '好', '怒', '怖', '安', '嫌', '哀', '昂', '驚', '恥', '喜'
]

EMOTION_CNT = 10

def getCSV(filepath):
    with open(filepath) as f:
        reader = csv.reader(f)
        data = [row for row in reader]

    return data

def getEmotionPoint(emotions):
    emotion_point = [0] * EMOTION_CNT
    for emotion in emotions:
        emotion_point[EMOTION_ROMA.index(emotion)] += 1

    return emotion_point

def mostSceneEmotions(scene_emotions):
    scene_most_emotions = {}
    for scene, emotions in scene_emotions.items():
        max_point = max(emotions)
        most_emotion = [EMOTION_KANJI[index] for index, point in enumerate(emotions) if max_point == point]
        scene_most_emotions[scene] = most_emotion

    return scene_most_emotions

def getSceneEmotions(data):
    emotion_analyzer = MLAsk()
    scene_emotions = {}

    for scene in data:
        res = emotion_analyzer.analyze(scene[1])

        # 感情値が無い時
        if res['emotion'] is None:
            continue

        emotion_point = getEmotionPoint(res['emotion'])
        if scene[0] in scene_emotions:
            for index, point in enumerate(emotion_point):
                scene_emotions[scene[0]][index] += point
        
        else :
            scene_emotions[scene[0]] = emotion_point

    return mostSceneEmotions(scene_emotions)


filename = '4obg8rf3nnQ'
filepath = './comment/' + filename + '-split.csv'

data = getCSV(filepath)
scene_emotion = getSceneEmotions(data)
print(scene_emotion)
