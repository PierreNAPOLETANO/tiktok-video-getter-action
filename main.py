from TikTokApi import TikTokApi, exceptions
import json
import sys

args = sys.argv
argsLength = len(args)

defaultVideoNumber = 20

if argsLength != 2 and argsLength != 3:
    print('use like this : python main.py [tiktokUsername] [numberofVideos=' + str(defaultVideoNumber) + ']')
    sys.exit()

api = TikTokApi()
numberOfVideos = int(args[2]) if argsLength == 3 else defaultVideoNumber
username = args[1]
try:
    videos = api.by_username(username, count=numberOfVideos)
except exceptions.TikTokCaptchaError:
    rint(json.dumps({'message': 'TikTok blocked the request using a Captcha'}))
    sys.exit()
except exceptions.TikTokNotFoundError:
    print(json.dumps({'message': 'User not found'}))
    sys.exit()
except Exception as e:
    print(json.dumps({'message': str(e)}))
    sys.exit()

print(json.dumps(videos))
