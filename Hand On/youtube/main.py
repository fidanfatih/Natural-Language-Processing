from youtube_stastistics import YTstats

API_KEY = "AIzaSyDxi_HowF_0WKoWQsFNAiSLwgMb5gWCEDk"
channel_id = "UC7F1zD7m2-pFHdSaZpV3_Ug"

yt = YTstats(API_KEY, channel_id)
data = yt.get_channel_statistics()
print(data)