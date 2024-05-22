import argparse

def parameters():
    
    parser = argparse.ArgumentParser(description="Simple CLI App")
    parser.add_argument('--name', type=str, help='Your name')
    args = parser.parse_args()