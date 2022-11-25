let search = $("#id_search");
let url = 'api/vacancy?search='

let addVacancy = function (vacancy, container) {
    container.append(
        `<a href="http://127.0.0.1:8000/vacancy/${vacancy.id}">
            <div class="card-body">
                <h5 class="card-title">${vacancy.name}</h5>
                <p class="salary_text">${vacancy.salary} KZT</p>
                <p>Компания:
                    <a class="company_title" href="http://127.0.0.1:8000//auth/profile/${vacancy.author}">
                        ${vacancy.author}
                    </a>
                </p>
                <p class="udated_vacancy mt-1">
                    Опубликовано: <span><b>${vacancy.updated_at}</b></span>
                </p>
            </div>
        </a>`
    )
};

renderResult = function (vacancies) {
    let vacancy_container = $("#vacancies");
    vacancy_container.empty();
    for (let vacancy of vacancies) {
      addVacancy(vacancy, vacancy_container);
    }
 };

let getVacancies = function () {
    let value = search.val()
    $.ajax({
        url: url + value
    }).done(
        function (data) {
            console.log(data)
            renderResult(data)
        }
    )
}

console.log(search);
search.on('keyup', getVacancies);