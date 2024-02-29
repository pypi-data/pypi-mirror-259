from django import forms
from .models import FileData, ImageData

class FileUpload(forms.ModelForm):
	class Meta:
		model = FileData
		fields = ('file', 'description')
		def save(self):
			file = super(FileUpload, self).save()
			return file


class ImageUpload(forms.ModelForm):
	class Meta:
		model = ImageData
		fields = ('file', 'description')
		def save(self):
			image = super(ImageUpload, self).save()
			return image


class ImageWidget(forms.widgets.ClearableFileInput):
	template_name = "forms/widgets/image_widget.html"
