#coding=utf8
import requests,json
#获取下载地址
def get_down_url(songid):
    req=requests.get("http://tingapi.ting.baidu.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery17206073972467458864_1511011710426&songid=%s&_=1511011713541" %songid)
    req.encoding='utf-8'
    #print(json.loads(req.text))
    json1=json.loads(req.text.replace("jQuery17206073972467458864_1511011710426(","").replace(");",""))
    print("下载地址:",json1["bitrate"]['show_link'])
    return json1["bitrate"]['show_link']
#下载保存文件
def music_down(url,music_name,artistname):
    f=open(music_name+'-'+artistname+'.mp3','wb')
    req_mp3=requests.get(url)
    f.write(req_mp3.content)
    f.close()
#搜索歌曲
music=input("请输入音乐:")
req_url="http://sug.music.baidu.com/info/suggestion?format=json&word=%s&version=2&from=0&callback=window.baidu.sug&third_type=0&client_type=0&_=1511013032878" %music
req_so=requests.get(req_url)
data=json.loads(req_so.text.replace("window.baidu.sug(","").replace(");",""))
for i in data["data"]["song"]:
    print ("\tsongid:"+str(i["songid"]),"音乐名字:"+i["songname"],"\t歌手:"+i["artistname"])
input_songid=input("请输入你要下载的songid:")
for i in data["data"]["song"]:
    if input_songid==str(i["songid"]):
        url=get_down_url(i["songid"])
        music_down(url,i["songname"],i["artistname"])
        print("下载完成")