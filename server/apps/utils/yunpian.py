import json
import requests


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【刘渊】您的验证码是{code}".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict

    def tpl_send_sms(self, mobile):
        """
        模板接口发短信
        """
        parmas = {
            "apikey": self.api_key,
            "tpl_id": 3574506,
            "text": "【刘渊】您好，您的订单已经处理完毕，请在您指定的提取时间来超市柜台提取",
            "mobile": mobile
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == "__main__":
    yun_pian = YunPian("3e75a85b2d44a808f50ab4e88cbc3a4f")
    yun_pian.tpl_send_sms("15918891965")
