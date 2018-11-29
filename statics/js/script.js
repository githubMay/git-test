$(document).ready(function(){
    $("#login").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username":user, "password":pwd};
        $.ajax({
            type:"post",
            url:"/",
            data:pd,
            cache:false,
            success:function(data){
                $("body").html("<p>"+data+"</p>");
                window.location.href = "http://blog.csdn.net/yusirxiaer";
            },
            error:function(){
                alert("error!");
            },
        });
    });
});