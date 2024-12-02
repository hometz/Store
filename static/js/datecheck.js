window.onload = function() {
    
    if (!localStorage.getItem("birthDateEntered")) {
        
        const birthDateInput = prompt("Введите вашу дату рождения (в формате YYYY-MM-DD):");

        if (birthDateInput) {
            const birthDate = new Date(birthDateInput);
            
            if (!birthDate.getTime()) {
                alert("Неверный формат даты. Пожалуйста, используйте формат YYYY-MM-DD.");
                return;
            }

            const today = new Date();
            const age = today.getFullYear() - birthDate.getFullYear();
            const month = today.getMonth() - birthDate.getMonth();
            if (month < 0 || (month === 0 && today.getDate() < birthDate.getDate())) {
                age--;
            }

            const daysOfWeek = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];
            const dayOfWeek = daysOfWeek[birthDate.getDay()];

            if (age >= 18) {
                alert(`Вы совершеннолетний. Дата рождения: ${birthDate.toLocaleDateString()} (${dayOfWeek})`);
            } else {
                alert("Вы несовершеннолетний, пожалуйста, получите разрешение родителей для использования сайта.");
            }

            localStorage.setItem("birthDateEntered", birthDateInput);
        } else {
            alert("Вы не ввели дату.");
        }
    }

    
};