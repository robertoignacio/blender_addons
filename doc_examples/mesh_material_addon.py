# https://medium.com/@kent_edoloverio/create-your-first-blender-addon-4fa84944199c

# basic information about the addon
bl_info = {
    "name": "Add Mesh and Material",
    "author": "Author",
    "version": (0, 1),
    "blender": (4, 0, 0),
    "location": "View3D > Add Mesh",
    "description": "Creates a mesh and can apply a material to it",
    "category": "3D View",
}

# import bpy object
import bpy

# Operator 1
# add a mesh cube using an bpy operator
# uses a class, note the case
class AddCubeOperator(bpy.types.Operator):
    """ Add a cube """
    bl_idname = "mesh.add_cube"
    bl_label = "Add Cube"
    
    # required execute() function
    def execute(self, context):
        # create a mesh cube
        bpy.ops.mesh.primitive_cube_add(size=3, enter_editmode=False, align='WORLD', location=(0, 0, 0))
        # tell Blender it is done
        return {'FINISHED'}

# Operator 2
# add a material to the mesh cube using an bpy operator
# create material, set properties, then assign to mesh cube
# uses a class, note the case
class AddMaterialOperator(bpy.types.Operator):
    """ Add a material to the cube """
    bl_idname = "mesh.add_material"
    bl_label = "Add material"
    
    # required execute() function
    def execute(self, context):
        # create a new material
        bpy.ops.object.material_slot_add()
        default_material = bpy.data.materials.new(name='Default Material')
        default_material.use_nodes = True
        # grab mesh from context
        mesh = context.object.data
        mesh.materials.clear()
        # assign material to mesh
        mesh.materials.append(default_material)
        # tell Blender it is done
        return {'FINISHED'}

# create button panel on VIEW_3D" after defining the Operators
# uses a class
class OperatorPanel(bpy.types.Panel):
    """ Display panel in 3D View """
    bl_label = "Add Cube"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'HEADER_LAYOUT_EXPAND'}
    
    # required draw() function
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        # button 1
        col.operator("mesh.add_cube", icon="MESH_CUBE")
        # button 2
        col.operator("mesh.add_material", icon="SHADING_RENDERED")

# initialize the button panel with the Operators
classes = (
    OperatorPanel,
    AddCubeOperator,
    AddMaterialOperator, 
    )

# required: register() when enabled
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

# required: unregister() when disbled
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


# run register() when loads
if __name__ == "__main__":
    register()

# how to install this script addon:
# Edit --> Preferences --> Add-ons --> Install
# at file manager, select this script.py
# Install add-on, enable add-on checkbox
# Save preferences
# Will be at the 3D View --> "Misc" tab