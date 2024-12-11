import torch
from transformers import BlipProcessor, BlipForConditionalGeneration, BlipForQuestionAnswering
from PIL import Image

# Load processors and models
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
qa_model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

def generate_caption(image_path):
    """
    Generate a caption for the given image
    
    Args:
        image_path (str): Path to the image file
    
    Returns:
        str: Generated caption for the image
    """
    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, return_tensors="pt").to("cpu")
    outputs = caption_model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption

def answer_question(image_path, question):
    """
    Answer a question about the given image
    
    Args:
        image_path (str): Path to the image file
        question (str): Question about the image
    
    Returns:
        str: Answer to the question
    """
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, text=question, return_tensors="pt").to("cpu")
    outputs = qa_model.generate(**inputs)
    answer = processor.decode(outputs[0], skip_special_tokens=True)
    return answer