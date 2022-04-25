# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AudioForm
from django.core.files.storage import FileSystemStorage
from deepgram_app.settings import *
# deepgram sdk
from deepgram import Deepgram
import asyncio
import json


def audio_upload(request):
    uploaded_file = {}
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            myfile = request.FILES['record']
            fs = FileSystemStorage()
            file = fs.save(myfile.name, myfile)
            uploaded_file['url'] = fs.url(file).replace(
                '%', '_').replace('20', '').replace(' ', '_')
            print(uploaded_file)
            asyncio.run(main(uploaded_file['url']))
            with open('./audio.json', 'r') as j:
                contents = json.loads(j.read())
        return render(request, 'audio.html', {
            'uploaded_file': uploaded_file, 'audio_contents': contents['results']['channels'][0]
            ['alternatives'][0]['transcript']})
    else:
        form = AudioForm()
    return render(request, 'home.html', {'form': form})


DEEPGRAM_API_KEY = env('DEEPGRAM_API')
MIMETYPE = 'audio/mpeg'


async def main(PATH_TO_FILE):
    # init the Deepgram SDK
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    # open audio file
    audio = open('.{}'.format(PATH_TO_FILE), 'rb')
    if MIMETYPE == 'audio/wav':
        source = {'buffer': audio, 'mimetype': MIMETYPE}
    else:
        source = {'buffer': audio, 'mimetype': MIMETYPE}
    response = await deepgram.transcription.prerecorded(source, {'punctuate': True})
    # save it to json
    audio_json = open('./audio.json', 'w')
    audio_json.write(json.dumps(response, indent=2))
