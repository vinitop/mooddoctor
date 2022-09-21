import textblob
from textblob import TextBlob
import keyboard # for keylogs

import nltk

from textblob import Word
import matplotlib.pyplot as plt
from PIL import Image


# Semaphore is for blocking the current thread
# Timer is to make a method runs after an `interval` amount of time
from threading import Semaphore, Timer

SEND_REPORT_EVERY = 59 # 10 minutes

class Keylogger:
    def __init__(self, interval):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        # this is the string variable that contains the log of all
        # the keystrokes within `self.interval`
        self.log = ""
        # for blocking after setting the on_release listener
        self.semaphore = Semaphore(0)

    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)
        """
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " "
            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "\n"
            elif name == "backspace":
                 name = ""
            elif name == "shift":
                 name = ""
            elif name == "[PRINT_SCREEN]":
                 name = ""
            elif name == "[LEFT_WINDOWS]":
                 name = ""
            elif name=="[dot]":
                name=". "
            #elif name =
            elif name == "decimal":
                name = "."
            elif name == "[CAPS_LOCK]":
                name = ""
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name

    

    def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """
        if self.log:
            # if there is something in log, report it
           
            # can print to a file, whatever you want
            print(self.log)
            with open('filename.txt','w') as f:
                print(self.log, file=f)
    #the count will be used to countt the number of positive, negative and neutral statments,
    #   every time the loop is excecited
        counter =0
        counter_1 =0
        counter_2= 0
        

        try:
            text = self.log

            obj = TextBlob(text)#textblob will be used for the analysis of statements.
            for sentence in obj.sentences:
                print(sentence)
                sentiment, subjectivity = sentence.sentiment

                
                
                print(obj.sentiment)
                if sentiment == 0:
                    


                    counter = counter+1
                    print('The text is neutral')
                    
                elif sentiment > 0:
                    
                    counter_1 = counter_1+1
                    print('The text is positive')
                    
                elif sentiment <0:
                    
                    counter_2 = counter_2+1
                    print('The text is negative')
                
                
            print('oVERALL NEGATIVE SENTIMENTS: ' ,counter_2)
            print('oVERALL postive SENTIMENTS: ' ,counter_1)
            print('oVERALL neutral SENTIMENTS: ' ,counter)
            OVR = counter+counter_1+counter_2
            ratio= (counter_1-counter_2+counter*0)/(OVR+0.0000000001)
            perc = ratio*100  #this will tell the percentage of positivity,and if in negative then negativity and 0 would mean neutral.
            print(perc,'%')

 # following will be the feeback given to you
            if perc>0:
                Image.open('pos.jpg').show()
            elif perc<0:
                Image.open('neg.jpg').show()
            else:
                 Image.open('neu.jpg').show()        







            #this is the pie chart representation of your diff. moods.
            my_data = [counter,counter_1,counter_2]
            my_labels = 'Neutral','Positive','Negative'
            my_colors = ['purple','lightsteelblue','silver']
            my_explode = (0, 0.1, 0)
            plt.pie(my_data,labels=my_labels,autopct='%1.1f%%',startangle=15, shadow = True, colors=my_colors, explode=my_explode)
            plt.title('My Mood Day')
            plt.axis('equal')
            plt.show()
            
            left = [1,2,3] 
  
    # heights of bars 
            height = [counter_1,counter_2,counter] 
  
    # labels for bars 
            tick_label = ['Positive', 'Negative', 'Neutral'] 
  
    # plotting a bar chart 
            plt.bar(left, height, tick_label = tick_label,width = 0.8, color = ['red', 'green']) 
  
    # naming the x-axis 
            plt.xlabel('x - axis') 
    # naming the y-axis 
            plt.ylabel('y - axis') 
    # plot title 
            plt.title('Sentiment Analysis') 
  
            # function to show the plot 
            plt.show() 





                
            


            









                
        except:
            print("unable to understand")
            pass ;

        self.log = ""
        Timer(interval=self.interval, function=self.report).start()



    def start(self):
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # block the current thread,
        # since on_release() doesn't block the current thread
        # if we don't block it, when we execute the program, nothing will happen
        # that is because on_release() will start the listener in a separate thread
        self.semaphore.acquire()

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()
