import os
import pygame
import tkinter
from tkinter import messagebox as mb
import math as mt
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

# Declaration of Additional Variable
font9 = "-family {Showcard Gothic} -size 14 -weight bold " \
        "-slant roman -underline 0 -overstrike 0"

# Make a Tkinter Canvas
window = tkinter.Tk()
window.title("Shoulder Joint Movement Model and Control Simulation (C) Dzikrur Rohmani Z. R. M. H.")
window.geometry("+250+10")

# Declare Attribute
TitlePos = tkinter.Frame(window, width=1050, height=40, background='#e2e6e2')
TitlePos.pack()
TitlePos.pack_propagate(0)

Title = tkinter.Label(TitlePos, text="Shoulder Joint Movement Model and Control Simulation", font=font9, bg='#e2e6e2')
Title.pack(pady=5, expand=tkinter.YES, side=tkinter.TOP)

MainPos = tkinter.Frame(window, width=1050, height=550, background='#e2e6e2')
MainPos.pack()
MainPos.pack_propagate(0)

MainPos1 = tkinter.Frame(MainPos, width=1050, height=400, background='#e2e6e2')
MainPos1.pack()
MainPos1.pack_propagate(0)

OpenGLPos = tkinter.LabelFrame(MainPos1, width=682, height=400, text='''OPEN GL''', background='#e2e6e2',
                               labelanchor=tkinter.N)
OpenGLPos.pack(padx=11, side=tkinter.LEFT)
OpenGLPos.pack_propagate(0)

embed = tkinter.LabelFrame(OpenGLPos, width=650, height=360, background='#e2e6e2')
embed.pack(expand=tkinter.YES)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

TombolPos = tkinter.Frame(MainPos1, width=368, height=400, background='#e2e6e2')
TombolPos.pack(padx=(5, 15), side=tkinter.TOP)

mf2 = tkinter.Frame(TombolPos, width=360, height=70, background='#e2e6e2')
mf2.pack(padx=0, pady=(3, 0))
mf2.pack_propagate(0)
mf2_1 = tkinter.Frame(mf2, width=180, height=50, bg="#e2e6e2")
mf2_1.pack(side=tkinter.LEFT)
mf2_2 = tkinter.Frame(mf2, width=180, height=50, bg="#e2e6e2")
mf2_2.pack(side=tkinter.RIGHT)


class Plot:
    def __init__(self, id, x, y, color):
        self.id = id
        self.x = x
        self.y = y
        self.color = color


class Axis:
    def __init__(self, top, judul, labelx, labely, width=4.0, height=1.1, type=1):
        self.master = top
        self.labelx = labelx
        self.labely = labely
        self.title = judul
        self.fig = Figure(figsize=(width, height))
        self.fig.set_facecolor('#e2e6e2')
        self.grafik_windows = FigureCanvasTkAgg(self.fig, self.master)
        self.ax = self.fig.add_subplot(111)
        self.grafik_windows.get_tk_widget().pack()
        self.Attribute()
        box = self.ax.get_position()
        if type == 1:
            self.ax.set_position([box.x0 + 0.01, box.y0 + box.height * 0.18,
                                  box.width * 1, box.height * 0.75])
        else:
            self.ax.set_position([box.x0 + box.width * 0.1, box.y0 + box.height * 0.05,
                                  box.width * 0.9, box.height * 0.9])
        self.toolbar = NavigationToolbar2Tk(self.grafik_windows, self.master)
        self.toolbar.config(background='#e2e6e2')
        self.toolbar._message_label.config(background='#e2e6e2')
        self.toolbar.update()

        def on_key_press_1(event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, self.grafik_windows, self.toolbar)

        self.grafik_windows.mpl_connect("key_press_event", on_key_press_1)

    def Attribute(self):
        self.ax.set_title(self.title, fontsize=8)
        self.ax.set_xlabel(self.labelx, fontsize=8)
        self.ax.set_ylabel(self.labely, fontsize=8)
        self.ax.tick_params(direction='in', labelsize=6)

    def draw_plot(self):
        self.ax.clear()
        self.Attribute()
        for item in self.plotlist:
            self.ax.plot(item.x, item.y, color=item.color, linewidth=1)
        self.grafik_windows.draw()

    def plot(self, x, y, color='blue'):
        self.plotlist = []
        self.add_plot(0, x, y, color)

    def add_plot(self, id, x, y, color='blue'):
        for i, item in enumerate(self.plotlist):  # Jika ada plot dengan id yg sama
            if item.id == id:
                self.plotlist[i] = Plot(id, x, y, color)
                self.draw_plot()
                return

        self.plotlist += [Plot(id, x, y, color)]  # Jika belum ada plot dengan id yang ditentukan
        self.draw_plot()

    def clearfig(self):
        self.ax.clear()
        self.Attribute()
        self.grafik_windows.draw()


