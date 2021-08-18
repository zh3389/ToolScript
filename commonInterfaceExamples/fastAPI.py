from fastapi import FastAPI

"""python
# 环境安装
pip install fastapi
pip install uvicorn
"""

app = FastAPI()

# 无参数
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 有参数
@app.get("/{img_path}")
def get_embeds(img_path: str):
    result = f'this is img path: {img_path}'
    return {"Hello": result}



# 上载文件
import io
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def get_img_embed(file: UploadFile = File(...)):
    """
    字节流文件转图像
    img = Image.open(io.BytesIO(input_data)).convert("RGB")
    """
    contents = await file.read()
    contents = io.BytesIO(contents)
    embed = f"{contents}"
    return embed


if __name__ == '__main__':
    """
    使用命令启动该脚本文件 --host 绑定到所有网卡
    uvicorn main:app --reload --host 0.0.0.0
    使用127.0.0.1:8000/docs访问api文档
    """