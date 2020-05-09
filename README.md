# StoryByNAO: Autonomous System Project Assignment
maintained by @nntdoan
This module read a story out loud with a virtual NAO robot perform gesture along side. 

## Required packages
Please install the required packages for this module, which are listed in requirements.txt. You can do so by cd to the directory of the project and use the command:

> pip install -r requirements.txt

Otherwise, specify the path to the requirements.txt. Also note that make sure you using pip for your Python 2. Depending on your system, you may need to specify pip2 install -re requirments.txt. </br>

We assume you have NAOqi stk working already in your system, and that you are more or less farmilar with working with Choregragh from Python. A note regarding your Python version: NAOqi stk only works with Python 2.7.x. This module is written in Python 2.7.x. So please make sure, if you have multiple Python installed in your system, when running this module, you call for Python 2 to run it instead of Python 3. Regarding older version of Python 2.7.x (so x < 18), many part of it has been deprecated and no longer maintained, which may interfere when you try to install the required packages. It is highly recommended you use Python 2.7.18. </br>

## Guide to run the module
From cmd, first you will need to cd (change directory) into the directory of the project:
> cd {path to the project folder from where you are at the momment}

Then you can run the story2NAOv2.py, which is the entry file of this module to read a story with NAO perform gestures alongside. The following command should read our group (project group 18) story:

> py -2 story2NAOv2.py --port {the port your NAO is listening on} --storyfile "storyg18.txt"

Arguments: </br>
--ip : Robot ip address, default="127.0.0.1" </br>
--port : Robot port number, default="9559" </br>
--path2story : Path to the directory where all story files are stored from root, default="./stories/" </br>
--storyfile : Name of the story file that is in the path2story that you want to read, default="example.txt" </br>
Among which, the --ip and --port is obtained from Choregraph -> Connection -> Connect to ... </br>
The default story file "example.txt" is the pre-processed version of Listing 1: Example annotated story, given in the Project Assignment.pdf by our instructor, Dr. Paul Vogt. </br>

## Instruction on how to write the story file

This module read the story marked with gestures. It commands a virtual NAO robot to perform these gestures in synchrony with an audio generated from the story text. It does not take care of the actuals stroke of the gesture, their order of appearance, etc. These are instead pre-planned in the story file in a markup language. For the markup language, please refer to the Project Assignment description. </br>

So altogether you should write your story with a markup language like this: </br>

`<g-beat {body part} {do}>` Story text `</g-beat>` </br>

e.g `<g-beat hand hello>` Hi `</g-beat>`

This module supports these gestures and their meaning as below. It should gracefully deal with unknown body part or unknown do by using the default `<g-beat head emphasis>` in place of the unknown. You can add new gestures following the instruction in the next section </br>
| do | body part | use to express |  
|---|---|---|
| hello | hand | greeting, hi, ciao, etc. |
| afraid | hand | oh no kind-of expression, etc. |
| anyone | hand | all, everyone, come on, etc. |
| big | hand | very, extremely, especially, giant, gigantic, etc. |
| emphasis | hand | important, on time, etc. |
| grab | hand | reach out grabbing a thing and look at it, etc. |
| offer | hand | let's shake hand kind-of expression, etc. |
| please | hand | I need help kind-of expression, etc. |
| point-forward | hand | hand forward, open up, you, your, etc. |
| point-to-body | hand | me, my, myself, I, etc. |
| run | hand | mimick running, run, walk, hurry up, etc. |
| small | hand | things that mean the opposite to big, etc. |
| think | hand | think, thought, head, etc. |
| agree | head | two consecutive nods |
| emphasis | head | very subtle, I assure you kind-of expression, etc. |
| look-around | head | I'm confused, look around, making eye contact with every one kind-of expression, etc. |
| nod | head | a single nod |
| point-front | head | look down and look up |

IMPORTANT NOTE: A perfect text parser is a whole project on its own and beyond the scope of this project. The text parser in this module is a very simple one that works on the space separate each element in the text, so all elements in your story should be single-space separated. Something like this:

`<g-beat head nod> Hello, </g-beat> I am <g-deictic hand point-to-body> a NAO robot. </g-deictic> My <g-beat hand emphasis> artificial </g-beat> intelligence allows me to make an adequate estimation of <g-beat head emphasis> <g-deictic hand point-forward> your </g-deictic> <g-iconic hand think> thoughts.`

## Guide to create a new gesture object
Should the default gesture exist in this module does not meet your needs, you can add new gesture as desire very easily as follows. </br>

1. Make a Timeline that perform the gesture in Choregraph, please consult Choregraph documentation for this </br>

2. Export motion in Python to clipboard. So right click on the Timeline -> Export motion to clipboard -> Python -> bezier/simplified (does not matter). We recommend bezier because it works better though. </br>

3. If this motion is mainly performed by NAO head, you should create a new .py file in gChoregraph/ghead and paste the result of 2. in there. 
Do similarly if the motion is mainly performed by NAO hand, but the .py file is put in gChoregragh/ghand instead. </br>
After pasting, delete all the unnessary things: import ..., Alproxy, try .. except ... Only need to keep the assignment of the 3 list names, times, keys and their values. Note that the module only support movement of head and hand for now, so you should only keep the joint names that belong to head and hand. So delete anything that does not belong to head and hand (i.e. ankle, hip, etc. ) if you happen to copy that too from Choregrah. </br>
They should cause no problem being there, and it is also easy to extend this module to control the whole body. This cleaning is mainly for better sanity and debugging. </br>
 
4. Name the .py file exactly like how you would use in a .txt story file. So for example, you create a gesture mean "love", and use it in the story as ..g-beat hand love ... The file should be love.py, and is located in gChoregraph/ghand. </br>

Now you should be able to use this gesture! </br>

 
