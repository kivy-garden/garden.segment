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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.graphics import Color, Ellipse, Line, Rectangle, Mesh
from kivy.utils import get_color_from_hex
from kivy.graphics.transformation import Matrix

class Segment(Widget):
    '''
    Segment class

    '''


    def __init__(self, **kwargs):
        super(Segment, self).__init__(**kwargs)

        with self.canvas:
            c = get_color_from_hex('efc727')
            Color(c[0], c[1], c[2], 100)
            
            self.segment_1 = Mesh(vertices=[
                20, 215, 0, 0,
                35, 230, 0, 0,
                95, 230, 0, 0,
                110, 215, 0, 0,
                95, 200, 0, 0,
                35, 200, 0, 0,
                ], indices=[0,1,2,3,4,5])

            self.segment_2 = Mesh(vertices=[
                15, 210, 0, 0,
                30, 195, 0, 0,
                30, 135, 0, 0,
                15, 120, 0, 0,
                0, 135, 0, 0,
                0, 195, 0, 0,
                ], indices=[0,1,2,3,4,5])
            
            self.segment_3 = Mesh(vertices=[
                115, 210, 0, 0,
                130, 195, 0, 0,
                130, 135, 0, 0,
                115, 120, 0, 0,
                100, 135, 0, 0,
                100, 195, 0, 0,
                ], indices=[0,1,2,3,4,5])

            self.segment_4 = Mesh(vertices=[
                20, 115, 0, 0,
                35, 130, 0, 0,
                95, 130, 0, 0,
                110, 115, 0, 0,
                95, 100, 0, 0,
                35, 100, 0, 0,
                ], indices=[0,1,2,3,4,5])

            self.segment_5 = Mesh(vertices=[
                15, 110, 0, 0,
                30, 95, 0, 0,
                30, 35, 0, 0,
                15, 20, 0, 0,
                0, 35, 0, 0,
                0, 95, 0, 0,
                ], indices=[0,1,2,3,4,5])

            self.segment_6 = Mesh(vertices=[
                15, 110, 0, 0,
                30, 95, 0, 0,
                30, 35, 0, 0,
                15, 20, 0, 0,
                0, 35, 0, 0,
                0, 95, 0, 0,
                ], indices=[0,1,2,3,4,5])

            self.segment_1.mode = 'triangle_fan'
            self.segment_2.mode = 'triangle_fan'
            self.segment_3.mode = 'triangle_fan'
            self.segment_4.mode = 'triangle_fan'
            self.segment_5.mode = 'triangle_fan'
            self.segment_6.mode = 'triangle_fan'

class SegmentTestApp(App):
        def build(self):
            box = BoxLayout(orientation='vertical', spacing=10, padding=10)
            segment = Segment()
            box.add_widget(segment)
            return box
            
if __name__ in ('__main__'):
    SegmentTestApp().run()