from rest_framework import serializers

from . import models

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'created_at'
        )
        extra_kwargs = {
            'email': {'write_only': True}
        }

class CourseSerializer(serializers.ModelSerializer):

    # Option 1 : using HyperlinkedRelated fields creates a link to a list of reviews
    reviews = serializers.HyperlinkedRelatedField(
       many=True, read_only=True, view_name='review-detail'
    )
    # Option 2 :using ReviewSerializer as a field includes all reviews with each course 
    # reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.Course
        fields = (
            'id',
            'title',
            'url',
            'reviews'
        )