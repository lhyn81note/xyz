import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Shapes 1.15


Rectangle {
    id: canvas
    visible: true
    width: 800
    height: 600
    anchors.fill: parent
    anchors.margins: 5

    property var nodes: ({})

    signal evtAny(var response)

    function updateNodeStatus(nodeId, status) {
        var node = canvas.nodes[nodeId]
        if (node) {
            node.textColor = status === 1 ? "white" : "black"
            node.bgColor = status === 1 ? "orange" : status === 2 ? "green" : status === 3 ? "red" : "white"
        } else {
            console.log("Node not found:", nodeId)
        }
    }

    ListModel {
        id: nodesModel
    }

    ListModel {
        id: connectionsModel
    }

    Component.onCompleted: {
        for (var i = 0; i < nodesData.length; i++) {
            nodesModel.append(nodesData[i])
        }
        for (var j = 0; j < connectionsData.length; j++) {
            connectionsModel.append(connectionsData[j])
        }
    }

    Repeater {
        model: nodesModel
        delegate: FlowNode {
            z:1
            nodeId: model.id
            text: model.text
            x: model.x
            y: model.y
            textColor: model.status === 1 ? "white" : "black"
            bgColor: model.status === 1 ? "orange" : model.status === 2 ? "green" : model.status === 3 ? "red" : "white"
            radius: model.type === "plc" ? 0 :20

            // 这是最神奇的隐式绑定!!!!!!!!
            // 子节点的Signal名称为 evtAddChild
            // 在这里的调用名称改为 onEvtAddChild
            onEvtAddChild :{
                if (!editable) {
                    evtAny({code: -1, type:"add_child", msg: "非管理员无法编辑流程!",data: null})
                } else {
                    evtAny({code: 0, type:"add_child", msg: "接受请求",data: model.id})
                }
            }

            onEvtDelSelf :{
                if (!editable) {
                    evtAny({code: -1, type:"del_self", msg: "非管理员无法编辑流程!",data: null})
                } else {
                    evtAny({code: 0, type:"del_self", msg: "接受请求",data: model.id})
                }
            }

            onEvtSetChild :{
                if (!editable) {
                    evtAny({code: -1, type:"set_child", msg: "非管理员无法编辑流程!",data: null})
                } else {
                    evtAny({code: 0, type:"set_child", msg: "接受请求",data: model.id})
                }
            }

            onEvtDoubleClick:{
                if (!editable) {
                    evtAny({code: -1, type:"edit_self", msg: "非管理员无法编辑流程!",data: null})
                } else {
                    evtAny({code: 0, type:"edit_self", msg: "接受请求",data: model.id})
                }
            }

            onEvtMove: {
                if (editable) {
                    evtAny({code: 0, type: "move", msg: "接受请求", data: {id: nodeId, x: x, y: y}})
                }
            }
            
            Component.onCompleted: {
                canvas.nodes[nodeId] = this
                // console.log("Node added:", nodeId, this)
            }
        }
    }

Repeater {
    model: connectionsModel
    delegate: Shape {
        z:0
        id: connectionShape
        property string from: model.from
        property string to: model.to
        
        // Calculate best connection points based on relative positions
        property bool isToBelow: canvas.nodes[to].y > canvas.nodes[from].y
        property bool isToAbove: canvas.nodes[to].y < canvas.nodes[from].y
        property bool isToRight: canvas.nodes[to].x > canvas.nodes[from].x
        property bool isToLeft: canvas.nodes[to].x < canvas.nodes[from].x
        property bool isXFarAway: Math.abs(canvas.nodes[to].x - canvas.nodes[from].x) > 100
        property bool isYFarAway: Math.abs(canvas.nodes[to].y - canvas.nodes[from].y) > 100
        
        // Select optimal connection points
        property real fromX: isToRight ? 
                            isXFarAway ? canvas.nodes[from].rightX : canvas.nodes[from].bothX : 
                            isXFarAway ? canvas.nodes[from].leftX : canvas.nodes[from].bothX
                            
        property real fromY: isToBelow ? 
                            isYFarAway ? canvas.nodes[from].bottomY : canvas.nodes[from].bothY : 
                            isYFarAway ? canvas.nodes[from].topY : canvas.nodes[from].bothY
        
        property real toX: isToRight ? 
                            isXFarAway ? canvas.nodes[to].leftX : canvas.nodes[to].bothX : 
                            isXFarAway ? canvas.nodes[to].rightX : canvas.nodes[to].bothX

        property real toY: isToBelow ? 
                            isYFarAway ? canvas.nodes[to].topY : canvas.nodes[to].bothY : 
                            isYFarAway ? canvas.nodes[to].bottomY : canvas.nodes[to].bothY
        
        // Midpoint for horizontal-vertical routing
        property real midX: (fromX + toX) / 2
        property real midY: (fromY + toY) / 2
        
        // First segment from source node
        ShapePath {
            strokeColor: "#5f5c5c"
            strokeWidth: 2
            startX: fromX
            startY: fromY
            
            PathLine {
                x: isToBelow || isToAbove ? fromX : midX
                y: isToBelow || isToAbove ? midY : fromY
            }
        }
        
        // Middle segment (horizontal or vertical)
        ShapePath {
            strokeColor: "#5f5c5c"
            strokeWidth: 2
            startX: isToBelow || isToAbove ? fromX : midX
            startY: isToBelow || isToAbove ? midY : fromY
            
            PathLine {
                x: isToBelow || isToAbove ? toX : midX
                y: isToBelow || isToAbove ? midY : toY
            }
        }
        
        // Final segment to target node
        ShapePath {
            strokeColor: "#5f5c5c"
            strokeWidth: 2
            startX: isToBelow || isToAbove ? toX : midX
            startY: isToBelow || isToAbove ? midY : toY
            
            PathLine {
                x: toX
                y: toY
            }
        }
    }
}

}
