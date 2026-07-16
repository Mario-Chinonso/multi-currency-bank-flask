import os
import random
import sys
from difflib import SequenceMatcher
from typing import Optional
import tkinter as tk
from tkinter import scrolledtext


def _is_microphone_ready() -> bool:
    try:
        import speech_recognition as sr  # type: ignore
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.1)
        return True
    except Exception:
        return False

try:
    import speech_recognition as sr
except ImportError:
    sr = None

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


class ChineseConversationAI:
    def __init__(self) -> None:
        self.recognizer = None
        self.microphone = None
        self.engine = None
        self.client = None
        self.topic = "日常生活"
        self.practice_phrase = "你好，我想练习中文。"
        self.history = []
        self.turn_count = 0
        self.current_prompt = "请试着用一句完整的中文介绍一下你自己。"
        self.gui = None

        if sr is not None:
            try:
                self.recognizer = sr.Recognizer()
                self.microphone = sr.Microphone()
            except Exception:
                self.recognizer = None
                self.microphone = None

        self.voice_available = _is_microphone_ready() and self.recognizer is not None and self.microphone is not None

        self._setup_tts()
        self._setup_openai()

    def _setup_tts(self) -> None:
        if pyttsx3 is None:
            return
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty("rate", 155)
            self.engine.setProperty("volume", 1.0)
            voices = self.engine.getProperty("voices")
            for voice in voices:
                name = voice.name.lower()
                if "mandarin" in name or "chinese" in name:
                    self.engine.setProperty("voice", voice.id)
                    break
        except Exception:
            self.engine = None

    def _setup_openai(self) -> None:
        if OpenAI is None:
            return
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            self.client = OpenAI(api_key=api_key)

    def speak(self, text: str) -> None:
        print("助手:", text)
        if self.engine is not None:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception:
                pass

    def listen(self) -> str:
        if not self.voice_available or self.recognizer is None or self.microphone is None:
            print("语音识别不可用。请直接输入文本。")
            return input("你（输入）：").strip()

        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("正在听你说话...")
                audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=8)
        except Exception as exc:
            print(f"麦克风初始化失败：{exc}")
            print("请直接输入文本。")
            return input("你（输入）：").strip()

        try:
            text = self.recognizer.recognize_google(audio, language="zh-CN")
            return text
        except Exception:
            print("没有听清楚，请再说一次。")
            return input("你（输入）：").strip()

    def get_pronunciation_feedback(self, user_text: str, target: str) -> str:
        if not user_text or not target:
            return ""

        similarity = SequenceMatcher(None, user_text, target).ratio()
        if similarity >= 0.75:
            return "发音和表达都很接近，继续保持。"
        if similarity >= 0.5:
            return "你已经接近了，试着更慢、更清楚地说。"
        return "可以再多练一次，注意发音、节奏和语调。"

    def _fallback_response(self, user_text: str) -> str:
        text = user_text.strip()
        if not text:
            return "请再说一次，我会继续帮你练习。"

        if any(word in text for word in ["再见", "bye", "退出", "结束", "stop"]):
            return "好的，再见！下次继续练习中文。"

        if "换话题" in text:
            topics = ["学校生活", "旅行", "饮食", "工作", "爱好"]
            self.topic = random.choice(topics)
            self.current_prompt = f"请用一句关于{self.topic}的中文说一说。"
            return f"好的，我们换到{self.topic}的话题。{self.current_prompt}"

        if "纠错" in text or "错误" in text:
            return "当然可以。请说一句中文，我会帮你纠正语法和表达。"

        if "天气" in text:
            self.current_prompt = "你可以说：今天天气很好，我想出去散步。"
            return f"天气是很好的练习话题。{self.current_prompt}"

        if "吃" in text or "饭" in text:
            self.current_prompt = "你可以说：我喜欢吃米饭和面条。"
            return f"食物话题很实用。{self.current_prompt}"

        if "介绍" in text or "自己" in text:
            self.current_prompt = "你可以说：我叫小明，我来自北京，我喜欢学习中文。"
            return f"可以。{self.current_prompt}"

        self.turn_count += 1
        if self.turn_count == 1:
            self.current_prompt = f"请继续用一句完整的话聊聊{self.topic}。"
            return f"很好！我们来练习{self.topic}。{self.current_prompt}"

        self.current_prompt = "你可以再说一句更自然的表达，我来帮你改得更顺。"
        return f"很好。{self.current_prompt}"

    def _openai_response(self, user_text: str) -> Optional[str]:
        if self.client is None:
            return None

        try:
            self.history.append({"role": "user", "content": user_text})
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "你是一个中文口语练习助手。"
                            "请用中文回答，语气自然，帮助学习者练习对话。"
                            "每次只给一个简洁、自然的回复。"
                            "如果用户说错了，礼貌地纠正并给出更自然的表达。"
                        ),
                    },
                    *self.history,
                ],
                temperature=0.7,
            )
            reply = response.choices[0].message.content.strip()
            self.history.append({"role": "assistant", "content": reply})
            return reply
        except Exception:
            return None

    def respond(self, user_text: str, from_voice: bool = False) -> str:
        if not user_text:
            return "我没有听清楚，请再说一次。"

        ai_reply = self._openai_response(user_text)
        if ai_reply:
            return ai_reply

        reply = self._fallback_response(user_text)
        feedback = self.get_pronunciation_feedback(user_text, self.practice_phrase)
        if from_voice:
            return f"{reply}\n\n发音反馈：{feedback}"
        return reply

    def run(self) -> None:
        self.speak("你好！我是你的中文对话练习助手。你可以直接用中文说话，我会帮你练习口语。")
        if not self.voice_available:
            self.speak("当前没有可用的语音输入，所以我们先用文本模式练习。")

        while True:
            user_text = self.listen()
            if not user_text:
                continue

            print("你：", user_text)
            if any(word in user_text for word in ["再见", "bye", "退出", "结束", "stop"]):
                self.speak("好的，再见！")
                break

            reply = self.respond(user_text, from_voice=True)
            self.speak(reply)

    def run_gui(self) -> None:
        app = ConversationGUI(self)
        self.gui = app
        app.mainloop()


