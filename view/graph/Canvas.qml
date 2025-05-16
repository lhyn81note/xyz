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
            id: connectionShape
            property string from: model.from
            property string to: model.to

            ShapePath {
                strokeColor: "#5f5c5c"
                strokeWidth: 2
                startX: canvas.nodes[from].x + canvas.nodes[from].width/2  // Center of node
                startY: canvas.nodes[from].y + canvas.nodes[from].height
                PathLine {
                    x: canvas.nodes[to].x + canvas.nodes[to].width/2
                    y: canvas.nodes[to].y
                }
            }
        }
    }
}