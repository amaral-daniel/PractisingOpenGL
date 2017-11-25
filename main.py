import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
     (0.5,  0.5, 0.0),  # top right
     (0.5, -0.5, 0.0),  # bottom right
    (-0.5, -0.5, 0.0),  # bottom left
    (-0.5,  0.5, 0.0)   # top left
)
edges = (  # note that we start from 0!
    (0, 1, 3),   # first triangle
    (1, 2, 3)    # second triangle
)

def setShaders():
    v = glCreateShader(GL_VERTEX_SHADER)
    f = glCreateShader(GL_FRAGMENT_SHADER)

    with open ("simpleshader.frag", "r") as myfile:
        ftext=myfile.readlines()
    with open ("simpleshader.vert", "r") as myfile:
        vtext=myfile.readlines()

    glShaderSource(v, vtext)
    glShaderSource(f, ftext)

    glCompileShader(v)
    glCompileShader(f)

    p = glCreateProgram()
    glAttachShader(p,v)
    glAttachShader(p,f)

    glLinkProgram(p)
    glUseProgram(p)


def Cube():
    glBegin(GL_TRIANGLES)
    for edge in edges:
        for vertex in edge:
            glColor4f(0.5,0.5,0.5,1.0)
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0,-10)
    print("antes de setar os shaders!!!!!!!!!!!!!!")
    setShaders()
    print("setou os shaders!!!!!!!!!!!!!!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        #glDrawArrays(GL_TRIANGLE_STRIP,0,4)
        pygame.display.flip()
        pygame.time.wait(10)


main()
