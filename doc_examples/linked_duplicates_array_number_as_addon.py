# https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
# second

# basic information about the addon
bl_info = {
    "name": "Cursor Array",
    "author": "Author",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Add Mesh",
    "description": "Copy active object at 3D cursor location",
    "category": "3D View",
}

import bpy
from bpy import context

# -----------------
# addon within class
class ObjectCursorArray(bpy.types.Operator):
    """ Object Cursor Array """
    bl_idname = "object.cursor_array"
    bl_label = "Cursor Array"
    bl_options = {'REGISTER', 'UNDO'}
    
    # required execute()
    def execute(self, context):
        scene = context.scene    # get the current scene
        cursor_location = scene.cursor.location    # get the 3D cursor location
        obj = context.active_object    # get the active object (tba: create one of there is none)

        total = 10    # add total objects
        
        # instantiate meshes
        for i in range(total):
            # make a copy of the active object
            obj_copy = obj.copy()
            # link the copied object to a collection in the scene
            scene.collection.objects.link(obj_copy)
            
            # place the instanced objects between the 3D cursor and the active object, based on 'i'
            factor = i / total
            # place the copied object at the cursor location
            obj_copy.location = (obj.location * factor) + (cursor_location * (1.0 - factor))
        
        # tell Blender the Operator is done
        return {'FINISHED'}

# -----------------
# button panel: to add a menu item you have to append a draw() function to an existing class

# -----------------
# required: register() when enabled
def register():
    bpy.utils.register_class(ObjectCursorArray)

# required: unregister() when disabled
def unregister():
    bpy.utils.unregister_class(ObjectCursorArray)

# -----------------
# change location of 3D cursor, run the script
# will create a linked copy of the active object at the 3D cursor location
# because objects.link(obj_copy) when editing the active object mesh all linked copies will change too

# -----------------
# run register() when loads
if __name__ = "___main__":
    register()