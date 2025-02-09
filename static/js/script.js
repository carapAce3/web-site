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
    showContent('menu');
});
const reviewBtn = document.getElementById("review-btn");
const modal = document.getElementById("review-modal");
const close = document.getElementsByClassName("close")[0];

reviewBtn.onclick = () => modal.style.display = "block";
close.onclick = () => modal.style.display = "none";
window.onclick = (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
  }
};