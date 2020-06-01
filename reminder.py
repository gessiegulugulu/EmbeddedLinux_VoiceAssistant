import time
import os

CN_NUM = {
    u'〇': 0,
    u'一': 1,
    u'二': 2,
    u'三': 3,
    u'四': 4,
    u'五': 5,
    u'六': 6,
    u'七': 7,
    u'八': 8,
    u'九': 9,

    u'零': 0,
    u'壹': 1,
    u'贰': 2,
    u'叁': 3,
    u'肆': 4,
    u'伍': 5,
    u'陆': 6,
    u'柒': 7,
    u'捌': 8,
    u'玖': 9,

    u'貮': 2,
    u'两': 2,
}
CN_UNIT = {
    u'十': 10,
    u'拾': 10,
    u'百': 100,
    u'佰': 100,
    u'千': 1000,
    u'仟': 1000,
    u'万': 10000,
    u'萬': 10000,
    u'亿': 100000000,
    u'億': 100000000,
    u'兆': 1000000000000,
}

def set_reminder(hour,min,sec):
    period=min*60+hour*60*60+sec
    time.sleep(period)
    path = os.getcwd() + "/reminder.wav"
    os.system('sox ' + path + ' -t waveaudio')


def cn2dig(cn):
    lcn = list(cn)
    unit = 0  # 当前的单位
    ldig = []  # 临时数组

    while lcn:
        cndig = lcn.pop()

        if cndig in CN_UNIT:
            unit = CN_UNIT.get(cndig)
            if unit == 10000:
                ldig.append('w')  # 标示万位
                unit = 1
            elif unit == 100000000:
                ldig.append('y')  # 标示亿位
                unit = 1
            elif unit == 1000000000000:  # 标示兆位
                ldig.append('z')
                unit = 1

            continue

        else:
            dig = CN_NUM.get(cndig)

            if unit:
                dig = dig * unit
                unit = 0

            ldig.append(dig)

    if unit == 10:  # 处理10-19的数字
        ldig.append(10)

    ret = 0
    tmp = 0

    while ldig:
        x = ldig.pop()

        if x == 'w':
            tmp *= 10000
            ret += tmp
            tmp = 0

        elif x == 'y':
            tmp *= 100000000
            ret += tmp
            tmp = 0

        elif x == 'z':
            tmp *= 1000000000000
            ret += tmp
            tmp = 0

        else:
            tmp += x

    ret += tmp
    return ret


def get(word):
    if word.rfind(r'小时')==-1:
        hour=0
        # min = cn2dig(min_key)
    else:
        hour_key = word[0:word.rfind(r'小时')]
        word=word[word.rfind(r'小时')+2:]
        if hour_key=="半":
            hour=0.5
        else:
            hour = cn2dig(hour_key)

    if word.rfind(r'分钟')==-1:
        min=0
    else:
        min_key=word[0:word.rfind(r'分钟')]
        word = word[word.rfind(r'分钟') + 2:]
        min = cn2dig(min_key)

    if word.rfind(r'秒')==-1:
        min=0
    else:
        sec_key=word[0:word.rfind(r'秒')]
        sec = cn2dig(sec_key)


    print(hour,' ',min,' ',sec,'?')

    set_reminder(hour,min,sec)


if __name__ == '__main__':
    get('五秒之后提醒我')
