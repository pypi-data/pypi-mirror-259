from abc import ABCMeta, abstractmethod
from typing import Dict
 
class AbsSchemaManager(metaclass=ABCMeta):
    @abstractmethod
    def load_schemas(self):
        pass
    
    @abstractmethod
    def save_schema(self, schema_name: str, schema_data: Dict):
        pass
      
    @abstractmethod
    def load_schema_name(schema_name: str) -> Dict:
        pass
    
    @abstractmethod
    def delete_schema(schema_name: str):
        pass
    
    
class AbsUserSchemaManager(AbsSchemaManager):
    @abstractmethod
    def load_schemas(self, user: str):
        pass
    
    @abstractmethod
    def save_schema(self, user: str, schema_data: Dict, schema_name: str):
        pass
      
    @abstractmethod
    def load_schema_name(schema_name: str, user: str) -> Dict:
        pass
    
    @abstractmethod
    def delete_schema(schema_name: str, user: str):
        pass