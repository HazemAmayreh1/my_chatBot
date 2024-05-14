function sendMessage(message) {
    $('<p><strong>You:</strong> ' + message + '</p>').appendTo('#chatbox');
    $.get("/get", { msg: message }).done(function(data) {
        $('<p><strong>Bot:</strong> ' + data.reply + '</p>').appendTo('#chatbox');
        $('#chatbox').scrollTop($('#chatbox')[0].scrollHeight);
    });
}
