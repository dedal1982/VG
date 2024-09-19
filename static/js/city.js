document.addEventListener('DOMContentLoaded', function() {

    const cityDiv = document.querySelector('.categories__city');
    if (cityDiv) {
        const city = localStorage.getItem('selectedCity');
        if (city) {
            cityDiv.textContent = city;
        }
    }

    // const categoryLinks = document.querySelectorAll('.categories__link');
    // const bannerSets = document.querySelectorAll('.banner__user');
    // const pageCnt = document.querySelector('.page')

    // categoryLinks.forEach(link => {
    //     link.addEventListener('click', function(event) {
    //         event.preventDefault();
    //         const bannerSetId = this.getAttribute('data-banner');

    //         let hasActiveBanner = false;

    //         bannerSets.forEach(set => {
    //             if (set.id === bannerSetId) {
    //                 set.classList.add('active');
    //                 hasActiveBanner = true;
    //             } else {
    //                 set.classList.remove('active');
    //             }
    //         });

    //         if (hasActiveBanner) {
    //             pageCnt.classList.add('active');
    //         } else {
    //             pageCnt.classList.remove('active');
    //         }
    //     });
    // });
})