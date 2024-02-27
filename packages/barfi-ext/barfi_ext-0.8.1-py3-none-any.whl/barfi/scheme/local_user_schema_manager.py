import pickle
from typing import Dict
from barfi.scheme.schema_manager import AbsSchemaManager, AbsUserSchemaManager
from .local_schema_manager import LocalSchemaManager

# User Schema Manager        
class LocalUserSchemaManager(AbsUserSchemaManager):
    def __init__(self, schema_path = None) -> None:
        if schema_path is None:
            schema_path = 'schemas.barfi'
        self.schema_path = schema_path
        
        self.schema_manager = LocalSchemaManager(schema_path)
    
    
    def get_schema_name(schema_name: str, user: str):
        return f'{schema_name}@{user}'
    
    
    def load_schemas(self, user: str):
        schemas = self.schema_manager.load_schemas();
        # 判断schemas是否包含schemas
        if 'schemas' not in schemas:
            return schemas
        
        _all = schemas['schemas']
        if (len(_all) == 0):
            return schemas
        # Dict 按名称过滤
        _filtered = {key: value for key, value in _all.items() if key.endswith(f'@{user}')}
        return {'schema_names': _filtered.keys(), 'schemas': _filtered}
    
    
    def save_schema(self, user: str, schema_data: Dict, schema_name: str):
        self.schema_manager.save_schema(self.get_schema_name(schema_name, user), schema_data)
    
        
    def load_schema_name(self, schema_name: str, user: str) -> Dict:
        return self.schema_manager.load_schema_name(self.get_schema_name(schema_name, user))
    
    
    def delete_schema(self, schema_name: str, user: str):
        self.schema_manager.delete_schema(self.get_schema_name(schema_name, user))