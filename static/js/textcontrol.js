document.addEventListener('DOMContentLoaded', () => {
    const toggleControls = document.getElementById('toggleControls');
    const controls = document.getElementById('controls');
    const fontSizeInput = document.getElementById('fontSize');
    const textColorInput = document.getElementById('textColor');
    const bgColorInput = document.getElementById('bgColor');

    toggleControls.addEventListener('change', () => {
        controls.style.display = toggleControls.checked ? 'block' : 'none';
    });

    fontSizeInput.addEventListener('input', () => {
        document.body.style.fontSize = `${fontSizeInput.value}px`;
    });

    textColorInput.addEventListener('input', () => {
        document.body.style.color = textColorInput.value;
    });

    bgColorInput.addEventListener('input', () => {
        document.body.style.backgroundColor = bgColorInput.value;
    });
});