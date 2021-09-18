from moviepy import *

# 剪辑一段视频50～60秒
video = VideoFileClip("myHolidays.mp4").subclip(50, 60)

# 添加一个Title在中间
txt_clip = (TextClip("My Holidays 2013", fontsize=70, color='white')
            .with_position('center')
            .with_duration(10))

# 导出视频
result = CompositeVideoClip([video, txt_clip])
result.write_videofile("myHolidays_edited.webm", fps=25)
