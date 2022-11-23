import numpy as np
import matplotlib.pyplot as plt
from quadtree import Point, Rect, QuadTree,CUADRADOS
from matplotlib import gridspec
import pandas as pd


def querys(x,y,w,h,color,ax):
    region = Rect(x, y, w, h)
    found_points = []
    qtree.query(region, found_points)

    ax.scatter([p.x for p in found_points], [p.y for p in found_points],
                facecolors='none', edgecolors=color, s=32)

    region.draw(ax, c=color)
def cantpuntos(x,y,w,h):
    region = Rect(x, y, w, h)
    found_points = []
    qtree.query(region, found_points)
    return len(found_points)
def esquinas(x,y,w,h):
    supizq=[x-w/2,y-h/2]
    supder=[x+w/2,y-h/2]
    botder=[x+w/2,y+h/2]
    botizq=[x-w/2,y+h/2]
    return supizq,supder,botder,botizq


DPI = 72
#dataframe with columns from 0 to 105 and index meses
 

god=[[135.0, 135.0, 270.0, 270.0], [337.5, 67.5, 135.0, 135.0], [472.5, 67.5, 135.0, 135.0], [472.5, 202.5, 135.0, 135.0], [303.75, 168.75, 67.5, 67.5], [371.25, 168.75, 67.5, 67.5], [371.25, 236.25, 67.5, 67.5], [303.75, 236.25, 67.5, 67.5], [303.75, 303.75, 67.5, 67.5], [371.25, 303.75, 67.5, 67.5], [371.25, 371.25, 67.5, 67.5], [303.75, 371.25, 67.5, 67.5], [421.875, 286.875, 33.75, 33.75], [455.625, 286.875, 33.75, 33.75], [455.625, 320.625, 33.75, 33.75], [421.875, 320.625, 33.75, 33.75], [506.25, 303.75, 67.5, 67.5], [489.375, 354.375, 33.75, 33.75], [514.6875, 345.9375, 16.875, 16.875], [531.5625, 345.9375, 16.875, 16.875], [531.5625, 362.8125, 16.875, 16.875], [514.6875, 362.8125, 16.875, 16.875], [523.125, 388.125, 33.75, 33.75], [489.375, 388.125, 33.75, 33.75], [421.875, 354.375, 
33.75, 33.75], [455.625, 354.375, 33.75, 33.75], [455.625, 388.125, 33.75, 33.75], [421.875, 388.125, 33.75, 33.75], [421.875, 421.875, 33.75, 33.75], [455.625, 421.875, 33.75, 33.75], [455.625, 455.625, 33.75, 33.75], [421.875, 455.625, 33.75, 33.75], [489.375, 421.875, 33.75, 33.75], [523.125, 421.875, 33.75, 33.75], [523.125, 455.625, 33.75, 33.75], [489.375, 455.625, 33.75, 33.75], [506.25, 506.25, 67.5, 67.5], [438.75, 506.25, 67.5, 67.5], [286.875, 421.875, 33.75, 33.75], [320.625, 421.875, 33.75, 33.75], [320.625, 455.625, 33.75, 33.75], [286.875, 455.625, 33.75, 33.75], [354.375, 421.875, 33.75, 33.75], [388.125, 421.875, 33.75, 33.75], [388.125, 455.625, 33.75, 33.75], [354.375, 455.625, 33.75, 33.75], [371.25, 506.25, 67.5, 67.5], [303.75, 506.25, 67.5, 67.5], [135.0, 405.0, 270.0, 270.0], [607.5, 67.5, 135.0, 135.0], [742.5, 67.5, 135.0, 135.0], [742.5, 202.5, 135.0, 135.0], [607.5, 202.5, 135.0, 135.0], [945.0, 135.0, 270.0, 270.0], [945.0, 405.0, 270.0, 270.0], [556.875, 286.875, 33.75, 33.75], [590.625, 286.875, 33.75, 33.75], [590.625, 320.625, 33.75, 33.75], [556.875, 320.625, 33.75, 33.75], [641.25, 303.75, 67.5, 67.5], [641.25, 371.25, 67.5, 67.5], [573.75, 371.25, 67.5, 67.5], [742.5, 337.5, 135.0, 135.0], [742.5, 472.5, 135.0, 135.0], [573.75, 438.75, 67.5, 67.5], [641.25, 438.75, 67.5, 67.5], [641.25, 506.25, 67.5, 67.5], [573.75, 506.25, 67.5, 67.5], [573.75, 573.75, 67.5, 67.5], [641.25, 573.75, 67.5, 67.5], [641.25, 641.25, 67.5, 67.5], [573.75, 641.25, 67.5, 67.5], [742.5, 607.5, 135.0, 135.0], [742.5, 742.5, 135.0, 135.0], [573.75, 708.75, 67.5, 67.5], [641.25, 708.75, 67.5, 67.5], [641.25, 776.25, 67.5, 67.5], [573.75, 776.25, 67.5, 67.5], [945.0, 675.0, 270.0, 270.0], [945.0, 945.0, 270.0, 270.0], [675.0, 945.0, 270.0, 270.0], [67.5, 607.5, 135.0, 135.0], [202.5, 607.5, 135.0, 135.0], [202.5, 742.5, 135.0, 135.0], [67.5, 742.5, 135.0, 135.0], [286.875, 556.875, 33.75, 33.75], [320.625, 556.875, 33.75, 33.75], [320.625, 590.625, 33.75, 33.75], [286.875, 590.625, 33.75, 33.75], [371.25, 573.75, 67.5, 67.5], [371.25, 641.25, 67.5, 67.5], [303.75, 641.25, 67.5, 67.5], [421.875, 556.875, 33.75, 33.75], [455.625, 556.875, 33.75, 33.75], [455.625, 590.625, 33.75, 33.75], [421.875, 590.625, 33.75, 33.75], [506.25, 573.75, 67.5, 67.5], [506.25, 641.25, 67.5, 67.5], [438.75, 641.25, 67.5, 67.5], [438.75, 708.75, 67.5, 67.5], [506.25, 
708.75, 67.5, 67.5], [506.25, 776.25, 67.5, 67.5], [438.75, 776.25, 67.5, 67.5], [337.5, 742.5, 135.0, 135.0], [405.0, 945.0, 270.0, 
270.0], [135.0, 945.0, 270.0, 270.0]]
meses=['2015/01','2015/02','2015/03','2015/04','2015/05','2015/06','2015/07','2015/08','2015/09','2015/10','2015/11','2015/12','2016/01','2016/02','2016/03','2016/04','2016/05','2016/06','2016/07','2016/08','2016/09','2016/10','2016/11','2016/12','2017/01','2017/02','2017/03','2017/04','2017/05','2017/06','2017/07','2017/08','2017/09','2017/10','2017/11','2017/12','2018/01','2018/02','2018/03','2018/04','2018/05','2018/06','2018/07','2018/08','2018/09','2018/10','2018/11','2018/12','2019/01','2019/02','2019/03','2019/04','2019/05','2019/06','2019/07','2019/08','2019/09','2019/10','2019/11','2019/12']
df1=pd.read_csv("./2014-2019.csv",sep=',',low_memory=False)
mimejordataframe=pd.DataFrame(index=meses,columns=range(0,106))
#get max and min X,Y
maxX=df1['X'].max()
maxY=df1['Y'].max()*-1
minX=df1['X'].min()
minY=df1['Y'].min()*-1
print(maxX,maxY,minX,minY)
cantidad=[]
#get coords in one month
contador=0
for mes in meses:
    coords=df1[df1['Fecha'].str.contains(mes)]

    coords=coords[['X','Y']].values

    #reflect coords in y axis
    coords[:,1]=coords[:,1]*-1

    width, height = 1080, 1080

    #normalize coords
    coords[:,0] = (coords[:,0] - minX) / (maxX - minX) * width
    coords[:,1] = (coords[:,1] - minY) / (maxY - minY) * height
    #rotate coords 180 degrees
    coords[:,1] = height - coords[:,1]



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


    comparar=[]

    for i in range(len(CUADRADOS)):
        puntomedio=[CUADRADOS[i][0],CUADRADOS[i][1]]
        for j in range(len(CUADRADOS)):
            if i!=j:
                esquina=esquinas(CUADRADOS[j][0],CUADRADOS[j][1],CUADRADOS[j][2],CUADRADOS[j][3])
                if puntomedio in esquina:
                    if CUADRADOS[i] not in comparar:
                        comparar.append(CUADRADOS[i])


    #borrar elementos de comparar en CUADRADOS

    for i in comparar:
        CUADRADOS.remove(i)

    #delete duplicates in CUADRADOS with for loop
    CUADRADOS2=[]
    for i in CUADRADOS:
        if i not in CUADRADOS2:
            CUADRADOS2.append(i)

    mitad=len(CUADRADOS2)//2
    CUADRADOS3=CUADRADOS2[:mitad]


    contador=0
    seriedetiempo=[]
    ax.invert_yaxis()
    for i in god:
        
        cantidad=cantpuntos(i[0],i[1],i[2],i[3])
        seriedetiempo.append(cantidad)


    mimejordataframe.loc[mes]=seriedetiempo





                



    plt.tight_layout()
    plt.savefig('./imagenes/algo.png')
    plt.close()
mimejordataframe.to_csv('dataframe.csv')









    #         #eliminated element in list
    #         print(i)
    #         CUADRADOS.remove(i)
    # print(sirven)
    # querys(sirven[0][0],sirven[0][1],sirven[0][2],sirven[0][3],'r',ax)
    # for i in sirven2:
    #     cantidad.append(cantpuntos(i[0],i[1],i[2],i[3]))
    # print(cantidad)



