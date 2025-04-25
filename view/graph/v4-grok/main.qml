import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Shapes 1.15

ApplicationWindow {
    id: canvas
    visible: true
    width: 800
    height: 600
    title: "Tree Visualization"

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
        delegate: Node {
            nodeId: model.id
            text: model.text
            x: model.x
            y: model.y
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