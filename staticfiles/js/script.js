document.addEventListener('DOMContentLoaded', function () {

    const cityOpen =document.querySelector('.logo__link');
    const cityModal = document.querySelector('.city__popup');
    const cityBody = document.querySelector('.city__body');
    const cityTown = document.querySelector('.header__town');
    const cityButton= document.querySelector('.city__button')
  
    cityModal.addEventListener('click',(e)=>{
    if(e.target === cityBody || e.target.getAttribute('data-close') === '' || e.target === cityButton){
      closeModal()
    }
  })
  
    cityOpen.addEventListener("click", function(e) {
      showModal()
    });
  
  
  
    function showModal(){
        cityModal.classList.add('active')
        document.body.classList.add('block-scroll')
    }
  
    function closeModal(){
        cityModal.classList.remove('active')
        document.body.classList.remove('block-scroll')
    }
  
  
    let selectedCity = '';
  
      const selected = document.querySelector('.select-selected');
      const items = document.querySelector('.select-items');
      const itemElements = document.querySelectorAll('.select-item');
      const select = document.querySelector('.custom-select')
    
      selected.addEventListener('click', function () {
        items.classList.toggle('select-hide');
        select.classList.toggle('active');
      });
    
      itemElements.forEach(function (item) {
        item.addEventListener('click', function () {
          selected.textContent = this.textContent;
          selectedCity = selected.textContent
          items.classList.add('select-hide');
          select.classList.remove('active');
        });
      });
    
      document.addEventListener('click', function (event) {
        if (!event.target.closest('.custom-select')) {
          items.classList.add('select-hide');
          select.classList.remove('active');
  
        }
      });
  
      cityButton.addEventListener("click", function(e) {
        e.preventDefault();
          if (selectedCity) {
              localStorage.setItem('selectedCity', selectedCity);
              window.location.href = '/catalog/'; // change to your target page
          } else {
              alert('Вы не выбрали город');
          }
      });
  
    });