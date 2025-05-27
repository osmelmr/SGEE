document.addEventListener('DOMContentLoaded', function() {
  const steps = Array.from(document.querySelectorAll('.form-step'));
  const btnNext = document.querySelector('.btn-next');
  const btnPrev = document.querySelector('.btn-prev');
  const btnRegistrar = document.querySelector('.btn-registrar');
  let currentStep = 0;

  function showStep(index) {
    steps.forEach((step, i) => {
      step.style.display = i === index ? 'block' : 'none';
    });

    // Mostrar/ocultar botones según el paso
    if (index === 0) {
      btnNext.style.display = 'inline-block';
      btnRegistrar.style.display = 'none';
      btnPrev.style.visibility = 'hidden'; // Oculto pero mantiene el espacio
    } else if (index === steps.length - 1) {
      btnNext.style.display = 'none';
      btnRegistrar.style.display = 'inline-block';
      btnPrev.style.visibility = 'visible';
    } else {
      btnNext.style.display = 'inline-block';
      btnRegistrar.style.display = 'none';
      btnPrev.style.visibility = 'visible';
    }
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