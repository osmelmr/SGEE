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

  // ==================== FUNCIONALIDADES DE VALIDACIÓN MEJORADAS ====================

  window.validarCamposVacios = function(formId) {
    const form = select(`#${formId}`);
    if (!form) return false;
    
    const campos = form.querySelectorAll('input[required], textarea[required], select[required]');
    let todosLlenos = true;
    
    campos.forEach(campo => {
      if (!campo.value.trim()) {
        todosLlenos = false;
        campo.classList.add('is-invalid');
        
        // Mostrar mensaje de error debajo del campo
        let errorMsg = campo.nextElementSibling;
        if (!errorMsg || !errorMsg.classList.contains('invalid-feedback')) {
          errorMsg = document.createElement('div');
          errorMsg.className = 'invalid-feedback';
          errorMsg.textContent = 'Este campo es obligatorio';
          campo.parentNode.appendChild(errorMsg);
        }
      } else {
        campo.classList.remove('is-invalid');
        const errorMsg = campo.nextElementSibling;
        if (errorMsg && errorMsg.classList.contains('invalid-feedback')) {
          errorMsg.remove();
        }
      }
    });
    return todosLlenos;
  };

  window.mostrarError = function(mensaje, elemento = null) {
    if (elemento) {
      // Eliminar mensajes de error previos
      const existingErrors = elemento.parentNode.querySelectorAll('.invalid-feedback');
      existingErrors.forEach(error => error.remove());
      
      // Mostrar error
      elemento.classList.add('is-invalid');
      const errorMsg = document.createElement('div');
      errorMsg.className = 'invalid-feedback d-block';
      errorMsg.textContent = mensaje;
      elemento.parentNode.appendChild(errorMsg);
      
      // Desplazarse al primer error si hay varios
      if (!document.querySelector('.is-invalid:focus')) {
        elemento.scrollIntoView({ behavior: 'smooth', block: 'center' });
        elemento.focus();
      }
    } else {
      // Mostrar error general
      const errorContainer = select('#error-message');
      if (errorContainer) {
        errorContainer.textContent = mensaje;
        errorContainer.style.display = 'block';
        setTimeout(() => errorContainer.style.display = 'none', 5000);
      } else {
        alert(mensaje);
      }
    }
  };

  window.validarNombreApellido = function(valor, campo) {
    const regex = /^[A-Za-zÁÉÍÓÚáéíóúñÑ\s]+$/;
    const valido = regex.test(valor);
    if (campo) {
      if (!valido && valor) {
        mostrarError('Solo se permiten letras y espacios', campo);
      } else {
        campo.classList.remove('is-invalid');
        const errorMsg = campo.nextElementSibling;
        if (errorMsg && errorMsg.classList.contains('invalid-feedback')) {
          errorMsg.remove();
        }
      }
    }
    return valido;
  };

  window.validarCorreo = function(correo, campo) {
    // Expresión regular mejorada para validación de correo
    const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const valido = regex.test(correo);
    
    if (campo) {
      // Mostrar ayuda sobre el formato esperado
      const helpText = campo.parentNode.querySelector('.email-help');
      if (!helpText) {
        const help = document.createElement('small');
        help.className = 'form-text text-muted email-help';
        help.textContent = 'Ejemplo válido: usuario@dominio.com';
        campo.parentNode.appendChild(help);
      }
      
      if (!valido && correo) {
        // Mensajes de error más descriptivos
        if (!correo.includes('@')) {
          mostrarError('El correo debe contener un @', campo);
        } else if (correo.indexOf('@') === 0 || correo.indexOf('@') === correo.length - 1) {
          mostrarError('El @ no puede estar al inicio o final', campo);
        } else if (!correo.includes('.')) {
          mostrarError('Falta el dominio (ej: .com, .net)', campo);
        } else if (correo.match(/@/g)?.length > 1) {
          mostrarError('Solo puede contener un @', campo);
        } else if (correo.includes('..')) {
          mostrarError('No puede contener puntos consecutivos', campo);
        } else {
          mostrarError('Formato de correo inválido. Ejemplo válido: usuario@dominio.com', campo);
        }
      } else {
        campo.classList.remove('is-invalid');
        const errorMsg = campo.nextElementSibling;
        if (errorMsg && errorMsg.classList.contains('invalid-feedback')) {
          errorMsg.remove();
        }
      }
    }
    return valido;
  };

  window.validarUsuario = function(usuario, campo) {
    const regex = /^[a-z][a-z0-9_]{3,}$/;
    const valido = regex.test(usuario);
    
    if (campo) {
      // Mostrar requisitos
      const helpText = campo.parentNode.querySelector('.username-help');
      if (!helpText) {
        const help = document.createElement('small');
        help.className = 'form-text text-muted username-help';
        help.textContent = 'Mínimo 4 caracteres (letras minúsculas, números o _)';
        campo.parentNode.appendChild(help);
      }
      
      if (!valido && usuario) {
        if (usuario.length < 4) {
          mostrarError('Mínimo 4 caracteres', campo);
        } else if (!/^[a-z]/.test(usuario)) {
          mostrarError('Debe comenzar con letra minúscula', campo);
        } else if (/[^a-z0-9_]/.test(usuario)) {
          mostrarError('Solo letras minúsculas, números y _', campo);
        } else {
          mostrarError('Formato de usuario inválido', campo);
        }
      } else {
        campo.classList.remove('is-invalid');
        const errorMsg = campo.nextElementSibling;
        if (errorMsg && errorMsg.classList.contains('invalid-feedback')) {
          errorMsg.remove();
        }
      }
    }
    return valido;
  };

  window.validarContraseña = function(contraseña, campo) {
    const regex = /^(?=.*\d)(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$/;
    const valido = regex.test(contraseña);
    
    if (campo) {
      // Mostrar requisitos
      const helpText = campo.parentNode.querySelector('.password-help');
      if (!helpText) {
        const help = document.createElement('small');
        help.className = 'form-text text-muted password-help';
        help.innerHTML = 'Requisitos:<br>- Mínimo 8 caracteres<br>- Al menos 1 número<br>- Al menos 1 mayúscula<br>- Al menos 1 carácter especial (!@#$%^&*)';
        campo.parentNode.appendChild(help);
      }
      
      if (!valido && contraseña) {
        let mensaje = 'La contraseña debe tener:';
        if (contraseña.length < 8) mensaje += '\n- Mínimo 8 caracteres';
        if (!/\d/.test(contraseña)) mensaje += '\n- Al menos 1 número';
        if (!/[A-Z]/.test(contraseña)) mensaje += '\n- Al menos 1 mayúscula';
        if (!/[!@#$%^&*]/.test(contraseña)) mensaje += '\n- Al menos 1 carácter especial (!@#$%^&*)';
        
        mostrarError(mensaje, campo);
      } else {
        campo.classList.remove('is-invalid');
        const errorMsg = campo.nextElementSibling;
        if (errorMsg && errorMsg.classList.contains('invalid-feedback')) {
          errorMsg.remove();
        }
      }
    }
    return valido;
  };

  window.validarTelefono = function(telefono, campo) {
    const regex = /^[\d\s+-]{8,15}$/;
    const valido = regex.test(telefono);
    
    if (campo) {
      if (!valido && telefono) {
        mostrarError('Formato inválido. Use solo números, +, - o espacios (8-15 caracteres)', campo);
      } else {
        campo.classList.remove('is-invalid');
        const errorMsg = campo.nextElementSibling;
        if (errorMsg && errorMsg.classList.contains('invalid-feedback')) {
          errorMsg.remove();
        }
      }
    }
    return valido;
  };

  window.verificarExistencia = async function(url, datos) {
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(datos),
      });
      const data = await response.json();
      return data.existe;
    } catch (error) {
      console.error('Error al verificar existencia:', error);
      return false;
    }
  };

  // ==================== FUNCIONALIDADES ESPECÍFICAS ====================

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
        
        // Añadir evento al nuevo botón eliminar
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

        // Validar campos vacíos
        if (!validarCamposVacios('form-crear-encuesta')) {
          mostrarError('Por favor complete todos los campos requeridos.');
          valido = false;
        }

        // Validar título de encuesta
        const tituloEncuesta = select('#titulo-encuesta');
        if (tituloEncuesta && !validarNombreApellido(tituloEncuesta.value, tituloEncuesta)) {
          valido = false;
        }

        if (!valido) return;

        // Verificar si la encuesta ya existe
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

  /**
   * Formulario de eventos
   */
  const initFormularioEventos = () => {
    const formEvento = select('#form-evento');
    if (formEvento) {
      formEvento.addEventListener('submit', async function (event) {
        event.preventDefault();
        let valido = true;

        // Validar campos vacíos
        if (!validarCamposVacios('form-evento')) {
          mostrarError('Por favor complete todos los campos requeridos.');
          valido = false;
        }

        // Validar nombre del evento
        const nombreEvento = select('#nombre-evento');
        if (nombreEvento && !validarNombreApellido(nombreEvento.value, nombreEvento)) {
          valido = false;
        }

        // Validar teléfono
        const telefonoContacto = select('#telefono-contacto');
        if (telefonoContacto && !validarTelefono(telefonoContacto.value, telefonoContacto)) {
          valido = false;
        }

        if (!valido) return;

        // Verificar si el evento ya existe
        try {
          const existeEvento = await verificarExistencia('/verificar-evento', { nombre: nombreEvento.value });
          if (existeEvento) {
            mostrarError('Ya existe un evento con ese nombre.', nombreEvento);
            return;
          }
          this.submit();
        } catch (error) {
          console.error('Error al verificar evento:', error);
          mostrarError('Error al verificar el evento. Intente nuevamente.');
        }
      });
    }
  };

  /**
   * Formulario informacion profesoral
   */
  const initFormularioProfesoral = () => {
    const formProfesoral = select('#form-profesoral');
    if (formProfesoral) {
      formProfesoral.addEventListener('submit', async function (event) {
        event.preventDefault();
        let valido = true;

        // Validar campos vacíos
        if (!validarCamposVacios('form-profesoral')) {
          mostrarError('Por favor complete todos los campos requeridos.');
          valido = false;
        }

        // Validar nombres y apellidos
        const nombre = select('#nombre-profesor');
        const primerApellido = select('#primer-apellido');
        const segundoApellido = select('#segundo-apellido');

        if (nombre && !validarNombreApellido(nombre.value, nombre)) valido = false;
        if (primerApellido && !validarNombreApellido(primerApellido.value, primerApellido)) valido = false;
        if (segundoApellido && segundoApellido.value && !validarNombreApellido(segundoApellido.value, segundoApellido)) valido = false;

        // Validar teléfono
        const telefono = select('#telefono');
        if (telefono && !validarTelefono(telefono.value, telefono)) valido = false;

        // Validar correo
        const correo = select('#correo');
        if (correo) {
          correo.addEventListener('input', function() {
            validarCorreo(this.value, this);
          });
          if (!validarCorreo(correo.value, correo)) valido = false;
        }

        if (!valido) return;

        // Verificar si el profesor ya existe
        try {
          const existeProfesor = await verificarExistencia('/verificar-profesor', {
            nombre: nombre.value,
            primerApellido: primerApellido.value,
            segundoApellido: segundoApellido?.value || ''
          });
          if (existeProfesor) {
            mostrarError('Ya existe un profesor con esos datos.');
            return;
          }
          this.submit();
        } catch (error) {
          console.error('Error al verificar profesor:', error);
          mostrarError('Error al verificar el profesor. Intente nuevamente.');
        }
      });
    }
  };

  /**
   * Formulario reporte de cumplimiento
   */
  const initFormularioReportes = () => {
    const formReporte = select('#form-reporte');
    if (formReporte) {
      formReporte.addEventListener('submit', async function (event) {
        event.preventDefault();
        let valido = true;

        // Validar campos vacíos
        if (!validarCamposVacios('form-reporte')) {
          mostrarError('Por favor complete todos los campos requeridos.');
          valido = false;
        }

        if (!valido) return;

        // Verificar si el código ya existe
        const codigo = select('#codigo');
        try {
          const existeCodigo = await verificarExistencia('/verificar-codigo', { codigo: codigo.value });
          if (existeCodigo) {
            mostrarError('Ya existe un reporte con ese código.', codigo);
            return;
          }
          this.submit();
        } catch (error) {
          console.error('Error al verificar código:', error);
          mostrarError('Error al verificar el código. Intente nuevamente.');
        }
      });
    }
  };

  /**
   * Formulario de registro
   */
  const initFormularioRegistro = () => {
    const formRegistro = select('#form-registro');
    if (formRegistro) {
      // Validación en tiempo real para el correo
      const correoInput = select('#correo');
      if (correoInput) {
        correoInput.addEventListener('input', function() {
          validarCorreo(this.value, this);
        });
        
        // Validar al perder el foco
        correoInput.addEventListener('blur', function() {
          if (this.value) validarCorreo(this.value, this);
        });
      }

      // Validación en tiempo real para el usuario
      const usuarioInput = select('#user');
      if (usuarioInput) {
        usuarioInput.addEventListener('input', function() {
          validarUsuario(this.value, this);
        });
      }

      formRegistro.addEventListener('submit', async function (event) {
        event.preventDefault();
        let valido = true;

        // Validar campos vacíos
        if (!validarCamposVacios('form-registro')) {
          mostrarError('Por favor complete todos los campos requeridos.');
          valido = false;
        }

        // Validar nombres y apellidos
        const nombre = select('#nombre');
        const primerApellido = select('#primer-apellido');
        const segundoApellido = select('#segundo-apellido');

        if (nombre && !validarNombreApellido(nombre.value, nombre)) valido = false;
        if (primerApellido && !validarNombreApellido(primerApellido.value, primerApellido)) valido = false;
        if (segundoApellido && segundoApellido.value && !validarNombreApellido(segundoApellido.value, segundoApellido)) valido = false;

        // Validar usuario
        const usuario = select('#user');
        if (usuario && !validarUsuario(usuario.value, usuario)) valido = false;

        // Validar contraseña
        const contraseña = select('#password');
        if (contraseña && !validarContraseña(contraseña.value, contraseña)) valido = false;

        // Validar teléfono
        const telefono = select('#telefono');
        if (telefono && !validarTelefono(telefono.value, telefono)) valido = false;

        // Validar correo
        const correo = select('#correo');
        if (correo && !validarCorreo(correo.value, correo)) valido = false;

        if (!valido) return;

        // Verificar si el usuario ya existe
        try {
          const existeUsuario = await verificarExistencia('/verificar-usuario', { usuario: usuario.value });
          if (existeUsuario) {
            mostrarError('El nombre de usuario ya está en uso.', usuario);
            return;
          }
          this.submit();
        } catch (error) {
          console.error('Error al verificar usuario:', error);
          mostrarError('Error al verificar el usuario. Intente nuevamente.');
        }
      });
    }
  };

  /**
   * Formulario de estrategia
   */
  const initFormularioEstrategia = () => {
    const formEstrategia = select('#form-estrategia');
    if (formEstrategia) {
      formEstrategia.addEventListener('submit', async function (event) {
        event.preventDefault();
        let valido = true;

        // Validar campos vacíos
        if (!validarCamposVacios('form-estrategia')) {
          mostrarError('Por favor complete todos los campos requeridos.');
          valido = false;
        }

        // Validar nombre de estrategia
        const tituloEstrategia = select('#titulo-estrategia');
        if (tituloEstrategia && !validarNombreApellido(tituloEstrategia.value, tituloEstrategia)) {
          valido = false;
        }

        if (!valido) return;

        // Verificar si la estrategia ya existe
        try {
          const existeEstrategia = await verificarExistencia('/verificar-estrategia', { titulo: tituloEstrategia.value });
          if (existeEstrategia) {
            mostrarError('Ya existe una estrategia con ese título.', tituloEstrategia);
            return;
          }
          this.submit();
        } catch (error) {
          console.error('Error al verificar estrategia:', error);
          mostrarError('Error al verificar la estrategia. Intente nuevamente.');
        }
      });
    }
  };

  // Inicializar todas las funcionalidades
  document.addEventListener("DOMContentLoaded", function() {
    initSeleccionarTodo();
    initFormularioEncuestas();
    initFormularioEventos();
    initFormularioProfesoral();
    initFormularioReportes();
    initFormularioRegistro();
    initFormularioEstrategia();
  });
})();