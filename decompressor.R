# if (!requireNamespace("haven", quietly = TRUE)) {
#   install.packages("haven", repos = "https://cloud.r-project.org/")
# }
#
# library(haven)
#
# input_file <- "data/t.xpt"
# output_file_csv <- "data/t_uncompressed.csv"
#
# data <- read_xpt(input_file)
# write.csv(data, output_file_csv, row.names = FALSE)
#
# print(head(data))
