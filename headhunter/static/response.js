let response_button = $('#response_button');
let response_modal = $('#responseModal');
response_button.on('click', function () {
    response_modal[0].style.display = "block";
});

let vacancy_id = window.location.pathname.split("/").pop();
let closeResponseModal = document.getElementById('modalResponse')
closeResponseModal.onclick = function () {
    response_modal[0].style.display = "none";
}

let send_response = $('#send_response')
send_response.on('click', function () {
    let resume_id = $('#select_resume').val()
    let message_input = $('#id_message').val()
    $.ajax({
        type: 'POST',
        url: 'add/response/',
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