class ConversationGUI(tk.Tk):
    def __init__(self, assistant: ChineseConversationAI) -> None:
        super().__init__()
        self.assistant = assistant
        self.title("中文口语练习助手")
        self.geometry("760x520")

        self.chat_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=("Microsoft YaHei", 11))
        self.chat_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.chat_area.configure(state="disabled")

        bottom_frame = tk.Frame(self)
        bottom_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.entry = tk.Entry(bottom_frame, font=("Microsoft YaHei", 12))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry.bind("<Return>", self.on_send)

        send_button = tk.Button(bottom_frame, text="发送", width=10, command=self.on_send)
        send_button.pack(side=tk.LEFT, padx=(8, 0))

        voice_button = tk.Button(bottom_frame, text="开始说话", width=12, command=self.on_voice)
        voice_button.pack(side=tk.LEFT, padx=(8, 0))

        self.append_message("助手", "你好！我会帮助你练习中文对话。你可以直接输入，或者点击开始说话。")
        if not self.assistant.voice_available:
            self.append_message("助手", "当前语音输入不可用，所以先用文本模式练习即可。")

    def append_message(self, role: str, text: str) -> None:
        self.chat_area.configure(state="normal")
        self.chat_area.insert(tk.END, f"{role}: {text}\n\n")
        self.chat_area.configure(state="disabled")
        self.chat_area.yview(tk.END)

    def on_send(self, event=None) -> None:
        user_text = self.entry.get().strip()
        if not user_text:
            return
        self.entry.delete(0, tk.END)
        self.append_message("你", user_text)
        reply = self.assistant.respond(user_text, from_voice=False)
        self.append_message("助手", reply)
        self.assistant.speak(reply)

    def on_voice(self) -> None:
        user_text = self.assistant.listen()
        if not user_text:
            return
        self.append_message("你", user_text)
        reply = self.assistant.respond(user_text, from_voice=True)
        self.append_message("助手", reply)
        self.assistant.speak(reply)


if __name__ == "__main__":
    try:
        assistant = ChineseConversationAI()
        if len(sys.argv) > 1 and sys.argv[1] == "--cli":
            assistant.run()
        else:
            assistant.run_gui()
    except KeyboardInterrupt:
        print("程序已结束。")
