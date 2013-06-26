Segment class
#############

The class`Segment` widget is a widget for displaying segment in Kivy.

- The value property of segment must be a string.
- The scale property of segment must be a float.
- The color property of segment must be a string.

Ex:

seg = Segment(scale=0.3, value="A.")

Are permitted : 0 1 2 3 4 5 6 7 8 9 and 0. 1. 2. 3. 4. 5. 6. 7. 8. 9.

And this : 

A b C d E F and A. b. C. d. E. F.

http://youtu.be/EkJ7Pp0p7zA