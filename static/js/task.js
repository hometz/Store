/*class Vacancy {
    constructor(profession, salary, phone) {
        this.profession = profession;
        this.salary = salary;
        this.phone = phone;
    }

    getProfession() {
        return this.profession;
    }

    setProfession(profession) {
        this.profession = profession;
    }

    getSalary() {
        return this.salary;
    }

    setSalary(salary) {
        this.salary = salary;
    }

    getPhone() {
        return this.phone;
    }

    setPhone(phone) {
        this.phone = phone;
    }

    addVacancy() {
        const profession = document.getElementById('profession').value;
        const salary = parseFloat(document.getElementById('salary').value);
        const phone = document.getElementById('phone').value;
        const newVacancy = new Vacancy(profession, salary, phone);
        vacancies.push(newVacancy);
        this.displayVacancies();
    }

    displayVacancies() {
        const list = document.getElementById('vacancy-list');
        list.innerHTML = '';
        vacancies.forEach(function(vacancy) {
            const li = document.createElement('li');
            li.textContent = `Профессия: ${vacancy.getProfession()}, Зарплата: ${vacancy.getSalary()}, Телефон: ${vacancy.getPhone()}`;
            list.appendChild(li);
        });
    }

    displayHighestPaidJobs() {
        const avgSalary = vacancies.reduce((sum, vacancy) => sum + vacancy.getSalary(), 0) / vacancies.length;
        const highSalaryJobs = vacancies.filter(vacancy => vacancy.getSalary() > avgSalary);

        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = '';
        highSalaryJobs.forEach(function(vacancy) {
            const p = document.createElement('p');
            p.textContent = `Профессия: ${vacancy.getProfession()}, Зарплата: ${vacancy.getSalary()}, Телефон: ${vacancy.getPhone()}`;
            resultDiv.appendChild(p);
        });
    }
}

class AdvancedVacancy extends Vacancy {
    constructor(profession, salary, phone, location) {
        super(profession, salary, phone);
        this.location = location;
    }

    getLocation() {
        return this.location;
    }

    setLocation(location) {
        this.location = location;
    }

    displayVacancies() {
        const list = document.getElementById('vacancy-list');
        list.innerHTML = '';
        vacancies.forEach(function(vacancy) {
            const li = document.createElement('li');
            li.textContent = `Профессия: ${vacancy.getProfession()}, Зарплата: ${vacancy.getSalary()}, Телефон: ${vacancy.getPhone()}, Местоположение: ${vacancy.getLocation() || 'Не указано'}`;
            list.appendChild(li);
        });
    }

    displayVacanciesByLocation(location) {
        const filteredVacancies = vacancies.filter(vacancy => vacancy.getLocation() === location);

        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = '';
        filteredVacancies.forEach(function(vacancy) {
            const p = document.createElement('p');
            p.textContent = `Профессия: ${vacancy.getProfession()}, Зарплата: ${vacancy.getSalary()}, Телефон: ${vacancy.getPhone()}, Местоположение: ${vacancy.getLocation()}`;
            resultDiv.appendChild(p);
        });
    }
}

let vacancies = [];

document.getElementById('add-vacancy-btn').addEventListener('click', function() {
    const profession = document.getElementById('profession').value;
    const salary = parseFloat(document.getElementById('salary').value);
    const phone = document.getElementById('phone').value;
    const location = document.getElementById('location').value;

    const vacancy = new AdvancedVacancy(profession, salary, phone, location);
    vacancies.push(vacancy);
    vacancy.displayVacancies();
});

document.getElementById('show-high-paid-jobs-btn').addEventListener('click', function() {
    console.log('btn');
    const vacancy = new AdvancedVacancy();
    vacancy.displayHighestPaidJobs();
});

document.getElementById('show-vacancies-by-location-btn').addEventListener('click', function() {
    const location = document.getElementById('location').value;
    const vacancy = new AdvancedVacancy();
    vacancy.displayVacanciesByLocation(location);
});*/



function Vacancy(profession, salary, phone) {
    this.profession = profession;
    this.salary = salary;
    this.phone = phone;
}

Vacancy.prototype.getProfession = function() {
    return this.profession;
};

