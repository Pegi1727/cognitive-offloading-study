# R/03_validation.R
d <- read.csv("screening_data.csv")

report <- c(
  paste("Total rows in dataset:", nrow(d)),
  paste("Duplicate IDs:", sum(duplicated(d$ID))),
  paste("Rows where Total != P2 + P4:", sum(d$Total != d$P2 + d$P4, na.rm=TRUE)),
  paste("Rows with Total < 12:", sum(d$Total < 12, na.rm=TRUE))
)

dir.create("outputs", showWarnings=FALSE)
writeLines(report, "outputs/R_validation.txt")
cat(paste(report, collapse="
"))