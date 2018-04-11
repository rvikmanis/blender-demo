import bpy
import json
from datetime import datetime


image_cache = {}


def get_image(path):
    if path not in image_cache:
        image_cache[path] = bpy.data.images.load(path)

    return image_cache[path]


def set_material_image_texture(material, image):
    texture = material.node_tree.nodes["Image Texture"]
    texture.image = image


def main():
    with open("variants.json") as variants_file:
        variants = json.load(variants_file)

    with open("output/performance.json", "w+") as performance_log_file:

        performance_log = {}

        # Render each output image
        for (name, variant) in variants.items():
            for (material_name, image_path) in variant["textures"].items():

                start_time = datetime.now()

                set_material_image_texture(
                    bpy.data.materials[material_name],
                    get_image(image_path)
                )

                # Render scene to output/{name}.jpg
                bpy.data.scenes['Scene'].render.filepath = ("output/%s.jpg" % name)
                bpy.ops.render.render(write_still=True)

                performance_log[name] = (datetime.now() - start_time).total_seconds()

        # Write performance log
        json.dump(performance_log, performance_log_file)


if __name__ == "__main__":
    main()
