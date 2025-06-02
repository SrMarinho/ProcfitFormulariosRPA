from pathlib import Path
from src.config import config
from src.utils.file_data_reader import FileDataReader


class Colaborador:
    def __init__(self):
        self.filePath = Path(config.assetPath) / 'colaboradores.xlsx'

    def getColaboradores(self):
        fdr = FileDataReader(str(self.filePath))

        batchSize = 1000
        for colaboradorBatch in fdr.stream(batchSize):
            for colaborador in colaboradorBatch:
                yield colaborador