from tsugu import tsugu_config, tsugu
import unittest


class TestTsugu(unittest.TestCase):

    def test_tsugu(self):
        def text_response(string):
            return [{"type": "string", "string": string}]

        def show_back_msg(data):
            import base64
            from PIL import Image
            import io

            if not data:
                return text_response("[无反馈数据]")
            else:
                for item in data:
                    if item["type"] == "string":
                        e_message = item["string"]
                        print(f"[文字信息]\n{e_message}")
                    elif item["type"] == "base64":
                        # 处理Base64编码的图像数据
                        base64_data = item["string"]
                        # 解码Base64数据
                        image_data = base64.b64decode(base64_data)
                        # 输出MB字节大小
                        print(f"[图像大小: {len(image_data) / 1024:.2f}KB]")
                        # 将二进制数据转换为 PIL 图像对象
                        image = Image.open(io.BytesIO(image_data))
                        # 保存图像文件
                        image.show()
                    else:
                        print(item)

        self.subTest(
            tsugu_config.set_use_proxies(True)
        )
        self.subTest(
            tsugu_config.set_proxies({
                "http": "http://127.0.0.1:7890",
                "https": "http://127.0.0.1:7890"
            })
        )
        self.subTest(
            show_back_msg(
                tsugu('玩家状态', '114514', 'red', '666808414'),
            )
        )


if __name__ == '__main__':
    unittest.main()


