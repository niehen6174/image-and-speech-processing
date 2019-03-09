from aip import AipSpeech
import os
from requests import get
import pyaudio
import wave
import time
from configparser import ConfigParser

conf=ConfigParser()
conf.read('config.conf')
APP_ID = conf.get('speech_config','APP_ID')
API_KEY = conf.get('speech_config','API_KEY')
SECRET_KEY = conf.get('speech_config','SECRET_KEy')

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def ping():
    try:
        html =get("http://www.baidu.com",timeout=2)
        if str(html)== '<Response [503]>': #检查能否上网 如果不能则不能使用语音合成功能
            print('question')
            check_net=False
        else:
            check_net=True
    except:
        check_net=False
    return check_net
def baidu_voice(voice):
    """ 你的 APPID AK SK """
    try:
        result  = client.synthesis(voice, 'zh', 1, {
            'vol': 8,'per':0
        })
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('auido.mp3', 'wb') as f:
                f.write(result)
        os.system('auido.mp3')
    except:
        return "语音合成出现问题 请检查"

    #time.sleep(t)
    #os.system('taskkill /f /im PotPlayerMini64.exe')
#baidu_voice('欢迎来到郑州轻工业大学ai人工智能实验室')
#baidu_voice('张文豪正在测试 unknown')

def baidu_speech_reco():
    try:
        with open('recode.wav', 'rb') as fp:
            results=fp.read()
            result = client.asr(results, 'wav', 16000, {'dev_pid': 1536, })
            #print(result)
            if 'result'  in result.keys():
                return str(result['result'][0])
            else:
                return '语音合成出现问题，请检查'
    except:
        return '语音合成出现问题，请检查'
#print(baidu_speech_reco())
def LuYin():   #录音功能
    CHUNK = 1024              #wav文件是由若干个CHUNK组成的，CHUNK我们就理解成数据包或者数据片段。1024
    FORMAT = pyaudio.paInt16  #这个参数后面写的pyaudio.paInt16表示我们使用量化位数 16位来进行录音。
    CHANNELS = 1              #代表的是声道，这里使用的单声道。 1
    RATE = 16000              # 采样率16k
    #RECORD_SECONDS = Time     #采样时间
    WAVE_OUTPUT_FILENAME = 'recode.wav'   #输出文件名

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
    print("* 录音开始")

    frames = []

    while CHANNELS==1:
        data = stream.read(CHUNK)
        frames.append(data)
    time.sleep(5)
    print("* 录音结束")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
#LuYin()
#print(baidu_speech_reco())