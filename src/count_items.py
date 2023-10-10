import bpy # noqa


def count_scene_content(context):
    """
    Simple demo function to count the objects in the scene
    Prints this to the windows console for visibility
    also returns it for use in testing
    """
    count = len(context.scene.objects)
    print(f'There are {count} items in the scene!')
    return count
