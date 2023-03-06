import trclab as tlab


class MyApp(tlab.TRCLabApp):

    def __init__(self):
        super().__init__("my_app")

    def on_enable(self):
        datasets = self.datasets.get_dataset(tlab.DatasetType.RSNA_ICH)
        # train_image_set = datasets.get_train_set()
        # self.logger.info(train_image_set)
        # self.logger.info(len(train_image_set))
        # for item in train_image_set:
        #     self.logger.info(item.ich_types.value)
        # self.logger.info(train_image_set[0].ich_types)

    def on_disable(self):
        self.logger.info(f"{self.app_name} has been disable")


if __name__ == '__main__':
    app = MyApp()
    app.run()
