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

            // 这是最神奇的隐式绑定!!!!!!!!
            // 子节点的Signal名称为 evtAddChild
            // 在这里的调用名称改为 onEvtAddChild
            onEvtAddChild :{
                console.log("添加子节点:", nodeId, model.text)
            }

            onEvtDelSelf :{
                console.log("删除节点:", nodeId, model.text)
            }

            onEvtDelChildren :{
                console.log("删除子节点:", nodeId, model.text)
            }

            onEvtDoubleClick:{
                console.log("双击节点:", nodeId, model.text)
            }
            
            
            Component.onCompleted: {
                canvas.nodes[nodeId] = this
                console.log("Node added:", nodeId, this)
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
                strokeColor: "black"
                strokeWidth: 2
                startX: canvas.nodes[from].x + 50  // Center of node
                startY: canvas.nodes[from].y + 50
                PathLine {
                    x: canvas.nodes[to].x + 50
                    y: canvas.nodes[to].y
                }
            }
        }
    }
}