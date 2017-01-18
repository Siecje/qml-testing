import QtQuick 2.7
import QtQuick.Controls 1.4
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

    Users {
        id: usersPage
        visible: false
    }

    Login {
        id: loginPage
    }

    ColumnLayout {
        anchors.fill: parent
        RowLayout {
            id: rowButtons
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
