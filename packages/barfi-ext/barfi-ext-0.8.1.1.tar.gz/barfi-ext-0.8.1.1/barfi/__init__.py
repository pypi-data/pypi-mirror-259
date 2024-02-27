import streamlit.components.v1 as components
from typing import List, Dict, Union

# import barfi components
from .block_builder import Block
from .compute_engine import ComputeEngine
from .scheme.local_schema_manager import LocalSchemaManager
from .scheme.schema_manager import AbsSchemaManager
from .scheme.preset import editor_preset

import os

_RELEASE = False

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        "st_barfi",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "client")
    _component_func = components.declare_component(
        "st_barfi", path=build_dir)

# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.

# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.

def st_barfi(base_blocks: Union[List[Block], Dict], schemaManager: AbsSchemaManager = None, load_schema: str = None, compute_engine: bool = True, key=None, show_menu: bool = True):
    if (schemaManager is not None) and (not isinstance(schemaManager, AbsSchemaManager)):
        raise TypeError(
            'Invalid type for schemaManager passed to the st_barfi component.')
    if (schemaManager is None): 
        schemaManager = LocalSchemaManager()
    editor_schema = schemaManager.load_schema_name(load_schema) if load_schema else None
    schemas_in_db = schemaManager.load_schemas()
    schema_names_in_db = schemas_in_db['schema_names']

    editor_setting = {'compute_engine': compute_engine}

    # base_blocks_data = [block._export() for block in base_blocks]

    if isinstance(base_blocks, List):
        base_blocks_data = [block._export() for block in base_blocks]
        base_blocks_list = base_blocks
    elif isinstance(base_blocks, Dict):
        base_blocks_data = []
        base_blocks_list = []
        for category, block_list in base_blocks.items():
            if not isinstance(block_list, List):
                raise TypeError(
                    'Invalid type for base_blocks passed to the st_barfi component.')
            for block in block_list:
                base_blocks_list.append(block)
                block_data = block._export()
                block_data['category'] = category
                base_blocks_data.append(block_data)
    else:
        raise TypeError(
            'Invalid type for base_blocks passed to the st_barfi component.')

    _from_client = _component_func(base_blocks=base_blocks_data, load_editor_schema=editor_schema,
                                   load_schema_names=schema_names_in_db, load_schema_name=load_schema, show_menu=show_menu, editor_setting=editor_setting,
                                   key=key, default={'command': 'skip', 'editor_state': {}})

    if _from_client['command'] == 'flush':
        print(_from_client)
        if not compute_engine:
            return _from_client
    if _from_client['command'] == 'execute':
        _ce = ComputeEngine(blocks=base_blocks_list)
        _ce.add_editor_state(_from_client['editor_state'])
        _ce._map_block_link()
        if not compute_engine:
            # return _ce.get_result()
            return _from_client
        _ce._execute_compute()
        return _ce.get_result()
    if _from_client['command'] == 'save':
        schemaManager.save_schema(
            schema_name=_from_client['schema_name'], schema_data=_from_client['editor_state'])
    if _from_client['command'] == 'load':
        load_schema = _from_client['schema_name']
        editor_schema = schemaManager.load_schema_name(load_schema)
    return {}


def barfi_schemas(schemaManager: AbsSchemaManager = None):
    if (schemaManager is not None) and (not isinstance(schemaManager, AbsSchemaManager)):
        raise TypeError(
            'Invalid type for schemaManager passed to the barfi_schemas function.')
    if (schemaManager is None):
        schemaManager = LocalSchemaManager()
    schemas_in_db = schemaManager.load_schemas()
    return schemas_in_db['schema_names']
