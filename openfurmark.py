import moderngl_window as mglw
from moderngl_window.text.bitmapped import TextWriter2D
import sys

import PyQt5    #for pyinstaller
from PyQt5.QtCore import Qt #for pyinstaller
from PyQt5 import QtCore, QtGui, QtOpenGL, QtWidgets #for pyinstaller


class App(mglw.WindowConfig):
    resource_dir = 'resources'
    vsync = False
    # fullscreen = True
    # hidden_window_framerate_limit = 900000

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.quad = mglw.geometry.quad_fs()
        self.program = self.load_program(vertex_shader='programs/vertex.glsl',
                                         fragment_shader='programs/fragment.glsl')
        self.set_uniform('u_resolution', self.window_size)

        self.texture1 = self.load_texture_2d('textures/fur.jpg')
        self.set_uniform('u_texture1', 1)
        self.texture1.use(location=1)

        self.texture2 = self.load_texture_2d('textures/noise.png')
        self.set_uniform('u_texture2', 2)
        self.texture2.use(location=2)

        self.texture3 = self.load_texture_2d('textures/wall.jpg')
        self.set_uniform('u_texture3', 3)
        self.texture3.use(location=3)

        self.tttimer = self.timer
        self.writer = TextWriter2D()
        self.writer.text = "Hello ModernGL!"
        self.writer1 = TextWriter2D()
        self.writer1.text = "https://github.com/Xxianna/FurMark-with-fps.git"

    def set_uniform(self, u_name, u_value):
        try:
            self.program[u_name] = u_value
        except KeyError:
            print(f'{u_name} not used in shader')

    def on_render(self, time, frame_time):
        self.ctx.clear()
        self.set_uniform('u_time', time)
        self.quad.render(self.program)
        if self.tttimer.time:
            self.writer.text = f"FPS: {self.tttimer.fps_average:.2f}"
            self.writer.draw((200, 200), size=30)
            self.writer1.draw((200, 150), size=30)
            # print(f"FPS: {self.tttimer.fps_average:.2f}") #无头模式下使用

def parse_resolution(resolution_str):
    try:
        width, height = map(int, resolution_str.split('x'))
        return width, height
    except ValueError:
        print("Invalid resolution format. Please use the format 'WIDTHxHEIGHT' (e.g., 1920x1080).")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        resolution = parse_resolution(sys.argv[1])
        App.window_size = resolution
    else:
        App.window_size = 1280, 720  # Default resolution

    # mglw.run_window_config(App) #默认模式
    # mglw.run_window_config(App, args=["-wnd", "headless"])  # 无窗口模式
    mglw.run_window_config(App, args=["-wnd", "pyqt5"])  # pyqt5模式 使用时屏蔽“python环境\Lib\site-packages\moderngl_window\context\pyqt5\window.py“中的        
    """
    if self._ctx:
            self.set_default_viewport()
    """