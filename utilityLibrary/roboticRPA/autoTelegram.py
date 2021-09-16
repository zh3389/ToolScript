import rpa as r

"""
环境搭建
pip install rpa
"""

r.telegram('1234567890', 'ID can be string or number, r.init() is not required')
r.telegram(1234567890, 'Hello World. Olá Mundo. नमस्ते दुनिया. 안녕하세요 세계. 世界,你好。')
r.telegram(1234567890, 'Use backslash n for new line\nThis is line 2 of the message')
r.telegram(1234567890, 'Sent using my VPS server endpoint https://tebel.org/rpapybot')
r.telegram(1234567890, 'Sent using your own hosted endpoint', 'https://your_endpoint')
