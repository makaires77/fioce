def check_installation():
    try:
        import torch
        print("PyTorch version:", torch.__version__)
    except ImportError:
        print("PyTorch is not installed.")

    try:
        import torch_geometric
        print("PyTorch Geometric version:", torch_geometric.__version__)
    except ImportError:
        print("PyTorch Geometric is not installed.")

if __name__ == "__main__":
    check_installation()