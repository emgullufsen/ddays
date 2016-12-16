from GUI import Application, ScrollableView, Document, Window, Cursor, rgb
from GUI.Files import FileType
from GUI.Geometry import pt_in_rect, offset_rect, rects_intersect
from GUI.StdColors import black, red


class Blee(Application):

	def __init__(self):
		Application.__init__(self)

	def open_app(self):
		self.new_cmd()

	def make_window(self, document):
		win = Window(size = (600,400), document = document)
		view = ScrollableView(model = document, extent = (1000, 1000), scrolling = 'hv')
		win.place(view, left = 0, top = 0, right = 0, bottom = 0, sticky = 'nsew')
		win.show()

	def make_document(self, fileref):
		return Document()


Blee().run()