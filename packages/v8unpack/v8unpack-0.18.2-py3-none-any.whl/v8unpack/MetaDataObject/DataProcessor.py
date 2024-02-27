from ..MetaDataObject.core.Container import Container


class DataProcessor(Container):
    version = '803'
    ext_code = {
        'mgr': '2',  # модуль менеджера
        'obj': '0',  # модуль объекта
    }
    help_file_number = 1

    def __init__(self, *, obj_name=None, options=None):
        super().__init__(obj_name=obj_name, options=options)

    @classmethod
    def get_decode_header(cls, header_data):
        return header_data[0][1][3][1]
