# https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
# https://docs.blender.org/api/4.1/bpy.types.Menu.html#bpy.types.Menu
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
    bl_options = {'REGISTER', 'UNDO'}    # enable undo
    
    # add a text value for total
    total: bpy.props.IntProperty(name="Steps", default=2, min=1, max=10)
    
    # required execute()
    def execute(self, context):
        scene = context.scene    # get the current scene
        cursor_location = scene.cursor.location    # get the 3D cursor location
        obj = context.active_object    # get the active object (tba: create one of there is none)

        # total = 10    # add total objects, when defined with props can be external to execute()      
        
        # instantiate meshes
        for i in range(self.total):
            # make a copy of the active object
            obj_copy = obj.copy()
            # link the copied object to a collection in the scene
            scene.collection.objects.link(obj_copy)
            
            # place the instanced objects between the 3D cursor and the active object, based on 'i'
            factor = i / self.total
            # place the copied object at the cursor location
            obj_copy.location = (obj.location * factor) + (cursor_location * (1.0 - factor))
        
        # tell Blender the Operator is done
        return {'FINISHED'}

# -----------------
# button panel: to add a menu item you have to append a draw() function to an existing class
def menu_func(self, context):
    self.layout.operator(ObjectCursorArray.bl_idname)


# -----------------
# required: register() when enabled
def register():
    bpy.utils.register_class(ObjectCursorArray)
    # append the menu item to VIEW3D Object view: obtained from mouse pointer tooltip
    bpy.types.VIEW3D_MT_object.append(menu_func)

# required: unregister() when disabled
def unregister():
    bpy.utils.unregister_class(ObjectCursorArray)
    # remove menu item
    bpy.types.VIEW3D_MT_object.remove(menu_func)

# -----------------
# to install: Edit --> Preferences --> Addons --> Install --> tick checkbox

# this thing will be at 3D View --> Object --> Cursor Array
# but can be appended anywhere, like

# -----------------
# run register() when loads
if __name__ == "__main__":
    register()