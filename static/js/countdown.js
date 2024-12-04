
function updateCountdown() {
   
    let endTime = localStorage.getItem('endTime');

    
    if (!endTime) {
        endTime = Date.now() + 60 * 60 * 1000;
        localStorage.setItem('endTime', endTime);
    }

    
    const remainingTime = endTime - Date.now();

    if (remainingTime <= 0) {
        document.getElementById('countdown').textContent = "Время вышло!";
        localStorage.removeItem('endTime');
    } else {
        const hours = Math.floor(remainingTime / (1000 * 60 * 60));
        const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

        
        document.getElementById('countdown').textContent = 
            `${hours}ч ${minutes}м ${seconds}с`;

        setTimeout(updateCountdown, 1000);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    console.log('aaaddddd');
    updateCountdown();
});