import os
import re
import subprocess
import threading
from datetime import datetime
import ipywidgets as widgets
from IPython.display import clear_output, display
from google.colab import files
import string
import time

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

# Gerenciador da fila de downloads
class DownloadQueueManager:
    def __init__(self):
        self.download_queue = []
        self.download_lock = threading.Lock()
        self.is_downloading = False

    def add_to_queue(self, video_url, folder_path):
        with self.download_lock:
            self.download_queue.append((video_url, folder_path))
            if not self.is_downloading:
                self.start_next_download()

    def start_next_download(self):
        with self.download_lock:
            if self.download_queue and not self.is_downloading:
                self.is_downloading = True
                video_url, folder_path = self.download_queue.pop(0)
                threading.Thread(target=self.download_video, args=(video_url, folder_path)).start()

    def download_video(self, video_url, folder_path):
        try:
            start_download(video_url, folder_path, self)
        except Exception as e:
            print(f"Erro ao baixar o vídeo: {e}")

    def download_finished(self):
        with self.download_lock:
            self.is_downloading = False
            if self.download_queue:
                self.start_next_download()

queue_manager = DownloadQueueManager()

def start_download(link, folder_path, queue_manager):
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

    print(f"Download completo: {final_output}")
    files.download(final_output)

# Interface para adicionar vídeos à fila
def play_all():
    link_input = widgets.Text(description="Link:")
    download_button = widgets.Button(description="Adicionar à fila")

    def on_button_click(b):
        video_url = link_input.value
        if video_url:
            date_folder = datetime.now().strftime("%Y-%m-%d")
            folder_id = "DOWNLOADER"
            folder_path = f"/content/{folder_id}/{date_folder}"
            os.makedirs(folder_path, exist_ok=True)
            queue_manager.add_to_queue(video_url, folder_path)
            clear_output(wait=True)
            print("Vídeo adicionado à fila de downloads.")
            display(link_input, download_button)
        else:
            print("Por favor, insira um link válido.")

    download_button.on_click(on_button_click)
    display(link_input, download_button)