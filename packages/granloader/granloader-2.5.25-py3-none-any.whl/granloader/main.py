import os
import re
import time
import string
import subprocess
import threading
import ipywidgets as widgets

from queue import Queue
from datetime import datetime
from google.colab import files
from IPython.display import clear_output, display

# Funções auxiliares
def get_video_id(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.*&v=)?([^&=%\?]{11})')
    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return youtube_regex_match.group(6)
    return None

def get_video_title(link):
    cmd = ["yt-dlp", "--get-title", link]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    title = result.stdout.strip()
    return title

def get_video_info(link):
  cmd = ["yt-dlp", "-F", link]
  result = subprocess.run(cmd, stdout=subprocess.PIPE, universal_newlines=True)
  lines = result.stdout.split('\n')
  max_resolution = 0
  for line in lines:
    if "mp4" in line and "video" in line:
      match = re.search(r'(\d{3,4})x(\d{3,4})', line)
      if match:
        width, height = map(int, match.groups())
        max_resolution = max(max_resolution, height)
  return max_resolution

def sanitize_filename(title):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    sanitized_filename = ''.join(c for c in title if c in valid_chars)
    return sanitized_filename

def find_latest_file(startswith, folder_path):
  relevant_files = [f for f in os.listdir(folder_path) if f.startswith(startswith) and not f.endswith(".ytdl")]
  full_paths = [os.path.join(folder_path, f) for f in relevant_files]
  if not full_paths:
    return None
  latest_file = max(full_paths, key=os.path.getctime)
  return latest_file

def monitor_download_progress(folder_path, title, resolution, download_ready_event):
  # Inicializa variáveis de tamanho de arquivo
  video_size = audio_size = 0
  try:
    while not download_ready_event.is_set():
      video_file = find_latest_file("video_temp", folder_path)
      audio_file = find_latest_file("audio_temp", folder_path)
      if video_file:
         video_size = os.path.getsize(video_file) / (1024 ** 2)
      if audio_file:
         audio_size = os.path.getsize(audio_file) / (1024 ** 2)
      
      # Limpa a saída e imprime o progresso atual
      clear_output(wait=True)
      print(f"Nome: {title}")
      print(f"Resolução: {resolution}p")
      print(f"Vídeo: {video_size:.2f} MB")
      print(f"Áudio: {audio_size:.2f} MB")
      time.sleep(1)
  
  finally:
      # Limpa a saída e exibe apenas o nome e a resolução quando o download está pronto
      clear_output(wait=True)
      print(f"Nome: {title}")
      print(f"Resolução: {resolution}p Finalizado")

def download_video(link, folder_path, queue_manager):
    title = get_video_title(link)
    resolution = get_video_info(link)
    sanitized_title = sanitize_filename(title)
    extension = ".mp4"

    output_audio = os.path.join(folder_path, "audio_temp")
    output_video = os.path.join(folder_path, "video_temp")

    video_thread = threading.Thread(target=lambda: subprocess.run(["yt-dlp", "-f", "bestvideo[vcodec^=avc][ext=mp4]", "-o", output_video, link]), daemon=True)
    audio_thread = threading.Thread(target=lambda: subprocess.run(["yt-dlp", "-f", "bestaudio", "-o", output_audio, link]), daemon=True)

    download_ready_event = threading.Event()

    video_thread.start()
    audio_thread.start()

    monitor_thread = threading.Thread(target=monitor_download_progress, args=(folder_path, title, resolution, download_ready_event), daemon=True)
    monitor_thread.start()

    video_thread.join()
    audio_thread.join()
    
    final_output = os.path.join(folder_path, sanitized_title + extension)
    print("\nMesclando arquivos e preparando para download.")
    cmd_merge = ["ffmpeg", "-i", output_video, "-i", output_audio, "-c", "copy", final_output]
    subprocess.run(cmd_merge)

    os.remove(output_video)
    os.remove(output_audio)

    download_ready_event.set()
    monitor_thread.join()

    if os.path.exists(final_output):
      clear_output()
      print(f"Iniciando download do arquivo final.")
      try:
        clear_output(wait=True)
        print("Este download pode demorar mais que o processo anterior.\n")
        print(f"Resolução: {resolution}p")
        files.download(final_output)
      except Exception as e:
        print(f"Erro no download do arquivo final: {e}")
    else:
      print("Erro: Arquivo não encontrado após download.")
    
    queue_manager.download_finished()
    files.download(final_output)

# Gerenciador da fila de downloads
class DownloadManager:
    def __init__(self):
        self.download_queue = Queue()
        self.current_downloads = []

    def add_download(self, video_url, video_title):
        self.download_queue.put((video_url, video_title))
        self.current_downloads.append(video_title)
        if not hasattr(self, 'download_thread') or not self.download_thread.is_alive():
            self.download_thread = threading.Thread(target=self.process_downloads)
            self.download_thread.start()

    def process_downloads(self):
        while not self.download_queue.empty():
            video_url, video_title = self.download_queue.get()
            folder_path = "/content/downloads"
            os.makedirs(folder_path, exist_ok=True)
            download_video(video_url, folder_path, video_title)
            self.current_downloads.remove(video_title)
            display_downloads(self.current_downloads)

def display_downloads(downloads_list):
    clear_output(wait=True)
    print("Fila de downloads:")
    for download in downloads_list:
        print(f"- {download}")
    display(link_input, add_button)

# Interface do usuário para adicionar downloads
download_manager = DownloadManager()

link_input = widgets.Text(description="URL do vídeo:")
add_button = widgets.Button(description="Adicionar à fila")

def play_all(b):
    video_url = link_input.value
    video_title = video_url.split('/')[-1]  # Simulação do título do vídeo baseado na URL
    download_manager.add_download(video_url, video_title)
    link_input.value = ''  # Limpar o campo de entrada

add_button.on_click(play_all)
display(link_input, add_button)