# CSAI Autonomous System Project Group 18
# by NNT Doan (u192067) and D Baltazar (u105006)
# ===========================================
import pyttsx3
import argparse
import qi
import stk.services
from naoqi import ALProxy
from os.path import isfile
from multiprocessing import Process
from unidecode import unidecode
import time
import importlib

def importGesture(hand=True, mean=''):
    """Either 'head' or 'hand' NOT both can be true
    (translate one gesture at a time to ensure consitent in time at later step)
    Meaning is a string that define the mean of the gesture.
    The funtion translates the markup of gestures to lists
    joint names and their values, which can be passed to Choregraph
    ------------------------------------------------"""
    if hand: PATH_TO_MOD = 'gChoregraph.ghand.'
    else: PATH_TO_MOD = 'gChoregraph.ghead.'
    mean = mean.replace('>','').replace('-','_')

    try:
        imported_mean = importlib.import_module(PATH_TO_MOD+mean)
        print 'Successful import gesture that means "{}"'.format(mean)
    except:
        imported_mean = importlib.import_module('gChoregraph.ghead.emphasis')
        print "Fail to import. No gesture with the meaning found. NAO will do 'head emphasis' instead!\n \
            To make NAO perform a gesture that express '{}', please follow the instruction in the README.md.\n \
            ".format(mean)
        return imported_mean.names, imported_mean.times, imported_mean.keys

    return imported_mean.names, imported_mean.times, imported_mean.keys


def syncGesture2Speech(path=''):
    """param path: path to the story file in .txt from root.
    The story is assumed to be in English.
    The funtion returns ----------------------------
    1. speech: the story for computer to generate audio
    2. times: list of seconds elapsed from the beginning of 
    speech, that marks the emergence of a gesture
    ------------------------------------------------"""
    if isfile(path) and path.endswith('.txt'):
        
        with open(path, 'r') as f:
            buffer = f.read().replace('\n',' ') # remove all line breaks left
        
        NEW_STR = buffer.replace('>', '> ').replace('<', ' <')
        NEW_STR = NEW_STR.replace('   ', ' ').replace('  ', ' ')
        NEW_STR = NEW_STR.replace(' .', '.')    
        buffer = unidecode(unicode(NEW_STR, encoding="utf-8")).split() # convert all non-ASCII character to ASCII
        
        tospeech, tempStr, idx, elapsed = [], [], 0, 0.5 # hyper-parameter
        gestD = {}
        engine = pyttsx3.init()
        engine.setProperty('rate', 100) # must be the same rate as the actual speaking rate below
        engine.setProperty('volume', 0.01) # Volume during reahersal, != 0 for debugging
        while idx < len(buffer):
            if '<' not in buffer[idx]:
                tempStr.append(buffer[idx])
                idx+=1
            elif '</' in buffer[idx]:
                idx+=1 # do nothing
            else:
                if len(tempStr)!=0:
                    # ========================================================
                    # SPEAKING REHEARSAL
                    # ... "internally" read the text to estimate the start time of 
                    # ... each gesture
                    start = time.time()
                    engine.say(' '.join(tempStr))
                    engine.runAndWait()
                    end = time.time()
                    # add the time it takes to speak the things before gesture
                    elapsed+=round(end-start, 6)  # {.6f} secs 
                    # ========================================================
                    tospeech.append(' '.join(tempStr))
                    tempStr=[]

                if len(tempStr)==0:
                    elapsed-=0.05 # time offset between two encapsulated gestures

                if buffer[idx+1] == 'head': 
                    nG, tG, kG = importGesture(hand=False, mean=buffer[idx+2])
                    for n, t, k in zip(nG, tG, kG):
                        preptime = max(t)//3 - 0.5 # preparation period of a gesture is the first 1/3 time +-0.5
                        gestD.setdefault( n, [[], []] )[0].extend([(i+elapsed-preptime)*0.95 for i in t]) #-preptime and speed up by 5%
                        gestD.setdefault( n, [[], []] )[1].extend(k) 
                elif buffer[idx+1] == 'hand':
                    nG, tG, kG = importGesture(hand=True, mean=buffer[idx+2])
                    for n, t, k in zip(nG, tG, kG):
                        preptime = max(t)//3 - 0.5 # preparation period of a gesture is the first 1/3 time +-0.5
                        gestD.setdefault( n, [[], []] )[0].extend([(i+elapsed-preptime)*0.95 for i in t]) #-preptime and speed up by 5%
                        gestD.setdefault( n, [[], []] )[1].extend(k) 
                else: print 'Warning! Body part {} is not supported. \n \
                            You can add new body part with its gesture \
                            following the instruction in README.md'.format(buffer[idx+1])

                idx+=3
        tospeech.append(' '.join(tempStr))
        engine.stop()

        # ========================================================
        sNames, sTimes, sKeys = [], [], []
        for k, v in gestD.items():
            sNames.append(k)
            sTimes.append(sorted(v[0]))
            sKeys.append(v[1]) 
        

        return sNames, sTimes, sKeys, tospeech

    print 'File not found! Please make sure path to file is correct \
        and the file is end with .txt'
    return



def moveNao(robotIP, PORT = 9559, names=[], times=[], keys=[]):

    print 'let move NAO' # debug log

    #==============================================
    try:
        # communicate with Choregraphe.
        motionProxy = ALProxy("ALMotion", robotIP, PORT)
        motionProxy.setStiffnesses("Body", 1.0)
        motionProxy.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err
    motionProxy.setStiffnesses("Body", 0.0)
    print 'stop move NAO' # debug log


def tellStory(toSpeak=[]):

    engine = pyttsx3.init()
    # PARAMETER: 
    # This configure the speaking voice.
    engine.setProperty('volume', 0.8) 
    engine.setProperty('rate', 100)

    #==========================================
    # PARAMETER:
    # This control the actual start time of the speech, 
    time.sleep(0) 
    #==========================================

    print 'Start speaking' # debug log
    engine.say('! '.join(toSpeak))
    engine.runAndWait()
    # for frag in toSpeak:
    #     engine.say(frag)
    #     engine.runAndWait()
    #     time.sleep(0) 
    print 'Finish speaking' # debug log
    engine.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default="9559",
                        help="Robot port number")
    parser.add_argument("--path2story", type=str, default="./stories/",
                        help="Path to story file from root")
    parser.add_argument("--storyfile", type=str, default="example.txt",
                        help="Path to story file from root")

    args = parser.parse_args()


    jointNames, jointTimes, jointKeys, story = syncGesture2Speech(path=args.path2story+args.storyfile)
    # # debug log
    # print jointNames
    # print jointTimes
    # print jointKeys
    #==============================================
    
    # Telling a story with gesture performed by NAO alongside
    p1=Process(target=moveNao, args=(args.ip, args.port, jointNames, jointTimes, jointKeys, ))
    p1.start()
    p2=Process(target=tellStory, args=(story,))
    p2.start()
    p1.join()
    p2.join()

    p1.terminate()
    p2.terminate()


