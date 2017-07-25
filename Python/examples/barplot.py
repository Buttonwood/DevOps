#!/usr/bin/python
# encoding:utf-8

import json,csv,svgwrite
from collections import defaultdict

data = defaultdict(dict)
with open("DEGs.kegg.data.csv", 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row  in reader:
                data[row[0]][row[1]] = row[2]

#print(json.dumps(data, indent=4))

cols = [ svgwrite.rgb(255, 182, 193),
        svgwrite.rgb(255, 160, 122),
        svgwrite.rgb( 32, 178, 170),
        svgwrite.rgb(135, 206, 250),
        svgwrite.rgb( 50, 205, 50)]

dwg = svgwrite.Drawing('barplot.2.svg',size=(1600,2400))
x = 300
y = 15
i = 0

for cata in data:
        n = 0
        for name in data[cata]:
                num = int(data[cata][name])
                y += 20
                h = num
                dwg.add(dwg.rect((x+10, y), (h, 10), stroke=svgwrite.rgb(10, 10, 16, '%'), fill=cols[i]))
                dwg.add(dwg.text(num, insert=(x+10+h+5, y+10), fill=cols[i], style="font-size:12px; font-family:Arial;text-anchor: start"))
                dwg.add(dwg.text(name, insert=(x, y+10), fill=cols[i], style="font-size:12px; font-family:Arial;text-anchor: end"))
                n += 1
        dwg.add(dwg.rect((x+450, y-(n-1)*20), (2.5, n*20), stroke=svgwrite.rgb(10, 10, 16, '%'), fill=cols[i]))
        dwg.add(dwg.text(cata, insert=(x+450+5, y-(n-1)*20 + n*10), fill=cols[i], style="font-size:15px; font-family:Arial;text-anchor: start"))
        i += 1

#dwg.add(dwg.line(start=(x+10, y+20), end=(x+400+10, y+20)))
#for z in range(0,5):
#       dwg.add(dwg.line(start=(x+100*z, y+20), end=(x+100*z, y+25)))
#       dwg.add(dwg.text(100*z, insert=(x+100*z, y+30), style="font-size:10px; font-family:Arial;text-anchor: start"))

dwg.add(dwg.rect((x+10, y+20), (400,2.5)))
for z in range(0,5):
   dwg.add(dwg.rect((x+10+100*z, y+20), (2.5,10)))
   dwg.add(dwg.text(100*z, insert=(x+10+100*z, y+50), style="font-size:10px; font-family:Arial;text-anchor: start"))
dwg.save()
