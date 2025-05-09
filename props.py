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

import bpy


class FlowmapPainterProperties(bpy.types.PropertyGroup):

    brush_spacing: bpy.props.FloatProperty(
        name="brush spacing",
        description="How much has the mouse to travel, bevor a new stroke is painted?",
        default=20,
        soft_min=0.1,
        soft_max=100,
        min=0,
        subtype='PIXEL'
    )

    trace_distance: bpy.props.FloatProperty(
        name="trace distance",
        description="How deep reaches your object into the scene?",
        min=0,
        soft_max=10000,
        default=1000,
        unit='LENGTH'
    )

    space_type_items = (
        (
            "uv_space",
            "UV Space",
            "Use it, if you want to transform your material UV Coordinates. Your object needs a UV Map",
            'UV',
            0,
        ),
        (
            "object_space",
            "Object Space",
            "Use it, if you want to transform your material Object Coordinates. If empty, current object is used. No UV Map needed in Vertex Paint",
            'OBJECT_DATAMODE',
            1,
        ),
        (
            "world_space",
            "World Space",
            "Similar to object Space, but it uses world coordinates",
            'WORLD_DATA',
            2,
        ),
    )

    space_type: bpy.props.EnumProperty(
        name="space type",
        description="Which space type is used for the direction color?",
        items=space_type_items,
        default=0
    )

    object: bpy.props.PointerProperty(
        name="object",
        description="Which object is used for the object space? Default is the active object itself.",
        type=bpy.types.Object
    )
