# R/02_screening_anova.R
library(stats)
d <- read.csv("screening_data.csv")
d$Group_Note <- factor(d$Group_Note)
dir.create("outputs", showWarnings=FALSE)

sink("outputs/R_screening_ANOVA.txt")
cat("--- One-Way ANOVA Results ---

")

for (outcome in c("P2", "P4", "Total")) {
  if (outcome %in% colnames(d)) {
    cat("
Outcome:", outcome, "
")
    fit <- aov(reformulate("Group_Note", response=outcome), data=d)
    print(summary(fit))
  }
}
sink()