import os
from locust import HttpUser, task, between

class ImageUploadUser(HttpUser):
    wait_time = between(1, 3)
    
    @task
    def upload_images(self):
        # Path to the directory containing the images
        images_dir = "media/uploads/"

        # Get a list of all image files in the directory
        image_files = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]

        # Loop through each image file
        for image_file in image_files:
            # Open the image file
            with open(os.path.join(images_dir, image_file), "rb") as image:
                # Upload the image file
                response = self.client.post("/api/upload/image/", files={"image": image})

            
                # Get the size of the uploaded image
                image_size = os.path.getsize(os.path.join(images_dir, image_file))
                print(f"Image Size: {image_size} bytes")
                # Save the image to the local hardware
                with open(f"downloaded_{image_file}", "wb") as downloaded_image:
                   downloaded_image.write(response.content)
                   
                
