import time
import torchvision.transforms as transforms
from torchvision.datasets import CelebA

# Define transformations
transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor(),
])

# Retry mechanism to download CelebA
max_attempts = 5  # Maximum number of download attempts
wait_time = 60 * 15  # 15 minutes wait time between attempts
attempt = 0


try:
    print("Starting download of CelebA dataset...")
    dataset = CelebA(root='./data', split='train', transform=transform, download=True)
    print("Completed download of CelebA dataset.\n")

except Exception as e:
    error_message = str(e)

    if "daily quota" in error_message.lower() and "img_align_celeba.zip" in error_message:
        print(f"Failed due to daily quota exceeded.")
        
    else:
        # Re-raise the exception if it's not related to the daily quota issue.
        raise
