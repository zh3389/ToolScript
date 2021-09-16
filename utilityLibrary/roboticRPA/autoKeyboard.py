import rpa as r

"""
环境搭建
pip install rpa
"""

r.init(visual_automation=True, chrome_browser=False)
r.keyboard('[cmd][space]')
r.keyboard('safari[enter]')
r.keyboard('[cmd][alt]1')
r.keyboard('mortal kombat[enter]')
r.wait(2.5)
r.snap('page.png', 'results.png')
r.close()
