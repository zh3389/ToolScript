import rpa as r

"""
环境搭建
pip install rpa
"""

r.init(visual_automation=True, chrome_browser=False)
print(r.read('pdf_window.png'))
print(r.read('image_preview.png'))
r.hover('anchor_element.png')
print(r.read(r.mouse_x(), r.mouse_y(), r.mouse_x() + 400, r.mouse_y() + 200))
r.close()
