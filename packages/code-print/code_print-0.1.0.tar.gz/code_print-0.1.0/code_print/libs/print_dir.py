import codecs
import os


def print_file_info(dirpath, level=0, exts=[]):
    """
    디렉토리 내 파일 정보 출력
    Args:
        dirpath: 디렉토리 경로
        level: 현재 폴더 깊이
    """
    indent = " "

    # 현재 폴더 정보 출력
    print(f"{indent}{dirpath}")

    # 현재 폴더 내 파일 목록 가져오기
    files = os.listdir(dirpath)
    files = list(filter(lambda item: item not in ["__pycache__", ".mypy_cache", "node_modules", ".git"], files))

    # 각 파일 정보 출력
    for file in files:
        filepath = os.path.join(dirpath, file)
        ext = os.path.splitext(file)[1]
        if os.path.isfile(filepath) and ext in exts:
            # 파일인 경우 내용 출력
            print_file_content(filepath, level + 1)
        elif os.path.isdir(filepath):
            # 하위 폴더인 경우 재귀적으로 출력
            print_file_info(filepath, level + 1, exts=exts)


def print_file_content(filepath, level=0, show_num=True):
    """
    파일 내용 출력
    Args:
        filepath: 파일 경로
        level: 현재 폴더 깊이
    """
    print("=====", filepath)
    with codecs.open(filepath, "r", "utf_8") as f:
        if show_num:
            line_num = 1
            for line in f.readlines():
                print(f"{line_num:4}:{line.rstrip()}")
                line_num += 1
        else:
            content = f.read()
            print(f"{content}")
