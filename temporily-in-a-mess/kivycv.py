#! /usr/bin/env python


# config must be done before any kivy.core.window import
if __name__ == '__main__':
    from kivy.config import Config
    Config.set('graphics','show_cursor',1)
    Config.set('graphics','fullscreen',0)
    # Config.set('graphics','width',640)
    # Config.set('graphics','height',480)
    Config.write()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

import cv2
import numpy as np




class CamApp(App):

    def build(self):
        self.img1 = Image()
        self.img1.on_touch_down = self.on_touch_down
        layout = BoxLayout()
        layout.add_widget(self.img1)
        # opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        # do the matching
        self.orb = cv2.ORB()
        self.kp, self.des = None, None
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        ret, self.frame = self.capture.read()
        Clock.schedule_interval(self.update, 1.0/60.0)
        return layout

    def on_touch_down(self,touch):
        self.kp, self.des = self.orb.detectAndCompute(self.frame,None)
        return True
        
    def update(self, dt):
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        # convert it to texture
        if self.kp != None:
            kp, des = self.orb.detectAndCompute(frame,None)
            matches = self.bf.match(self.des,des)
            matches = sorted(matches, key = lambda x:x.distance)
            print 'len =', len(matches), type(matches[0]), matches[0]
            # frame = cv2.drawMatches(self.frame, self.kp, frame, kp, matches[:10], flags=2)

        buf1 = cv2.flip(frame, -1)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1

    def on_stop(self):
        self.capture.release()

if __name__ == '__main__':
    CamApp().run()

