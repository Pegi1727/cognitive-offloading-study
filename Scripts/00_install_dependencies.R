# R/00_install_dependencies.R
packages <- c("readr", "dplyr", "stats")
missing <- packages[!vapply(packages, requireNamespace, logical(1), quietly=TRUE)]
if (length(missing)) install.packages(missing, repos="https://cloud.r-project.org")