from django import forms
from .models import Post, Comment


class PostForm(forms.Form):

    class Meta:
        model = Post
        fields = "__all__"


class CommentForm(forms.Form):

    class Meta:
        model = Comment
        fields = "__all__"
        # exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment",
        }
        error_messages = {
            'user_name': {
                'required': 'Your name must not be empty!',
                'max_length': 'Pleae enter a shorter name!'
            }
        }
