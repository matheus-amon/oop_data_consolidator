from abc import ABC, abstractmethod

class DataSource(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def start():
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def get_data(self):
        raise NotImplementedError("Método não implementado")
    
    @abstractmethod
    def transform_data_to_df(self):
        raise NotImplementedError("Método não implementado")
    
    @abstractmethod
    def save_data(self):
        raise NotImplementedError("Método não implementado")
