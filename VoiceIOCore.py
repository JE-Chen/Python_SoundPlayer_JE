from SpeechToText import SpeechToText
from TextToSpeech import TextToSpeech
from Play_Sound import Play_Sound

class VoiceIOCore():

    def __init__(self):
        try:
            self.SpeechToText=SpeechToText()
            self.TextToSpeech=TextToSpeech()
            self.Play_Sound=Play_Sound()
        except Exception as Errr:
            print(Errr)