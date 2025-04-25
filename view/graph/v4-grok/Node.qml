import QtQuick 2.15

Rectangle {
    id: node
    width: 100
    height: 50
    color: "lightblue"
    border.color: "black"
    radius: 15

    property string nodeId: ""
    property string text: ""
    property bool dragging: false

    Text {
        anchors.centerIn: parent
        text: node.text
    }

    MouseArea {
        anchors.fill: parent
        acceptedButtons: Qt.LeftButton
        property real startX
        property real startY

        onPressed: function(mouse) {
            if (mouse.button === Qt.LeftButton) {
                var mousePos = mapToItem(node.parent, mouse.x, mouse.y); // Map mouse coordinates to node's parent
                startX = mousePos.x;
                startY = mousePos.y;
                dragging = true;
            }
        }

        onReleased: function(mouse) {
            if (mouse.button === Qt.LeftButton) {
                dragging = false;
            }
        }

        onPositionChanged: function(mouse) {
            if (dragging) {
                var mousePos = mapToItem(node.parent, mouse.x, mouse.y); // Map mouse coordinates to node's parent
                var dx = mousePos.x - startX;
                var dy = mousePos.y - startY;
                node.x += dx;
                node.y += dy;
                startX = mousePos.x;
                startY = mousePos.y;
            }
        }
    }
}