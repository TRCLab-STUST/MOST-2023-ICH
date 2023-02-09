from trclab.application import TRCLabApp


class MyApp(TRCLabApp):

    def __init__(self):
        super().__init__("my_app")

    def on_enable(self):
        self.logger.info("Hello World")
        pass

    def on_disable(self):
        pass


if __name__ == '__main__':
    app = MyApp()
    app.run()
