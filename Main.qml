import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

ApplicationWindow {
    id: appWindow
    objectName: "appWindow"
    title: "QML Application"
    visible: true
    width: 800;
    height: 600;
    minimumWidth: mainRect.implicitWidth;
    minimumHeight: mainRect.implicitHeight;

    // Users {
    //     id: usersPage
    //     visible: false
    // }

    Login {
        id: loginPage
        function onLogin(){
          var usersPage = Qt.createQmlObject('Users { id: usersPage }', appWindow, 'Main.qml')
          mainRect.replace(usersPage);
          rowButtons.visible = true;
        }
    }

    ColumnLayout {
        anchors.fill: parent
        RowLayout {
            id: rowButtons
            visible: false
            Layout.preferredHeight: 40
            Layout.fillWidth: true
            Button {
                text: "Login"
                onClicked: {
                    mainRect.replace(loginPage)
                }
            }
            Button {
                text: "Users"
                onClicked: {
                    mainRect.replace(usersPage)
                }
            }
        }

        StackView {
            id: mainRect
            objectName: "mainRect"
            Layout.preferredHeight: parent.height - rowButtons.height
            Layout.fillWidth: true

            initialItem: loginPage
        }
    }
}
