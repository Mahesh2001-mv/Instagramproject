function openModal(imageSrc) {
    const modal = document.getElementById('post-modal');
    const modalImage = document.getElementById('modal-image');
    modal.style.display = 'block';
    modalImage.src = imageSrc;
}

function closeModal() {
    const modal = document.getElementById('post-modal');
    modal.style.display = 'none';
}

window.onclick = function(event) {
    const modal = document.getElementById('post-modal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const likeButton = document.getElementById('like-button');
    const likeCount = document.getElementById('like-count');
    let likes = 0;
    let isLiked = false;

    likeButton.addEventListener('click', () => {
        if (isLiked) {
            likes--;
            likeButton.src = 'like-icon.png'; // Change back to the default icon
        } else {
            likes++;
            likeButton.src = 'liked-icon.png'; // Change to the liked icon
        }
        isLiked = !isLiked;
        likeCount.textContent = likes;
    });
});
