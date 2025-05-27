document.addEventListener('DOMContentLoaded', function() {
  const steps = Array.from(document.querySelectorAll('.form-step'));
  const btnNext = document.querySelector('.btn-next');
  const btnPrev = document.querySelector('.btn-prev');
  const btnSubmit = document.querySelector('.btn-submit');
  let currentStep = 0;

  function showStep(index) {
    steps.forEach((step, i) => {
      step.style.display = i === index ? 'block' : 'none';
    });
    btnPrev.style.display = index === 0 ? 'none' : 'inline-block';
    btnNext.style.display = index === steps.length - 1 ? 'none' : 'inline-block';
    btnSubmit.style.display = index === steps.length - 1 ? 'inline-block' : 'none';
  }

  btnNext.addEventListener('click', function() {
    if (currentStep < steps.length - 1) {
      currentStep++;
      showStep(currentStep);
    }
  });

  btnPrev.addEventListener('click', function() {
    if (currentStep > 0) {
      currentStep--;
      showStep(currentStep);
    }
  });

  showStep(currentStep);
});