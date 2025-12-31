# Pipeline CI/CD - Flask + Vue + GitLab

## Integrantes del Equipo

- Unai San Juan Roces (UO275963)

## Descripción del Proyecto

Este proyecto implementa un pipeline CI/CD completo utilizando:

- **Backend**: Flask (Python)
- **Frontend**: Vue.js
- **CI/CD**: GitLab CI/CD
- **Contenedorización**: Docker

## Características del Pipeline

El pipeline automatiza las siguientes tareas:

1. **Tests Automáticos**: Ejecución de pruebas unitarias en el backend
2. **Análisis Estático**: Verificación de calidad de código con Flake8
3. **Construcción de Imágenes**: Build de contenedores Docker
4. **Generación de Reportes**: Informes automáticos de ejecución

## Estructura del Pipeline

### Etapas

1. **Test**: Ejecuta las pruebas del backend y frontend
2. **Build**: Construye las imágenes Docker
3. **Analyze**: Realiza análisis estático del código
4. **Report**: Genera reportes de ejecución

## Ejecución Local

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

El backend estará disponible en `http://localhost:5000`

### Frontend
```bash
cd frontend
npm install
npm run serve
```

El frontend estará disponible en `http://localhost:8080`

### Con Docker Compose
```bash
docker-compose up
```

## Endpoints del Backend

- `GET /api/health` - Verificación de estado
- `GET /api/data` - Obtención de datos

## Tests

Para ejecutar los tests manualmente:
```bash
cd backend
pytest -v
```

## Análisis Estático

Para ejecutar el análisis de código:
```bash
cd backend
flake8 .
```

## Requisitos

- Python 3.11+
- Node.js 18+
- Docker
- GitLab account

## Notas

- El pipeline se ejecuta automáticamente en cada push
- Las imágenes Docker se publican en el registry de GitLab
- Los reportes se almacenan como artifacts por 1 semana