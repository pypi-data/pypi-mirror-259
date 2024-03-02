# Overview
_PaRaVis_ is a powerful GUI designed for extracting, visualizing, and analyzing Rao's Q based on VIs. The GUI comprises three main sections, each enhancing usability and functionality for different process aspects.

### 1. Vegetation Index Analysis
The code provides a user-friendly interface for importing stacked raster datasets, selecting specific bands, and calculating multiple indices simultaneously. spatial visualizations with customization options enhance the exploration of vegetation indices. Users can also select and save calculated indices (based on their CV value) as GeoTIFF files for future analysis.

### 2. Rao's Q Index Computation
This section focuses on the computation of Rao's Q index from raster files in both unidimensional and multidimensional modes. offering  parameter customization options. parallelization using the Ray framework optimizes computational efficiency, reducing processing time significantly. The code employs the "tqdm" library to monitor processing time.

### 3. Visualization and Analysis
This part emphasizes visualizing and analyzing Rao's Q outputs through an intuitive interface. Various widgets facilitate seamless file selection, output path definition, and customization of plot settings. The tool generates insightful plots, histograms, difference heatmaps, and split plots, making complex operations accessible to users.