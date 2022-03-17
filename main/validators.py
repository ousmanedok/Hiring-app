import os

from django.core.exceptions import ValidationError


def validate_image_file(value):
    #  [0] returns path+filename
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".jpeg", ".jpg", ".png"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Please upload a valid image file")
    file_size = value.file.size
    limit_mb = 1
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max file size is {}MB".format(limit_mb))


def validate_resume_file(value):
    #  [0] returns path+filename
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".pdf", ".doc", ".docx"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Please upload a pdf or word document")
    file_size = value.file.size
    limit_mb = 1
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max file size is {}MB".format(limit_mb))