UpView = tkinter.Frame(MainPos1, width=368, height=400, background='#e2e6e2')
UpView.pack(padx=5)
UpView.pack_propagate(0)

axuv = Axis(UpView, "Transversal Angle Plane", 'Flexion/ Extension', 'Adduction/ Abduction', width=2, height=2, type=2)

MainPos2 = tkinter.Frame(MainPos, width=1050, height=150, background='#e2e6e2')
MainPos2.pack()
MainPos2.pack_propagate(0)
Ax1Pos = tkinter.Frame(MainPos2, width=260, height=150, background='#e2e6e2')
Ax1Pos.pack(side=tkinter.LEFT)
Ax1Pos.pack_propagate(0)
Ax2Pos = tkinter.Frame(MainPos2, width=260, height=150, background='#e2e6e2')
Ax2Pos.pack(side=tkinter.LEFT)
Ax2Pos.pack_propagate(0)
Ax3Pos = tkinter.Frame(MainPos2, width=260, height=150, background='#e2e6e2')
Ax3Pos.pack(side=tkinter.LEFT)
Ax3Pos.pack_propagate(0)
Ax4Pos = tkinter.Frame(MainPos2, width=260, height=150, background='#e2e6e2')
Ax4Pos.pack(side=tkinter.LEFT)
Ax4Pos.pack_propagate(0)

ax1 = Axis(Ax1Pos, "Flexion/Extension", 't', 'Theta')
ax2 = Axis(Ax2Pos, "Adduction/Abduction", 't', 'Phi')
ax3 = Axis(Ax3Pos, "Torque", 't', 'Torque')
ax4 = Axis(Ax4Pos, "Error", 't', 'Error')


def inverse(x):
    M_invers = np.zeros([2, 2])
    I = np.identity(2)
    y = np.zeros([4, 4])

    for a in range(2):
        for b in range(2):
            y[a][b] = x[a][b]
            y[a][b + 2] = I[a][b]
    for a in range(2):
        for b in range(4):
            if b != a:
                c = y[b][a] / y[a][a]
                for d in range(4):
                    y[b][d] = y[b][d] - c * y[a][d]
    for a in range(2):
        c = y[a][a]
        for b in range(4):
            y[a][b] = y[a][b] / c
    for a in range(2):
        for b in range(2):
            M_invers[a][b] = y[a][b + 2]

    return M_invers


def function(teta_1, teta_2, tetadot1, tetadot2):
    tetadotdot1 = (tau1[-1] - (massa_t * panjang_t ** 2 * tetadot1) / 3 - massa_t * grav * a_t * panjang_t * mt.cos(
        teta_2) * mt.sin(teta_1) + massa_t * a_t ** 2 * panjang_t ** 2 * tetadot2 * mt.sin(2 * teta_2) * tetadot1) / (
                              massa_t * a_t ** 2 * panjang_t ** 2 * mt.cos(teta_2) ** 2)
    tetadotdot2 = (tau2[-1] - (massa_t * panjang_t ** 2 * a_t ** 2 * mt.sin(
        2 * teta_2) * tetadot1 ** 2) / 2 - massa_t * grav * a_t * panjang_t * mt.cos(teta_1) * mt.sin(teta_2)) / (
                              massa_t * panjang_t ** 2 * a_t ** 2 + (massa_t * panjang_t ** 2) / 3)

    return [tetadotdot1, tetadotdot2]


