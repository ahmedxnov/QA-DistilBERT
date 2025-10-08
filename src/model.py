from transformers import pipeline
from transformers.pipelines import QuestionAnsweringPipeline
import torch
from typing import Union
from .config import DEFAULT_MODEL, DEFAULT_TASK, DEFAULT_DEVICE

def load_QA_answerer(
    model: str = DEFAULT_MODEL, 
    dtype: torch.dtype = torch.float16, 
    device: Union[int, str] = DEFAULT_DEVICE
) -> QuestionAnsweringPipeline:
    return pipeline(
        task=DEFAULT_TASK,
        model=model,
        dtype=dtype,
        device=device
    )
    
