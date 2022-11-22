import numpy as np
import matplotlib.pyplot as plt
from quadtree import Point, Rect, QuadTree,CUADRADOS
from matplotlib import gridspec
import pandas as pd


def querys(x,y,w,h,color,ax):
    region = Rect(x, y, w, h)
    found_points = []
    qtree.query(region, found_points)
    print('Number of found points =', len(found_points))

    ax.scatter([p.x for p in found_points], [p.y for p in found_points],
                facecolors='none', edgecolors=color, s=32)

    region.draw(ax, c=color)
def cantpuntos(x,y,w,h):
    region = Rect(x, y, w, h)
    found_points = []
    qtree.query(region, found_points)
    print('Number of found points =', len(found_points))
    return len(found_points)

DPI = 72
np.random.seed(60)
df1=pd.read_csv("./2014-2019.csv",sep=',',low_memory=False)
#get coords in one month
df1=df1[df1['Fecha'].str.contains("2019/01")]

coords=df1[['X','Y']].values

#reflect coords in y axis
coords[:,1]=coords[:,1]*-1


width, height = 600, 400



#normalize coords
coords[:,0] = (coords[:,0] - coords[:,0].min()) / (coords[:,0].max() - coords[:,0].min()) * width
coords[:,1] = (coords[:,1] - coords[:,1].min()) / (coords[:,1].max() - coords[:,1].min()) * height
print(coords)
points = [Point(*coord) for coord in coords]


domain = Rect(width/2, height/2, width, height)
qtree = QuadTree(domain, 30)

for point in points:
    qtree.insert(point)

print('Number of points in the domain =', len(qtree))

fig = plt.figure(figsize=(700/DPI, 500/DPI), dpi=DPI)
ax = plt.subplot()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
qtree.draw(ax)

ax.scatter([p.x for p in points], [p.y for p in points], s=4)
ax.set_xticks([])
ax.set_yticks([])

# querys(0.00, 0.00, 300.00, 200.00, 'r', ax)

# querys(300.00, 200.00, 600.00, 400.00, 'b', ax)
# querys(0.00, 200.00, 300.00, 400.00, 'y', ax)
print(len(CUADRADOS))
sirven=[]
for i in CUADRADOS:
    if(cantpuntos(i[0],i[1],i[2],i[3])<=30):
        sirven.append(i)
        #eliminated element in list
        print(i)
        CUADRADOS.remove(i)
print(sirven)
querys(sirven[0][0],sirven[0][1],sirven[0][2],sirven[0][3],'r',ax)


ax.invert_yaxis()
plt.tight_layout()
plt.savefig('search-quadtree22.png', DPI=100)
plt.show()