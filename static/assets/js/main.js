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

    // Limpiar siempre que no haya mensaje o el campo esté vacío
    if (!mensaje || campo.value.trim() === '') {
      if (errorElement) errorElement.remove();
      campo.classList.remove('is-invalid', 'is-valid');
      
      // Si el campo está vacío y es requerido, mostrar error
      if (campo.required && campo.value.trim() === '') {
        errorElement = document.createElement('div');
        errorElement.className = 'error-validacion';
        errorElement.textContent = 'Este campo es obligatorio';
        contenedor.appendChild(errorElement);
        campo.classList.add('is-invalid');
      }
    } else {
      // Mostrar mensaje de error personalizado
      if (!errorElement) {
        errorElement = document.createElement('div');
        errorElement.className = 'error-validacion';
        contenedor.appendChild(errorElement);
      }
      errorElement.textContent = mensaje;
      campo.classList.add('is-invalid');
      campo.classList.remove('is-valid');
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
      }
    });
    
    return valido;
  }

  // ==================== VALIDACIONES PARA ESTRATEGIA EDUCATIVA ====================

  function validarCurso() {
    const campo = document.getElementById('curso');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    const regex = /^[0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]*$/;
    if (!regex.test(valor)) {
      mostrarError(campo, 'El curso solo puede contener números y caracteres especiales');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  function validarAnoEscolar() {
    const campo = document.getElementById('ano-escolar');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    const regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
    if (!regex.test(valor)) {
      mostrarError(campo, 'El año escolar solo puede contener letras');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  function validarGrupo() {
    const campo = document.getElementById('grupo');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    const regex = /^ID[A-Z]{2,}\d{3}$/;
    if (!regex.test(valor)) {
      mostrarError(campo, 'Debe comenzar con "ID" en mayúsculas, seguido de 2+ letras y 3 números');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  function validarAutor() {
    const campo = document.getElementById('autor');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    const regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
    if (!regex.test(valor)) {
      mostrarError(campo, 'No puede contener números ni caracteres especiales');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  // ==================== VALIDACIONES PARA FORMULARIO DE EVENTOS ====================

  function validarFechasEvento() {
    const fechaInicio = document.getElementById('fecha-inicio');
    const fechaFin = document.getElementById('fecha-fin');
    if (!fechaInicio || !fechaFin) return true;

    const valorInicio = fechaInicio.value;
    const valorFin = fechaFin.value;

    if (!valorInicio || !valorFin) {
      return true;
    }

    const fechaInicioObj = new Date(valorInicio);
    const fechaFinObj = new Date(valorFin);

    if (fechaFinObj < fechaInicioObj) {
      mostrarError(fechaFin, 'La fecha de fin no puede ser anterior a la fecha de inicio');
      return false;
    }
    
    mostrarError(fechaFin, '');
    return true;
  }

  function validarProfesor() {
    const campo = document.getElementById('profesor-cargo');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    const regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/;
    if (!regex.test(valor)) {
      mostrarError(campo, 'El nombre no puede contener números ni caracteres especiales');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  function validarTelefonoContacto() {
    const campo = document.getElementById('telefono-contacto');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    const regex = /^[0-9+]*$/;
    if (!regex.test(valor)) {
      mostrarError(campo, 'Solo se permiten números y el símbolo +');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  // ==================== VALIDACIONES PARA FORMULARIO PROFESORAL ====================

  function validarNombreProfesor() {
    const campo = document.getElementById('nombre-profesor');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    const regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,50}$/;
    if (!regex.test(valor)) {
      mostrarError(campo, 'Solo letras y espacios (2-50 caracteres)');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  function validarPrimerApellido() {
    const campo = document.getElementById('primer-apellido');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    const regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,50}$/;
    if (!regex.test(valor)) {
      mostrarError(campo, 'Solo letras y espacios (2-50 caracteres)');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  function validarSegundoApellido() {
    const campo = document.getElementById('segundo-apellido');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (valor) {
      const regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{0,50}$/;
      if (!regex.test(valor)) {
        mostrarError(campo, 'Solo letras y espacios (máx. 50 caracteres)');
        return false;
      }
    }
    
    mostrarError(campo, '');
    return true;
  }

  function validarAsignatura() {
    const campo = document.getElementById('asignatura');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    const regex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]{5,50}$/;
    if (!regex.test(valor)) {
      mostrarError(campo, 'Solo letras, números y espacios (5-50 caracteres)');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  function validarSolapin() {
    const campo = document.getElementById('solapin');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    const regex = /^[A-Za-z]\d{6}$/;
    if (!regex.test(valor)) {
      mostrarError(campo, 'Formato: Letra seguida de 6 números');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  function validarTelefonoProfesor() {
    const campo = document.getElementById('telefono');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    const regex = /^\+?\d{7,15}$/;
    if (!regex.test(valor)) {
      mostrarError(campo, '7-15 dígitos, puede comenzar con +');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  function validarCorreo() {
    const campo = document.getElementById('correo');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!regex.test(valor)) {
      mostrarError(campo, 'Ingrese un correo válido (ej: usuario@dominio.com)');
      return false;
    }
    
    if (valor.length > 50) {
      mostrarError(campo, 'Máximo 50 caracteres');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  function validarBrigadaAsignada() {
    const campo = document.getElementById('brigada-asignada');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    if (valor.length > 10) {
      mostrarError(campo, 'Máximo 10 caracteres');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  function validarBrigadasImpartir() {
    const campo = document.getElementById('brigadas-impartir');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    if (valor.length > 50) {
      mostrarError(campo, 'Máximo 50 caracteres');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  function validarDescripcion() {
    const campo = document.getElementById('descripcion-profesor');
    if (!campo) return true;
    
    const valor = campo.value.trim();
    
    if (campo.required && !valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (!valor) {
      mostrarError(campo, '');
      return true;
    }
    
    if (valor.length > 500) {
      mostrarError(campo, 'Máximo 500 caracteres');
      return false;
    }
    
    mostrarError(campo, '');
    return true;
  }

  // ==================== CONFIGURACIÓN DE VALIDACIONES ====================

  function configurarValidacionEstrategia() {
    const formEstrategia = document.getElementById('form-estrategia');
    if (!formEstrategia) return;

    const configurarValidacionCampo = (id, validacionFn) => {
      const campo = document.getElementById(id);
      if (campo) {
        campo.addEventListener('input', function() {
          // Limpiar estados previos al escribir
          campo.classList.remove('is-invalid', 'is-valid');
          const contenedor = campo.closest('.form-group');
          const errorElement = contenedor.querySelector('.error-validacion');
          if (errorElement) errorElement.remove();
          
          validacionFn();
        });
        campo.addEventListener('blur', validacionFn);
      }
    };

    configurarValidacionCampo('curso', validarCurso);
    configurarValidacionCampo('ano-escolar', validarAnoEscolar);
    configurarValidacionCampo('grupo', validarGrupo);
    configurarValidacionCampo('autor', validarAutor);

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

  function configurarValidacionEventos() {
    const formEvento = document.getElementById('form-evento');
    if (!formEvento) return;

    // Configurar validación cruzada de fechas
    const fechaInicio = document.getElementById('fecha-inicio');
    const fechaFin = document.getElementById('fecha-fin');
    if (fechaInicio && fechaFin) {
      fechaInicio.addEventListener('change', validarFechasEvento);
      fechaFin.addEventListener('change', validarFechasEvento);
    }

    // Configurar validaciones específicas
    const configurarValidacionCampo = (id, validacionFn) => {
      const campo = document.getElementById(id);
      if (campo) {
        campo.addEventListener('input', function() {
          campo.classList.remove('is-invalid', 'is-valid');
          const contenedor = campo.closest('.form-group');
          const errorElement = contenedor.querySelector('.error-validacion');
          if (errorElement) errorElement.remove();
          
          validacionFn();
        });
        campo.addEventListener('blur', validacionFn);
      }
    };

    configurarValidacionCampo('profesor-cargo', validarProfesor);
    configurarValidacionCampo('telefono-contacto', validarTelefonoContacto);

    formEvento.addEventListener('submit', function(e) {
      const valido = validarCamposVacios(this) && 
                    validarFechasEvento() && 
                    validarProfesor() && 
                    validarTelefonoContacto();
      
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

  function configurarValidacionProfesoral() {
    const formProfesoral = document.getElementById('form-profesoral');
    if (!formProfesoral) return;

    const configurarValidacionCampo = (id, validacionFn) => {
      const campo = document.getElementById(id);
      if (campo) {
        campo.addEventListener('input', function() {
          campo.classList.remove('is-invalid', 'is-valid');
          const contenedor = campo.closest('.form-group');
          const errorElement = contenedor.querySelector('.error-validacion');
          if (errorElement) errorElement.remove();
          
          validacionFn();
        });
        campo.addEventListener('blur', validacionFn);
      }
    };

    configurarValidacionCampo('nombre-profesor', validarNombreProfesor);
    configurarValidacionCampo('primer-apellido', validarPrimerApellido);
    configurarValidacionCampo('segundo-apellido', validarSegundoApellido);
    configurarValidacionCampo('asignatura', validarAsignatura);
    configurarValidacionCampo('solapin', validarSolapin);
    configurarValidacionCampo('telefono', validarTelefonoProfesor);
    configurarValidacionCampo('correo', validarCorreo);
    configurarValidacionCampo('brigada-asignada', validarBrigadaAsignada);
    configurarValidacionCampo('brigadas-impartir', validarBrigadasImpartir);
    configurarValidacionCampo('descripcion-profesor', validarDescripcion);

    formProfesoral.addEventListener('submit', function(e) {
      const valido = validarCamposVacios(this) && 
                    validarNombreProfesor() && 
                    validarPrimerApellido() && 
                    validarSegundoApellido() && 
                    validarAsignatura() && 
                    validarSolapin() && 
                    validarTelefonoProfesor() && 
                    validarCorreo() && 
                    validarBrigadaAsignada() && 
                    validarBrigadasImpartir() && 
                    validarDescripcion();
      
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

  const header = select("#header");
  if (header) {
    const headerScrolled = () => {
      header.classList.toggle("header-scrolled", window.scrollY > 100);
    };
    window.addEventListener("load", headerScrolled);
    onscroll(document, headerScrolled);
  }

  const backToTop = select(".back-to-top");
  if (backToTop) {
    const toggleBackToTop = () => {
      backToTop.classList.toggle("active", window.scrollY > 100);
    };
    window.addEventListener("load", toggleBackToTop);
    onscroll(document, toggleBackToTop);
  }

  on("click", ".mobile-nav-toggle", function (e) {
    const navbar = select("#navbar");
    if (navbar) {
      navbar.classList.toggle("navbar-mobile");
      this.classList.toggle("bi-list");
      this.classList.toggle("bi-x");
    }
  });

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

  const heroCarouselIndicators = select("#hero-carousel-indicators");
  const heroCarouselItems = select('#heroCarousel .carousel-item', true);

  if (heroCarouselIndicators && heroCarouselItems) {
    heroCarouselItems.forEach((item, index) => {
      (index === 0) ?
      heroCarouselIndicators.innerHTML += "<li data-bs-target='#heroCarousel' data-bs-slide-to='" + index + "' class='active'></li>":
        heroCarouselIndicators.innerHTML += "<li data-bs-target='#heroCarousel' data-bs-slide-to='" + index + "'></li>"
    });
  }

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
    }
  };

  // ==================== INICIALIZACIÓN ====================

  document.addEventListener("DOMContentLoaded", function() {
    configurarValidacionEstrategia();
    configurarValidacionEventos();
    configurarValidacionProfesoral();
    initSeleccionarTodo();
    initFormularioEncuestas();
  });

})();