
## Steps

1. [Export All Health Data](https://support.apple.com/en-gb/guide/iphone/iph5ede58c3d/ios)
2. `xsltproc extract-swimming-workouts.xsl >swimming-workouts.xml`
3. `./swimming-lap-times-to-csv.py >times.csv`
4. In R, `source("plot-times.R")`
