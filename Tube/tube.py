import yt_dlp as youtube_dl
irl = input("irl: ")

# URL do vídeo que você deseja baixar
video_url = irl
# Configurações de download
ydl_opts = {
    'format': 'bestaudio/best',  # Baixa o melhor áudio disponível
    'outtmpl': '%(title)s.%(ext)s',  # Nomeia o arquivo como o título do vídeo
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # Extrai apenas o áudio
        'preferredcodec': 'mp3',  # Converte para mp3
        'preferredquality': '192',  # Qualidade do mp3 (192kbps)
    }],
    'extractaudio': True,  # Apenas áudio
    'audioformat': 'mp3',  # Define o formato de saída como mp3
}

# Função para baixar o áudio
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
