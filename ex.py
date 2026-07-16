"""
Welcome, beginner.
This file is not the app itself. It is a teacher-style explanation of AI.py.
Think of it like a professor sitting beside you and explaining each part slowly.

========================================
1. WHAT THIS PROGRAM IS TRYING TO DO
========================================

The file AI.py is a small Chinese conversation practice assistant.
Its job is simple:
- it welcomes you,
- it listens to your message,
- it gives you a reply,
- and it helps you practice speaking Chinese.

We did not make it perfect like a big company AI product.
Instead, we made a beginner-friendly version that is easy to understand.

So the first idea to understand is this:
A program is like a set of instructions.
If you write the instructions clearly, the computer can follow them.

========================================
2. WHY WE IMPORT THINGS AT THE TOP
========================================

In Python, imports are like opening tools from a toolbox.
If we want to use a feature, we must first bring it into the program.

Example:
import os

This gives us access to operating system tools.
We use os to read environment variables such as the OpenAI key if one exists.

Example:
import random

This helps us choose random topics like travel, food, school, and hobbies.

Example:
import sys

This lets us read command-line arguments like --cli.
That means if you run the script in terminal mode, Python can detect it.

Example:
from difflib import SequenceMatcher

This helps us compare strings.
We use it for a very simple pronunciation-like feedback feature.
It checks how similar two strings are.

Example:
import tkinter as tk
from tkinter import scrolledtext

Tkinter is Python's built-in tool for making windows and buttons.
We use it to create a simple graphical user interface (GUI).

========================================
3. THE HELPER FUNCTION _is_microphone_ready
========================================

Here is the first important function:

def _is_microphone_ready() -> bool:
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.1)
        return True
    except Exception:
        return False

What is happening here?

1. We try to import a library called speech_recognition.
2. We create a recognizer object.
3. We create a microphone object.
4. We test whether the microphone can be used.
5. If everything works, we return True.
6. If something fails, we return False.

This is a very safe way to check if voice input is possible.
If the microphone is not available, the program can still continue.

This is smart because beginners often run into microphone problems.
Instead of crashing, the program gracefully says:
"I cannot use voice right now, so I will use text mode."

========================================
4. IMPORTING OPTIONAL LIBRARIES SAFELY
========================================

Next, the file tries to import several libraries carefully:

try:
    import speech_recognition as sr
except ImportError:
    sr = None

This means:
- if speech_recognition is installed, we use it,
- if not, we set sr = None.

Why do we do this?
Because some machines do not have the package installed.
If we do not handle this safely, the whole program would stop.

The same idea is used for pyttsx3 and openai.

pyttsx3 is a text-to-speech library.
It allows the computer to speak out loud.
If it is not installed, the program simply continues without speech.

openai is used only if you want the assistant to use OpenAI's API,
which can make replies feel more intelligent.
Without it, the program still works using its own built-in reply system.

========================================
5. THE MAIN CLASS: ChineseConversationAI
========================================

The most important part of the program is the class:

class ChineseConversationAI:

A class is like a blueprint.
It groups related behavior together.
Instead of writing separate functions for everything, we make a class that owns:
- the conversation logic,
- the voice settings,
- the reply logic,
- the GUI connection.

This is a very common pattern in Python.

========================================
6. THE __init__ METHOD
========================================

The __init__ method runs automatically when we create an object from this class.
It is like the constructor of a house.
When the house is built, it gets its initial furniture and settings.

The code inside it sets up the basic state of the assistant.

For example:
self.recognizer = None
self.microphone = None

These are variables that will hold voice-related objects.

Then the program checks if speech_recognition exists.
If it does, it tries to create a recognizer and microphone object.
If something fails, it sets them to None.

Then we compute:
self.voice_available = _is_microphone_ready() and self.recognizer is not None and self.microphone is not None

This is a simple sentence that says:
"Voice is available only if the microphone test passed and the recognizer and microphone objects exist."

This is very helpful because it prevents the program from crashing.

========================================
7. THE TEXT-TO-SPEECH SETUP
========================================

The method _setup_tts sets up the voice output.

It tries to initialize pyttsx3 and set the speech rate and volume.

For example:
self.engine = pyttsx3.init()

This creates a speech engine.
Then we change the speaking speed:
self.engine.setProperty("rate", 155)

A higher number means faster speech.
Then we set the volume.

The next part checks the available voices:
for voice in voices:
    name = voice.name.lower()
    if "mandarin" in name or "chinese" in name:
        self.engine.setProperty("voice", voice.id)
        break

This means:
If the system has a Chinese voice, we use it.
If not, the computer may still speak in another voice.

========================================
8. THE OPENAI SETUP
========================================

The method _setup_openai checks whether OpenAI is installed.
If the environment variable OPENAI_API_KEY exists, we use it.

This is optional.
Without it, the assistant uses a built-in fallback system.

So the program has two modes:
- smart mode with OpenAI
- simple mode without OpenAI

This design is beginner-friendly because it does not force you to use any API.

========================================
9. THE speak METHOD
========================================

The speak method is simple:

def speak(self, text: str) -> None:
    print("助手:", text)
    if self.engine is not None:
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception:
            pass

What does this do?

- It prints the message to the terminal.
- If a speech engine exists, it makes the computer speak the text.

This is how the assistant talks back to you.

========================================
10. THE listen METHOD
========================================

The listen method lets the assistant receive your voice input.

If voice input is not available, it asks you to type your message instead.

This is an important beginner-friendly decision.
It means the program will not fail just because microphone support is missing.

The method tries to open the microphone and listen.
If it fails, it prints an explanation and asks for typed input.

This is one of the best parts of the program: it is robust.

========================================
11. THE PRONUNCIATION FEEDBACK METHOD
========================================

The method get_pronunciation_feedback compares the user's sentence to a target phrase.

It uses SequenceMatcher, which is a simple string comparison tool.

The idea is:
- if the input is very similar to the target phrase, give positive feedback,
- if it is somewhat similar, encourage the user to speak more clearly,
- if it is not similar, suggest more practice.

This is not true pronunciation scoring.
It is a simple educational simulation.

But it teaches the beginner how to think about feedback:
"Your attempt is close, but you can improve."

========================================
12. THE FALLBACK RESPONSE SYSTEM
========================================

The method _fallback_response gives responses when OpenAI is not being used.

It checks the user's sentence for words such as:
- 再见 (goodbye)
- 换话题 (change topic)
- 天气 (weather)
- 吃 (eat)
- 介绍 (introduce)

Depending on what the user says, the assistant responds with a suitable prompt.

Example:
If the user says "天气", the assistant says:
"天气是很好的练习话题。"

This makes the conversation feel more natural and more useful.

========================================
13. THE OPENAI RESPONSE METHOD
========================================

The method _openai_response sends the user's message to OpenAI if an API key exists.

It builds a conversation history and sends it to the model.
This allows the assistant to respond in a more human-like way.

If the OpenAI request fails, the method returns None,
so the program falls back to the built-in response system.

This is a very good pattern in programming:
"Try the advanced option first, but have a backup plan."

========================================
14. THE respond METHOD
========================================

The respond method is the main conversation controller.
It receives the user's input and decides what to do:

- if the input is empty, return a message asking for input,
- try OpenAI if available,
- otherwise use the fallback response,
- optionally add pronunciation feedback.

This method acts like the brain of the assistant.
It brings all the smaller parts together.

========================================
15. THE run METHOD
========================================

The run method is the conversation loop.
It is one of the most important parts of the program.

The loop works like this:
1. greet the user,
2. ask for input,
3. process the message,
4. respond,
5. repeat until the user says goodbye.

This is how the assistant stays interactive.

========================================
16. THE GUI CLASS: ConversationGUI
========================================

The ConversationGUI class creates the window.
It uses Tkinter to build a simple chat window.

The program creates:
- a text area where the chat appears,
- an input box where the user types,
- a send button,
- a voice button.

The append_message method is used to show text in the chat box.

This makes the program friendly for beginners because they can use a window instead of only the terminal.

========================================
17. HOW THE PROGRAM STARTS
========================================

At the bottom of the file we have:

if __name__ == "__main__":
    try:
        assistant = ChineseConversationAI()
        if len(sys.argv) > 1 and sys.argv[1] == "--cli":
            assistant.run()
        else:
            assistant.run_gui()
    except KeyboardInterrupt:
        print("程序已结束。")

This is the startup section.
It means:
- create the assistant object,
- if the user passed --cli, run the terminal version,
- otherwise run the GUI version.

The if __name__ == "__main__" line is a very common Python pattern.
It ensures that this code only runs when the file is executed directly.

========================================
18. A SIMPLE BEGINNER SUMMARY
========================================

If you remember only a few ideas, remember these:

1. Python programs are made of small instructions.
2. A class groups related behavior together.
3. Functions help organize actions.
4. We use try/except to avoid crashes.
5. A conversation loop keeps the program interactive.
6. A GUI gives users a window to work with.
7. The assistant can work without voice input by using text input.

========================================
19. FINAL THOUGHT
========================================

You do not need to understand everything at once.
Programming becomes easier when you learn one small piece at a time.

The best way to learn this file is to read it slowly, then ask:
- What is this function doing?
- What are the variables storing?
- What happens next in the conversation?

That is exactly how good programmers learn.
"""

print("This file is a beginner-friendly explanation of AI.py.")
print("Open it in your editor and read it slowly.")
print("You are learning how a real small Python project is built.")
