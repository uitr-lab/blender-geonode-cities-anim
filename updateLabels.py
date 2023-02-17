import bpy

scene = bpy.context.scene

def pop(obj, start, rate, scene):
    obj.data.body = 'Population: ' + str(int(round(start+rate*scene.frame_current/bpy.context.scene.render.fps,0))) + 'k'

def recalculate_pop(scene):
    pop(scene.objects['Text.000'], 100, 20, scene)
    pop(scene.objects['Text.001'], 55, 15, scene)
    pop(scene.objects['Text.002'], 33, 10, scene)

bpy.app.handlers.frame_change_pre.clear()
bpy.app.handlers.frame_change_pre.append(recalculate_pop)