[![Header](https://i.postimg.cc/1XrrC9N4/Screenshot-from-2022-12-16-17-25-25.png "Header")](yashkumarvaibhav.github.io/mysite)  
  
  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)  
  
# Hello, folks! <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px">  
  
This project is crated only for those who are having interest in building Virtual Assistant. Generally it takes a lots of time to write code from scratch to build Virtual Assistant. So, we have built a Library called "ChelsiAI", which gives you easy functionality to build your own Virtual Assistant.  
  
# Content-  
  
1. What is ChelsiAI?  
2. Prerequisite  
3. Getting Started- How to use it?  
4. What it can do (Features it supports)  
5. Future / Request Features  
6. Contribute  
7. Contact me  
8. Donate  
9. Thank me on-  

## YouTube Tutorial-

Click on the image below to watch the tutorial on YouTube-

**Tutorial 1-**

[![ChelsiAI Tutorial 1](https://i.postimg.cc/W1kkPzJd/Screenshot-from-2022-12-16-19-53-40.png)](https://www.youtube.com/@yashvaibhav95467)


  
## **1. What is Chelsi AI?**  
  
Chelsi AI is a Python Module which is able to perform task like Chatbot, Assistant etc. It provides base functionality for any assistant application. This ChelsiAI is built using Tensorflow, Pytorch, Transformers and other opensource libraries and frameworks. Well, you can contribute on this project to make it more powerful.  
     
  
  
## 2. Prerequisite  
      
- To use it only Python (> 3.6) is required.  
      
- To contribute in project: Python is the only prerequisite for basic scripting, Machine Learning and Deep Learning knowledge will help this model to do task like AI-ML. Read How to contribute section of this page.  
      



## 3. Getting Started- How to use it?  
  
  
### 3.1. Installation-

* Install the latest version-  

   ```bash
   pip install ChelsiAI
   ```  

#### Optional Steps (Common Installation Issues)-

* [Optional Step] If Pyaudio is not working or not installed you might need to install it seperately-
	
	In the case of Mac OSX do:
	
	```python
	brew install portaudio
	pip install pyaudio
	```
	In the case of Windows or Linux do:
	
	- Download pyaudio from: lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
	
	- ```pip install PyAudio-0.2.11-cp310-cp310-win_amd64.whl```

* [Optional Step] If pycountry is not working or not installed then Install "python3-pycountry" Package on Ubuntu/Linux-
	
	```
	sudo apt-get update -y
	sudo apt-get install -y python3-pycountry
	```

* [Optional Step] You might need to Install [Microsoft Visual C++ Redistributable for Visual Studio 2022](https://visualstudio.microsoft.com/downloads/#microsoft-visual-c-redistributable-for-visual-studio-2022)

### 3.2. Code You Need-
 
   You need only this piece of code-  

```
import ChelsiAI  
	 
# create your own function  
# It must contain parameter 'feature_command' which is the command you want to execute  
# Return is optional  
# If you want to provide return value it should only return text (str)  
# Your return value will be displayed or call out by the choice of OutputMethods of ChelsiAI  
  
def custom_function(feature_command="custom command"):  
    # write your code here to do something with the command  
	# perform some tasks # return is optional  
	return feature_command + ' Executed'  
  
obj = ChelsiAI.ChelsiAI(input_method=ChelsiAI.InputsMethods.voice_input_google_api,
                        output_method=ChelsiAI.OutputMethods.voice_output,
                        backend_tts_api='pyttsx3',
                        api_key="c6fd2013918f9bc9a12c5394a819af49",
                        detect_wake_word=False,
                        wake_word_detection_method=ChelsiAI.InputsMethods.voice_input_google_api,
                        bot_name="Chelsi",
                        display_intent=True,
                        google_speech_recognition_input_lang='en',
                        google_speech_recognition_key=None,
                        google_speech_recognition_duration_listening=5)  
 
obj.register_feature(feature_obj=custom_function, feature_command='custom feature')  
  
obj.start()
```  
 
  ### 3.3. **Whats now?**  
  
  It will start your AI, it will ask you to give input and accordingly it will produce output.    
   You can configure  `input_mechanism` and  `output_mechanism` parameter for voice input/output or text input/output.  
  
   ### 3.4. Let's understand the Parameters-  
   
  ```bash  
:param input_method: (object) method to get input from user <allowed values: [InputsMethods.text_input, InputsMethods.voice_input_google_api, InputsMethods.voice_input_deepspeech_streaming]>  
:param output_method: (object) method to give output to user <allowed values: [OutputMethods.text_output, OutputMethods.voice_output]  
:param backend_tts_api: (str) [Default 'pyttsx3'] backend tts api to use <allowed values: ['pyttsx3', 'gtts']>  
:param api_key: (str) [Default ''] api key to use ChelsiAI get it from http://Chelsi-ai-api.herokuapp.com  
:param detect_wake_word: (bool) [Default True] detect wake word or not <allowed values: [True, False]>  
:param wake_word_detection_method: (object) [Default None] method to detect wake word <allowed values: [InputsMethods.voice_input_google_api, InputsMethods.voice_input_deepspeech_streaming]  
:param bot_name: (str) [Default 'Chelsi'] name of the bot  
:param display_intent: (bool) [Default True] display intent or not <allowed values: [True, False]>  
:param google_speech_recognition_input_lang: (str) [Default 'en'] language of the input Check supported languages here: https://cloud.google.com/speech-to-text/docs/languages  
:param google_speech_recognition_key: (str) [Default None] api key to use Google Speech API  
:param google_speech_recognition_duration_listening: (int) [Default 5] duration of the listening  
  
READ MORE: Google Speech API (Pricing and Key) at: https://cloud.google.com/speech-to-text
```  

## 4. What it can do (Features it supports)-  
  
1. Currently, it supports only english language  
2. Supports voice and text input/output.  
3. Supports AI based voice input and by using google api voice input.   
4. Lightweight and able to understand natural language (commands)  
5. Ability to add your own custom functions.  
  
### 4.1. Supported Commands-  
  
1. you can ask the date: Say- ???what is the date today???  
2. you can ask the time: Say- ???what is the time now???  
3. you can ask joke: Say- ???tell me a joke???  
4. you can ask for news: Say- ???tell me the news???  
5. you can ask weather: Say- ???what is the weather???, ???tell me the weather???, ???tell me about the weather???, ???tell me about the weather in < city>???  
6. you can ask about: Say- ???tell me about < topic>???  
7. you can open website: Say- ???open website < website name>???, ???open website < website name><.extension>???, ???open website techport.in???  
8. you can play on youtube: Say- ???play on youtube < video name>???, ???play < video name> on youtube???  
9. you can send a WhatsApp message: Say- ???send WhatsApp message??????  
10. you can send an email: Say- ???send email???  
11. greet: Say- ???greet???, ???hello???, ???hey???, ???hi???, ???good morning???, ???good afternoon???, ???good evening???  
12. goodbye: Say- ???goodbye???, ???bye???, ???see you later???  
13. conversation: Say- ???conversation???, ???chat???, ???talk???, ???talk with chatbot???  
14. you can take a screenshot of the current screen: Say- ???take screenshot???  
15. you can click a photo: Say- ???click photo???  
16. you can check internet speed: Say- ???check internet speed???  
17. you can download a youtube video: Say- ???download youtube video???  
18. you can check covid cases: Say- ???covid cases in < country>???, ???covid cases < country>???  
19. you can ask to play games: Say- ???play games??? 
20. you can ask places near me: Say- "cafe near me"
21. you can say : Say- "i am bored"
22. you can control volume: Say- "open volume controller"

### 4.2. Supported Input/Output Methods (Which option do I need to choose?)-  
  
1. **For text input-**'  
  
   ``text_input`` Just ask input from command line  
     
3. **For voice input-**  
  
	  ```voice_input_google_api``` It use google free API. After using few minutes GoogleAPI might restrict you to use it. It's a limitation from GoogleAPI. But it's fast, very accurate and consume very less memory.  
	     
	  **or**  
	   
	  ```voice_input_deepspeech_streaming``` ChelsiAI's own Machine Learning model to process voice input and convert into text for further processing. Little slow as compared to GoogleAPI, consume more memory, less accurate. But it's free to use and no restriction.  
  
4. **For text output-**  
  
	  ```text_output``` Just print output in command line  
  
5. **For voice output-**  
  
	  ```voice_output``` It use 'gtts' or 'pyttsx3' backend to produce voice output. You can set backend_tts_api.  
     
## 5. Future/Request Features-  
 
**WIP**  
  
**You tell me**  
  
  
## 6. Contribute-  
 
**Instructions Coming Soon**  
  
## 7. Contact me-  
  
- [Instagram](https://www.instagram.com/yashkumarvaibhav)  
      
- [YouTube](https://www.youtube.com/@yashvaibhav9546)  
      
  
  
## 8. Donate-  
  
[Donate and Contribute to run me this project, and buy a domain](https://www.buymeacoffee.com/)  
  
**_Feel free to use my code, don't forget to mention credit. All the contributors will get credits in this repo._**  
  
**_Mention below line for credits-_**  
  
      
  
## 9. Thank me on-  
  
- Follow me on Instagram:  [https://www.instagram.com/yashkumarvaibhav](https://www.instagram.com/yashkumarvaibhav)  
      
- Subscribe me on YouTube:  [https://www.youtube.com/@yashvaibhav9546](https://www.youtube.com/@yashvaibhav95467)  
  
## License  
  
[MIT](https://choosealicense.com/licenses/mit/)
