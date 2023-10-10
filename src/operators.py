import bpy # noqa
from . import functions

from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class AT_OT_count_scene_items(Operator):
    """
    Name of the class is following Blender convention:
    AT_ : Addon template (or project initials)
    OT_ : Operator
    count_scene_items : What the operator does
    """
    bl_idname = 'addon_template.count_scene_items'  # Internal operator ID
    bl_label = 'Count Scene Items'  # Text on the button
    bl_options = {'REGISTER'}

    def execute(self, context):
        functions.count_items_in_scene(context)
        return {'FINISHED'}


operators = [
    AT_OT_count_scene_items
]


def register():
    for operator in operators:
        register_class(operator)


def unregister():
    for operator in reversed(operators):
        unregister_class(operator)
