import QtQuick 2.15
import QtQuick.Shapes 1.15

Shape {
    id: connection
    property real x1: 0
    property real y1: 0
    property real x2: 0
    property real y2: 0
    
    ShapePath {
        strokeColor: "black"
        strokeWidth: 2
        fillColor: "transparent"
        startX: x1
        startY: y1
        PathLine {
            x: x2
            y: y2
        }
    }
}