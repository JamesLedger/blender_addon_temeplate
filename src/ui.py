import bpy # noqa
from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class ExamplePanel(Panel):
    bl_label = 'Example Panel'  # Visible name of panel
    bl_space_type = 'PROPERTIES'  # Where in the UI the panel goes
    bl_region_type = 'WINDOW'  # More specifc location
    bl_context = 'scene'

    def draw(self, context):
        layout = self.layout
        layout.label(text="This is how to do a header!")

        row = layout.row()
        row.operator('addon_template.count_scene_items')


def register():
    register_class(ExamplePanel)


def unregister():
    unregister_class(ExamplePanel)
