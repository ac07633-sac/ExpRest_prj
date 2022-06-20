from rest_framework import serializers
from .models import Post, Vote

class PostSerializer(serializers.ModelSerializer):
    #specify model and fields
    
    #to allow only read
    # these fields will not be asked during the post request     
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')    
    #important lesson
    #following needs to be defined in class Meta
    
    #get vote also in the output
    votes = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Post
        #fields = ['id', 'title', 'url', 'poster', 'created']
        fields = ['id', 'title', 'url', 'poster','poster_id', 'created', 'votes']        
        
    #to get vote also in the output
    #function name should be like following only for the selected variable name
    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()
        
        
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        #fields = ['id', 'title', 'url', 'poster', 'created']
        fields = ['id']  