import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Shapes 1.15

ApplicationWindow {
    id: window
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
        var nodes = nodesData
        for (var i = 0; i < nodes.length; i++) {
            nodesModel.append(nodes[i])
        }
        var connections = connectionsData
        for (var j = 0; j < connections.length; j++) {
            connectionsModel.append(connections[j])
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
                window.nodes[nodeId] = this
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
                startX: window.nodes[from].x + 50  // Center of node
                startY: window.nodes[from].y + 25
                PathLine {
                    x: window.nodes[to].x + 50
                    y: window.nodes[to].y + 25
                }
            }
        }
    }
}