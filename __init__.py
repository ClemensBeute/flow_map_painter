# Copyright (C) 2021 Clemens Beute

# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Flow Map Painter",
    "author": "Clemens Beute <feedback.clemensbeute@gmail.com>",
    "version": (1, 5),
    "blender": (4, 4, 3),
    "category": "Paint",
    "location": "Paint Brush Tool Panel",
    "description": "A brush tool for flow map painting. The brush gets the color of the painting direction",
    "warning": "",
    "doc_url": "",
}

import bpy

from .ops import FLOWMAP_OT_FLOW_MAP_PAINT_2D, FLOWMAP_OT_FLOW_MAP_PAINT_3D, FLOWMAP_OT_FLOW_MAP_PAINT_VERTCOL
from .props import FlowmapPainterProperties


def draw_interface(self, context, mode):
    """combined draw, wich handles every panel interface dependeing on given mode"""

    self.layout.separator()

    split1 = self.layout.split(factor=0.55)
    split2 = split1.split(factor=0.15)
    # split.use_property_split = True
    column1 = split2.column()
    column2 = split2.column()
    column3 = split1.column()

    # space
    if mode == '3D_PAINT' or mode == 'VERTEX_PAINT':
        column1.label(icon='ORIENTATION_GLOBAL')
        column2.label(text="Space Type")
        column3.prop(context.scene.flowmap_painter_props, "space_type", text="")

        if context.scene.flowmap_painter_props.space_type == "object_space":
            column1.label(text="")
            column2.label(text="Object")
            column3.prop_search(context.scene.flowmap_painter_props, "object", context.scene, "objects", text="")

    # spacing
    column1.label(icon='ONIONSKIN_ON')
    column2.label(text="Brush Spacing")
    column3.prop(context.scene.flowmap_painter_props, "brush_spacing", slider=True, text="")

    # trace distance
    if mode == '3D_PAINT' or mode == 'VERTEX_PAINT':
        column1.label(icon='CON_TRACKTO')
        column2.label(text="Trace Distance")
        column3.prop(context.scene.flowmap_painter_props, "trace_distance", slider=True, text="")

    # exit
    self.layout.separator()

    splitexit = self.layout.split(factor=0.078)
    splitcol1 = splitexit.column()
    splitcol2 = splitexit.column()
    splitcol1.label(icon='EVENT_ESC')
    txt1 = splitcol2.row()
    txt1.active = False
    txt1.label(text="press ESC to Exit")

    splitcol1.label(text="")
    txt2 = splitcol2.row()
    txt2.active = False
    txt2.label(text="Flowmap painting mode")

    self.layout.separator()

    # paint
    if mode == '2D_PAINT':
        self.layout.operator("flowmap.flow_map_paint_two_d", text="Flowmap 2D Paint Mode", icon='ANIM_DATA')
    if mode == '3D_PAINT':
        self.layout.operator("flowmap.flow_map_paint_three_d", text="Flowmap 3D Paint Mode", icon='ANIM_DATA')
    if mode == 'VERTEX_PAINT':
        self.layout.operator("flowmap.flow_map_paint_vcol", text="Flowmap Vertex Paint Mode", icon='ANIM_DATA')

    self.layout.separator()


class FLOWMAP_PT_FLOW_MAP_PAINT_2D(bpy.types.Panel):

    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Tool"
    bl_label = "2D Flowmap Paint"
    bl_context = ".imagepaint_2d"

    def draw(self, context):
        draw_interface(self, context, mode='2D_PAINT')
        return


class FLOWMAP_PT_FLOW_MAP_PAINT_3D(bpy.types.Panel):

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    bl_label = "3D Flowmap Paint"
    bl_context = "imagepaint"

    @classmethod
    def poll(self, context):
        """Poll Return defines, when to display the Class (Dont show flowmap painter in Properties)"""
        return context.area.type == "VIEW_3D"

    def draw(self, context):
        draw_interface(self, context, mode='3D_PAINT')
        return


class FLOWMAP_PT_FLOW_MAP_PAINT_VERTCOL(bpy.types.Panel):

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    bl_label = "3D Flowmap Vertex Paint"
    bl_context = "vertexpaint"

    @classmethod
    def poll(self, context):
        """Poll Return defines, when to display the Class (Dont show flowmap painter in Properties)"""
        return context.area.type == "VIEW_3D"

    def draw(self, context):
        draw_interface(self, context, mode='VERTEX_PAINT')
        return


def register():

    # PROPS
    bpy.utils.register_class(FlowmapPainterProperties)
    bpy.types.Scene.flowmap_painter_props = bpy.props.PointerProperty(type=FlowmapPainterProperties)

    # OPERATORS
    bpy.utils.register_class(FLOWMAP_OT_FLOW_MAP_PAINT_2D)
    bpy.utils.register_class(FLOWMAP_OT_FLOW_MAP_PAINT_3D)
    bpy.utils.register_class(FLOWMAP_OT_FLOW_MAP_PAINT_VERTCOL)

    # PANELS
    bpy.utils.register_class(FLOWMAP_PT_FLOW_MAP_PAINT_2D)
    bpy.utils.register_class(FLOWMAP_PT_FLOW_MAP_PAINT_3D)
    bpy.utils.register_class(FLOWMAP_PT_FLOW_MAP_PAINT_VERTCOL)

    return None


def unregister():

    # PROPS
    del bpy.types.Object.flowmap_painter_props
    bpy.utils.register_class(FlowmapPainterProperties)

    # OPERATORS
    bpy.utils.unregister_class(FLOWMAP_OT_FLOW_MAP_PAINT_2D)
    bpy.utils.unregister_class(FLOWMAP_OT_FLOW_MAP_PAINT_3D)
    bpy.utils.unregister_class(FLOWMAP_OT_FLOW_MAP_PAINT_VERTCOL)

    # PANELS
    bpy.utils.unregister_class(FLOWMAP_PT_FLOW_MAP_PAINT_2D)
    bpy.utils.unregister_class(FLOWMAP_PT_FLOW_MAP_PAINT_3D)
    bpy.utils.unregister_class(FLOWMAP_PT_FLOW_MAP_PAINT_VERTCOL)

    return None
