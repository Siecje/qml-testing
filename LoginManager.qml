import QtQuick 2.3
import QtQuick.Controls 1.4
import QtQuick.Dialogs 1.2
import QtQuick.Layouts 1.1

Item {
    id: loginManager

    signal loginSuccess()
    signal loginFailure()

    signal serverNames(var serverNames)
    signal lastLogin(string login)
    signal lastServer(string server)

    Component.onCompleted: {
        loginManager.serverNames(['One', 'Two']);
    }
}
