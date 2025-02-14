import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 300
    title: "Login Window"

    // 背景图
    Image {
        anchors.fill: parent
        source: "login.png"
        fillMode: Image.PreserveAspectFit
    }

    // 用户下拉列表
    ComboBox {
        id: userComboBox
        x: 50; y: 50
        width: 300

        // 示例用户列表
        model: ["User 1", "User 2", "User 3"]
    }

    // 密码输入框
    TextInput {
        id: passInput
        x: 50; y: 100
        width: 300
        echoMode: TextInput.Password
    }

    // 确定按钮
    Button {
        id: loginButton
        x: 50; y: 150
        text: "Login"
        width: 300
        onClicked: {
            console.log("User:", userComboBox.currentText())
            console.log("Password:", passInput.text)
            // 这里添加登录逻辑
        }
    }
}