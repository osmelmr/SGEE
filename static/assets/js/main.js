(function () {
  "use strict";

  // ==================== FUNCIONES DE UTILIDAD ====================

  /**
   * Selecciona un elemento del DOM.
   * @param {string} el - Selector del elemento.
   * @param {boolean} all - Si es true, selecciona todos los elementos que coincidan.
   * @returns {Element|NodeList} El elemento o lista de elementos encontrados.
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

  // ==================== VALIDACIÓN DE FORMULARIOS ====================

  /**
   * Muestra u oculta un mensaje de error para un campo
   * @param {HTMLElement} campo - Elemento input/select/textarea
   * @param {string} mensaje - Mensaje de error a mostrar (si está vacío, oculta el error)
   */
  function mostrarError(campo, mensaje) {
    const contenedor = campo.closest('.form-group');
    let errorElement = contenedor.querySelector('.error-validacion');
    
    if (mensaje) {
      if (!errorElement) {
        errorElement = document.createElement('div');
        errorElement.className = 'error-validacion text-danger mt-1 small';
        contenedor.appendChild(errorElement);
      }
      errorElement.textContent = mensaje;
      campo.classList.add('is-invalid');
      campo.classList.remove('is-valid');
    } else {
      if (errorElement) errorElement.remove();
      campo.classList.remove('is-invalid');
      campo.classList.add('is-valid');
    }
  }

  /**
   * Valida si los campos requeridos de un formulario están vacíos
   * @param {HTMLFormElement} form - Elemento del formulario a validar
   * @returns {boolean} - True si todos los campos requeridos están llenos
   */
  function validarCamposVacios(form) {
    let valido = true;
    const camposRequeridos = form.querySelectorAll('[required]');
    
    camposRequeridos.forEach(campo => {
      if (campo.disabled || campo.readOnly) return;
      
      if (!campo.value.trim()) {
        mostrarError(campo, 'Este campo es obligatorio');
        valido = false;
      } else {
        mostrarError(campo, '');
      }
    });
    
    return valido;
  }

  // ==================== VALIDACIONES ESPECÍFICAS PARA ESTRATEGIA EDUCATIVA ====================

  function validarCurso() {
    const campo = document.getElementById('curso');
    if (!campo) return true; // No está en esta página
    
    const valor = campo.value;
    const regex = /^[0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]*$/;
    
    if (valor && !regex.test(valor)) {
      mostrarError(campo, 'El curso solo puede contener números y caracteres especiales');
      return false;
    } else {
      mostrarError(campo, '');
      return true;
    }
  }

  function validarAnoEscolar() {
    const campo = document.getElementById('ano-escolar');
    if (!campo) return true;
    
    const valor = campo.value;
    const regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
    
    if (valor && !regex.test(valor)) {
      mostrarError(campo, 'El año escolar solo puede contener letras');
      return false;
    } else {
      mostrarError(campo, '');
      return true;
    }
  }

  function validarGrupo() {
    const campo = document.getElementById('grupo');
    if (!campo) return true;
    
    const valor = campo.value;
    const regex = /^ID[A-Z]{2,}\d{3}$/;
    
    if (valor && !regex.test(valor)) {
      mostrarError(campo, 'Debe comenzar con "ID" en mayúsculas, seguido de 2+ letras y 3 números');
      return false;
    } else {
      mostrarError(campo, '');
      return true;
    }
  }

  function validarAutor() {
    const campo = document.getElementById('autor');
    if (!campo) return true;
    
    const valor = campo.value;
    const regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
    
    if (valor && !regex.test(valor)) {
      mostrarError(campo, 'No puede contener números ni caracteres especiales');
      return false;
    } else {
      mostrarError(campo, '');
      return true;
    }
  }

  // ==================== CONFIGURACIÓN DE VALIDACIONES ====================

  function configurarValidacionEstrategia() {
    const formEstrategia = document.getElementById('form-estrategia');
    if (!formEstrategia) return;

    // Configurar eventos para validaciones específicas
    const configurarValidacionCampo = (id, validacionFn) => {
      const campo = document.getElementById(id);
      if (campo) {
        campo.addEventListener('input', validacionFn);
        campo.addEventListener('blur', validacionFn);
      }
    };

    configurarValidacionCampo('curso', validarCurso);
    configurarValidacionCampo('ano-escolar', validarAnoEscolar);
    configurarValidacionCampo('grupo', validarGrupo);
    configurarValidacionCampo('autor', validarAutor);

    // Validación al enviar el formulario
    formEstrategia.addEventListener('submit', function(e) {
      const valido = validarCamposVacios(this) && 
                    validarCurso() && 
                    validarAnoEscolar() && 
                    validarGrupo() && 
                    validarAutor();
      
      if (!valido) {
        e.preventDefault();
        const primerError = this.querySelector('.is-invalid');
        if (primerError) {
          primerError.focus();
          primerError.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }
    });
  }

  // ==================== FUNCIONALIDADES GENERALES ====================

  /**
   * Cambia el estilo del header al hacer scroll.
   * Añade la clase 'header-scrolled' cuando el scroll supera 100px.
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
   * Se activa cuando el scroll supera 100px.
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
   * Cambia entre iconos de menú (bi-list) y cerrar (bi-x).
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
   * Solo funciona cuando la navegación está en modo móvil.
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

  // ==================== COMPONENTES INTERACTIVOS ====================

  /**
   * Configura los indicadores del carrusel hero.
   * Crea los puntos de navegación para cada slide del carrusel.
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
   * Inicializa el slider de la galería con Swiper.
   * Configura autoplay, paginación y responsive breakpoints.
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

  // ==================== ANIMACIONES ====================

  /**
   * Verifica la visibilidad de elementos con animaciones al hacer scroll.
   * Añade la clase 'visible' cuando el elemento entra en la ventana visible.
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

  // Configura listeners para verificar visibilidad
  window.addEventListener("load", checkVisibility);
  window.addEventListener("scroll", checkVisibility);
  window.addEventListener("resize", checkVisibility);

  /**
   * Animación de habilidades (skills).
   * Usa Waypoint.js para activar la animación de barras de progreso cuando el elemento entra en vista.
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

  // ==================== FUNCIONALIDADES ESPECÍFICAS ====================

  /**
   * Funcionalidad de seleccionar todo en tablas.
   * Permite seleccionar/deseleccionar todos los checkboxes de una tabla.
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

      // Actualiza el icono del botón según el estado
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

      // Actualiza el botón cuando se cambian checkboxes individuales
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
   * Funcionalidad de formulario de encuestas.
   * Permite agregar/eliminar preguntas y validar el formulario.
   */
  const initFormularioEncuestas = () => {
    const agregarPreguntaBtn = select("#agregar-pregunta");
    const formCrearEncuesta = select("#form-crear-encuesta");

    if (agregarPreguntaBtn && formCrearEncuesta) {
      let contadorPreguntas = 1;

      // Agrega una nueva pregunta al formulario
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
        
        // Añade evento al botón de eliminar
        nuevaPregunta.querySelector('.btn-eliminar').addEventListener('click', function() {
          eliminarPregunta(this);
        });
      });

      // Elimina una pregunta del formulario
      window.eliminarPregunta = function(boton) {
        const pregunta = boton.closest('.pregunta');
        if (confirm('¿Estás seguro de que deseas eliminar esta pregunta?')) {
          pregunta.remove();
          reorganizarPreguntas();
        }
      };

      // Reorganiza las preguntas restantes después de eliminar una
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
    }
  };

  // ==================== INICIALIZACIÓN ====================

  /**
   * Inicializa todas las funcionalidades cuando el DOM está listo.
   */
  document.addEventListener("DOMContentLoaded", function() {
    // Funcionalidades generales
    configurarValidacionEstrategia();
    initSeleccionarTodo();
    initFormularioEncuestas();

    // Configuración de eventos para campos requeridos en todos los formularios
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
      const camposRequeridos = form.querySelectorAll('[required]');
      camposRequeridos.forEach(campo => {
        campo.addEventListener('blur', () => {
          if (!campo.value.trim()) {
            mostrarError(campo, 'Este campo es obligatorio');
          } else {
            mostrarError(campo, '');
          }
        });
      });
    });
  });

})();