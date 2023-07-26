<<<<<<< HEAD
import pydub
from pydub import AudioSegment
from pydub.playback import play

# 사운드 파일 불러오기
sound = AudioSegment.from_file("phonecert.wav", format="wav")

# 좌우 채널 분리
left_channel = sound.split_to_mono()[0]
right_channel = sound.split_to_mono()[1]

#사용자가 원하는 왼쪽/오른쪽 값 입력받기
user_left_sound=input("user_left_sound : ")
user_right_sound=input("user_right_sound : ")


left_channel=left_channel+user_left_sound
right_channel=right_channel+user_right_sound

#합치기
adjusted_sound = AudioSegment.from_mono_audiosegments(left_channel, right_channel)

#출력
play(adjusted_sound)
=======
import wave
import pydub
from pydub import AudioSegment
from pydub.playback import play
#from pydub import Audiosegment

# beep 파일 불러오기(beep wav 파일)
beep = AudioSegment.from_file("beep.wav", format="wav")

# noSound 파일 불러오기(공백 wav 파일)
noSound = AudioSegment.from_file("noSound.wav", format="wav")


values=AudioSegment.empty()

def soundPeriod(input_time,cnt):
    global values     #values 변수를 전역 변수로 선언

<<<<<<<< HEAD:soundGenerator.py
    userTime=input_time*1000   #1초 = 1000, 60초 = 60000초
    period_length=float(userTime/cnt)
    period_length2=float(period_length/2)
    file=beep[0:period_length2]+noSound[0:period_length2]

    for _ in range(cnt):
        play(file)
        values=values+file

    # WAV 파일로 출력
    output_file = "output_wav2.wav"
    values.export(output_file, format="wav")
    print("WAV 파일로 출력되었습니다:", output_file)

#soundPeriod(1,5) #1초, 5회(주기 5)
========
#출력
play(adjusted_sound)
>>>>>>>> a12e68a9d37df4f98d4b557457ce8867ffc9a282:soundOutputLR.py
>>>>>>> a12e68a9d37df4f98d4b557457ce8867ffc9a282
