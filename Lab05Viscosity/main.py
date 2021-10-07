import csv
import math
import os
from scipy.stats import linregress
import pandas as pd

excel_file = "data.xlsx"
writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

# loops through v2 csv files (the ones where the the data has been trimmed)
# and calculates the x, y in meters, displacement in meters, Time Adjusted
# and graphs displacement by time.

for file in os.scandir():
    # get filename file
    fn = file.path[2:]

    # checks if file is csv and if it is v2
    if ".csv" in fn and "v2" in fn:

        # opens csv
        with open(fn, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            rows = [[i for i in row] for row in spamreader]

        # since data is read by line (row), this transposes to columns
        columns = list(zip(*rows[1:]))

        # assigns header for no reason
        header = rows[0]

        # gets # of 0 data rows
        n = 0
        for i in columns[1]:
            if float(i) == 0:
                n += 1

        # calculates everything except displacement
        times = [float(i) for i in columns[0] if float(i) > 0][n:]
        timesAdjusted = [float(i) - float(times[0]) for i in times if float(i) > 0]
        xs = [float(i) / 39.37 for i in columns[1] if float(i) != 0]
        ys = [float(i) / 39.37 for i in columns[2] if float(i) != 0]
        x = [float(i) for i in columns[1] if float(i) != 0]
        y = [float(i) for i in columns[2] if float(i) != 0]

        # calculates displacement
        x1 = xs[0]
        y1 = ys[0]
        d = [math.sqrt((ys[i] - y1) ** 2 + (xs[i] - x1) ** 2) for i in range(len(xs))]

        # calculates linear regression
        result = linregress(timesAdjusted, d)

        # Assigns header and values for dataframe
        headers = ["Time Adjusted (s)", "Time (s)", "X (in)", "Y (in)", "X (m)", "Y (m)", "Displacement (m)"]
        values = list(zip(*[timesAdjusted, times, x, y, xs, ys, d]))

        pd.set_option("display.max_columns", None)
        df = pd.DataFrame(values)
        df.columns = headers

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        sheet_name = fn[:-4]

        df.to_excel(writer, sheet_name=sheet_name, index=False)

        # Access the XlsxWriter workbook and worksheet objects from the dataframe.
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]

        # Create a chart object.
        chart = workbook.add_chart({'type': 'scatter'})

        # Configure the series of the chart from the dataframe data.
        max_row = len(df)
        dCol = 6
        chart.add_series({
            'categories': [sheet_name, 1, 0, max_row, 0],
            'values': [sheet_name, 1, dCol, max_row, dCol],
            'marker': {'type': 'circle', 'size': 0.01},
            'trendline': {'type': 'linear',
                          'display_equation': True,
                          },
        })

        # Configure certain chart properties
        chart.set_legend({'position': 'none'})
        chart.set_size({'x_scale': 1.35, 'y_scale': 1.5})
        chart.set_title({
            'name': 'Displacement-Time Scatterplot',
            'name_font': {
                'name': 'Times New Roman'
            },
        })

        # Configure the chart axes.
        chart.set_x_axis({'name': 'Time (s)',
                          'major_gridlines': {'visible': True}})
        chart.set_y_axis({'name': 'Displacement (m)',
                          'major_gridlines': {'visible': True}})

        # Insert the chart into the worksheet.
        worksheet.insert_chart('I2', chart)

        # repeat, for every csv file, until all sheets are created in
        # the workbook.

# Close the Pandas Excel writer and output the Excel file.
writer.save()
