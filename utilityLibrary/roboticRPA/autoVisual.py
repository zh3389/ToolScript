import rpa as r

"""
环境搭建
pip install rpa
"""

r.init(visual_automation=True, chrome_browser=False)
r.dclick('outlook_icon.png')
r.click('new_mail.png')
r.type('message_box.png', 'message')
r.click('send_button.png')
r.close()
