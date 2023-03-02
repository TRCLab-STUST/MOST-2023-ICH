import trclab as tlab
from trclab.img import ImageType
from trclab.ich import ICHType


class MyApp(tlab.TRCLabApp):

    def __init__(self):
        super().__init__("my_app")

    def on_enable(self):
        self.logger.info("ImageType")
        self.logger.info(ImageType("dcm"))
        self.logger.info(ICHType(0))
        self.logger.info(ICHType["intraventricular"])
        self.logger.info(
            self.datasets.get_dataset(tlab.DatasetType.RSNA_ICH).get_train_set()
        )
        self.logger.info("Hello World")

    def on_disable(self):
        self.logger.info(f"{self.app_name} has been disable")


if __name__ == '__main__':
    app = MyApp()
    app.run()
