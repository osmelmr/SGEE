let showStep;

document.addEventListener('DOMContentLoaded', function() {
  const steps = Array.from(document.querySelectorAll('.form-step'));
  const btnNext = document.querySelector('.btn-next');
  const btnPrev = document.querySelector('.btn-prev');
  const btnRegistrar = document.querySelector('.btn-registrar');
  let currentStep = 0;

  showStep = function(index) {
    steps.forEach((step, i) => {
      step.style.display = i === index ? 'block' : 'none';
    });
    if (index === 0) {
      btnNext.style.display = 'inline-block';
      btnRegistrar.style.display = 'none';
      btnPrev.style.visibility = 'hidden';
    } else if (index === steps.length - 1) {
      btnNext.style.display = 'none';
      btnRegistrar.style.display = 'inline-block';
      btnPrev.style.visibility = 'visible';
    } else {
      btnNext.style.display = 'inline-block';
      btnRegistrar.style.display = 'none';
      btnPrev.style.visibility = 'visible';
    }
    currentStep = index;
  };

  if (btnNext) {
    btnNext.addEventListener('click', function() {
      if (currentStep < steps.length - 1) {
        showStep(currentStep + 1);
      }
    });
  }

  if (btnPrev) {
    btnPrev.addEventListener('click', function() {
      if (currentStep > 0) {
        showStep(currentStep - 1);
      }
    });
  }

  showStep(currentStep);
});

function getStepIndexOfElement(element) {
  const step = element.closest('.form-step');
  if (!step) return;
  const steps = Array.from(document.querySelectorAll('.form-step'));
  const index = steps.indexOf(step);
  if (typeof showStep === 'function' && index !== -1) {
    showStep(index);
  }
}