import trclab as tlab


class MyApp(tlab.TRCLabApp):

    def __init__(self):
        super().__init__("my_app")

    def on_enable(self):
        self.datasets.get_dataset(tlab.DatasetType.ICH_420).get_train_set()
        self.datasets.get_dataset(tlab.DatasetType.ICH_420).get_test_set()
        self.logger.info("Hello World")

    def on_disable(self):
        self.logger.info(f"{self.app_name} has been disable")


if __name__ == '__main__':
    app = MyApp()
    app.run()
