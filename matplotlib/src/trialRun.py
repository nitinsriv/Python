import matplotlib.pyplot as mp
import numpy as np
import matplotlib.mlab as mlab

#plot with a range
mp.plot(range(10))

#add labels to axes
#watch out for single quotes
mp.xlabel('measured')
mp.ylabel('calculated')

#display grid
#watch out for case sensitive 'True',
#'true' will give error
mp.grid(True)

#usign gca()
#get line
#set marker on line
#set color of line
my_plot=mp.gca()
print(type(my_plot))

line=my_plot.lines[0]
print(line)

line.set_marker('o')
mp.setp(line,color='g')

mp.clf()

#plot (x,y) with y=f(x)
ar=np.arange(10)
print(ar)
linear=ar;
sq=[e*e for e in ar]
print(sq)

# approach 1: plot each line individually
mp.plot(ar,sq,'g')
mp.plot()
mp.plot(ar,ar,'b')

#approach2: plot two lines in one command
lines = mp.plot(ar,linear,ar,sq)

#legend for the plot
leg = mp.legend(('linear', 'square'), loc='lower right')

#specify markers for both lines in one command
#notice 'g:+' and 'r--o'
mp.plot(ar,linear,'g:+',ar,sq,'r--o')

#specify legend
mp.legend(('linear','square'))

#specify symbol
#notice format r'$\pi$'
symbol = mp.text(2,30,r'$\pi$')

#draw annotation
arrow = mp.annotate('Symbol of pi',xy=(2,30),xytext=(1,60), arrowprops={'facecolor':'r'})

#label x-axis points 
mp.xticks(range(11),('I','II','III','IV','V','VI','VII','VIII','IX','X','XI'))

#get axes
#use locator to intrapolate
ax = mp.gca()
major_locator = mp.MultipleLocator(6)
ax.xaxis.set_major_locator(major_locator)

mp.clf()

#plot bar
bar =  mp.bar((1,3,5),(70,25,40))

mp.clf()

#plot histogram
# example data
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)

num_bins = 40

fig, ax = mp.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, normed=1)

# add a 'best fit' line
y = mlab.normpdf(bins, mu, sigma)
ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')


