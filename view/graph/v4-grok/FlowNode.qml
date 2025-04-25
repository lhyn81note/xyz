import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Shapes 1.15

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

    signal evtAddChild(string nodeId)
    signal evtDelSelf(string nodeId)
    signal evtDelChildren(string nodeId)
    signal evtDoubleClick(string nodeId)

    Text {
        anchors.centerIn: parent
        text: node.text
    }

    MouseArea {
        anchors.fill: parent
        acceptedButtons: Qt.LeftButton
        property real startX
        property real startY

        onDoubleClicked: function(mouse) {
            if (mouse.button === Qt.LeftButton) {
                node.evtDoubleClick(node.nodeId); // Emit signal on double-click
            }
        }

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
            } else if (mouse.button === Qt.RightButton) {
                node.Clicked(nodeId); // Emit signal on right-click
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

    Menu {
        id: contextMenu
        MenuItem {
            text: "添加下一指令"
            onTriggered: evtAddChild(node.nodeId)
        }
        MenuItem {
            text: "删除本条指令"
            onTriggered: evtDelSelf(node.nodeId)
        }
        MenuItem {
            text: "删除指令链"
            onTriggered: evtDelChildren(node.nodeId)
        }
    }

    MouseArea {
        anchors.fill: parent
        acceptedButtons: Qt.RightButton

        onClicked: function(mouse) {
            if (mouse.button === Qt.RightButton) {
                contextMenu.open(); // Open context menu on right-click
            }
        }
    }
}