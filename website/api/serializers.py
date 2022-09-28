from rest_framework import serializers
from blog.models import Post, Author, Tag, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    author = AuthorSerializer(many=False)
    tags = TagSerializer(many=True)
    comments = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = obj.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

    def get_total_comments(self, obj):
        comments_count = obj.comments.all().count()

        return comments_count
