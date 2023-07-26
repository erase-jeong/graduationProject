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