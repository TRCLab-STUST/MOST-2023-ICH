from enum import IntEnum, unique


@unique
class ICHType(IntEnum):
    # 腦實質出血 (Intraparenchymal Hemorrhage)
    INTRAPARENCHYMAL = 0
    # 腦室內出血 (Intraventricular Hemorrhage)
    INTRAVENTRICULAR = 1
    # 蜘蛛網膜下腔出血 (Subarachnoid Hemorrhage)
    SUBARACHNOID = 2
    # 硬腦膜下腔出血 (Subdural Hemorrhage)
    SUBDURAL = 3
    # 硬腦膜上出血 (Epidural Hemorrhage)
    EPIDURAL = 4
