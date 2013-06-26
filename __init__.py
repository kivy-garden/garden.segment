#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

'''
Segment
=======

The :class:`Segment` widget is a widget for displaying segment.

The value property of segment must be a string.
The scale property of segment must be a float.
The color property of segment must be a string.

Ex::

seg = Segment(scale=0.3, value="A.")

Are permitted : 0 1 2 3 4 5 6 7 8 9 and 0. 1. 2. 3. 4. 5. 6. 7. 8. 9.

and

A b C d E F and A. b. C. d. E. F.

'''

__all__ = ('Segment',)

__title__ = 'garden.segment'
__version__ = '0.2'
__author__ = 'julien@hautefeuille.eu'

import kivy
kivy.require('1.7.1')
from kivy.config import Config
from kivy.app import App
from kivy.properties import StringProperty
from kivy.properties import BoundedNumericProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Ellipse, Mesh, Scale
from kivy.utils import get_color_from_hex


class Segment(RelativeLayout):
    '''
    Segment class

    The class`Segment` widget is a widget for displaying segment.

    The value property of segment must be a string.
    The scale property of segment must be a float.
    The color property of segment must be a string.

    Ex::

    seg = Segment(scale=0.3, value="A.")

    Are permitted : 0 1 2 3 4 5 6 7 8 9 and 0. 1. 2. 3. 4. 5. 6. 7. 8. 9.

    and

    A b C d E F and A. b. C. d. E. F.

    '''

    # Object properties configuration
    scale = BoundedNumericProperty(0.1, min=0.1, max=1, errorvalue=0.2)
    color = StringProperty('2fc827')
    value = StringProperty('A.')

    def __init__(self, **kwargs):     
        super(Segment, self).__init__(**kwargs)

        # Drawing meshes configuration, indices range meshes and mode
        self.indice = xrange(0, 6)
        self.xmode = 'triangle_fan'
        
        # Segment matrix configuration
        seg_1 = [
                20, 215, 0, 0,
                35, 230, 0, 0,
                95, 230, 0, 0,
                110, 215, 0, 0,
                95, 200, 0, 0,
                35, 200, 0, 0,
                ]
        seg_2 = [
                15, 210, 0, 0,
                30, 195, 0, 0,
                30, 135, 0, 0,
                15, 120, 0, 0,
                0, 135, 0, 0,
                0, 195, 0, 0,
                ]
        seg_3 = [
                115, 210, 0, 0,
                130, 195, 0, 0,
                130, 135, 0, 0,
                115, 120, 0, 0,
                100, 135, 0, 0,
                100, 195, 0, 0,
                ]
        seg_4 = [
                20, 115, 0, 0,
                35, 130, 0, 0,
                95, 130, 0, 0,
                110, 115, 0, 0,
                95, 100, 0, 0,
                35, 100, 0, 0,
                ]
        seg_5 = [
                15, 110, 0, 0,
                30, 95, 0, 0,
                30, 35, 0, 0,
                15, 20, 0, 0,
                0, 35, 0, 0,
                0, 95, 0, 0,
                ]
        seg_6 = [
                115, 110, 0, 0,
                130, 95, 0, 0,
                130, 35, 0, 0,
                115, 20, 0, 0,
                100, 35, 0, 0,
                100, 95, 0, 0,
                ]
        seg_7 = [
                20, 15, 0, 0,
                35, 30, 0, 0,
                95, 30, 0, 0,
                110, 15, 0, 0,
                95, 0, 0, 0,
                35, 0, 0, 0,
                ]

        # Drawing association
        type_0 = [seg_1, seg_2, seg_3, seg_5, seg_6, seg_7]
        type_1 = [seg_3, seg_6]
        type_2 = [seg_1, seg_3, seg_4, seg_5, seg_7]
        type_3 = [seg_1, seg_3, seg_4, seg_6, seg_7]
        type_4 = [seg_2, seg_3, seg_4, seg_6]
        type_5 = [seg_1, seg_2, seg_4, seg_6, seg_7]
        type_6 = [seg_1, seg_2, seg_4, seg_5, seg_6, seg_7]
        type_7 = [seg_1, seg_3, seg_6]
        type_8 = [seg_1, seg_2, seg_3, seg_4, seg_5, seg_6, seg_7]
        type_9 = [seg_1, seg_2, seg_3, seg_4, seg_6, seg_7]
        type_A = [seg_1, seg_2, seg_3, seg_4, seg_5, seg_6]
        type_b = [seg_2, seg_4, seg_5, seg_6, seg_7]
        type_C = [seg_1, seg_2, seg_5, seg_7]
        type_d = [seg_3, seg_4, seg_5, seg_6, seg_7]
        type_E = [seg_1, seg_2, seg_4, seg_5, seg_7]
        type_F = [seg_1, seg_2, seg_4, seg_5]

        # Routing association
        self.type_dic = {
                "0" : type_0,
                "0.": type_0,
                "1" : type_1,
                "1.": type_1,
                "2" : type_2,
                "2.": type_2,
                "3" : type_3,
                "3.": type_3,
                "4" : type_4,
                "4.": type_4,
                "5" : type_5,
                "5.": type_5,
                "6" : type_6,
                "6.": type_6,
                "7" : type_7,
                "7.": type_7,
                "8" : type_8,
                "8.": type_8,
                "9" : type_9,
                "9.": type_9,
                "A" : type_A,
                "A.": type_A,
                "b" : type_b,
                "b.": type_b,
                "C" : type_C,
                "C.": type_C,
                "d" : type_d,
                "d.": type_d,
                "E" : type_E,
                "E.": type_E,
                "F" : type_F,
                "F.": type_F,
                }

        # Binding refresh drawing method
        self.bind(
            pos=self._update_canvas, 
            size=self._update_canvas,
            value=self._update_canvas
            )

    def _update_canvas(self, *args):

        with self.canvas:

            # Refresh
            self.canvas.clear()

            # Configure
            Color(
                get_color_from_hex(self.color)[0], 
                get_color_from_hex(self.color)[1], 
                get_color_from_hex(self.color)[2], 100)

            # Scale
            Scale(self.scale)

            # Draw meshes
            def make_mesh(self, ttype, *args):
                ''' Drawing meshes
                '''
                for segment in ttype:
                    Mesh(
                        vertices=segment, 
                        indices=self.indice, 
                        mode=self.xmode
                        )
                if len(self.value) > 1:
                    Ellipse(
                        pos=(135, 0), 
                        size=(25,25), 
                        segments=360
                        )

            # Avoid if session
            for key, val in self.type_dic.items():
                if self.value == key:
                    make_mesh(self, ttype=val)
      

class SegmentTestApp(App):

    def build(self):
        from kivy.clock import Clock
        from kivy.uix.gridlayout import GridLayout
        import random

        def refresh_task(self, *args):
            seg.value = random.choice('123AbCdEF')
            seg1.value = random.choice('123')

        box = GridLayout(cols=8, padding=20)
        seg = Segment(scale=0.3, value="9.")
        seg1 = Segment(scale=0.8, value="A.")
        
        box.add_widget(seg)
        box.add_widget(seg1)

        Clock.schedule_interval(refresh_task, 1)

        return box
            
if __name__ == '__main__':
    SegmentTestApp().run()