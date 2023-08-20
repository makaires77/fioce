import torch


def check_pytorch():
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


def check_gpu():
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print("GPU is available")
        print("GPU Device Name:", torch.cuda.get_device_name(0))
        print("CUDA Version:", torch.version.cuda)
    else:
        device = torch.device("cpu")
        print("GPU is not available, using CPU")

    return device