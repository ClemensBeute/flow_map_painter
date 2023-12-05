# Flow Map Painter [Blender]

This blender add-on provides a brush tool for flow map painting.

It supports 2D Image Editor - Paint Mode and also the 3D Viewport - Texture Paint Mode and 3D Viewport - Vertex Paint Mode.

![image](https://github.com/ClemensBeute/flow_map_painter/assets/3758308/704e9279-ea38-40d4-9fdf-1cfbd3ddfd1a)

## Usage
You find it, when you are in the named modes.

It's located in the right side Panel in the Tool category -> 3D Flow Map Paint / 2D Flow Map Paint.

Make sure the image you want to paint on is selected in your material.

The Color Space of the image should be set to Linear. For maximum quality I would suggest using the exr format. With exr blender also doesn't change the color space to sRGB, every time you save it.

Also make sure, if you are using multiple UV layers, that you highlight the one, you want to use, if you are painting in 3D.



To paint, simply hit the Flowmap Paint Mode Button. This sets your brush into the Flowmap Paint Mode. Hit ESC to exit the mode.
The shortcuts for navigation and brush setting should work, while you are in the Mode, but your clicking is restricted just for painting.

Note that most of the brush setting, like falloff, brushstrength pen pressure and so on are taken into account from the normal brush settings.



UV space should work fine for most applications, but there is also object and world space, if you need it.



Also note that if you use vertex paint, the color is stored in sRGB. But you will need to convert it to linear, to function correctly. You can do that by running it through a gamma node, set to 0.5.



In the flow_map_examples.blend you can find some example materials and nodes, to tinker with. If you want to test the hair shader, you might need to install Secrop's ShaderNodesExtra2.80 add-on.



for bug reports and feedback, send me an e-mail:

feedback.clemensbeute@gmail.com

If you want to support me, you can also purchase the addon at gumroad:  
https://clemensbeute.gumroad.com/l/heZDT?layout=profile
