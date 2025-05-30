(function () {
  "use strict";

  // ==================== FUNCIONES UTILITARIAS ====================

  const select = (el, all = false) => {
    el = el.trim();
    return all ? [...document.querySelectorAll(el)] : document.querySelector(el);
  };

  // ==================== NÚCLEO DE VALIDACIÓN ====================

  function mostrarError(campo, mensaje = '') {
    const contenedor = campo.closest('.form-group') || campo.closest('.form-control');
    if (!contenedor) return;

    let errorElement = contenedor.querySelector('.error-validacion');

    if (errorElement) errorElement.remove();
    campo.classList.remove('is-invalid', 'is-valid');

    if (mensaje) {
      errorElement = document.createElement('div');
      errorElement.className = 'error-validacion';
      errorElement.textContent = mensaje;
      contenedor.appendChild(errorElement);
      campo.classList.add('is-invalid');
    } else if (campo.value.trim() !== '') {
      campo.classList.add('is-valid');
    }
  }

  function validarCamposVacios(form) {
    let valido = true;
    const campos = form.querySelectorAll('input:not([type="hidden"]), textarea, select');
    
    campos.forEach(campo => {
      if (campo.disabled || campo.readOnly) return;
      
      if (!campo.value.trim()) {
        mostrarError(campo, 'Este campo es obligatorio');
        valido = false;
      } else {
        mostrarError(campo);
      }
    });
    
    return valido;
  }

  function validarCampoGenerico(campo, regex, mensajeError) {
    const valor = campo.value.trim();
    
    if (!valor) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (regex && !regex.test(valor)) {
      mostrarError(campo, mensajeError || 'El formato no es válido');
      return false;
    }
    
    mostrarError(campo);
    campo.classList.add('is-valid');
    return true;
  }

  // ==================== VALIDACIONES ESPECÍFICAS ====================

  function validarCurso() {
    const campo = document.getElementById('curso');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]*$/,
      'El curso solo puede contener números y caracteres especiales'
    );
  }

  function validarAnoEscolar() {
    const campo = document.getElementById('ano-escolar');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/,
      'El año escolar solo puede contener letras'
    );
  }

  function validarGrupo() {
    const campo = document.getElementById('grupo');
    if (!campo) return true;
    const valor = campo.value.trim();
    return validarCampoGenerico(
      campo,
      /^ID[A-Z]{2}\d{3}$/,
      'Debe comenzar con "ID" en mayúsculas, seguido de 2 letras y 3 números'
    );
  }

  function validarAutor() {
    const campo = document.getElementById('autor');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/,
      'No puede contener números ni caracteres especiales'
    );
  }

  function validarFechasEvento() {
    const fechaInicio = document.getElementById('fecha-inicio');
    const fechaFin = document.getElementById('fecha-fin');
    if (!fechaInicio || !fechaFin) return true;
    
    const validoInicio = validarCampoGenerico(fechaInicio);
    const validoFin = validarCampoGenerico(fechaFin);
    
    if (!validoInicio || !validoFin) return false;
    
    if (new Date(fechaFin.value) < new Date(fechaInicio.value)) {
      mostrarError(fechaFin, 'La fecha de fin no puede ser anterior a la fecha de inicio');
      return false;
    }
    
    if (fechaInicio.value === fechaFin.value) {
      const validoHoraInicio = validarHoraInicio();
      const validoHoraFin = validarHoraFin();
      return validoHoraInicio && validoHoraFin;
    }
    
    return true;
  }
  
  function validarTelefonoContacto() {
    const campo = document.getElementById('telefono-contacto');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[0-9+]*$/,
      'Solo se permiten números y el símbolo +'
    );
  }
  
  function validarHoraInicio() {
    const campo = document.getElementById('hora-inicio');
    const horaFin = document.getElementById('hora-fin');
    const fechaInicio = document.getElementById('fecha-inicio');
    const fechaFin = document.getElementById('fecha-fin');
    
    if (!campo.value) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (fechaInicio.value && fechaFin.value && 
        fechaInicio.value === fechaFin.value && 
        horaFin.value && campo.value > horaFin.value) {
      mostrarError(campo, 'Cuando las fechas son iguales, la hora de inicio no puede ser posterior a la hora de fin');
      return false;
    }
    
    mostrarError(campo);
    return true;
  }
  
  function validarHoraFin() {
    const campo = document.getElementById('hora-fin');
    const horaInicio = document.getElementById('hora-inicio');
    const fechaInicio = document.getElementById('fecha-inicio');
    const fechaFin = document.getElementById('fecha-fin');
    
    if (!campo.value) {
      mostrarError(campo, 'Este campo es obligatorio');
      return false;
    }
    
    if (fechaInicio.value && fechaFin.value && 
        fechaInicio.value === fechaFin.value && 
        horaInicio.value && campo.value < horaInicio.value) {
      mostrarError(campo, 'Cuando las fechas son iguales, la hora de fin no puede ser anterior a la hora de inicio');
      return false;
    }
    
    mostrarError(campo);
    return true;
  }

  function validarNombreProfesor() {
    const campo = document.getElementById('nombre-profesor');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,50}$/,
      'Solo letras y espacios (2-50 caracteres)'
    );
  }

  function validarPrimerApellido() {
    const campo = document.getElementById('primer-apellido');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,50}$/,
      'Solo letras y espacios (2-50 caracteres)'
    );
  }

  function validarSegundoApellido() {
    const campo = document.getElementById('segundo-apellido');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{0,50}$/,
      'Solo letras y espacios (máx. 50 caracteres)'
    );
  }

  function validarAsignatura() {
    const campo = document.getElementById('asignatura');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]{5,50}$/,
      'Solo letras, números y espacios (5-50 caracteres)'
    );
  }

  function validarSolapin() {
    const campo = document.getElementById('solapin');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[A-Za-z]\d{6}$/,
      'Formato: Letra seguida de 6 números'
    );
  }

  function validarTelefonoProfesor() {
    const campo = document.getElementById('telefono');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^\+?\d{7,15}$/,
      '7-15 dígitos, puede comenzar con +'
    );
  }

  function validarCorreo() {
    const campo = document.getElementById('correo');
    if (!campo) return true;
    const valido = validarCampoGenerico(
      campo,
      /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
      'Ingrese un correo válido (ej: usuario@dominio.com)'
    );
    
    if (valido && campo.value.length > 50) {
      mostrarError(campo, 'Máximo 50 caracteres');
      return false;
    }
    
    return valido;
  }

  function validarGrupoAsignada() {
    const campo = document.getElementById('grupo-asignada');
    if (!campo) return true;
    const valido = validarCampoGenerico(campo);
    
    if (valido && campo.value.length > 10) {
      mostrarError(campo, 'Máximo 10 caracteres');
      return false;
    }
    
    return valido;
  }

  function validarGruposImpartir() {
    const campo = document.getElementById('grupos-impartir');
    if (!campo) return true;
    const valido = validarCampoGenerico(campo);
    
    if (valido && campo.value.length > 50) {
      mostrarError(campo, 'Máximo 50 caracteres');
      return false;
    }
    
    return valido;
  }

  function validarDescripcion() {
    const campo = document.getElementById('descripcion-profesor');
    if (!campo) return true;
    const valido = validarCampoGenerico(campo);
    
    if (valido && campo.value.length > 500) {
      mostrarError(campo, 'Máximo 500 caracteres');
      return false;
    }
    
    return valido;
  }

  function validarCodigo() {
    const campo = document.getElementById('codigo');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[A-Za-z0-9]{1,10}$/,
      'Solo letras y números (máx. 10 caracteres)'
    );
  }

  function validarPeriodo() {
    const campo = document.getElementById('periodo');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]*$/,
      'El periodo solo puede contener números y caracteres especiales'
    );
  }

  function validarFecha() {
    const campo = document.getElementById('fecha');
    if (!campo) return true;
    return validarCampoGenerico(campo);
  }

  function validarAutorReporte() {
    const campo = document.getElementById('autor');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/,
      'No puede contener números ni caracteres especiales'
    );
  }

  function validarInstitucion() {
    const campo = document.getElementById('institucion');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s.,-]*$/,
      'Solo letras, números, espacios y algunos caracteres especiales (.,-)'
    );
  }

  function validarTextoLargo(campoId, maxCaracteres) {
    const campo = document.getElementById(campoId);
    if (!campo) return true;
    
    const valido = validarCampoGenerico(campo);
    
    if (valido && campo.value.length > maxCaracteres) {
      mostrarError(campo, `Máximo ${maxCaracteres} caracteres`);
      return false;
    }
    
    return valido;
  }

  function validarNombreUsuario() {
    const campo = document.getElementById('nombre');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,50}$/,
      'Solo letras y espacios (2-50 caracteres)'
    );
  }

  function validarPrimerApellidoUsuario() {
    const campo = document.getElementById('primer-apellido');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,50}$/,
      'Solo letras y espacios (2-50 caracteres)'
    );
  }

  function validarSegundoApellidoUsuario() {
    const campo = document.getElementById('segundo-apellido');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{0,50}$/,
      'Solo letras y espacios (máx. 50 caracteres)'
    );
  }

  function validarGrupoUsuario() {
    const campo = document.getElementById('grupo');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^ID[A-Z]{2}\d{3}$/,
      'Debe comenzar con "ID" en mayúsculas, seguido de 2+ letras y 3 números'
    );
  }

  function validarSolapinUsuario() {
    const campo = document.getElementById('solapin');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[A-Za-z]\d{6}$/,
      'Formato: Letra seguida de 6 números'
    );
  }

  function validarTelefonoUsuario() {
    const campo = document.getElementById('telefono');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^\+?\d{7,15}$/,
      '7-15 dígitos, puede comenzar con +'
    );
  }

  function validarCorreoUsuario() {
    const campo = document.getElementById('correo');
    if (!campo) return true;
    const valido = validarCampoGenerico(
      campo,
      /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
      'Ingrese un correo válido (ej: usuario@dominio.com)'
    );
    
    if (valido && campo.value.length > 50) {
      mostrarError(campo, 'Máximo 50 caracteres');
      return false;
    }
    
    return valido;
  }

  function validarUsuario() {
    const campo = document.getElementById('user');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-z]{5,20}$/,
      'Solo letras minúsculas (5-20 caracteres)'
    );
  }

  function validarPassword() {
    const campo = document.getElementById('password');
    if (!campo) return true;
    
    if (campo.value.length < 8) {
      mostrarError(campo, 'Mínimo 8 caracteres');
      return false;
    }
    
    if (!/[A-Z]/.test(campo.value)) {
      mostrarError(campo, 'Debe contener al menos una mayúscula');
      return false;
    }
    
    if (!/\d/.test(campo.value)) {
      mostrarError(campo, 'Debe contener al menos un número');
      return false;
    }
    
    if (!/[!@#$%^&*(),.?":{}|<>]/.test(campo.value)) {
      mostrarError(campo, 'Debe contener al menos un caracter especial');
      return false;
    }
    
    mostrarError(campo);
    return true;
  }

  function validarTituloEncuesta() {
    const campo = document.getElementById('titulo-encuesta');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s]*$/,
      'El título no puede contener caracteres especiales'
    );
  }

  function validarAutorEncuesta() {
    const campo = document.getElementById('autor-encuesta');
    if (!campo) return true;
    return validarCampoGenerico(
      campo,
      /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]*$/,
      'No puede contener números ni caracteres especiales'
    );
  }

  function validarDescripcionEncuesta() {
    const campo = document.getElementById('descripcion-encuesta');
    if (!campo) return true;
    return validarTextoLargo('descripcion-encuesta', 500);
  }

  // ==================== CONFIGURACIÓN DE FORMULARIOS ====================

  function configurarValidacionFormulario(formId, validaciones) {
    const form = document.getElementById(formId);
    if (!form) return;

    Object.entries(validaciones).forEach(([id, validacionFn]) => {
      const campo = document.getElementById(id);
      if (!campo) return;

      campo.addEventListener('blur', function() {
        validacionFn();
      });

      campo.addEventListener('input', function() {
        if (this.value.trim() !== '') {
          mostrarError(this);
        }
      });
    });

    form.addEventListener('submit', function(e) {
      let valido = true;
      
      if (!validarCamposVacios(this)) {
        valido = false;
      }

      Object.values(validaciones).forEach(fn => {
        if (!fn()) valido = false;
      });

      if (!valido) {
        e.preventDefault();
        const primerError = this.querySelector('.is-invalid');
        if (primerError) {
          primerError.focus();
          primerError.scrollIntoView({ 
            behavior: 'smooth', 
            block: 'center' 
          });
        }
      }
    });
  }

  // ==================== INICIALIZACIÓN ====================

  document.addEventListener("DOMContentLoaded", function() {
    configurarValidacionFormulario('form-estrategia', {
      'curso': validarCurso,
      'ano-escolar': validarAnoEscolar,
      'grupo': validarGrupo,
      'autor': validarAutor
    });

    configurarValidacionFormulario('form-evento', {
      'fecha-inicio': () => validarFechasEvento(),
      'fecha-fin': () => validarFechasEvento(),
      'hora-inicio': validarHoraInicio,
      'hora-fin': validarHoraFin,
      'telefono-contacto': validarTelefonoContacto
    });

    configurarValidacionFormulario('form-profesoral', {
      'nombre-profesor': validarNombreProfesor,
      'primer-apellido': validarPrimerApellido,
      'segundo-apellido': validarSegundoApellido,
      'asignatura': validarAsignatura,
      'solapin': validarSolapin,
      'telefono': validarTelefonoProfesor,
      'correo': validarCorreo,
      'grupo-asignada': validarGrupoAsignada,
      'grupos-impartir': validarGruposImpartir,
      'descripcion-profesor': validarDescripcion
    });

    configurarValidacionFormulario('form-reporte', {
      'grupo': validarGrupo,
      'codigo': validarCodigo,
      'periodo': validarPeriodo,
      'fecha': validarFecha,
      'autor': validarAutorReporte,
      'institucion': validarInstitucion,
      'resumen': () => validarTextoLargo('resumen', 500),
      'objetivos': () => validarTextoLargo('objetivos', 1000),
      'actividades': () => validarTextoLargo('actividades', 1500),
      'resultados': () => validarTextoLargo('resultados', 1500),
      'analisis': () => validarTextoLargo('analisis', 2000),
      'desafios': () => validarTextoLargo('desafios', 1500),
      'proximos-pasos': () => validarTextoLargo('proximos-pasos', 1500)
    });

    configurarValidacionFormulario('form-registro', {
      'nombre': validarNombreUsuario,
      'primer-apellido': validarPrimerApellidoUsuario,
      'segundo-apellido': validarSegundoApellidoUsuario,
      'grupo': validarGrupoUsuario,
      'solapin': validarSolapinUsuario,
      'telefono': validarTelefonoUsuario,
      'correo': validarCorreoUsuario,
      'user': validarUsuario,
      'password': validarPassword
    });

    configurarValidacionFormulario('form-crear-encuesta', {
      'titulo-encuesta': validarTituloEncuesta,
      'autor-encuesta': validarAutorEncuesta,
      'descripcion-encuesta': validarDescripcionEncuesta
    });
  });

})();