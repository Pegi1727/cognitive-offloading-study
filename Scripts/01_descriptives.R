# R/01_descriptives.R
library(readr)
library(dplyr)

# Assuming screening_data.csv exists in the root
d <- read_csv("screening_data.csv", show_col_types=FALSE)
dir.create("outputs", showWarnings=FALSE)

# Basic descriptive statistics based on available columns
result <- d |>
  group_by(Group_Note) |>
  summarise(
    n = n(),
    mean_total = mean(Total, na.rm=TRUE),
    sd_total = sd(Total, na.rm=TRUE),
    .groups = "drop"
  )

write_csv(result, "outputs/R_descriptives.csv")
print(result)