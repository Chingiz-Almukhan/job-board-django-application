let search = $("#id_search");
let url = 'api/vacancy?search='

let addVacancy = function (vacancy, container) {
    let link = $('#id_for_link').val()
    container.append(
        `<a href="/${link}/${vacancy.id}">
            <div class="card-body">
                <h5 class="card-title">${vacancy.name}</h5>
                <p>${vacancy.category}</p>
                <p class="salary_text">${vacancy.salary} KZT</p>
                <p>Компания:
                    <a class="company_title" href="/auth/profile/${vacancy.author}">
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