# https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
# save base_only_register as base_installable.py (with .py extension), at a path location
# install: Preferences --> Add-ons --> Install... --> select the file
# if you want it enabled on restart, check the checkbox for Save as Default
# When enabled, Blender runs the addon script and register() function.
# When disabled, Blender runs the unregister() function.

import bpy

# container class, named
class ObjectMoveX(bpy.types.Operator):
    """ Tooltip """    # tooltip for menu items and buttons
    bl_idname = "object.move_x"    # unique id, has to have bl_
    bl_label = "Move X by 1"    # display name
    bl_options = {'REGISTER', 'UNDO'}    # register, and enable undo for Operator
    
    def execute(self, context):
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0
        
        # tell Blender that the Operator finished successfully
        return {'FINISHED'}

# outside of ObjectMoveX class

def menu_func(self, context):
    self.layout.operator(ObjectMoveX.bl_idname)

# required: register()
def register():
    bpy.utils.register_class(ObjectMoveX)
    # add the Operator to an existing menu
    bpy.types.VIEW3D_MT_object.append(menu_func)

# required: unregister()
# unregister after execute()
def unregister():
    bpy.utils.unregister_class(ObjectMoveX)

# run register() when the script is executed
if __name__ == "__main__":
    register()