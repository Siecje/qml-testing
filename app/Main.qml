import QtQuick 2.3
import QtQuick.Controls 1.4

ApplicationWindow {
    id: appWindow
    objectName: "appWindow"
    visible: true
    width: 800;
    height: 600;
    
    Rectangle {
        id: mainRect
        objectName: "mainRect"
        anchors.fill: parent
        Loader {
            id: pageLoader
            objectName: "pageLoader"
            focus: true
            anchors.fill: parent
        }
        state: "login"
        states: [
            State {
                name: "login"
                PropertyChanges { target: pageLoader; source: "Login.qml"; }
            },
            State {
                name: "app"
                PropertyChanges { target: pageLoader; source: "Users.qml"; }
            }
        ]
    }
}
