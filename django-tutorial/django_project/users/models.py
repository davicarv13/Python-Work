from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	#Relação de user x profile é de um para um
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	#default define uma imagem padrão caso o user não insira sua imagem
	#upload_to define o diretório para onde as imagens serão upadas
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		#f function só disponível com Python 3.6 ou acima
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):

		#Executa método save da classe pai
		super().save()

		#Abre o image, passando para url de onde ela está
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)

			#Override da imagem maior que 300 pixels
			img.save(self.image.path)

