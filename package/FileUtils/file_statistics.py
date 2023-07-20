import os
from collections import Counter

def get_file_size(file_path):
    """
    Return the size of the file in bytes.
    """
    return os.path.getsize(file_path)

def count_lines(file_path):
    """
    Return the total number of lines in the file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return len(lines)

def calculate_word_frequency(file_path):
    """
    Return a dictionary with word frequencies in the file.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    words = content.split()
    word_freq = Counter(words)
    return dict(word_freq)
    


def count_file_extensions(directory_path):
    """
    Count the number of files with each unique file extension in a directory.
    """
    file_extensions = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            _, ext = os.path.splitext(file)
            file_extensions.append(ext)
    
    extension_counts = Counter(file_extensions)
    return dict(extension_counts)


def analyze_directory(directory_path):
    """
    Analyze the distribution of file sizes in a directory and return a summary.
    """
    file_sizes = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_sizes.append(file_size)
    
    summary = {}
    if file_sizes:
        summary = {
            'total_files': len(file_sizes),
            'min_size': min(file_sizes),
            'max_size': max(file_sizes),
            'average_size': sum(file_sizes) / len(file_sizes)
        }
    
    return summary
        





















        
    words = content.split()
    word_freq = Counter(words)
    return dict(word_freq)

def analyze_directory(directory_path):
    """
    Analyze the distribution of file sizes in a directory and return a summary.
    """
    file_sizes = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_sizes.append(file_size)
    
    summary = {}
    if file_sizes:
        summary = {
            'total_files': len(file_sizes),
            'min_size': min(file_sizes),
            'max_size': max(file_sizes),
            'average_size': sum(file_sizes) / len(file_sizes)
        }
    
    return summary

def count_file_extensions(directory_path):
    """
    Count the number of files with each unique file extension in a directory.
    """
    file_extensions = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            _, ext = os.path.splitext(file)
            file_extensions.append(ext)
    
    extension_counts = Counter(file_extensions)
    return dict(extension_counts)
