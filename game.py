Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: /home/student/neriya21_lab10/meet2019y1lab10/lab_10.py ======
Traceback (most recent call last):
  File "/home/student/neriya21_lab10/meet2019y1lab10/lab_10.py", line 107, in <module>
    pieces[p1,p2,p3,p4,p5,p6,p7,p8,p9]
NameError: name 'pieces' is not defined
>>> 
====== RESTART: /home/student/neriya21_lab10/meet2019y1lab10/lab_10.py ======
Traceback (most recent call last):
  File "/home/student/neriya21_lab10/meet2019y1lab10/lab_10.py", line 147, in <module>
    turtle.register_shape(p7)
  File "<string>", line 8, in register_shape
  File "/usr/lib/python3.6/turtle.py", line 1133, in register_shape
    shape = Shape("image", self._image(name))
  File "/usr/lib/python3.6/turtle.py", line 479, in _image
    return TK.PhotoImage(file=filename)
  File "/usr/lib/python3.6/tkinter/__init__.py", line 3545, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "/usr/lib/python3.6/tkinter/__init__.py", line 3501, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "gif7.gif": no such file or directory
>>> 
>>> 
