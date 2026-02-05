///Create IN

sel = hou.selectedNodes()

if len(sel) == 1:
    curPath = sel[0].parent()
    objPath = sel[0].path()
    pos = sel[0].position() + hou.Vector2(0,-1)
    
    mkMerge = curPath.createNode("object_merge")
    mkMerge.setPosition(pos)
    try:
        mkMerge.setName(sel[0].name() + "_merge")
    except:
        mkMerge.setName(sel[0].name() + "_merge1")
    mkMerge.parm("xformtype").set(1)
    mkMerge.parm("objpath1").set(objPath)
