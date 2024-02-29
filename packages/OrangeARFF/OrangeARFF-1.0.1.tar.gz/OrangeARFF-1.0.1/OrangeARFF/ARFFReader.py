from Orange.data.io import FileFormat
from scipy.io import arff
import pandas as pd
from Orange.data.pandas_compat import table_from_frame, table_to_frame


class ARFFReader(FileFormat):
    """Reader for ARFF files"""
    EXTENSIONS = ('.arff',)
    DESCRIPTION = 'ARFF file'
    SUPPORT_SPARSE_DATA = True

    def __init__(self, filename):
        super().__init__(filename)

    def read(self):
        data = arff.loadarff(self.filename)  # self.filename.encode(sys.getdefaultencoding())
        df = pd.DataFrame(data[0])
        out_data = table_from_frame(df)
        return out_data

    @classmethod
    def write_file(cls, filename, data):
        pass
