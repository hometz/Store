// Функция для обновления обратного отсчета
function updateCountdown() {
    // Получаем текущее время и оставшееся время из localStorage
    let endTime = localStorage.getItem('endTime');

    // Если еще нет времени окончания, устанавливаем его (через 1 час)
    if (!endTime) {
        endTime = Date.now() + 60 * 60 * 1000; // 1 час от текущего времени
        localStorage.setItem('endTime', endTime);
    }

    // Расчет оставшегося времени
    const remainingTime = endTime - Date.now();

    if (remainingTime <= 0) {
        document.getElementById('countdown').textContent = "Время вышло!";
        localStorage.removeItem('endTime'); // Очистить таймер по завершении
    } else {
        const hours = Math.floor(remainingTime / (1000 * 60 * 60));
        const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

        // Обновление отображаемого времени
        document.getElementById('countdown').textContent = 
            `${hours}ч ${minutes}м ${seconds}с`;

        // Обновляем каждый 1 секунду
        setTimeout(updateCountdown, 1000);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    console.log('aaaddddd');
    updateCountdown();
});