def runge_kutta(t_1, t_2, ttd_1, ttd_2):
    k_1 = np.zeros([2, 1])
    k_2 = np.zeros([2, 1])
    k_3 = np.zeros([2, 1])
    k_4 = np.zeros([2, 1])

    tetadotdot = function(t_1, t_2, ttd_1, ttd_2)
    k_1[0] = (h / 2) * tetadotdot[0]
    k_1[1] = (h / 2) * tetadotdot[1]
    tetadotdot = function(t_1 + (h * (ttd_1 + (k_1[0] / 2))) / 2, t_2 + (h * (ttd_2 + (k_1[1] / 2))) / 2,
                          ttd_1 + k_1[0], ttd_2 + k_1[1])
    k_2[0] = (h / 2) * tetadotdot[0]
    k_2[1] = (h / 2) * tetadotdot[1]
    tetadotdot = function(t_1 + (h * (ttd_1 + (k_1[0] / 2))) / 2, t_2 + (h * (ttd_2 + (k_1[1] / 2))) / 2,
                          ttd_1 + k_2[0], ttd_2 + k_2[1])
    k_3[0] = (h / 2) * tetadotdot[0]
    k_3[1] = (h / 2) * tetadotdot[1]
    tetadotdot = function(t_1 + (h * (ttd_1 + k_3[0])), t_2 + (h * (ttd_2 + k_3[1])), ttd_1 + (2 * k_3[0]),
                          ttd_2 + (2 * k_3[1]))
    k_4[0] = (h / 2) * tetadotdot[0]
    k_4[1] = (h / 2) * tetadotdot[1]

    tetadot1_n = ttd_1 + (k_1[0] + 2 * k_2[0] + 2 * k_3[0] + k_4[0]) / 3
    tetadot2_n = ttd_2 + (k_1[1] + 2 * k_2[1] + 2 * k_3[1] + k_4[1]) / 3

    teta1_n = t_1 + h * (tetadot1_n + ((k_1[0] + k_2[0] + k_3[0]) / 3))
    teta2_n = t_2 + h * (tetadot2_n + ((k_1[1] + k_2[1] + k_3[1]) / 3))

    return teta1_n, teta2_n, tetadot1_n, tetadot2_n


def glWin():
    # SetupPixelFormat
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    glShadeModel(GL_SMOOTH)  # // Enables Smooth Color Shading
    glClearDepth(1.0)  # // Depth Buffer Setup
    glEnable(GL_DEPTH_TEST)  # // Enable Depth Buffer
    glDepthFunc(GL_LESS)  # // The Type Of Depth Test To Do

    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glEnable(GL_TEXTURE_2D)

    Sphere = gluNewQuadric()
    cylinder = gluNewQuadric()
    disk = gluNewQuadric()

    gluQuadricNormals(Sphere, GLU_SMOOTH)  # // Create Smooth Normals
    gluQuadricNormals(cylinder, GLU_SMOOTH)  # // Create Smooth Normals
    gluQuadricNormals(disk, GLU_SMOOTH)  # // Create Smooth Normals

    mat_specular = [8.0, 8.0, 1.0, 0.0]
    mat_shinines = 40.0
    light_position = [120.6, 14.0, 41.0, 10.7]

    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_BACK, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shinines)
    glMaterialfv(GL_BACK, GL_SHININESS, mat_shinines)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT3, GL_SPECULAR, mat_specular)
    glLightfv(GL_LIGHT1, GL_POSITION, light_position)
    glLightfv(GL_LIGHT2, GL_POSITION, light_position)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)
    glEnable(GL_LIGHT3)
    glDepthFunc(GL_LEQUAL)


