import sys
import webbrowser


def search(line):
    st = line.split('==')[0]
    query = (f"{st} github")
    # print(query)
    webbrowser.open(f"https://google.com/?q={query}")


if __name__ == "__main__":
    req_path = sys.argv[1] if len(sys.argv) > 1 else './requirements.txt'
    with open(req_path, 'r') as fi:
        for line in fi:
            line = line.strip()
            search(line)
