from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers


from posts.models import Post, Group, Comment, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
        read_only_fields = ('user',)
        validators = [
            serializers.UniqueTogetherValidator(
                Follow.objects.all(),
                fields=['user', 'following'],
                message='Вы уже подписаны на автора',
            )
        ]

    def validate_following(self, value):
        print(value)
        if self.context['request'].user == value:
            raise serializers.ValidationError(
                'Нельзя подписаться на себя'
            )
        return value
