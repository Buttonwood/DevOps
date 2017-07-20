
```
Mon	App	Len	Sd
Apr. 3	leaf	0.85	0.16
Apr. 18	leaf	1.01	0.1
May. 3	leaf	1.26	0.13
May. 18	leaf	1.6	0.08
Jun. 2	leaf	3.02	0.2
Jun. 17	leaf	3.59	0.44
Jul. 2	leaf	3.73	0.44
Jul. 17	leaf	4.86	0.8
Aug. 1	leaf	5.47	0.25
Aug. 16	leaf	5.71	0.62
Aug. 31	leaf	6.03	0.82
Sept. 20	leaf	6.15	0.84
Sept. 30	leaf	6.21	0.79
Apr. 3	fruit	2	0.381575681
Apr. 18	fruit	2.7	0.405955663
May. 3	fruit	5.8	0.435583899
May. 18	fruit	12.6	1.106526095
Jun. 2	fruit	12.89	0.466047208
Jun. 17	fruit	13.03	0.28213472
Jul. 2	fruit	13.15	0.037859389
Jul. 17	fruit	13.31	0.884759854
Aug. 1	fruit	13.43	0.812649986
Aug. 16	fruit	13.52	0.91016482
Aug. 31	fruit	13.6	1.053565375
Sept. 20	fruit	13.69	1.043264108
Sept. 30	fruit	13.76	0.98


data <- read.csv('C:\\Users\\User_2\\Downloads\\data1.csv')
data$Mon <- factor(data$Mon, levels=unique(as.character(data$Mon)))

### 折线图
p <- ggplot(data = data, aes(x = Mon, y = Len, group = App, colour = App, shape = App)) + 
    geom_line() + 
    geom_point(size = 3) +
  	geom_errorbar(aes(ymin=Len-Sd, ymax=Len+Sd), width=.2) +
    scale_fill_brewer(palette="Reds") + theme_minimal()
    
### barplot
p <- ggplot(data = data, aes(x = Mon, y = Len, group = App, colour = App, shape = App)) + 
    geom_line() + 
    geom_point(size = 3) +
	geom_bar(data = data, aes(x = Mon, y = Len, fill = App), stat = "identity", alpha = 0.8, position=position_dodge()) +
  	geom_errorbar(aes(ymin=Len-Sd, ymax=Len+Sd), width=.2, position=position_dodge(.9)) +
    scale_fill_brewer(palette="Reds") + theme_minimal()
```
