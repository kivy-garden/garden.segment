#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

'''
Segment
=======

The :class:`Segment` widget is a widget for displaying segment. 

'''

__all__ = ('Segment')

__title__ = 'garden.segment'
__version__ = '0.1'
__author__ = 'julien@hautefeuille.eu'

import kivy
kivy.require('1.7.1')
from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import BoundedNumericProperty
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.graphics import (Color, Ellipse, Line, Rectangle, Mesh, Scale, 
Translate, PopMatrix, PushMatrix)
from kivy.utils import get_color_from_hex
from kivy.graphics.transformation import Matrix
from kivy.uix.stencilview import StencilView

class Segment(RelativeLayout):
    '''
    Segment class

    '''

    scale = NumericProperty(0.5)
    color = ListProperty(get_color_from_hex('2fc827'))
    value = StringProperty("E.")

    def __init__(self, **kwargs):
        
        super(Segment, self).__init__(**kwargs)

        segment_dict = {
            'seg_1' : [
                20, 215, 0, 0,
                35, 230, 0, 0,
                95, 230, 0, 0,
                110, 215, 0, 0,
                95, 200, 0, 0,
                35, 200, 0, 0,
                ],
            'seg_2' : [
                15, 210, 0, 0,
                30, 195, 0, 0,
                30, 135, 0, 0,
                15, 120, 0, 0,
                0, 135, 0, 0,
                0, 195, 0, 0,
                ],
            'seg_3' : [
                115, 210, 0, 0,
                130, 195, 0, 0,
                130, 135, 0, 0,
                115, 120, 0, 0,
                100, 135, 0, 0,
                100, 195, 0, 0,
                ],
            'seg4' : [
                20, 115, 0, 0,
                35, 130, 0, 0,
                95, 130, 0, 0,
                110, 115, 0, 0,
                95, 100, 0, 0,
                35, 100, 0, 0,
                ]
            }

        self.bind(pos=self._update_canvas, size=self._update_canvas)



    def _update_canvas(self, *args):

        matrix_1 = 

        if self.value == "E.":
            pass
        
        with self.canvas:
            self.canvas.clear()
            Color(self.color[0], self.color[1], self.color[2], 100)
            Scale(self.scale)

            self.segment_1 = Mesh(vertices=[
                20, 215, 0, 0,
                35, 230, 0, 0,
                95, 230, 0, 0,
                110, 215, 0, 0,
                95, 200, 0, 0,
                35, 200, 0, 0,
                ], indices=[0,1,2,3,4,5], mode='triangle_fan')
            
            self.segment_2 = Mesh(vertices=[
                15, 210, 0, 0,
                30, 195, 0, 0,
                30, 135, 0, 0,
                15, 120, 0, 0,
                0, 135, 0, 0,
                0, 195, 0, 0,
                ], indices=[0,1,2,3,4,5], mode='triangle_fan')
            
            self.segment_3 = Mesh(vertices=[
                115, 210, 0, 0,
                130, 195, 0, 0,
                130, 135, 0, 0,
                115, 120, 0, 0,
                100, 135, 0, 0,
                100, 195, 0, 0,
                ], indices=[0,1,2,3,4,5], mode='triangle_fan')

            self.segment_4 = Mesh(vertices=[
                20, 115, 0, 0,
                35, 130, 0, 0,
                95, 130, 0, 0,
                110, 115, 0, 0,
                95, 100, 0, 0,
                35, 100, 0, 0,
                ], indices=[0,1,2,3,4,5], mode='triangle_fan')

            self.segment_5 = Mesh(vertices=[
                15, 110, 0, 0,
                30, 95, 0, 0,
                30, 35, 0, 0,
                15, 20, 0, 0,
                0, 35, 0, 0,
                0, 95, 0, 0,
                ], indices=[0,1,2,3,4,5], mode='triangle_fan')

            self.segment_6 = Mesh(vertices=[
                115, 110, 0, 0,
                130, 95, 0, 0,
                130, 35, 0, 0,
                115, 20, 0, 0,
                100, 35, 0, 0,
                100, 95, 0, 0,
                ], indices=[0,1,2,3,4,5], mode='triangle_fan')

            self.segment_7 = Mesh(vertices=[
                20, 15, 0, 0,
                35, 30, 0, 0,
                95, 30, 0, 0,
                110, 15, 0, 0,
                95, 0, 0, 0,
                35, 0, 0, 0,
                ], indices=[0,1,2,3,4,5])
            
            thept = Ellipse(pos=(135, 0), size=(25,25), segments=360)

            # self.segment_1.mode = 'triangle_fan'
            # self.segment_2.mode = 'triangle_fan'
            # self.segment_3.mode = 'triangle_fan'
            # self.segment_4.mode = 'triangle_fan'
            # self.segment_5.mode = 'triangle_fan'
            # self.segment_6.mode = 'triangle_fan'
            # self.segment_7.mode = 'triangle_fan'
            
class SegmentTestApp(App):
    def build(self):
        box = GridLayout(cols=3, padding=20)

        box.add_widget(Segment())
        box.add_widget(Segment())
        box.add_widget(Segment())
        box.add_widget(Segment())
        box.add_widget(Segment())
        box.add_widget(Segment())

        return box
            
if __name__ in ('__main__'):
    SegmentTestApp().run()