def render1(teta1, teta2):
    teta1_draw = teta1-(np.pi/2)
    teta2_draw = teta2+(np.pi/2)

    glLoadIdentity()
    glEnable(GL_LIGHTING)

    xpos = -2 / 5
    ypos = -0 / 5
    zpos = -15 / 5

    teta1_degree = (teta1 * 180) / np.pi
    teta2_degree = (teta2 * 180) / np.pi
    teta1_dedraw = (teta1_draw * 180) / np.pi
    teta2_dedraw = (teta2_draw * 180) / np.pi

    tp = 0.130  # ; //panjang tangan
    tl = 0.1  # ; //lebar tangan
    tt = 0.0175  # ;//tebal tangan

    # print(panjang_1 * mt.cos(teta1_draw) * mt.sin(teta2_draw), panjang_1 * mt.sin(teta1) * mt.cos(teta2))
    # print(panjang_1 * mt.sin(teta1_draw) * mt.sin(teta2_draw), -panjang_1 * mt.cos(teta1) * mt.cos(teta2))
    # print(panjang_1 * mt.cos(teta2_draw), -panjang_1 * mt.sin(teta2))

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    gluSphere(gluNewQuadric(), 0.09, 32, 32)
    glPopMatrix()

    h1 = 0 #5
    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glRotatef(teta1_dedraw-h1, 0.0, 0.0, 1.0)
    glRotatef(teta2_dedraw-h1, 0.0, 1.0, 0.0)
    gluCylinder(gluNewQuadric(), 0.080, 0.060, panjang_1, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glTranslatef(panjang_1 * mt.cos(teta1_draw-(h1*np.pi/180)) * mt.sin(teta2_draw-(h1*np.pi/180)),
                 panjang_1 * mt.sin(teta1_draw-(h1*np.pi/180)) * mt.sin(teta2_draw-(h1*np.pi/180)),
                 panjang_1 * mt.cos(teta2_draw-(h1*np.pi/180)))
    gluSphere(gluNewQuadric(), 0.080, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glRotatef(teta1_dedraw, 0.0, 0.0, 1.0)
    glRotatef(teta2_dedraw, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, panjang_1)
    gluCylinder(gluNewQuadric(), 0.065, 0.035, panjang_2, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glTranslatef((panjang_1+panjang_2) * mt.cos(teta1_draw) * mt.sin(teta2_draw), (panjang_1+panjang_2) * mt.sin(teta1_draw) * mt.sin(teta2_draw), (panjang_1+panjang_2) * mt.cos(teta2_draw))
    gluSphere(gluNewQuadric(), 0.040, 32, 32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(xpos, ypos, zpos)
    glTranslatef((panjang_1+panjang_2) * mt.cos(teta1_draw) * mt.sin(teta2_draw), (panjang_1+panjang_2) * mt.sin(teta1_draw) * mt.sin(teta2_draw), (panjang_1+panjang_2) * mt.cos(teta2_draw))
    # glRotatef(-teta3*180/np.pi, 0.0, 1.0, 0.0)
    glRotatef(teta1_degree, 0.0, 0.0, 1.0)
    glRotatef(teta2_degree, 1.0, 0.0, 0.0)
    glRotatef(-45, 0.0, 1.0, 0.0)
    glRotatef(-90, 1.0, 0.0, 0.0)

    # hand
    glRotate(-180, 1, 0, 0)  # ;
    glRotate(-45, 0, 0, 1)  # ;
    # // gldisable(gl_lighting);
    glEnable(GL_LIGHTING)  # ;
    glBegin(GL_POLYGON)  # ; //awal poligon  atap
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, 0)  # ;   //posisi dalam x y z  +tt
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, tp)  # ;
    glEnd()  # ;              //akhir poligon

    glBegin(GL_POLYGON)  # ;     //dasar -tt
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, tp)  # ;
    glEnd()

    glBegin(GL_POLYGON)  # ;   //samping kiri -t1
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, tp)  # ;
    glEnd()

    glBegin(GL_POLYGON)  # ;   //samping kanan +tl
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, tt, tp)  # ;
    glEnd()

    glBegin(GL_POLYGON)  # ;    //depan sumbu z +tp
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, tp)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, tp)  # ;
    glEnd()

    glBegin(GL_POLYGON)  # ;   //belakang sumbu z 0
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(tl, -tt, 0)  # ;
    glColor3f(1 / 3, 1 / 3, 1 / 3)
    glVertex3f(-tl, -tt, 0)  # ;
    glEnd()


    # {first segment}
    # {centre fingers}
    jarip = 0.025  # ;
    jarip1 = 0.023  # ;
    jarip2 = 0.027  # ;
    glTranslate(0, 0, tp)  # ; {ref} //pindahkan referensi koordinat
    glRotate(360, 1, 0, 0)  # ;   {rotation1}
    # glEnable(GL_LIGHTING)  # ;
    gluCylinder(gluNewQuadric(), 0.0080, 0.0075, jarip, 32, 10)  # ;    //jari tengan dengan panjang jarip
    gluSphere(gluNewQuadric(), 0.0080, 32, 32)  # ; //sendi

    # {pointer finger}
    jarispace = 0.05  # ;
    glTranslate(jarispace, 0, 0)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.0075, 0.0075, jarip, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)  # ;

    # {tumb}
    glTranslate(jarispace, 0, 0)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.0095, 0.0095, jarip, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0097, 32, 32)  # ;

    # {jari manis}
    glTranslate(-3 * jarispace, 0, 0)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.007, 0.007, jarip, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)  # ;

    # {kelingking}
    glTranslate(-jarispace, 0, 0)  # ; {ref}
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)  # ;
    gluCylinder(gluNewQuadric(), 0.007, 0.007, jarip, 32, 10)  # ;

    # {second segment}
    # {kelingking}
    glTranslate(0, 0, jarip)  # ; {ref}
    glRotate(10, 1, 0, 0)  # ;   {rotation1}
    gluCylinder(gluNewQuadric(), 0.007, 0.007, jarip1, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)  # ;

    glTranslate(0, 0, jarip1)  # ; {ref}
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)  # ;

    glTranslate(0, 0, -jarip1)  # ; {ref}

    # {jari manis}
    glTranslate(jarispace, 0, 0)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.007, 0.007, jarip1, 32, 32)  # ;
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)  # ;

    # {jari tengah}
    glTranslate(jarispace, 0, 0)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.007, 0.007, jarip1, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0072, 32, 32)  # ;

    # {jari telunjuk}
    glTranslate(jarispace, 0, 0)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.0075, 0.0075, jarip1, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)  # ;

    # {tumb}
    glTranslate(jarispace, 0, 0)  # ; {ref}
    # //jarip1:=0.15;
    gluCylinder(gluNewQuadric(), 0.0095, 0.0095, jarip1, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0097, 32, 32)  # ;
    glTranslate(0, 0, jarip1)  # ; {ref}
    gluSphere(gluNewQuadric(), 0.0097, 32, 32)  # ;

    # {third segment}

    # {telunjuk}
    glTranslate(-jarispace, 0, 0)  # ; {ref}
    glRotate(10, 1, 0, 0)  # ;   {rotation1}
    gluCylinder(gluNewQuadric(), 0.0075, 0.0065, jarip2, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)  # ;
    glTranslate(0, 0, jarip2)  # ; {ref}
    gluSphere(gluNewQuadric(), 0.0067, 32, 32)  # ;

    # {jaritengah}
    glTranslate(-jarispace, 0, -jarip2)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.0075, 0.0065, jarip2, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)  # ;
    glTranslate(0, 0, jarip2)  # ; {ref}
    gluSphere(gluNewQuadric(), 0.0067, 32, 32)  # ;

    # {jari manis}
    glTranslate(-jarispace, 0, -jarip2)  # ; {ref}
    gluCylinder(gluNewQuadric(), 0.0075, 0.0065, jarip2, 32, 10)  # ;
    gluSphere(gluNewQuadric(), 0.0077, 32, 32)  # ;
    glTranslate(0, 0, jarip2)  # ; {ref}
    gluSphere(gluNewQuadric(), 0.0067, 32, 32)  # ;
    glPopMatrix()


