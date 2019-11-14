import numpy as np
from IPython.display import SVG

PLOT_WD = 2800
PLOT_HT = 2800
PLOT_CTR = [PLOT_WD // 2, PLOT_HT //2]

IMG_WD = 600
IMG_HT = 600

SVG_HEADER = "<?xml version=\"1.0\" ?>\n" +\
            "<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" \n" +\
            "width=\"600\" height=\"600\" " +\
            "viewBox=\"0 0 {} {}\" ".format(PLOT_WD, PLOT_HT) +\
            ">\n\n"

SVG_FOOTER = "\n\n</svg>\n"

def draw_radar(div): 
    out = ""
    delta = 360 / div
    for i in range(10):
        out += "\t<circle cx=\"{}\" cy=\"{}\" r=\"{}\" ".format(PLOT_CTR[0], 
                               PLOT_CTR[1], (i + 1) * 100)
        out += "stroke=\"gray\" stroke-width=\"10\" fill=\"none\" />\n"
    out += "\n"
    for i in range(9): 
        angle = np.radians(90 + (i * delta))
        x = PLOT_CTR[0] + (1000 * np.cos(angle))
        y = PLOT_CTR[1] + (1000 * np.sin(angle))
        out += "\t<path d=\"M {},{} L {},{}\" ".format(PLOT_CTR[0], PLOT_CTR[1], 
                              x, y)
        out += "stroke=\"gray\" stroke-width=\"10\" fill=\"none\" />\n"
    out += "\n"
    
    return out

def draw_pts(pts): 
    out = ""
    out += "<polygon points=\""
    delta = 360 / len(pts)
    for i in range(len(pts)): 
        angle = np.radians(90 + (i * delta))
        x = PLOT_CTR[0] + (pts[i] * 100 * np.cos(angle))
        y = PLOT_CTR[1] + (pts[i] * 100 * np.sin(angle))
        out += "{},{} ".format(x, y)
    out += "\" stroke=\"black\" stroke-width=\"10\" fill=\"blue\" fill-opacity=\"0.5\" />\n"    
    return out

def draw_label(pt_name): 
    out = ""
    delta = 360 / len(pt_name)
    for i in range(len(pt_name)): 
        angle = np.radians(90 + (i * delta))
        x = PLOT_CTR[0] + 1050 * np.cos(angle)
        y = PLOT_CTR[1] + 1050 * np.sin(angle)
        out += "\t<text x=\"{}\" y=\"{}\" ".format(x, y)
        out += "style=\"stroke: none; fill: black; font-size: 100; "
        if(i in {0, 4, 5}): 
            out += "text-anchor: middle; " 
        elif(i in {1, 2, 3}): 
            out += "text-anchor: end; "
        else: 
            out += "text-anchor: start; "
        if(i in {2, 3, 6, 7}): 
            out += "alignment-baseline: middle; "
        elif(i in {8, 0, 1}): 
            out += "alignment-baseline: hanging; " 
        else: 
            out += "alignment-baseline: baseline; "
        out += "\" >" 
        out += "{}".format(pt_name[i]) 
        out += "</text>\n"
    out += "\n"
    return out


def draw_file_plot(name, att_name, pts, pt_names): 
    n = len(pt_names)
    fname = "{}-{}-plot.svg".format(name, att_name)
    file = open(fname, "w")
    file.write(SVG_HEADER)
    file.write(draw_radar(n))
    file.write(draw_label(pt_names))
    file.write(draw_pts(pts))
    file.write(SVG_FOOTER)
    file.close()
    return fname

def draw_plot(name, att_name, pts, pt_names): 
    fname = draw_file_plot(name, att_name, pts, pt_names)
    img = SVG(fname)
    return img