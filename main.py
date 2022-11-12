from pytube import YouTube
import os


# Read Sounds
sounds = open('músicas.txt', 'r+').read().split('\n')

print('Carregando Músicas')

for index, sound in enumerate(sounds):
    print(f'{index+1}/{len(sounds)}')
    yt = YouTube(sound)

    video = yt.streams.filter(only_audio=True).first()
    
    out_file = video.download(output_path='músicas')

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    print(f'Salvo {yt.title}')