Vacancy.prototype.setProfession = function(profession) {
    this.profession = profession;
};

Vacancy.prototype.getSalary = function() {
    return this.salary;
};

Vacancy.prototype.setSalary = function(salary) {
    this.salary = salary;
};

Vacancy.prototype.getPhone = function() {
    return this.phone;
};

Vacancy.prototype.setPhone = function(phone) {
    this.phone = phone;
};

Vacancy.prototype.addVacancy = function() {
    const profession = document.getElementById('profession').value;
    const salary = parseFloat(document.getElementById('salary').value);
    const phone = document.getElementById('phone').value;
    const newVacancy = new Vacancy(profession, salary, phone);
    vacancies.push(newVacancy);
    this.displayVacancies();
};

Vacancy.prototype.displayVacancies = function() {
    const list = document.getElementById('vacancy-list');
    list.innerHTML = '';
    vacancies.forEach(function(vacancy) {
        const li = document.createElement('li');
        li.textContent = `Профессия: ${vacancy.getProfession()}, Зарплата: ${vacancy.getSalary()}, Телефон: ${vacancy.getPhone()}`;
        list.appendChild(li);
    });
};

Vacancy.prototype.displayHighestPaidJobs = function() {
    const avgSalary = vacancies.reduce((sum, vacancy) => sum + vacancy.getSalary(), 0) / vacancies.length;
    const highSalaryJobs = vacancies.filter(vacancy => vacancy.getSalary() > avgSalary);

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '';
    highSalaryJobs.forEach(function(vacancy) {
        const p = document.createElement('p');
        p.textContent = `Профессия: ${vacancy.getProfession()}, Зарплата: ${vacancy.getSalary()}, Телефон: ${vacancy.getPhone()}`;
        resultDiv.appendChild(p);
    });
};

function AdvancedVacancy(profession, salary, phone, location) {
    Vacancy.call(this, profession, salary, phone);
    this.location = location;
}

AdvancedVacancy.prototype = Object.create(Vacancy.prototype);
AdvancedVacancy.prototype.constructor = AdvancedVacancy;

AdvancedVacancy.prototype.getLocation = function() {
    return this.location;
};

AdvancedVacancy.prototype.setLocation = function(location) {
    this.location = location;
};

AdvancedVacancy.prototype.displayVacancies = function() {
    const list = document.getElementById('vacancy-list');
    list.innerHTML = '';
    vacancies.forEach(function(vacancy) {
        const li = document.createElement('li');
        li.textContent = `Профессия: ${vacancy.getProfession()}, Зарплата: ${vacancy.getSalary()}, Телефон: ${vacancy.getPhone()}, Местоположение: ${vacancy.getLocation() || 'Не указано'}`;
        list.appendChild(li);
    });
};

AdvancedVacancy.prototype.displayVacanciesByLocation = function(location) {
    const filteredVacancies = vacancies.filter(vacancy => vacancy.getLocation() === location);

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '';
    filteredVacancies.forEach(function(vacancy) {
        const p = document.createElement('p');
        p.textContent = `Профессия: ${vacancy.getProfession()}, Зарплата: ${vacancy.getSalary()}, Телефон: ${vacancy.getPhone()}, Местоположение: ${vacancy.getLocation()}`;
        resultDiv.appendChild(p);
    });
};

let vacancies = [];

document.getElementById('add-vacancy-btn').addEventListener('click', function() {
    const profession = document.getElementById('profession').value;
    const salary = parseFloat(document.getElementById('salary').value);
    const phone = document.getElementById('phone').value;
    const location = document.getElementById('location').value;

    const vacancy = new AdvancedVacancy(profession, salary, phone, location);
    vacancies.push(vacancy);
    vacancy.displayVacancies();
});

document.getElementById('show-high-paid-jobs-btn').addEventListener('click', function() {
    const vacancy = new AdvancedVacancy();
    vacancy.displayHighestPaidJobs();
});

document.getElementById('show-vacancies-by-location-btn').addEventListener('click', function() {
    const location = document.getElementById('location').value;
    const vacancy = new AdvancedVacancy();
    vacancy.displayVacanciesByLocation(location);
});

