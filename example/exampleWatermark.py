from blind_watermark import WaterMark
import cv2

"""
# 环境搭建
pip install blind-watermark
给图像加盲水印的脚本
"""


class HideWaterMark():
    def __init__(self,
                 watermark_img,
                 watermark_bit=[True, False, True, True, True, False],
                 watermark_str="zh"):
        self.password_wm = 1  # 水印图密码
        self.password_img = 1  # 加密图密码
        self.watermark_img = watermark_img  # 水印图的path
        self.watermark_bit = watermark_bit  # 水印图的bit列表
        self.watermark_str = watermark_str  # 水印图的str

    def encoder_img(self, original_img, output_encoder_img):
        """
        :param original_img: 需要加水印的原图
        :param output_encoder_img: 加水印后的图像
        :return:
        """
        bwm = WaterMark(password_wm=self.password_wm, password_img=self.password_img)
        bwm.read_img(original_img)  # 需要加水印的原图
        bwm.read_wm(self.watermark_img)  # read watermark
        bwm.embed(output_encoder_img)

    def decoder_img(self, output_encoder_img, decoder_watermark_img):
        """
        :param output_encoder_img: 含有水印的图
        :param decoder_watermark_img: 解出来的水印图
        :return:
        """
        w, h, _ = cv2.imread(self.watermark_img).shape
        bwm = WaterMark(password_wm=self.password_wm, password_img=self.password_img)
        bwm.extract(filename=output_encoder_img, wm_shape=(w, h), out_wm_name=decoder_watermark_img)

    def encoder_bit(self, original_img, output_encoder_img):
        """
        :param original_img: 需要加水印的原图
        :param output_encoder_img: 加bit水印后的图像
        :return:
        """
        bwm = WaterMark(password_wm=self.password_wm, password_img=self.password_img)
        bwm.read_img(original_img)
        bwm.read_wm(self.watermark_bit, mode='bit')
        bwm.embed(output_encoder_img)

    def decoder_bit(self, output_encoder_img):
        """
        :param output_encoder_img: 含有水印的图
        :return: 解出来的水印bit
        """
        bwm = WaterMark(password_wm=self.password_wm, password_img=self.password_img)
        wm_extract = bwm.extract(output_encoder_img, wm_shape=len(self.watermark_bit), mode='bit')
        print(wm_extract)
        return wm_extract

    def encoder_str(self, original_img, output_encoder_img):
        """
        :param original_img: 需要加水印的原图
        :param output_encoder_img: 加str水印后的图像
        :return:
        """
        bwm = WaterMark(password_wm=self.password_wm, password_img=self.password_img)
        bwm.read_img(original_img)
        bwm.read_wm(self.watermark_str, mode='str')
        bwm.embed(output_encoder_img)

    def decoder_str(self, output_encoder_img):
        """
        :param output_encoder_img: 含有水印的图
        :return: 解出来的水印str
        """
        bwm = WaterMark(password_wm=self.password_wm, password_img=self.password_img)
        wm_extract = bwm.extract(output_encoder_img, wm_shape=len(self.watermark_str), mode='str')
        print(wm_extract)
        return wm_extract


if __name__ == '__main__':
    watermark_img = "./1.png"
    watermark_bit = [True, False, True, True, True, False]
    watermark_str = "zh"
    hwm = HideWaterMark(watermark_img)
    hwm.encoder_img("input_img_path", "output_encoder_img_path")  # 需要加水印的图像路径, 加水印后的输出路径
    hwm.decoder_img("output_encoder_img_path", "decoder_watermark_img")  # 需要解水印的图像路径, 解出的水印图路径
    hwm.encoder_bit("input_img_path", "output_encoder_img_path")  # 需要加水印的图像路径, 加水印后的输出路径
    hwm.decoder_bit("output_encoder_img_path")  # 需要解水印的图像路径 返回水印bit
    hwm.encoder_str("input_img_path", "output_encoder_img_path")  # 需要加水印的图像路径, 加水印后的输出路径
    hwm.decoder_str("output_encoder_img_path")  # 需要解水印的图像路径, 返回水印str
