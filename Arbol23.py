class Node:
	def __init__(self, apellido, par = None):
		self.apellido = list([apellido])
		self.padre = par
		self.hijo = list()
		
	def __str__(self):
		if self.padre:
			return str(self.padre.apellido) + ' : ' + str(self.apellido)
		return 'raiz : ' + str(self.apellido)
	
	def __lt__(self, node):
		return self.apellido[0] < node.apellido[0]
		
	def _isLeaf(self):
		return len(self.hijo) == 0
			
	# Agregar nuevo nivel
	def _add(self, new_node):
		for hijo in new_node.hijo:
			hijo.padre = self
		self.apellido.extend(new_node.apellido)
		self.apellido.sort()
		self.hijo.extend(new_node.hijo)
		if len(self.hijo) > 1:
			self.hijo.sort()
		if len(self.apellido) > 2:
			self._split()
	
	# buscar noso correcto
	def _agregar(self, new_node):
		if self._isLeaf():
			self._add(new_node)
		elif new_node.apellido[0] > self.apellido[-1]:
			self.hijo[-1]._agregar(new_node)
		else:
			for i in range(0, len(self.apellido)):
				if new_node.apellido[0] < self.apellido[i]:
					self.hijo[i]._agregar(new_node)
					break
	
	# cuando existen mas de 3 nodos se crea  nuevo nivel	
	def _split(self):
		left_hijo = Node(self.apellido[0], self)
		right_hijo = Node(self.apellido[2], self)
		if self.hijo:
			self.hijo[0].padre = left_hijo
			self.hijo[1].padre = left_hijo
			self.hijo[2].padre = right_hijo
			self.hijo[3].padre = right_hijo
			left_hijo.hijo = [self.hijo[0], self.hijo[1]]
			right_hijo.hijo = [self.hijo[2], self.hijo[3]]
					
		self.hijo = [left_hijo]
		self.hijo.append(right_hijo)
		self.apellido = [self.apellido[1]]
		
		if self.padre:
			if self in self.padre.hijo:
				self.padre.hijo.eliminar(self)
			self.padre._add(self)
		else:
			left_hijo.padre = self
			right_hijo.padre = self
			
		
	def _buscar(self, item):

		if item in self.apellido:
			return item
		elif self._isLeaf():
			return False
		elif item > self.apellido[-1]:
			return self.hijo[-1]._buscar(item)
		else:
			for i in range(len(self.apellido)):
				if item < self.apellido[i]:
					return self.hijo[i]._buscar(item)
		
	def _eliminar(self, item):
		pass
		
	
	def _preorden(self):
		print (self) 
		for hijo in self.hijo:
			hijo._preorden()
	
class arbolmway:
	def __init__(self):
		print("Arbol __init__")
		self.raiz = None
		
	def agregar(self, item):
		print("agregarar contacto: " + str(item))
		if self.raiz is None:
			self.raiz = Node(item)
		else:
			self.raiz._agregar(Node(item))
			while self.raiz.padre:
				self.raiz = self.raiz.padre
		return True
	
	def buscar(self, item):
		return self.raiz._buscar(item)
		
	def eliminar(self, item):
		self.raiz.eliminar(item)
		
		
	def preorden(self):
		print ('----Preorden----')
		self.raiz._preorden()
		
arbol23 = arbolmway()

