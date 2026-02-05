///Connect nodes

import hou

inputs = hou.selectedNodes()[1:]
target = hou.selectedNodes()[0]
target_con = len(target.inputConnections())
for count, node in enumerate(inputs):
    target.setInput(count+target_con, node)
