import trclab as tlab


class MyApp(tlab.TRCLabApp):

    def __init__(self):
        super().__init__("my_app")

    def on_enable(self):
        datasets = self.datasets.get_dataset(tlab.DatasetType.RSNA_ICH)
        train_image_set = datasets.get_train_set()
        for idx, ich_image in enumerate(train_image_set):
            if idx > 5:
                return

            print(ich_image.image_type)

    def on_disable(self):
        self.logger.info(f"{self.app_name} has been disable")


if __name__ == '__main__':
    app = MyApp()
    app.run()
