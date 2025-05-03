-- Tabla para el modelo Profesor
CREATE TABLE Profesor (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    primer_apellido VARCHAR(50) NOT NULL,
    segundo_apellido VARCHAR(50),
    sexo VARCHAR(20) NOT NULL CHECK (sexo IN ('masculino', 'femenino', 'otro')),
    categoria_docente VARCHAR(20) NOT NULL CHECK (categoria_docente IN ('instructor', 'asistente', 'auxiliar', 'titular')),
    asignatura VARCHAR(50) NOT NULL,
    solapin VARCHAR(10) UNIQUE NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    correo VARCHAR(50) NOT NULL,
    descripcion TEXT NOT NULL
);

-- Tabla para el modelo Grupo
CREATE TABLE Grupo (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    curso VARCHAR(20) NOT NULL,
    anio_escolar VARCHAR(10) NOT NULL,
    caracterizacion TEXT NOT NULL,
    guia_id INTEGER UNIQUE,
    FOREIGN KEY (guia_id) REFERENCES Profesor (id) ON DELETE SET NULL
);

-- Tabla intermedia para la relación muchos a muchos entre Grupo y Profesor
CREATE TABLE Grupo_Profesores (
    grupo_id INTEGER NOT NULL,
    profesor_id INTEGER NOT NULL,
    PRIMARY KEY (grupo_id, profesor_id),
    FOREIGN KEY (grupo_id) REFERENCES Grupo (id) ON DELETE CASCADE,
    FOREIGN KEY (profesor_id) REFERENCES Profesor (id) ON DELETE CASCADE
);

-- Tabla para el modelo Reporte
CREATE TABLE Reporte (
    id SERIAL PRIMARY KEY,
    grupo VARCHAR(10),
    codigo VARCHAR(10),
    periodo VARCHAR(10),
    fecha DATE,
    autor VARCHAR(50),
    institucion VARCHAR(50),
    resumen TEXT,
    objetivos TEXT,
    actividades TEXT,
    resultados TEXT,
    analisis TEXT,
    desafios TEXT,
    proximos_pasos TEXT,
    anexos VARCHAR(255),
    estrategia_id INTEGER NOT NULL,
    FOREIGN KEY (estrategia_id) REFERENCES Estrategia (id) ON DELETE CASCADE
);

-- Tabla para el modelo Encuesta
CREATE TABLE Encuesta (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    autor VARCHAR(100) DEFAULT 'Desconocido',
    estado VARCHAR(10) NOT NULL CHECK (estado IN ('activa', 'inactiva'))
);

-- Tabla para el modelo Pregunta
CREATE TABLE Pregunta (
    id SERIAL PRIMARY KEY,
    texto VARCHAR(255) NOT NULL,
    encuesta_id INTEGER NOT NULL,
    FOREIGN KEY (encuesta_id) REFERENCES Encuesta (id) ON DELETE CASCADE
);

-- Tabla para el modelo Usuario
CREATE TABLE Usuario (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(150),
    last_name VARCHAR(150),
    email VARCHAR(254),
    is_staff BOOLEAN DEFAULT FALSE,
    is_superuser BOOLEAN DEFAULT FALSE,
    cargo VARCHAR(20) NOT NULL CHECK (cargo IN ('profesor_principal', 'usuario')),
    sexo VARCHAR(10) NOT NULL CHECK (sexo IN ('masculino', 'femenino', 'otro')),
    grupo VARCHAR(50),
    solapin VARCHAR(10) UNIQUE NOT NULL,
    telefono VARCHAR(15),
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla intermedia para la relación muchos a muchos entre Usuario y Encuesta
CREATE TABLE Usuario_Encuestas (
    usuario_id INTEGER NOT NULL,
    encuesta_id INTEGER NOT NULL,
    PRIMARY KEY (usuario_id, encuesta_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario (id) ON DELETE CASCADE,
    FOREIGN KEY (encuesta_id) REFERENCES Encuesta (id) ON DELETE CASCADE
);

-- Tabla intermedia para la relación muchos a muchos entre Usuario y Evento
CREATE TABLE Usuario_Eventos (
    usuario_id INTEGER NOT NULL,
    evento_id INTEGER NOT NULL,
    PRIMARY KEY (usuario_id, evento_id),
    FOREIGN KEY (usuario_id) REFERENCES Usuario (id) ON DELETE CASCADE,
    FOREIGN KEY (evento_id) REFERENCES Evento (id) ON DELETE CASCADE
);

-- Tabla para el modelo Estrategia
CREATE TABLE Estrategia (
    id SERIAL PRIMARY KEY,
    curso VARCHAR(20) NOT NULL,
    anio_escolar VARCHAR(10) NOT NULL,
    grupo VARCHAR(20) NOT NULL,
    nombre VARCHAR(255) DEFAULT 'Estrategia_{id}',
    autor VARCHAR(255) DEFAULT 'autor_{id}',
    plan_estudios TEXT DEFAULT 'plan_estudios_{id}',
    obj_general TEXT DEFAULT 'objetivo_general_{id}',
    obj_estrategia TEXT DEFAULT 'objetivos_estrategia_{id}',
    dir_grupo VARCHAR(255) DEFAULT 'direccion_grupo_{id}',
    caract_grupo TEXT DEFAULT 'caracteristicas_grupo_{id}',
    colect_pedagogico TEXT DEFAULT 'colectivo_pedagogico_{id}',
    dim_curricular TEXT DEFAULT 'dimension_curricular_{id}',
    dim_extensionista TEXT DEFAULT 'dimension_extensionista_{id}',
    dim_politica TEXT DEFAULT 'dimension_politico_ideologica_{id}',
    obj_dc TEXT DEFAULT 'obj_dc_{id}',
    plan_dc TEXT DEFAULT 'plan_dc_{id}',
    obj_de TEXT DEFAULT 'obj_de_{id}',
    plan_de TEXT DEFAULT 'plan_de_{id}',
    obj_dp TEXT DEFAULT 'obj_dp_{id}',
    plan_dp TEXT DEFAULT 'plan_dp_{id}',
    evaluacion TEXT DEFAULT 'evaluacion_integral_{id}',
    otros_aspectos TEXT DEFAULT 'otros_aspectos_{id}',
    conclusiones TEXT DEFAULT 'conclusiones_{id}',
    grupo_id INTEGER UNIQUE,
    FOREIGN KEY (grupo_id) REFERENCES Grupo (id) ON DELETE SET NULL
);

-- Tabla para el modelo Evento
CREATE TABLE Evento (
    id SERIAL PRIMARY KEY,
    nombre_evento VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    ubicacion_evento VARCHAR(100) NOT NULL,
    tipo_evento VARCHAR(20) NOT NULL CHECK (tipo_evento IN ('academico', 'cultural', 'deportivo', 'social')),
    profesor_encargado_id INTEGER,
    telefono_contacto VARCHAR(15) NOT NULL,
    FOREIGN KEY (profesor_encargado_id) REFERENCES Profesor (id) ON DELETE SET NULL
);