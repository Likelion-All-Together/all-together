const hamburgerButtons = document.querySelectorAll('.hamburger-btn');
const modifyBoxes = document.querySelectorAll('.post-detail__write-comments-box-modify-box');

const hidden = 'hidden';

hamburgerButtons.forEach((hamburgerBtn, index) => {
    hamburgerBtn.addEventListener('click', function() {
        if(modifyBoxes[index].classList.contains(hidden)) {
            modifyBoxes[index].classList.remove(hidden);
        } else {
            modifyBoxes[index].classList.add(hidden);
        }
    })
});