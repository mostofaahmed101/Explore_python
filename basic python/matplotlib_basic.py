#from matplotlib import pyplot as mpl
import matplotlib.pyplot as mpl
import numpy as np
from matplotlib import style





# print("matplotlib version is:", mpl.__version__)

mpl.suptitle("SUPTITLE")

                     # plot

# style.use("ggplot")
mpl.subplot(3,3,1)
font1 ={"family":"serif", "color":"red", "size":25}
font2 ={"family":"serif", "color":"blue", "size":10}

px2 = [1,2,5,8]
py2 = [0,3,5,1]
mpl.plot([1,2,5,8], [0,5,3,7],"o-k", label="1st plot")
mpl.plot(px2,py2,"x--r", label="2nd plot")

mpl.title("Title", fontdict=font1, loc="right")
mpl.xlabel("X AXIS", fontdict=font2)
mpl.ylabel("Y AXIS", fontdict=font2)

mpl.legend()
mpl.grid(color="black", linestyle="--", linewidth="0.5")


                         #plot without X Axis

mpl.subplot(3,3,2)
mpl.plot([5,3,8,6],"o--r", ms=15, mec="#000000", mfc="gold", linewidth=10)   


                    # bar

mpl.subplot(3,3,3)
bx = [2,4,6,8]
by = [30,40,50,70]
bx2 = [1,3,5,7]
by2 = [20,40,55,60]
mpl.bar(bx, by, label="man")
mpl.bar(bx2, by2, label="woman", width=0.5)
mpl.legend()


                    # barh

mpl.subplot(3,3,4)
bx3 = ["A", "B", "C","D"]
by3 = [100,500,350,600]
mpl.barh(bx3, by3, height=0.5)



                    # scatter

mpl.subplot(3,3,5)
mpl.scatter([1,3,5,7], [2,4,6,1], label="my scatter", alpha=0.3)
# mpl.plot([1,3,5,7], [2,4,6,1],"o", label="my scatter") 

mpl.title("scatter")
mpl.xlabel("X Axis")
mpl.ylabel("Y Axis")
mpl.legend(title="legend title")



                    # pie charts

mpl.subplot(3,3,6)
piX = [100,230,150,60,250]
pieLabels = ["tello", "mello", "bello", "hello", "gello"]
piecolors = ["gold", "#32a81d", "red", "pink", "black"]

mpl.pie(piX, labels=pieLabels, startangle=90, shadow=True, colors=piecolors)



                    # Histogram

mpl.subplot(3,3,7)
hx1 = np.random.uniform(0.00, 3.0, 1000)
mpl.hist(hx1, 100)
mpl.title("uniform Histogram")

mpl.subplot(3,3,8)
hx2 = np.random.normal(5.0, 1.0, 1000)
mpl.hist(hx2, 100)
mpl.title("Normal Histogram")



                # Random Normal Scatter
                
mpl.subplot(3,3,9)
Sx1 = np.random.normal(5.0, 1.0, 500)
Sy1 = np.random.normal(10.0, 2.0, 500)
mpl.scatter(Sx1, Sy1)
mpl.title("Random Normal Scatter")

mpl.show()

