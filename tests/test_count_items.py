import pytest
import bpy

import count_items

@pytest.fixture
def new_scene_context():
    """
    Creates a new scene and adds two cubes to it.
    Returns the context of the new scene.
    """
    bpy.ops.scene.new(type='EMPTY')

    # Adds 2 cubes to the initially empty scene
    bpy.ops.mesh.primitive_cube_add()
    bpy.ops.mesh.primitive_cube_add()

    return bpy.context


class TestExampleFunctions:
    def test_count_items_in_scene_with_two_cubes(self, new_scene_context):
        # Arrange
        expected_scene_count = 2

        # Act
        actual_scene_count = src.count_items.count_scene_content(new_scene_context)

        # Assert
        assert expected_scene_count == actual_scene_count, (
            f'Expected {expected_scene_count} but got {actual_scene_count}'
        )
