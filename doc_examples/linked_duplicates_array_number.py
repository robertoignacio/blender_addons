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

# -----------------
total = 10

# add total objects
for i in range(total):
    # make a copy of the active object
    obj_copy = obj.copy()
    # link the copied object to a collection in the scene
    scene.collection.objects.link(obj_copy)
    # place the instanced objects between the 3D cursor and the active object, based on 'i'
    factor = i / total
    # place the copied object at the cursor location
    obj_copy.location = (obj.location * factor) + (cursor_location * (1.0 - factor))

# -----------------
# change location of 3D cursor, run the script
# will create a linked copy of the active object at the 3D cursor location
# because objects.link(obj_copy) when editing the active object mesh all linked copies will change too