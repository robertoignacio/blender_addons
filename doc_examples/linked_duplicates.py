# https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
# second

import bpy
from bpy import context

# get the current scene
scene = context.scene

# get the 3D cursor location
cursor_location = scene.cursor.location

# get the active object (tba: create one of there is none)
obj = context.active_object

# make a copy of the active object
obj_copy = obj.copy()

# link the copied object to a collection in the scene
scene.collection.objects.link(obj_copy)

# place the copied object at the cursor location
obj_copy.location = cursor_location

# when installed, will create a linked copy of the active object at the 3D cursor locatiion