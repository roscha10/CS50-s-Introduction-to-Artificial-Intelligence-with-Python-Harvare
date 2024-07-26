# CS50

## CS50’s Introduction to Artificial Intelligence with Python

# Resumen del Curso de Inteligencia Artificial con Python de Harvard

En las primeras semanas del curso, hemos explorado varios conceptos y proyectos que muestran la aplicación práctica y teórica de la inteligencia artificial. A continuación, se detalla el aprendizaje obtenido en cada semana:

## Semana 0: Búsqueda

### Proyecto: Degrees
- **Descripción**: Exploración del juego "Six Degrees of Kevin Bacon", donde conectamos dos actores a través de sus papeles en películas.
- **Tecnología**: Implementación utilizando el algoritmo de búsqueda en anchura (BFS).

### Proyecto: Tic-Tac-Toe
- **Descripción**: Implementación del juego Tic-Tac-Toe, diseñando un programa que utiliza el algoritmo Minimax para predecir y realizar el mejor movimiento posible.
- **Tecnología**: Algoritmo Minimax.

## Semana 1: Conocimiento

### Proyecto: Knights
- **Descripción**: Resolución de un acertijo lógico con caballeros y bribones, donde los caballeros siempre dicen la verdad y los bribones siempre mienten.
- **Tecnología**: Lógica proposicional para inferir identidades basadas en afirmaciones.

### Proyecto: Minesweeper
- **Descripción**: Desarrollo de una versión del juego Buscaminas, utilizando sentencias lógicas para inferir y revelar las casillas seguras del tablero.
- **Tecnología**: Representación del conocimiento mediante lógica.

## Semana 2: Incertidumbre

### Proyecto: Heredity
- **Descripción**: Análisis genético para determinar la probabilidad de heredar características particulares, utilizando modelos de probabilidad condicional y conjunta.
- **Tecnología**: Probabilidad condicional y conjunta.

### Proyecto: PageRank
- **Descripción**: Estudio del algoritmo PageRank de Google para clasificar páginas web basadas en su importancia relativa dentro de la red.
- **Tecnología**: Modelos de probabilidad para interpretar la navegación web.

## Semana 3: Crossword

### Proyecto: Crossword
- **Descripción**: Desarrollo de un generador de crucigramas que utiliza programación de restricciones y técnicas de backtracking para resolver la disposición óptima de palabras en una cuadrícula.
- **Detalles Técnicos**:
  - **Modelado de Variables**: Cada espacio en blanco en la cuadrícula se modela como una variable con atributos específicos para su posición y longitud.
  - **Restricciones**: Incluyen restricciones unarias que requieren que las palabras se ajusten exactamente a la longitud de las variables y restricciones binarias que requieren coincidencia de letras en las intersecciones.
  - **Algoritmos Implementados**: 
    - **Backtracking**: Para explorar sistemáticamente las combinaciones de palabras.
    - **AC-3**: Para reducir los dominios de las variables asegurando la consistencia antes del backtracking.
    - **Heurísticas de Selección**: Como la de Mínimos Valores Restantes (MRV) y la heurística de valores menos restrictivos para mejorar la eficiencia del algoritmo.
- **Resultados Esperados**: Un sistema capaz de completar crucigramas eficientemente, demostrando la aplicación de la IA en la resolución de problemas complejos de satisfacción de restricciones.


## Semana 4: Compras

### Proyecto: Shopping
- **Descripción**: Desarrollo de una inteligencia artificial para predecir si los usuarios que navegan en un sitio de compras en línea completarán una compra.
- **Tecnología**: Utilización del clasificador de vecino más cercano (KNN) para analizar y predecir comportamientos de compra basados en características de sesión de usuario.
- **Implementación**:
  - **Análisis de Datos**: Uso de un conjunto de datos que contiene aproximadamente 12,000 sesiones de usuarios, incluyendo información sobre el tipo de páginas visitadas, duración de la visita, tasas de rebote, y más.
  - **Modelado y Evaluación**: Entrenamiento de un modelo KNN para predecir compras, evaluando el modelo en términos de sensibilidad (tasa de verdaderos positivos) y especificidad (tasa de verdaderos negativos).
- **Resultados Esperados**:
  - El modelo busca superar la precisión de una predicción aleatoria, proporcionando insights valiosos sobre los comportamientos de compra, lo que podría ayudar a personalizar la experiencia de compra y mejorar las estrategias de marketing.

### Objetivos de Aprendizaje:
- Aplicar técnicas de aprendizaje automático para resolver problemas prácticos de negocio.
- Comprender y manejar las métricas de evaluación para modelos clasificatorios en escenarios de datos desbalanceados.

Cada proyecto ha reforzado nuestra comprensión de los principios de la inteligencia artificial y ha mejorado nuestra habilidad para aplicar estos conceptos en la solución de problemas complejos.
