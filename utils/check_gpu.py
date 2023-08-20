import torch

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

if __name__ == "__main__":
    device = check_gpu()