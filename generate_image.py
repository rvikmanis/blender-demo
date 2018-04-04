import bpy
import os

working_dir = os.path.dirname(os.path.realpath(__file__))

color = (
    int(os.environ["COLOR_R"]),
    int(os.environ["COLOR_G"]),
    int(os.environ["COLOR_B"]),
)

bpy.data.materials["Material"].diffuse_color = color
bpy.data.scenes['Scene'].render.filepath = os.path.join(working_dir, "output.png")
bpy.ops.render.render(write_still=True)
