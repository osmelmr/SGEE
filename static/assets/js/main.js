(function () {
  "use strict";

  /**
   * Selecciona un elemento del DOM.
   * @param {string} el - Selector del elemento.
   * @param {boolean} all - Si es true, selecciona todos los elementos que coincidan.
   * @returns {Element|NodeList}
   */
  const select = (el, all = false) => {
    el = el.trim();
    return all ? [...document.querySelectorAll(el)] : document.querySelector(el);
  };

  /**
   * Añade un event listener a un elemento.
   * @param {string} type - Tipo de evento (ej: 'click', 'scroll').
   * @param {string} el - Selector del elemento.
   * @param {Function} listener - Función a ejecutar en el evento.
   * @param {boolean} all - Si es true, añade el listener a todos los elementos que coincidan.
   */
  const on = (type, el, listener, all = false) => {
    const selectEl = select(el, all);
    if (selectEl) {
      if (all) selectEl.forEach((e) => e.addEventListener(type, listener));
      else selectEl.addEventListener(type, listener);
    }
  };

  /**
   * Añade un event listener para el evento scroll.
   * @param {Element} el - Elemento al que se añade el listener.
   * @param {Function} listener - Función a ejecutar en el evento scroll.
   */
  const onscroll = (el, listener) => {
    el.addEventListener("scroll", listener);
  };

  // ==================== FUNCIONALIDADES GENERALES ====================

  /**
   * Añade la clase 'header-scrolled' al header cuando se hace scroll.
   */
  const header = select("#header");
  if (header) {
    const headerScrolled = () => {
      header.classList.toggle("header-scrolled", window.scrollY > 100);
    };
    window.addEventListener("load", headerScrolled);
    onscroll(document, headerScrolled);
  }

  /**
   * Muestra u oculta el botón "Back to Top" según la posición del scroll.
   */
  const backToTop = select(".back-to-top");
  if (backToTop) {
    const toggleBackToTop = () => {
      backToTop.classList.toggle("active", window.scrollY > 100);
    };
    window.addEventListener("load", toggleBackToTop);
    onscroll(document, toggleBackToTop);
  }

  /**
   * Alternar la navegación móvil.
   */
  on("click", ".mobile-nav-toggle", function (e) {
    const navbar = select("#navbar");
    if (navbar) {
      navbar.classList.toggle("navbar-mobile");
      this.classList.toggle("bi-list");
      this.classList.toggle("bi-x");
    }
  });

  /**
   * Activar dropdowns en la navegación móvil.
   */
  on(
    "click",
    ".navbar .dropdown > a",
    function (e) {
      const navbar = select("#navbar");
      if (navbar && navbar.classList.contains("navbar-mobile")) {
        e.preventDefault();
        if (this.nextElementSibling) {
          this.nextElementSibling.classList.toggle("dropdown-active");
        }
      }
    },
    true
  );

  /**
   * Indicadores del carrusel hero.
   */
  const heroCarouselIndicators = select("#hero-carousel-indicators");
  const heroCarouselItems = select('#heroCarousel .carousel-item', true);

  if (heroCarouselIndicators && heroCarouselItems) {
    heroCarouselItems.forEach((item, index) => {
      (index === 0) ?
      heroCarouselIndicators.innerHTML += "<li data-bs-target='#heroCarousel' data-bs-slide-to='" + index + "' class='active'></li>":
        heroCarouselIndicators.innerHTML += "<li data-bs-target='#heroCarousel' data-bs-slide-to='" + index + "'></li>"
    });
  }

  /**
   * Inicializar el slider de la galería.
   */
  const gallerySlider = select(".gallery-slider");
  if (gallerySlider) {
    new Swiper(gallerySlider, {
      speed: 400,
      loop: true,
      centeredSlides: true,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
      slidesPerView: "auto",
      pagination: {
        el: ".swiper-pagination",
        type: "bullets",
        clickable: true,
      },
      breakpoints: {
        320: {
          slidesPerView: 1,
          spaceBetween: 20,
        },
        640: {
          slidesPerView: 3,
          spaceBetween: 20,
        },
        992: {
          slidesPerView: 5,
          spaceBetween: 20,
        },
      },
    });
  }

  /**
   * Verificar visibilidad de elementos con animaciones al hacer scroll.
   */
  const checkVisibility = () => {
    const elements = document.querySelectorAll(
      ".fade-in, .slide-in-left, .slide-in-right, .fade-in-up, .rotate-in, .scale-in, .gallery-slide-in, .gallery-scale-in, .footer-fade-in"
    );
    elements.forEach((element) => {
      const elementTop = element.getBoundingClientRect().top;
      const elementBottom = element.getBoundingClientRect().bottom;
      const delay = element.getAttribute("data-delay") || 0;

      if (elementTop < window.innerHeight && elementBottom >= 0) {
        setTimeout(() => element.classList.add("visible"), delay);
      }
    });
  };

  window.addEventListener("load", checkVisibility);
  window.addEventListener("scroll", checkVisibility);
  window.addEventListener("resize", checkVisibility);

  /**
   * Animación de habilidades (skills).
   */
  const skillsContent = select(".skills-content");
  if (skillsContent) {
    new Waypoint({
      element: skillsContent,
      offset: "80%",
      handler: function (direction) {
        const progressBars = select(".progress .progress-bar", true);
        progressBars.forEach((el) => {
          el.style.width = el.getAttribute("aria-valuenow") + "%";
        });
      },
    });
  }
 /**
   * Funcionalidad de seleccionar todo en tablas
   */
  const initSeleccionarTodo = () => {
    const btnSeleccionarTodo = select("#btn-seleccionar-todo");
    const checkboxes = document.querySelectorAll(".seleccionar-fila");

    if (btnSeleccionarTodo && checkboxes.length > 0) {
      btnSeleccionarTodo.addEventListener("click", function () {
        const isChecked = !btnSeleccionarTodo.classList.contains("active");
        checkboxes.forEach((checkbox) => checkbox.checked = isChecked);
        btnSeleccionarTodo.classList.toggle("active", isChecked);
        updateIcon();
      });

      function updateIcon() {
        const icon = btnSeleccionarTodo.querySelector("i");
        if (btnSeleccionarTodo.classList.contains("active")) {
          icon.classList.remove("bi-check-all");
          icon.classList.add("bi-x-circle");
        } else {
          icon.classList.remove("bi-x-circle");
          icon.classList.add("bi-check-all");
        }
      }

      checkboxes.forEach((checkbox) => {
        checkbox.addEventListener("change", function () {
          const allChecked = Array.from(checkboxes).every((cb) => cb.checked);
          btnSeleccionarTodo.classList.toggle("active", allChecked);
          updateIcon();
        });
      });
    }
  };

  /**
   * Funcionalidad de formulario de encuestas
   */
  const initFormularioEncuestas = () => {
    const agregarPreguntaBtn = select("#agregar-pregunta");
    const formCrearEncuesta = select("#form-crear-encuesta");

    if (agregarPreguntaBtn && formCrearEncuesta) {
      let contadorPreguntas = 1;

      agregarPreguntaBtn.addEventListener('click', function() {
        contadorPreguntas++;
        const preguntasContainer = select("#preguntas-encuesta");

        const nuevaPregunta = document.createElement('div');
        nuevaPregunta.classList.add('pregunta', 'mb-3', 'p-3', 'border', 'rounded');
        nuevaPregunta.innerHTML = `
          <div class="form-group">
              <label for="pregunta${contadorPreguntas}">Pregunta ${contadorPreguntas}</label>
              <input type="text" id="pregunta${contadorPreguntas}" name="pregunta${contadorPreguntas}" class="form-control" required>
          </div>
          <div class="text-right">
              <button type="button" class="btn btn-danger btn-sm btn-eliminar">
                  <i class="bi bi-trash"></i> Eliminar
              </button>
          </div>
        `;
        preguntasContainer.appendChild(nuevaPregunta);
        
        nuevaPregunta.querySelector('.btn-eliminar').addEventListener('click', function() {
          eliminarPregunta(this);
        });
      });

      window.eliminarPregunta = function(boton) {
        const pregunta = boton.closest('.pregunta');
        if (confirm('¿Estás seguro de que deseas eliminar esta pregunta?')) {
          pregunta.remove();
          reorganizarPreguntas();
        }
      };

      function reorganizarPreguntas() {
        const preguntas = document.querySelectorAll('.pregunta');
        preguntas.forEach((pregunta, index) => {
          const numeroPregunta = index + 1;
          pregunta.querySelector('label').textContent = `Pregunta ${numeroPregunta}`;
          const input = pregunta.querySelector('input');
          input.id = `pregunta${numeroPregunta}`;
          input.name = `pregunta${numeroPregunta}`;
        });
        contadorPreguntas = preguntas.length;
      }

      formCrearEncuesta.addEventListener('submit', async function (event) {
        event.preventDefault();
        let valido = true;

        if (!validarCamposVacios('form-crear-encuesta')) {
          mostrarError('Por favor complete todos los campos requeridos.');
          valido = false;
        }

        const tituloEncuesta = select('#titulo-encuesta');
        if (tituloEncuesta && !validarNombreApellido(tituloEncuesta.value, tituloEncuesta)) {
          valido = false;
        }

        if (!valido) return;

        try {
          const existeEncuesta = await verificarExistencia('/verificar-encuesta', { titulo: tituloEncuesta.value });
          if (existeEncuesta) {
            mostrarError('Ya existe una encuesta con ese título.', tituloEncuesta);
            return;
          }
          this.submit();
        } catch (error) {
          console.error('Error al verificar encuesta:', error);
          mostrarError('Error al verificar la encuesta. Intente nuevamente.');
        }
      });
    }
  };
  // Inicializar todas las funcionalidades
  document.addEventListener("DOMContentLoaded", function() {
    initSeleccionarTodo();
 });
})();