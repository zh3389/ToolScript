from wordcloud import WordCloud

"""
环境搭建
pip install wordcloud
"""

wordcloud = WordCloud(font_path="./assets/FZCCHJW.TTF", width=800, height=400, background_color="white")
wordcloud.generate(["a", "b", "c"])
wordcloud.to_file("output_img_name.png")