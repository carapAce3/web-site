// Функция для отображения соответствующего контента
function showContent(contentId) {
    // Скрыть все контенты
    const contents = document.querySelectorAll('.content');
    contents.forEach(content => {
        content.classList.remove('active');
    });

    // Скрыть все изображения
    const images = document.querySelectorAll('.content-image');
    images.forEach(image => {
        image.style.display = 'none';
    });

    // Показать выбранный контент и изображение
    const selectedContent = document.getElementById(contentId);
    const selectedImage = document.getElementById(contentId + '-img');
    
    selectedContent.classList.add('active');
    if (selectedImage) {
        selectedImage.style.display = 'block';
    }
}

// Инициализация по умолчанию
document.addEventListener('DOMContentLoaded', function() {
    showContent('main');
});