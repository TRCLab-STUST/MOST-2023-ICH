import trclab as tlab
from trclab.datasets import *


class MyApp(tlab.TRCLabApp):

    def __init__(self):
        super().__init__("my_app")

    def on_enable(self):
        self.logger.info("Hello World")
        self.logger.info(ICH127FileManager().folder_path)

    def on_disable(self):
        self.logger.info(f"{self.app_name} has been disable")


if __name__ == '__main__':
    app = MyApp()
    app.run()
