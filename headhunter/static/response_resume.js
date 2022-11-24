let response_b = $('#response_resume');
let response_m = $('#responseModalResume');
response_b.on('click', function () {
    response_m[0].style.display = "block";
});

let resume_id = window.location.pathname.split("/").pop();
console.log(resume_id)
let closeResponseModalResume = document.getElementById('modalResponseResume')
closeResponseModalResume.onclick = function () {
    response_m[0].style.display = "none";
}

let send_response = $('#send_response')
send_response.on('click', function () {
    let vacancy_id = $('#select_resume').val()
    let message_input = $('#id_message').val()
    $.ajax({
        type: 'POST',
        url: '/vacancy/add/response/',
        data: {
            'vacancy': vacancy_id,
            'resume': resume_id,
            'message': message_input,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),

        },
        success: function () {
            alert('Ваш отклик добавлен!');
            response_modal[0].style.display = "none";
        },
        error: function () {
            alert('Вы уже оставляли отклик');
            response_modal[0].style.display = "none";
        }
    });
});
