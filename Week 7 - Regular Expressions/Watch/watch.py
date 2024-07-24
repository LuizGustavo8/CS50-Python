import re

def parse(s):
    # Encontra a URL do YouTube no atributo src do iframe
    match = re.search(r'src="(https?://(?:www\.)?youtube\.com/embed/(\w+))"', s)
    if match:
        video_id = match.group(2)  # Obtém o ID do vídeo
        return f"https://youtu.be/{video_id}"
    return None

def main():
    print(parse(input("HTML: ")))

if __name__ == "__main__":
    main()
