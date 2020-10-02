from rest_framework import serializers

from models.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'post_type',
            'content',
            'upvotes',
            'downvotes',
            'post_date',
            'total_votes',
        ]
