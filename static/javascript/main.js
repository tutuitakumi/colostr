$(function(){

    $('#form').on('submit', function(e){
        $.ajax({
            data:{
                text: $("textarea").val()
            },
            type: 'POST',
            url: '/changeText'
        })
        .done(function(data){
            console.log(data)
            $("#result").empty()
            $("#result").append(
                `<p>${data}</p>`
            )
            document.getElementById('result').style.backgroundColor = `${data}`
        })
        e.preventDefault();
    })
})