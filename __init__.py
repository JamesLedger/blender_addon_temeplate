import bpy # noqa
from .src import operators
from .src import ui

bl_info = {
        "name": "Example Blender Addon",
        "description": "Quick template for a Blender Addon",
        "author": "James Ledger",
        "version": (0, 1),
        "blender": (3, 1, 0),
        "location": "Properties > Example addon"
}


def register():
    operators.register()
    ui.register()


def unregister():
    ui.unregister()
    operators.unregister()
