import bpy    # pip install bpy

# container class, named
class ObjectMoveX(bpy.types.Operator):
    """ Tooltip """    # tooltip for menu items and buttons
    bl_idname = "object.move_x"    # unique id, has to have bl_
    bl_label = "Move X by 1"    # display name
    bl_options = {'REGISTER', 'UNDO'}    # register, and enable undo for Operator
    
    # run execute() when calling the Operator
    def execute(self, context):
        
        # run this script
        # scene = bpy.context.scene    # its narrower to pass context.scene than bpy.context.scene
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

# to run this script: shortcut Alt+P will register(), not execute()
# to execute it: open search menu [F3], type the bl_label string [Move X by 1], then [return]