import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.0

import "login.js" as App

Item {
    id: loginPage
    objectName: "loginPage"
    width: 800;
    height: 600;
    anchors.fill: parent;
    
    ListModel {
        id: serverModel
        objectName: "serverModel"
        function add(name){
            serverModel.append({
                                "text": name,
                               })
        }
    }
    
    ColumnLayout {
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        anchors.margins: 3
        spacing: 3
        Column {
            spacing: 20
            anchors.horizontalCenter: parent.horizontalCenter
            
            ComboBox {
                id: cmbServers
                objectName: "cmbServers"
                model: serverModel
            }
            
            TextField {
                id: login
                objectName: "login"
                placeholderText: qsTr("Login")
                focus: true
                Layout.fillWidth: true
                onAccepted: {
                    btnSubmit.clicked()
                }
            }
            
            TextField {
                id: password
                objectName: "password"
                placeholderText: qsTr("Password")
                echoMode: TextInput.Password
                Layout.fillWidth: true
                onAccepted: {
                    btnSubmit.clicked()
                }
            }
            
            Button {
                id: btnSubmit
                objectName: "btnSubmit"
                text: qsTr("Login")
                Layout.fillWidth: true
                onClicked: {
                    App.submitLogin();
                }
            }
            
            Label {
                id: error
                objectName: "error"
                Layout.fillWidth: true
            }
        }
    }
    Component.onCompleted: {
        App.onLoad();
    }
}
