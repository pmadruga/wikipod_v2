# OpenShot Video Editor is a program that creates, modifies, and edits video files.
#   Copyright (C) 2009  Jonathan Thomas
#
# This file is part of OpenShot Video Editor (http://launchpad.net/openshot/).
#
# OpenShot Video Editor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenShot Video Editor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OpenShot Video Editor.  If not, see <http://www.gnu.org/licenses/>.


# Import Blender's python API.  This only works when the script is being
# run from the context of Blender.  Blender contains it's own version of Python
# with this library pre-installed.
import bpy

# Debug Info:
# ./blender -b test.blend -P demo.py
# -b = background mode
# -P = run a Python script within the context of the project file

# Init all of the variables needed by this script.  Because Blender executes
# this script, OpenShot will inject a dictionary of the required parameters
# before this script is executed.
params = {
    'title': 'Oh Yeah! OpenShot!',
    'extrude': 0.1,
    'bevel_depth': 0.02,
    'spacemode': 'CENTER',
    'text_size': 1.5,
    'width': 1.0,
    'fontname': 'Bfont',

    'color': [0.8, 0.8, 0.8],
    'alpha': 1.0,

    'output_path': '/tmp/',
    'fps': 24,
    'quality': 90,
    'file_format': 'PNG',
    'color_mode': 'RGBA',
    'horizon_color': [0.57, 0.57, 0.57],
    'resolution_x': 1920,
    'resolution_y': 1080,
    'resolution_percentage': 100,
    'start_frame': 20,
    'end_frame': 25,
    'animation': True,
}


#BEGIN INJECTING PARAMS
params['file_name'] = u'TitleFileName'
params['start_x'] = 3.8
params['start_y'] = 4.13
params['start_z'] = 2.65
params['end_x'] = -4.6
params['end_y'] = 4.13
params['end_z'] = 3.21
params['diffuse_color'] = [1.0, 1.0, 1.0, 1.0]
params['alpha'] = 10.0
params['glare1_type'] = u'GHOSTS'
params['glare1_streaks'] = 4.0
params['glare1_color'] = 0.25
params['glare1_angle'] = 0.0
params['glare2_type'] = u'STREAKS'
params['glare2_streaks'] = 4.0
params['glare2_color'] = 0.25
params['glare2_angle'] = 0.0
params['start_frame'] = 1
params['end_frame'] = 250
params['animation_speed'] = u'1'
params['resolution_x'] = 1280
params['resolution_y'] = 720
params['resolution_percentage'] = 50
params['quality'] = 100
params['file_format'] = u'PNG'
params['color_mode'] = u'RGBA'
params['alpha_mode'] = 1
params['animation'] = True
params['output_path'] = u'/home/pedro/.openshot_qt/blender/20G2UQET40/TitleFileName'
#END INJECTING PARAMS

#ONLY RENDER 1 FRAME FOR PREVIEW
params['start_frame'] = 45
params['end_frame'] = 45
#END ONLY RENDER 1 FRAME FOR PREVIEW


# The remainder of this script will modify the current Blender .blend project
# file, and adjust the settings.  The .blend file is specified in the XML file
# that defines this template in OpenShot.
# ----------------------------------------------------------------------------

# Modify the Location of the Wand
sphere_object = bpy.data.objects["Sphere"]
sphere_object.location = [params["start_x"], params["start_y"], params["start_z"]]

# Modify the Start and End keyframes
bpy.data.actions["SphereAction"].fcurves[0].keyframe_points[0].co = (1.0, params["start_x"])
bpy.data.actions["SphereAction"].fcurves[0].keyframe_points[0].handle_left.y = params["start_x"]
bpy.data.actions["SphereAction"].fcurves[0].keyframe_points[0].handle_right.y = params["start_x"]

bpy.data.actions["SphereAction"].fcurves[1].keyframe_points[0].co = (1.0, params["start_y"])
bpy.data.actions["SphereAction"].fcurves[1].keyframe_points[0].handle_left.y = params["start_y"]
bpy.data.actions["SphereAction"].fcurves[1].keyframe_points[0].handle_right.y = params["start_y"]

