library(dplyr)
library(parsedate)
library(lubridate)

d <- read.csv("times.csv")

d |>
  mutate(date = parse_date(date)) |>
  mutate(month = format(floor_date(date, unit = "month")), format = "%Y-%m") |>
  ggplot(aes(x = factor(month), y = seconds)) +
  geom_boxplot() +
  xlab("") -> g

print(g)
