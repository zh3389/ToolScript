import rpa as r

"""
环境搭建
pip install rpa
"""

r.init(visual_automation=True)
r.type(600, 300, 'open source')
r.click(900, 300)
r.snap('page.png', 'results.png')
r.hover('button_to_drag.png')
r.mouse('down')
r.hover(r.mouse_x() + 300, r.mouse_y())
r.mouse('up')
r.close()
