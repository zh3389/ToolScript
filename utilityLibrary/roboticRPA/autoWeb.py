import rpa as r

"""
环境搭建
pip install rpa
"""

r.init()
r.url('https://www.google.com')
r.type('//*[@name="q"]', 'decentralization[enter]')
print(r.read('result-stats'))
r.snap('page', 'results.png')
r.close()
