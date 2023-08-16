
  (function() { // A   
    const itemWrapperEl = document.querySelector('.item-wrapper'),  
          leftBtnEl = document.getElementById('left-btn'),  
          rightBtnEl = document.getElementById('right-btn');  

    function moveSlides(direction) { // B
      const item = itemWrapperEl.querySelector('.item'),  
            itemMargin = parseFloat(getComputedStyle(item).marginRight);
            itemWidth = itemMargin + item.offsetWidth + 2; 

      let itemCount = Math.round(itemWrapperEl.scrollLeft / itemWidth); 

      if (direction === 'left') {
        itemCount = itemCount - 1;
      } else {
        itemCount = itemCount + 1;
      }
      itemWrapperEl.scrollLeft = itemWidth * itemCount; 
    }

    leftBtnEl.addEventListener("click", e => moveSlides("left")); // C
    rightBtnEl.addEventListener("click", e => moveSlides("right"));
  })();