def Start():
    global Status

    Status = 1
    pass


def Stop():
    global Status

    Status = 2
    pass


def Clear():
    global Status, t, h, teta_1, teta_2, ttn_1, ttn_2, wqt, tau1, tau2, reftheta, refphi, theta, phi, RMSE, \
        ebef_theta, ebef_phi, sum_jum_theta, sum_jum_phi, err_theta, err_phi

    ###INIT
    Status = 0
    t = 0.0
    h = 0.05
    teta_1, teta_2 = 0, 0
    wqt = 0

    ttn_1, ttn_2 = [], []

    tau1 = [10]
    tau2 = [0.5]

    reftheta, refphi = [], []
    theta, phi = [], []

    RMSE = 0
    ebef_theta, ebef_phi = 0, 0
    sum_jum_theta, sum_jum_phi = 0, 0
    err_theta, err_phi = [0], [0]

    ax1.clearfig()
    ax2.clearfig()
    ax3.clearfig()
    ax4.clearfig()
    axuv.clearfig()
    pass


def About():
    mb.showinfo("About", "PID Controller Shoulder Movement by Dzikrur Rohmani Z R M H.\n\nBiomedical Engineering Department\nInstitut Teknologi \
Sepuluh Nopember (ITS) Surabaya")


def Close():
    global Running

    Running = False


