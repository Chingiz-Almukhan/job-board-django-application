window.addEventListener('load', function() {
    let reg_button = $('#register_button');
    let log_button = $('#login_button');
    let register = $('#registerModal');
    let login = $('#loginModal');
    // let form = $('.modal-content');
    reg_button.on('click', function() {
        register[0].style.display = "block";
    });
    log_button.on('click', function() {
        login[0].style.display = "block";
    });
    });

let registerModal = document.getElementById('registerModal')
let closeRegister = document.getElementById('modalRegisterClose')
closeRegister.onclick = function() {
    registerModal.style.display = "none";
  }

let loginModal = document.getElementById('loginModal')
let closeLogin = document.getElementById('closeLogin')
closeLogin.onclick = function() {
    loginModal.style.display = "none";
  }


let employer = document.getElementById('id_user_role_0')
let applicant = document.getElementById('id_user_role_1')

let nameLabel = document.getElementsByClassName('form-label')[0]

employer.onclick = function () {
    nameLabel.textContent = 'Название компании'
}

applicant.onclick = function () {
    nameLabel.textContent = 'Имя'
}
