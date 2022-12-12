from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from PIL import Image

from .models import Product

REQUIRED_FORMATS = ['jpg', 'png']


class ProductImageField(serializers.ImageField):
    def to_representation(self, image):
        if not image:
            return None
        import os
        image_filename, image_format = os.path.splitext(image.name)
        image_filename = f'/media/{image_filename}'
        image_format = image_format.replace('.', '')

        image_dict = {
            "path": image_filename,
            "formats": [image_format
                        ]
            }
        return image_dict


class ProductSerializer(serializers.ModelSerializer):
    image = ProductImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'title', 'sku', 'price', 'status', 'image']