mf2_1_button1 = tkinter.Button(mf2_1, width=15, text="START", command=Start)
mf2_1_button1.pack(pady=5)
mf2_1_button2 = tkinter.Button(mf2_2, width=15, text="STOP", command=Stop)
mf2_1_button2.pack(pady=5)
mf2_1_button3 = tkinter.Button(mf2_1, width=15, text="CLEAR", command=Clear)
mf2_1_button3.pack(pady=5)
mf2_1_button4 = tkinter.Button(mf2_2, width=15, text="ABOUT", command=About)
mf2_1_button4.pack(pady=5)
mf2_1_button4 = tkinter.Button(TombolPos, width=15, text="CLOSE", command=Close)
mf2_1_button4.pack(pady=5)

rmse = tkinter.Frame(TombolPos, bg="#e2e6e2")
rmse.pack(pady=(10, 10))
rmse1 = tkinter.Label(rmse, text="RMSE\t=", bg="#e2e6e2")
rmse1.pack(side=tkinter.LEFT)
rmse2 = tkinter.Entry(rmse, width=10, justify=tkinter.CENTER)
rmse2.pack(padx=10, side=tkinter.RIGHT)

if __name__ == "__main__":
    ###constant variable
    grav = 9.8
    tetadot = np.array(([0.0], [0.0]))

    ###input initial condition
    ###UPPERARM INISIAL
    panjang_1 = 0.383  # upper arm length
    massa_1 = (0.022 * (73 * grav) + 4.76) / grav  # upper arm
    a_1 = 0.507

    ###FOREARM INISIAL
    panjang_2 = 0.517  # lower arm length
    massa_2 = (0.013 * (73 * grav) + 2.41) / grav  # forearm
    a_2 = 0.417

    ###HAND INISIAL
    panjang_3 = 0.130  # hand
    massa_3 = (0.005 * (73 * grav) + 0.75) / grav  # hand
    a_3 = 0.515

    ###single pendulum approach
    panjang_t = panjang_1 + panjang_2 + panjang_3
    massa_t = massa_1 + massa_2 + massa_3
    pusat_m = ((massa_1 * a_1 * panjang_1) + (massa_2 * (a_2 * panjang_2 + panjang_1)) + (
                massa_3 * (a_3 * panjang_3 + panjang_2 + panjang_1))) / massa_t
    a_t = pusat_m / panjang_t

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0., 0.69, 0.69, 0.2)
    glViewport(0, 0, display[0], display[1])
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50.0, display[0] / display[1], 1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    ###INIT
    Status = 0
    t = 0.0
    h = 0.001
    wqt = 0

    tau1 = [10]
    tau2 = [0.5]

    ttn = 0
    ppn = 0

    reftheta, refphi = [], []
    theta, phi = [], []

    RMSE = 0
    ebef_theta, ebef_phi = 0, 0
    sum_jum_theta, sum_jum_phi = 0, 0
    err_theta, err_phi = [0], [0]

    Running = True
    while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False

        glWin()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        render1(ttn, ppn)
        if Status == 1:
            # PPID_theta = kp_theta * err_theta[-1]
            # sum_jum_theta += err_theta[-1] * h
            # IPID_theta = ki_theta * sum_jum_theta
            # vel_theta = (err_theta[-1] - ebef_theta) / h
            # DPID_theta = kd_theta * vel_theta
            # tau1 += [PPID_theta + IPID_theta + DPID_theta]
            #
            # PPID_phi = kp_phi * err_phi[-1]
            # sum_jum_phi += err_phi[-1] * h
            # IPID_phi = ki_phi * sum_jum_phi
            # vel_phi = (err_phi[-1] - ebef_phi) / h
            # DPID_phi = kd_phi * vel_phi
            # tau2 += [PPID_phi + IPID_phi + DPID_phi]

            # ebef_theta = err_theta[-1]
            # ebef_phi = err_phi[-1]
            v1 = 0.5 * (err_theta[-1]**2)
            v2 = 0.5 * (err_phi[-1]**2)
            try:
                gradien1 = v1 * theta[-1] * (1 - theta[-1])
                gradien2 = v2 * phi[-1] * (1 - phi[-1])
            except:
                gradien1 = v1 * ttn * (1 - ttn)
                gradien2 = v2 * ppn * (1 - ppn)
            tau1 += [tau1[-1] - (0.9 * gradien1)]
            tau2 += [tau2[-1] - (0.9 * gradien2)]
            reftheta += [np.exp(-2 * t) * np.cos(10 * np.pi * t)]
            refphi += [0]
            theta_n, phi_n, thetadot_n, phidot_n = runge_kutta(ttn, ppn, tetadot[0], tetadot[1])
            tetadot[0] = thetadot_n
            tetadot[1] = phidot_n
            theta += [theta_n]
            phi += [phi_n]
            ttn = theta_n
            ppn = phi_n
            err_theta += [(reftheta[-1] - theta[-1])]
            err_phi += [(refphi[-1] - phi[-1])]
            RMSE += err_theta[-1] ** 2
            RMSE += err_phi[-1] ** 2
            RMSE /= 2
            wqt = wqt + 1
            t += h

            ax1.plot((np.arange(wqt)), reftheta)
            ax2.plot((np.arange(wqt)), refphi)
            ax1.add_plot(1, (np.arange(wqt)), theta, color="red")
            ax2.add_plot(1, (np.arange(wqt)), phi, color="red")
            axuv.plot(reftheta, refphi)
            axuv.add_plot(1, theta, phi, color="red")
            ax3.plot(np.arange(wqt + 1), tau1)
            ax3.add_plot(1, np.arange(wqt + 1), tau2, color="red")
            ax4.plot(np.arange(wqt + 1), err_theta)
            ax4.add_plot(1, np.arange(wqt + 1), err_phi, color="red")
            rmse2.delete(0, tkinter.END)
            # rmse2.insert(0, '{:2.5f}'.format(np.sqrt(RMSE)))

        pygame.display.flip()
        pygame.time.wait(1)
        try:
            window.update()
        except tkinter.TclError:
            Running = False
    pygame.quit()
