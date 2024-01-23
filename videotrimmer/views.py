from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
import moviepy.editor as mp
from videotrimmer.models import Video
from videotrimmer.serializers import VideoSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def videoList(request):
    videoList = Video.objects.all()
    serialized =  VideoSerializer(videoList, many=True)
    return JsonResponse(serialized.data, status=status.HTTP_200_OK, safe=False)


@api_view(['GET'])
def video(request, id):
    if request.method == "GET":
        video = Video.objects.get(pk=id)
        serialized =  VideoSerializer(video)
        return JsonResponse(serialized.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addVideo(request):
   # movie_data = JSONParser().parse(request)
    print(request.FILES)
    file = request.FILES['file'].read()
    Video.objects.create( content=file)
    
    return JsonResponse({'status': 'success'})
@api_view(['PUT'])
def trimVideo(request, id):
    try:
        video = Video.objects.get(pk=id)
        content = video.content
        start_time = float(request.POST.get('start_time'))
        end_time = float(request.POST.get('end_time'))

        video_clip = mp.VideoFileClip(io.BytesIO(video_content))
        trimmed_clip = video_clip.subclip(start_time, end_time)
        trimmed_content = trimmed_clip.write_videofile()
        video.content = trimmed_content
        video.save()
        return JsonResponse({'status': 'success'})

    except Video.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 


# Create your views here.
