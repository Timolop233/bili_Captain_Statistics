import requests

test = False #是否开启测试模式

page = 1 #页数

if test == True:
    url = f'https://api.live.bilibili.com/xlive/app-room/v1/guardTab/topList?roomid=4895312&page={page}&ruid=1576121'
elif test == False:
    room_id = input("请输入直播间房间号：")
    ruid = input("请输入主播uid：")
    url = f'https://api.live.bilibili.com/xlive/app-room/v1/guardTab/topList?roomid={room_id}&page={page}&ruid={ruid}'

headers = {
    'Host': "api.live.bilibili.com",
    'Origin': "https://live.bilibili.com",
    'Referer': f"https://live.bilibili.com/{room_id}",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    'Cookie': '1'
}
re1 = requests.request('get', url, headers=headers).json()
num = re1['data']['info']['num'] #获取现役舰长人数
list_pages = 0  #列数
order = 1
print("舰长数为:",num)
print("正在处理，请稍后.....")

while num:
    url = f'https://api.live.bilibili.com/xlive/app-room/v1/guardTab/topList?roomid={room_id}&page={page}&ruid={ruid}&1576121page_size=10'
    response = requests.request('get', url, headers=headers).json()
    order = order + 1
    uid = response['data']['list'][list_pages]['uid']
    name = response['data']['list'][list_pages]['username']
    if test == True:
        print(order, uid, "", name )
    list_pages = list_pages + 1 #读取下一列数据
    if list_pages == 10:
        page = page + 1 #翻页
        list_pages = 0  #翻页后列表重置
