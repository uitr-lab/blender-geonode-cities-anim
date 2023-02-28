import bpy

scene = bpy.context.scene

def pop(obj, start, rate, scene):
    obj.data.body = 'Population - +' + str(int(round((start)+rate*scene.frame_current/bpy.context.scene.render.fps,0))) + '%'

def yr(obj, start, rate, scene):
    obj.data.body = '' + str(int(round((start)+rate*scene.frame_current/bpy.context.scene.render.fps,0))) + ''


def recalculate_pop(scene):

    pop(scene.objects['Text.003'], 5, 1, scene)
    yr(scene.objects['Text.004'], 2023, 2, scene)


bpy.app.handlers.frame_change_pre.clear()
bpy.app.handlers.frame_change_pre.append(recalculate_pop)