bpy.data.actions["SphereAction"].fcurves[2].keyframe_points[0].co = (1.0, params["start_z"])
bpy.data.actions["SphereAction"].fcurves[2].keyframe_points[0].handle_left.y = params["start_z"]
bpy.data.actions["SphereAction"].fcurves[2].keyframe_points[0].handle_right.y = params["start_z"]
#################
bpy.data.actions["SphereAction"].fcurves[0].keyframe_points[1].co = (300.0, params["end_x"])
bpy.data.actions["SphereAction"].fcurves[0].keyframe_points[1].handle_left.y = params["end_x"]
bpy.data.actions["SphereAction"].fcurves[0].keyframe_points[1].handle_right.y = params["end_x"]

bpy.data.actions["SphereAction"].fcurves[1].keyframe_points[1].co = (300.0, params["end_y"])
bpy.data.actions["SphereAction"].fcurves[1].keyframe_points[1].handle_left.y = params["end_y"]
bpy.data.actions["SphereAction"].fcurves[1].keyframe_points[1].handle_right.y = params["end_y"]

bpy.data.actions["SphereAction"].fcurves[2].keyframe_points[1].co = (300.0, params["end_z"])
bpy.data.actions["SphereAction"].fcurves[2].keyframe_points[1].handle_left.y = params["end_z"]
bpy.data.actions["SphereAction"].fcurves[2].keyframe_points[1].handle_right.y = params["end_z"]

# Change the material settings (color, alpha, etc...)
material_object = bpy.data.materials["Material.001"]
bpy.data.materials["Material.001"].node_tree.nodes[1].inputs["Base Color"].default_value = params["diffuse_color"]
bpy.data.materials["Material.001"].node_tree.nodes[1].inputs["Emission"].default_value = params["diffuse_color"]
bpy.data.materials["Material.001"].node_tree.nodes[1].inputs["Alpha"].default_value = params["alpha"]

# Change Composite Node settings
glare_node = bpy.data.scenes[0].node_tree.nodes["Glare"]
glare_node.color_modulation = params["glare1_color"]
glare_node.glare_type = params["glare1_type"]
glare_node.streaks = params["glare1_streaks"]
glare_node.angle_offset = params["glare1_angle"]

glare_node = bpy.data.scenes[0].node_tree.nodes["Glare.001"]
glare_node.color_modulation = params["glare2_color"]
glare_node.glare_type = params["glare2_type"]
glare_node.streaks = params["glare2_streaks"]
glare_node.angle_offset = params["glare2_angle"]

# Set the render options.  It is important that these are set
# to the same values as the current OpenShot project.  These
# params are automatically set by OpenShot
bpy.context.scene.render.filepath = params["output_path"]
bpy.context.scene.render.fps = params["fps"]
bpy.context.scene.render.image_settings.file_format = params["file_format"]
bpy.context.scene.render.image_settings.color_mode = params["color_mode"]
bpy.context.scene.render.film_transparent = params["alpha_mode"]
bpy.context.scene.render.resolution_x = params["resolution_x"]
bpy.context.scene.render.resolution_y = params["resolution_y"]
bpy.context.scene.render.resolution_percentage = params["resolution_percentage"]
bpy.context.scene.frame_start = params["start_frame"]
bpy.context.scene.frame_end = params["end_frame"]

# Animation Speed (use Blender's time remapping to slow or speed up animation)
animation_speed = int(params["animation_speed"])  # time remapping multiplier
new_length = int(params["end_frame"]) * animation_speed  # new length (in frames)
bpy.context.scene.frame_end = new_length
bpy.context.scene.render.frame_map_old = 1
bpy.context.scene.render.frame_map_new = animation_speed
if params["start_frame"] == params["end_frame"]:
    bpy.context.scene.frame_start = params["end_frame"]
    bpy.context.scene.frame_end = params["end_frame"]

# Render the current animation to the params["output_path"] folder
bpy.ops.render.render(animation=params["animation"])
