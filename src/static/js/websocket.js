// websocket scripts
console.log(window.location)
var loc=window.location
var formData=$("#form")
var msgInput=$("#id_message")
var chatHolder=$("#chat-items")
var me=$("#myUsername").val()

var wsStart='ws://'
if(loc.protocol=='https:'){
    wsStart='wss://'
}
var endpoint = wsStart + loc.host + loc.pathname

//var socket=new ReconnectingWebSocket(endpoint)
var socket=new ReconnectingWebSocket(endpoint)
//socket.debug = true;
//socket.timeoutInterval = 5400;
//automaticOpen=false

socket.onmessage=function(e){
    console.log("message",e)
console.log('data='+e.data)
    var chatDataMsg=JSON.parse(e.data)
    if(chatDataMsg.username===me){
        chatHolder.append("<li class=\"btn btn-secondary pull-right mr-4\">"+chatDataMsg.message+"</li><br><br>")//+" via "+chatDataMsg.username+
    }else{
        chatHolder.append("<li class=\"btn btn-primary pull-left ml-4\">"+chatDataMsg.message+"</li><br><br>")//+" via "+chatDataMsg.username+
    }

}
socket.onopen=function(e){
    console.log("open",e)
    formData.submit(function(event){
        event.preventDefault()
        var msgText=msgInput.val()
        if(msgText===""){
            console.log("Empty message due to multiple connected websockets in Background")
            console.log("Please Reload the page")
        }else{
            var finalData={
                'message': msgText
            }
            socket.send(JSON.stringify(finalData))
            formData[0].reset()
        }
    })
}
socket.onerror=function(e){
    console.log("error",e)

}
socket.onclose=function(e){
    console.log("close",e)

}