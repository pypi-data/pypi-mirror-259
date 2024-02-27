import pickle
from typing import Dict
from barfi.scheme.schema_manager import AbsSchemaManager, AbsUserSchemaManager

# Schema Manager
class LocalSchemaManager(AbsSchemaManager):
    def __init__(self, schema_path = None) -> None:
        if schema_path is None:
            schema_path = 'schemas.barfi'
        self.schema_path = schema_path
    
    
    def load_schemas():
        try:
            with open('schemas.barfi', 'rb') as handle_read:
                schemas = pickle.load(handle_read)
        except FileNotFoundError:
            schemas = {}

        schema_names = list(schemas.keys())
        return {'schema_names': schema_names, 'schemas': schemas}


    def save_schema(schema_name: str, schema_data: Dict):
        try:
            with open('schemas.barfi', 'rb') as handle_read:
                schemas = pickle.load(handle_read)
        except FileNotFoundError:
            schemas = {}

        with open('schemas.barfi', 'wb') as handle_write:
            schemas[schema_name] = schema_data
            pickle.dump(schemas, handle_write, protocol=pickle.HIGHEST_PROTOCOL)


    def load_schema_name(schema_name: str) -> Dict:
        schemas_barfi = LocalSchemaManager.load_schemas()
        if schema_name in schemas_barfi['schema_names']:
            return schemas_barfi['schemas'][schema_name]
        else:
            raise ValueError(
                f'Schema :{schema_name}: not found in the saved schemas')


    def delete_schema(schema_name: str):
        try:
            with open('schemas.barfi', 'rb') as handle_read:
                schemas = pickle.load(handle_read)
        except FileNotFoundError:
            schemas = {}

        if schema_name in schemas:
            del schemas[schema_name]
        else:
            raise ValueError(
                f'Schema :{schema_name}: not found in the saved schemas')
        
        with open('schemas.barfi', 'wb') as handle_write:
            pickle.dump(schemas, handle_write, protocol=pickle.HIGHEST_PROTOCOL)